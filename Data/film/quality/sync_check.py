#!/usr/bin/env python3
"""Synchronisation test on the RENDERED, MUXED film (Gate 4).

Audio side: demux the AAC track from the final MP4, run faster-whisper on it, and measure, for every caption in the
timeline, the onset delta between the expected caption start and the first ASR word of that caption; and for every
visual cue, the delta between the cue time the animation used and the ASR onset of the cue word in the muxed audio.

Video side: decode the MP4 (not the PNG frames) and measure mean luminance just after each scene start (fade-in),
mid-scene (content), and just before scene end (fade-out); run ffmpeg blackdetect over the whole file and compare
the black intervals with the scene boundaries. Extract a contact sheet of cue frames per scene for visual review.

Usage: .venv/bin/python quality/sync_check.py --mp4 deliverables/TAKEDA_2040_FINAL.mp4 --timeline timeline/timeline.json --out quality/sync_check.json
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

VP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(VP / 'audio' / 'alignment'))
import asr_check  # noqa: E402  (reuses model, normaliser, soundfile loader)

FF = str(VP / 'tools' / 'bin' / 'ffmpeg')


def run(cmd: list[str]) -> str:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f'command failed: {" ".join(cmd)}\n{r.stderr[-2000:]}')
    return r.stdout + r.stderr


def luminance_at(mp4: str, t: float) -> float:
    """Mean 8-bit luma of the frame at t, decoded from the MP4 and downscaled to 96x54."""
    r = subprocess.run([FF, '-v', 'error', '-ss', f'{t:.3f}', '-i', mp4, '-frames:v', '1', '-vf', 'scale=96:54', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        return float('nan')
    return float(np.frombuffer(r.stdout, dtype=np.uint8).mean())


def tok(s: str) -> list[str]:
    return asr_check.norm(s)


def first_match(words, tokens, t_from: float, t_to: float, min_match=2):
    """Earliest ASR position within [t_from, t_to] where the next tokens match the caption's leading tokens."""
    seq = [(i, tok(w['word'])) for i, w in enumerate(words) if t_from <= w['start'] <= t_to]
    flat = []
    for i, ts in seq:
        for x in ts:
            flat.append((i, x))
    want = tokens[:min_match]
    for k in range(len(flat) - len(want) + 1):
        if [x for _, x in flat[k:k + len(want)]] == want:
            return words[flat[k][0]]
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--mp4', default='deliverables/TAKEDA_2040_FINAL.mp4')
    ap.add_argument('--timeline', default='timeline/timeline.json')
    ap.add_argument('--out', default='quality/sync_check.json')
    ap.add_argument('--frames-dir', default='quality/sync_frames')
    a = ap.parse_args()
    mp4 = str(VP / a.mp4)
    tl = json.load((VP / a.timeline).open())
    scenes = tl['scenes']
    frames_dir = VP / a.frames_dir
    frames_dir.mkdir(parents=True, exist_ok=True)

    # ---- 1. audio: demux + ASR on the muxed track
    wav = str(frames_dir / 'final_audio_48k.wav')
    run([FF, '-y', '-v', 'error', '-i', mp4, '-vn', '-ac', '1', '-ar', '48000', '-c:a', 'pcm_s16le', wav])
    heard, words, dur = asr_check.transcribe(wav)
    print(f'[asr] muxed track {dur:.2f}s, {len(words)} words')

    caption_deltas, cue_deltas, per_scene = [], [], []
    for sc in scenes:
        s0 = sc['start']
        caps = sc['captions']
        cap_rows = []
        for c in caps:
            toks = tok(c['text'])
            exp = s0 + c['start']  # captions are stored scene-relative in timeline.json
            w = None
            for k in range(min(3, len(toks))):  # match the first, else second, else third token near the expected onset
                cand = [x for x in words if abs(x['start'] - exp) <= 1.2 and tok(x['word'])[:1] == toks[k:k + 1]]
                if cand:
                    w = min(cand, key=lambda x: abs(x['start'] - exp))
                    break
            d = round(w['start'] - exp, 3) if w else None
            cap_rows.append({'caption': c['text'][:70], 'expected_start': round(exp, 3), 'asr_start': w['start'] if w else None, 'delta_s': d})
            if d is not None:
                caption_deltas.append(d)
        cue_rows = []
        # cue word text comes from scenes.json via timeline? timeline stores cue times only; use scenes.json for words
        per_scene.append({'id': sc['id'], 'start': s0, 'captions': cap_rows, 'cues': cue_rows})
    sc_doc = json.load((VP / 'screenplay' / 'scenes.json').open())['scenes']
    cue_words = {s['id']: s['cue_words'] for s in sc_doc}
    for ps, sc in zip(per_scene, scenes):
        for key, t_rel in sc['cues'].items():
            word = cue_words[sc['id']].get(key)
            t_abs = sc['start'] + t_rel
            toks = tok(word) if word else []
            cand = [w for w in words if abs(w['start'] - t_abs) <= 1.5 and toks and tok(w['word'])[:1] == toks[:1]]
            best = min(cand, key=lambda w: abs(w['start'] - t_abs)) if cand else None
            d = round(best['start'] - t_abs, 3) if best else None
            ps['cues'].append({'cue': key, 'word': word, 'animation_time': round(t_abs, 3), 'asr_onset': best['start'] if best else None, 'delta_s': d})
            if d is not None:
                cue_deltas.append(d)

    # ---- 1b. audio placement by cross-correlation (signal level, independent of ASR word-boundary jitter)
    track, _ = asr_check.load_audio_16k(wav)
    sr = 16000
    placement = []
    for sc in scenes:
        src, _ = asr_check.load_audio_16k(str(VP / sc['audio']))
        probe = src[: min(len(src), 6 * sr)]
        s0 = int(round(sc['start'] * sr))
        lo, hi = max(0, s0 - sr), min(len(track), s0 + len(probe) + sr)
        win = track[lo:hi]
        n = len(win) + len(probe)
        corr = np.fft.irfft(np.fft.rfft(win, n) * np.conj(np.fft.rfft(probe, n)), n)
        lag = int(np.argmax(corr[: len(win) - len(probe) + 1]))
        found = (lo + lag) / sr
        placement.append({'id': sc['id'], 'expected_start_s': round(sc['start'], 4), 'found_start_s': round(found, 4), 'error_ms': round((found - sc['start']) * 1000, 1)})
    max_err_ms = max(abs(p['error_ms']) for p in placement)
    print(f'[xcorr] max placement error {max_err_ms:.1f} ms')

    # ---- 2. video: luminance at boundaries, blackdetect
    lum_rows = []
    for sc in scenes:
        s0, s1 = sc['start'], sc['end']
        lum_rows.append({'id': sc['id'], 'after_start_0.05s': round(luminance_at(mp4, s0 + 0.05), 1), 'mid_scene_1.5s': round(luminance_at(mp4, s0 + 1.5), 1),
                         'mid_scene_half': round(luminance_at(mp4, (s0 + s1) / 2), 1), 'before_end_0.05s': round(luminance_at(mp4, max(s0, s1 - 0.05)), 1)})
    # pix_th 0.03 ≈ luma 8/255: true black (fades) is detected, the dark 'ink' palette (mean luma ≈ 17–28) is not
    bd = run([FF, '-v', 'info', '-i', mp4, '-vf', 'blackdetect=d=0.15:pix_th=0.03', '-an', '-f', 'null', '-'])
    blacks = [(float(m.group(1)), float(m.group(2)), float(m.group(3))) for m in re.finditer(r'black_start:([\d.]+) black_end:([\d.]+) black_duration:([\d.]+)', bd)]
    boundaries = [sc['start'] for sc in scenes] + [tl['total_duration']]
    black_rows, stray = [], []
    for b0, b1, bdur in blacks:
        near = min(boundaries, key=lambda x: abs(x - b0 - 0.4))
        at_boundary = any(b0 - 0.8 <= x <= b1 + 0.8 for x in boundaries)
        black_rows.append({'start': b0, 'end': b1, 'duration': bdur, 'nearest_boundary': near, 'at_scene_boundary': at_boundary})
        if not at_boundary or bdur > 1.6:
            stray.append({'start': b0, 'end': b1, 'duration': bdur})

    # ---- 3. cue-frame contact sheets per scene (frame at cue + 0.6 s so the fade has landed)
    sheets = []
    for sc in scenes:
        times = [sc['start'] + t + 0.6 for t in sorted(sc['cues'].values())]
        tiles = []
        for k, t in enumerate(times):
            p = frames_dir / f"{sc['id']}_cue{k:02d}_{t:.2f}.png"
            run([FF, '-y', '-v', 'error', '-ss', f'{t:.3f}', '-i', mp4, '-frames:v', '1', '-vf', 'scale=640:360', str(p)])
            tiles.append(p)
        n = len(tiles)
        cols = 3
        layout = '|'.join(f'{(i % cols) * 640}_{(i // cols) * 360}' for i in range(n))
        sheet = frames_dir / f"{sc['id']}_cues.png"
        inputs = []
        for p in tiles:
            inputs += ['-i', str(p)]
        if n == 1:
            run([FF, '-y', '-v', 'error', *inputs, str(sheet)])
        else:
            run([FF, '-y', '-v', 'error', *inputs, '-filter_complex', ''.join(f'[{i}:v]' for i in range(n)) + f'xstack=inputs={n}:layout={layout}:fill=black[o]', '-map', '[o]', str(sheet)])
        for p in tiles:
            p.unlink()
        sheets.append(str(sheet.relative_to(VP)))

    def stats(xs):
        if not xs:
            return None
        arr = np.array(xs)
        return {'n': len(xs), 'mean_s': round(float(arr.mean()), 3), 'median_s': round(float(np.median(arr)), 3), 'abs_max_s': round(float(np.abs(arr).max()), 3), 'p95_abs_s': round(float(np.percentile(np.abs(arr), 95)), 3)}

    n_caps = sum(len(sc['captions']) for sc in scenes)
    n_cues = sum(len(sc['cues']) for sc in scenes)
    report = {
        '_about': 'Synchronisation test run on the muxed deliverable (audio demuxed from the MP4, frames decoded from the MP4).',
        'mp4': a.mp4, 'asr_model': asr_check.MODEL_SIZE, 'audio_duration_s': round(dur, 3), 'asr_words': len(words),
        'audio_placement_xcorr': {'max_abs_error_ms': max_err_ms, 'per_scene': placement,
                                  'note': 'Each scene WAV (first 6 s) cross-correlated against the demuxed track near its timeline start; this is the authoritative placement test. ASR deltas below include Whisper word-boundary jitter (≈0.1–0.6 s after pauses) and are a secondary, content-level check.'},
        'captions': {'total': n_caps, 'matched': len(caption_deltas), **(stats(caption_deltas) or {})},
        'cues': {'total': n_cues, 'matched': len(cue_deltas), **(stats(cue_deltas) or {})},
        'luminance_8bit': lum_rows,
        'black_intervals': black_rows, 'stray_black_intervals': stray,
        'cue_frame_sheets': sheets,
        'per_scene': per_scene,
        'pass': {
            'audio_placed_within_1_frame_all_scenes': max_err_ms <= 1000 / tl['fps'],
            'captions_matched_ratio_ge_0.9': len(caption_deltas) >= 0.9 * n_caps,
            'caption_onset_median_le_0.15s': bool(caption_deltas) and abs(float(np.median(caption_deltas))) <= 0.15,
            'cue_onset_median_le_0.05s': bool(cue_deltas) and abs(float(np.median(cue_deltas))) <= 0.05,
            'cue_onset_p95_le_0.35s': bool(cue_deltas) and float(np.percentile(np.abs(cue_deltas), 95)) <= 0.35,
            'every_scene_has_visible_content': all(r['mid_scene_1.5s'] > 12 and r['mid_scene_half'] > 12 for r in lum_rows),
            'every_scene_fades_to_black': all(r['before_end_0.05s'] < 20 for r in lum_rows),
            'no_stray_black_intervals': not stray,
            'film_opens_on_black': luminance_at(mp4, 0.0) < 8,
            'film_ends_on_black': luminance_at(mp4, tl['total_duration'] - 0.04) < 8,
        },
    }
    report['pass_all'] = all(report['pass'].values())
    (VP / a.out).write_text(json.dumps(report, indent=1))
    print(json.dumps({k: report[k] for k in ('captions', 'cues', 'pass', 'pass_all')}, indent=1))
    print('stray black:', stray)
    for r in lum_rows:
        print(r)


if __name__ == '__main__':
    main()
