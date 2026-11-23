# Audio review — narration

**Model.** Kokoro-82M (`kokoro` 0.9.4, Apache-2.0 weights `hexgrad/Kokoro-82M`), voice `af_heart`, speed 1.12, 24 kHz mono synthesis, resampled to 48 kHz stereo at mux. Sentence-level synthesis with a 0.42 s inter-sentence pause; per-scene WAVs in `audio/narration/final/` with `manifest.json` (measured durations, sentence offsets).

**Voice selection.** Six voices were synthesised on the same 4-sentence pharma passage (`audio/samples/`: af_heart, af_bella, am_fenrir, am_michael, bf_emma, bm_george) and round-tripped through ASR (`audio/samples/ab_asr_report.json`). `af_heart` had the lowest WER on drug names and the most even pacing (RTF 0.045 on MPS, peak −4.1 dBFS, RMS −26.2 dBFS). British voices mispronounced several brand names; the two male US voices were slower at equal speed.

**Pronunciation.** 30 inline-phoneme entries (`audio/pronunciation/pronunciation_dictionary.json`), verified by probing misaki output (`probe_phonemes.py`) and by listening to the A/B samples: Entyvio, Takeda, Skyrizi, Rinvoq, vedolizumab, zasocitinib, oveporexton, rusfertide, tirzepatide, Amitiza, CUDA, Lessines, Humira, Stelara, Tremfya, Nimbus, Innovent, orexin, Zepbound, AbbVie, Caremark, Nabla, Iambic, Arctoris, Strateos, Los Angeles, Shonan.

**ASR verification of the final narration** (`audio/alignment/final_asr.json`, faster-whisper `small.en`): WER per scene 0.00–0.145 (S09 0.00, S01 0.019, S08 0.026, S14 0.033, S04 0.037, S12 0.043, S07 0.048, S03 0.059, S02 0.077, S10 0.085, S13 0.088, S05 0.107, S11 0.141, S06 0.145). Every residual substitution was classified:

| Type | Examples | Verdict |
|---|---|---|
| ASR spelling of brand/drug names | Entyvio→"entivio", tirzepatide→"terzepatide", zasocitinib→"zasocytinib", Cerevel→"sarival", Amitiza→"amateza", Vyvanse→"5 ants" | phonemes verified correct; ASR vocabulary limit |
| Number formatting in the normaliser | "twenty twenty-six"→"20 26" vs "2026"; "one point two"→"1 2" | not an audio error |
| British vs US spelling | centres/centers, programme/program, licence/license, organisation/organization | not an audio error |
| Homophones | half→"5" (after "four and a"), write→"right" | not an audio error |
| Rare word | orexin→"erexin"; "its Shonan"→"it's shown on" | phonemes ɔɹˈɛksɪn / ʃˈOnɑn confirmed; ASR limit |

No omitted or inserted sentences; every cue word was found (103/103 cues resolved in `timeline.json`).

**Levels and mix.** Narration-only track (no music, by design: nothing available under a verified licence that fit the register). `alimiter=limit=0.95` guards the mix; scenes are placed by `adelay` at their timeline starts with 0.6 s gaps and a 2.5 s / 4.5 s hold on the opening and closing title cards. Loudness and the sync measurements on the muxed file are in `quality/synchronization_report.md`.

**Pace.** 954 words over 386.6 s of speech ≈ 148 words per minute at speed 1.12 — within the 140–160 wpm documentary range. Longest sentence 25 words (S13).

**Known limitations.** Single neural voice with no emotional direction beyond punctuation and speed; a few brand names remain opaque to ASR (so pronunciation of those is verified by ear, not automatically).
