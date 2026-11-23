# Final validation — TAKEDA 2040 film

Date: 2026-11-22. Validator: production agent, re-reading every artefact from disk. Nothing below is reported from memory; each line names the file that proves it.

## Deliverables (video_production/deliverables/)

| File | Size | Proof |
|---|---|---|
| `TAKEDA_2040_FINAL.mp4` | 18,853,840 B | sha256 `b3b64c8d…d259` (`SHA256SUMS.txt`); ffprobe JSON below |
| `TAKEDA_2040_SILENT.mp4` | 10,026,979 B | sha256 `ebfdc094…d48f`; same frame sequence, no audio |
| `TAKEDA_2040_SUBTITLES.srt` | 80 cues | last cue 00:06:35,152 → 00:06:36,440 "Decide at every gate." |
| `TAKEDA_2040_TRANSCRIPT.md` | 14 scenes, 80 timestamped captions | built from `timeline/timeline.json` (absolute times) |
| `VIDEO_RESEARCH_REFERENCES.md` | 83 claim references, 67 sources, 26 strategy ids, 0 unresolved | built by `research/build_evidence_ledger.py` |
| `TAKEDA_2040_FINAL_ffprobe.json` | — | copied from `renders/final/` |

### ffprobe (verbatim from `TAKEDA_2040_FINAL_ffprobe.json`)

```json
{
 "size_mb": 17.98, "container": "mov,mp4,m4a,3gp,3g2,mj2", "duration_s": 402.167,
 "video": {"codec": "h264", "width": 1920, "height": 1080, "fps": "30/1", "pix_fmt": "yuv420p", "frames": "12065", "duration_s": 402.167},
 "audio": {"codec": "aac", "channels": 2, "sample_rate": "48000", "duration_s": 402.166},
 "subtitles": 1, "timeline_duration_s": 402.166666, "av_delta_s": 0.001,
 "checks": {"has_audio": true, "is_1080p": true, "fps_ok": true, "duration_matches_timeline": true, "av_aligned": true},
 "pass": true
}
```

Runtime **6 min 42.17 s** (target 5–7 min). Loudness −20.5 LUFS integrated, LRA 4.8 LU.

## Gates

| Gate | Requirement | Evidence | Status |
|---|---|---|---|
| G1 | Evidence ledger + central thesis before screenplay | `research/evidence_ledger.json`, `research/selected_insights.md`, `strategy/central_thesis.md` | ✔ |
| G2 | Render + narration sample before production | `renders/final/PROOF_pipeline_test.mp4` (22.17 s, ffprobe pass), `audio/samples/` 6-voice A/B + ASR | ✔ |
| G3 | Script, storyboard and scenes consistent | `screenplay/master_script.md`, `storyboard.md`, `narration.txt` generated from `scenes.json` + `timeline.json`; `strategy/editorial_review.md` | ✔ |
| G4 | Sync tested on rendered media | `quality/sync_check.json` `pass_all: true`; `quality/synchronization_report.md` | ✔ |

## Requirement checklist

| Requirement | Result |
|---|---|
| Only existing MEDICINE research; no new pharmaceutical research | Every figure traces to a claim id in `New_mediciine/evidence_library` (`quality/evidence_audit.md`); 0 unresolved ids; research cutoff 2026-11-21 shown on the closing card |
| FACT / INTERPRETATION / HYPOTHESIS / SCENARIO / RECOMMENDATION / ASSUMPTION preserved | kinds in `scenes.json`, chips on screen (SCENARIO S05, ASSUMPTION S13, BET ids), qualifiers for PARTIALLY_SUPPORTED/INCONCLUSIVE claims |
| Never present hypothetical amounts as Takeda's budget | S13 narration "planning assumptions, not a budget"; on-screen "ASSUMPTION · NOT A TAKEDA BUDGET" |
| Never claim Takeda can eliminate LOE | S10 "delay erosion, and measure it"; S03 "It delayed the fall. It did not prevent it." |
| No paid image / TTS / video APIs; no ElevenLabs | Kokoro-82M (Apache-2.0), Motion Canvas (MIT), faster-whisper (MIT), static ffmpeg, local Chrome — `TECHNICAL_STACK.md` |
| Competitors 10–20% of narration; Takeda ≥ 70% | 19.2% of words (S02–S04), 18.9% of runtime; Takeda-centred ≥ 80% (`screenplay/master_script.md` header) |
| 14–22 scenes | 14 |
| 5–7 minutes, 1080p30, H.264/AAC, narrated, synchronised, subtitled | 6:42, 1920×1080, 30 fps, h264/aac, mov_text SRT muxed; sync `pass_all: true` |
| Editable production assets | `motion/src/` (14 scene files + lib), `screenplay/scenes.json`, `timeline/`, `audio/narration/final/*.wav`, `subtitles/`, build scripts |
| Skills | `.kiro/skills/cinematic-motion-design`, `pharmaceutical-evidence-storytelling`, `narration-synchronization-qa` |
| Project maps updated | root `map.md`, `New_mediciine/map.md`, root `PROJECT_STATE.md`, `CONTINUE.md` |

## Quality documents

`quality/evidence_audit.md` · `scientific_review.md` · `visual_review.md` · `audio_review.md` · `synchronization_report.md` · `sync_check.json` · `sync_frames/` (14 cue sheets) · this file.

## Known limitations (disclosed, not hidden)

1. Narration is a single neural voice without music; ASR cannot confirm the spelling-level pronunciation of a few drug names (verified by ear in the A/B samples).
2. Two scientific precision notes for a future cut: say "narcolepsy type 1" in the voice track (the card already does); soften "not been demonstrated anywhere" to "in the sources reviewed".
3. Rendering is software-rasterised; a full re-render takes ≈ 7 min, a single scene ≈ 30 s.
4. The film reflects strategy v2 and the registry as of 2026-11-21; regulatory statuses (zasocitinib review, biosimilar decisions) will change.
5. `video_production/motion/output/final/` (12,065 PNGs, 1.5 GB), `motion/node_modules/`, `.venv/` and `tools/bin` binaries are not committed; they are reproducible from the scripts in `TECHNICAL_STACK.md`.
