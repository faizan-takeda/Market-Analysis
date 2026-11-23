# TECHNICAL STACK — TAKEDA 2040 film

Everything below is open-source or already installed on the production machine. No paid image, video or voice API was used; no network service was called at render time (model weights were downloaded once from Hugging Face).

## Machine

Apple M4 Pro, macOS 26.7.3, 14 cores, 48 GB. Google Chrome 157.0.8103.79 (already installed) is used as the headless render surface. Node v18.20.2 (system). Python 3.12.16 via `uv` venv at `video_production/.venv`.

## Pipeline at a glance

```
screenplay/scenes.json ──► audio/tts/synthesize.py (Kokoro-82M) ──► audio/narration/final/S01..S14.wav + manifest.json
        │                                 │
        │                                 └─► audio/alignment/asr_check.py (faster-whisper small.en) ──► final_asr.json (WER + word onsets)
        │                                                                                              │
        └──────────────► timeline/build_timeline.py ◄───────────────────────────────────────────────────┘
                              │   (scene starts, frame counts, cue times = ASR word onsets, captions, SRT, tails)
                              ▼
                 timeline/timeline.json  +  subtitles/TAKEDA_2040_SUBTITLES.srt
                              │
                              ▼  (imported by motion/src/lib/stage.ts — every visual beat waits for its measured cue)
                 motion/src/scenes/s01..s14.tsx  ──► motion/scripts/render.mjs (Vite + Motion Canvas Renderer in headless Chrome via puppeteer-core)
                              │                                   ──► motion/output/final/000000.png … 012064.png
                              ▼
                 motion/scripts/encode.mjs (static ffmpeg 7.0: libx264 CRF 18 yuv420p; per-scene adelay mix → AAC 192k; mov_text SRT; ffprobe verification)
                              │
                              ▼
                 renders/final/TAKEDA_2040_FINAL.mp4 (+ _ffprobe.json), renders/silent/TAKEDA_2040_SILENT.mp4 → deliverables/
                              │
                              ▼
                 quality/sync_check.py (ASR on the demuxed track, luminance at boundaries, blackdetect, cue-frame sheets) → quality/sync_check.json
```

## Components and versions

| Layer | Tool | Version | Licence | Why this one |
|---|---|---|---|---|
| Animation | Motion Canvas `@motion-canvas/core`, `/2d`, `/vite-plugin` | 3.17.2 | MIT | Programmatic, deterministic 2D motion graphics in TypeScript; generator-based timing lets each beat wait for an absolute film time (`cueAt`). Remotion was rejected on licence terms. |
| Headless render | Custom Vite 5.4.21 plugin `/headless` + `Renderer` from core + `puppeteer-core` 25.18.1 driving local Chrome 157 | — | MIT / BSD | The editor UI's RENDER button is manual; this harness renders a time range to PNGs from the command line and verifies the frame count. Chrome flags: `--use-angle=swiftshader --enable-unsafe-swiftshader --force-device-scale-factor=1`. |
| Language | TypeScript 5.9.3 | — | Apache-2.0 | Scenes typecheck with `npx tsc --noEmit`. |
| Narration (TTS) | Kokoro-82M via `kokoro` 0.9.4 + `misaki` 0.9.4 (G2P), `espeakng-loader` 0.2.4 fallback, PyTorch 2.15.0 on MPS | 82M params | Apache-2.0 (code and weights) | Fast (RTF ≈ 0.05 on MPS), consistent voice, inline phoneme override `[word](/phonemes/)` used by the pronunciation dictionary. Voice `af_heart`, speed 1.12, sentence-level synthesis with measured sentence offsets. Qwen3-TTS and Piper were evaluated and rejected (speed / quality). |
| ASR verification | `faster-whisper` 1.2.1 (`small.en`, CPU int8, CTranslate2 4.9.0) | — | MIT | Word timestamps for cue placement and WER per scene; audio decoded with `soundfile` 0.14.0 to avoid a PyAV API mismatch. |
| Encode / mux / probe | `static-ffmpeg` 3.0 (bundles ffmpeg/ffprobe 7.0 with libx264, aac) symlinked at `tools/bin/` | 7.0 | LGPL/GPL | evermeet.cx download was blocked; the pip wheel works offline. |
| Numerics | numpy 2.5.5 | — | BSD | Luminance stats, resampling. |

