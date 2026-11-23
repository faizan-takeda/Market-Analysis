# Synchronisation report — tested on the muxed deliverable (Gate 4)

**File under test:** `video_production/deliverables/TAKEDA_2040_FINAL.mp4` — 18,853,840 bytes, sha256 `b3b64c8d95d373af5ed85549014a6fb26fda49ac4d74c054553a6b187fd6d259` (see `deliverables/SHA256SUMS.txt`).
**Method:** `quality/sync_check.py` → `quality/sync_check.json`; frames and audio were taken from the MP4 itself, not from the PNG sequence or the source WAVs. Run after the final encode (2026-11-22 09:07 local).

## 1. Container (ffprobe, `deliverables/TAKEDA_2040_FINAL_ffprobe.json`)

| Check | Value | Pass |
|---|---|---|
| Video | h264, 1920×1080, 30/1 fps, yuv420p, 12,065 frames, 402.167 s | ✔ |
| Audio | aac, 2 ch, 48 kHz, 402.166 s | ✔ |
| Subtitles | 1 stream, mov_text, eng, 80 cues (last ends 06:36.44) | ✔ |
| Timeline | 402.166666 s / 12,065 frames; video − timeline = 0.000 s; video − audio = 0.001 s | ✔ |
| Loudness (ebur128) | I = −20.5 LUFS, LRA 4.8 LU | consistent across scenes |

## 2. Audio placement — signal level (authoritative)

Each scene's narration WAV (first 6 s) was cross-correlated with the demuxed track around its timeline start.

| Scene | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | S09 | S10 | S11 | S12 | S13 | S14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| error (ms) | 5.0 | 4.7 | 5.0 | 4.7 | 4.7 | 4.7 | 4.9 | 5.0 | 4.9 | 4.6 | 5.3 | 4.9 | 5.3 | 4.6 |

Maximum 5.3 ms = 0.16 frame; the constant ≈ 5 ms is the AAC encoder's priming offset, identical for every scene. **Pass** (threshold: one frame, 33.3 ms).

## 3. Word-level check — ASR on the muxed track (faster-whisper small.en)

930 words recognised on 402.18 s of audio.

| Measure | n matched / total | median | mean | p95 abs | max abs | Pass rule |
|---|---|---|---|---|---|---|
| Visual cue vs spoken cue word | 101 / 103 | 0.007 s | 0.022 s | 0.26 s | 0.90 s | median ≤ 0.05 s, p95 ≤ 0.35 s ✔ |
| Caption onset vs first word | 78 / 80 | 0.069 s | 0.083 s | 0.57 s | 0.64 s | median ≤ 0.15 s, ≥ 90% matched ✔ |

Per-scene mean cue delta is within ±0.09 s for 13 scenes (S12 0.197 s because of one outlier). The outliers (S12 "plasma" 0.90 s, S14 "Decide" 0.57 s, S05 "Takeda" 0.55 s) are all first words after a pause, where Whisper's word boundary is known to drift; the signal-level test above shows the audio itself is placed to the millisecond. Captions lead the voice by ≈ 70 ms on average because Kokoro's sentences begin with a short breath; this is the conventional direction for subtitles. The two unmatched cues (S12 "Alphabet", "Regeneron") and two unmatched captions (S13 "Twenty twenty-seven…", "Twenty twenty-eight…") are ASR vocabulary/number-format misses, not timing failures; their frames were checked by eye (`quality/sync_frames/S12_cues.png`, `S13_cues.png`).

## 4. Picture — decoded from the MP4

| Check | Result | Pass |
|---|---|---|
| Fade-in: mean luma at scene start + 0.05 s | 5.1 (dark scenes) / 74.8–104.8 (light scenes, overlay 85% opaque) for all 14 | ✔ |
| Content present: mean luma at +1.5 s and mid-scene | 17.3–28.0 (dark) / 237.7–248.7 (light), all > 12 | ✔ |
| Fade-out: mean luma at scene end − 0.05 s | 0.0 for all 14 scenes | ✔ |
| First frame / last frame | black (< 8) / black (< 8) | ✔ |
| blackdetect (d ≥ 0.15 s, pix_th 0.03) | 9 intervals, 0.17–0.37 s, every one at a scene boundary; none mid-scene | ✔ |
| Cue-frame sheets (frame at every cue + 0.6 s, 14 sheets) | `quality/sync_frames/S01…S14_cues.png`; inspected S01, S05, S06, S10, S13, S14 in detail, all beats present | ✔ |
| Boundary frames by eye | S01 title holds 24.4–25.3 s, fades by 25.9 s; S02 fades in from 26.23 s. Closing title holds 398–401.4 s; frame at 402.1 s is black. | ✔ |

## 5. Fixes made during this gate (and what was re-tested)

1. **S01 and S14 overran their slots** in the first full render (title cards still fading in when the next scene began / when the film ended). Fix: `--tails S01=2.5,S14=4.5` in `build_timeline.py` (total 395.17 s → 402.17 s); full re-render; re-encode; this report.
2. **S11 evidence strip** lacked the Cerevel consideration claim (CLM-009053): added to `scenes.json`, S11 range re-rendered in place, re-encoded.
3. **S10 "most members pay $0" pill** was narrower than its text (white text invisible on the light background): widened; S10 range re-rendered in place; re-encoded; sync check re-run (identical audio results; `pass_all: true`).
4. **Sync-check tooling:** caption times in `timeline.json` are scene-relative (SRT is absolute) — the checker and the transcript generator were corrected; `blackdetect` threshold lowered from 0.10 to 0.03 so the dark palette is not mistaken for black; cross-correlation placement test added.

## Verdict

`pass_all: true`. Audio is placed within 5.3 ms of the timeline in every scene; visual beats land within one ASR word-boundary of their spoken cue; every scene fades in and out on the clock; the film opens and closes on black; subtitles are muxed and timed absolutely.