## Commands (run from `video_production/`)

```bash
# 1. narration (≈ 25 s for the whole film on MPS)
.venv/bin/python audio/tts/synthesize.py --scenes screenplay/scenes.json --out audio/narration/final --voice af_heart --speed 1.12 --force
# 2. ASR check (per-scene WER + word onsets)
.venv/bin/python audio/alignment/asr_check.py --batch audio/narration/final/asr_manifest.json --out audio/alignment/final_asr.json
# 3. timeline, captions, SRT (tails hold the opening and closing title cards)
.venv/bin/python timeline/build_timeline.py --scenes screenplay/scenes.json --narration audio/narration/final --asr audio/alignment/final_asr.json \
  --out timeline/timeline.json --srt subtitles/TAKEDA_2040_SUBTITLES.srt --concat timeline/audio_concat.json --gap 0.6 --tails S01=2.5,S14=4.5
# 4. typecheck + previews (fast look at any film time)
(cd motion && npx tsc --noEmit && node scripts/preview.mjs --name act1 --times 4.5,14.5,22)
# 5. full render (≈ 7 min for 12,065 frames) and encode (≈ 2 min)
(cd motion && node scripts/render.mjs --name final --from 0 --to 402.166667 --fps 30)
(cd motion && node scripts/encode.mjs --name final --timeline ../timeline/timeline.json --out ../renders/final/TAKEDA_2040_FINAL.mp4 \
  --silent ../renders/silent/TAKEDA_2040_SILENT.mp4 --srt ../subtitles/TAKEDA_2040_SUBTITLES.srt)
# 6. re-render one scene in place (frame numbers are absolute; keep --clean false)
(cd motion && node scripts/render.mjs --name final --clean false --from 266.67 --to 295.8 --fps 30)
# 7. synchronisation and black-frame QA on the muxed file
.venv/bin/python quality/sync_check.py --mp4 deliverables/TAKEDA_2040_FINAL.mp4 --timeline timeline/timeline.json --out quality/sync_check.json
# 8. documents regenerated from the same sources
.venv/bin/python research/build_evidence_ledger.py && .venv/bin/python screenplay/build_screenplay_docs.py
```

## Design decisions worth knowing

- **Timing comes from the audio, never from the script.** `timeline.json` is built from the synthesised WAV durations and ASR word onsets; the scenes import it at build time and `cueAt(t0, t)` waits to an absolute film time. Changing a word re-times the picture automatically after steps 1–3.
- **Scenes end on the clock.** `finish()` holds to `duration − fade`, fades to black, and holds to the exact scene end. A beat that would run past the end is given a `--tails` hold rather than allowed to drift (the first cut had S01 and S14 overrun their slots; fixed by tails of 2.5 s and 4.5 s).
- **Partial re-renders are safe** because the exporter numbers frames by absolute index; `encode.mjs` reads the full contiguous sequence.
- **Audio placement uses the same timeline**: each scene WAV is `adelay`-ed to its start (ms) and mixed, then padded/trimmed to the total; `-shortest` is not used (it dropped frames in the proof clip).
- **CJS interop**: `@motion-canvas/core` default import is unwrapped with `motionCanvasImport.default ?? motionCanvasImport`.
- **JSX fragments inside `.map`** render only a stray dot in this harness; each element type is mapped separately.
- Pronunciation fixes live in `audio/pronunciation/pronunciation_dictionary.json` (Entyvio, Vyvanse, oveporexton, zasocitinib, rusfertide, Shonan, Skyrizi, Rinvoq, Stelara, tirzepatide…) and are applied by `synthesize.py` as inline Kokoro phonemes.

## Known limitations

- ASR cannot verify the spelling of drug names (it hears "Entivio"); pronunciation was checked by ear in the voice A/B (`audio/samples/`).
- Kokoro is a single-speaker neural voice; it has no emotional direction controls beyond speed and punctuation.
- Node 18 triggers Vite's CJS-API deprecation warning; harmless.
- Renders are software-rasterised (SwiftShader); 12,065 frames take ≈ 7 minutes.
