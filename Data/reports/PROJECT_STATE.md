# PROJECT_STATE — MEDICINE 2040

**Current phase:** All eight phases executed through session 2; project in **maintain/extend** mode. Open items are in `quality/final_validation.md` §4 and `CONTINUE.md`.
**Session 3 (2026-11-22):** the narrated film **TAKEDA 2040** (6:42, 1080p30, 14 scenes, 83 claim references, sync-verified) is complete in `video_production/` — see `video_production/PROJECT_STATE.md` and `video_production/quality/final_validation.md`. The registries were not modified by the film.
**Last checkpoint:** 2026-11-22 ~09:10 IST (session 3, film); previous 2026-11-21 ~20:20 IST (session 2, Kiro Crew dashboard; lead model Claude Fable 5.1; 25 subagent runs across 6 waves on the same model)
**Registry counts:** 524 sources (294 T1 / 136 T2 / 80 T3 / 13 T4 / 1 T5; 327 retrieved + 128 api_json, 55 metadata_only, 14 blocked/paywalled/unavailable) · 1,401 claims (1,262 FACT / 108 INTERPRETATION / 21 HYPOTHESIS / 10 RECOMMENDATION; 1,188 SUPPORTED / 166 PARTIALLY_SUPPORTED / 27 NEEDS_MORE_RESEARCH / 19 INCONCLUSIVE / 1 CONTRADICTED; 113 with contrary evidence; 110 maturity-tagged; 43 with audit corrections) · 110 conflict records · validation PASS

## Phase status

| Phase | Status | Evidence |
|---|---|---|
| 0 Environment & operating system | DONE | ROS, protocols, rubric, schemas, CLI, briefs, git (29+ commits) |
| 1 Source discovery | DONE | EDGAR inventories, 20 annual reports text-extracted, coverage ledger (85 computed rows) |
| 2 Deep company research | DONE (waves 1–2) | 12 shards merged; dossiers v1.1; 5 horizontal report sets; gap-fill pass |
| 3 Independent evidence audit | DONE (2 rounds) | 187 claims re-inspected, 46 FDA dates + 43 CT.gov statuses live-checked; 27 proposals applied; Gate 1: LLY PASS, JNJ/ABBV CONDITIONAL PASS, TAK repairs applied (re-audit pending) |
| 4 Cross-company synthesis | DONE | `master_comparison.md` + 12 matrices + 21 lessons; decision-grade with conditions |
| 5 Takeda baseline | DONE (Gate 2 PASS) | 16 capability areas classified; 14 IVB items |
| 6 Strategy & capital allocation | DONE (v2 after council) | 18 bets, 37 assumptions, 69 gates, 54 milestones, 5 scenarios + stress case; portfolios USD 1,130 / 1,920 (+1,030 contingent) / 3,155m (ASSUMPTION); council 119 verdicts; Director decision record |
| 7 Executive application | DONE (hub v3) | 11 pillars, 197 reports in-app, 12 views on real data, grounded Q&A (BM25 + optional local open-source LLM), single-file export 8.5 MB, 254 tests |
| 8 Final validation | DONE | `quality/final_validation.md` |

## Completed this session (chronological)
Wave 1: A1 Lilly, A2 J&J, A3 AbbVie, A5 Takeda, A6 AI/robotics, A8 policy, A9 partnerships, A12 pipeline (396 sources / 879 claims) · merge adapter `scripts/merge_shards.py` · Wave 2: A10 audit, A7 commercial, A14 gap-fill, A13 app v2 · audit applied (`apply_audit.py`) · Wave 3: A11a comparison, A11b future-of-pharma + analogies, A15 dossier integrator, A13 hub v3 (Takeda white/red design, reader, Q&A, single file) · Ollama standalone install + `qwen2.5:3b` · Wave 4: A11c bets/capital, A10-bis audit round 2 (`apply_audit2.py`) · Wave 5: A11e council/red team, A13 final pass, A11c-bis strategy v2, A16 deliverables · final validation, maps, CONTINUE.

## Blocked / limitations (see final_validation.md §4 for the full list)
- Hosts blocking scripted access: fiercepharma/biotech, lda.senate.gov, opensecrets, businesswire, forbes, investor.lilly.com/investor.jnj.com (harness fetch only) → recorded per source; lobbying totals for J&J/AbbVie missing.
- Homebrew cannot run inside the agent sandbox (`sandbox_apply`); Ollama installed from the official standalone tarball into `tools/ollama/` instead.
- Subagent default cap is 100 tool calls (two wave-1 runs lost); later waves used 400 + save-as-you-go.
- `independent_corroboration` empty structurally; Takeda Gate 1 re-audit pending; BET-18 not independently reviewed.

## Known failures / rejected directions (keep)
- Brief errors corrected by agents: emraclidine impairment (4.5bn Q4-2024, not 3.5bn 2025); OpenAI–Lilly date (2024-06-25); ARCH is a knowledge graph; AbbVie pledge USD 100bn/10y (not 10bn); Lilly guidance 91–92bn is the Oct-2026 raise; "Strateos closed 2023" unconfirmed.
- Derived-number errors caught by audit: CVS/Zepbound 15 months (not 11); Caplyta MDD seven months (not nine); 29/18 AI entries attributed to a claim that lacks the count.
- First XBRL pass: J&J 52/53-week mislabel, R&D tag selection (RUN-0001).
- Strategy v1 → v2: BET-15 rejected (leverage arithmetic), plasma BUILD → EXPERIMENT, orexin and option engine downsized, Entyvio timing widened.

## Next actions (ordered — detail in CONTINUE.md)
1. Takeda Gate 1 re-audit · 2. A7/A8 REVISE items (flag calibration; lobbying totals via browser/bulk) · 3. back-fill `independent_corroboration` · 4. independent review of BET-18 · 5. strategic research gaps (Entyvio exclusivity/benefit channel, competitor orexin, robotics installed bases, TuneLab uptake, venture-arm scale) · 6. full-text readouts + leadership transcripts · 7. quarterly refresh cycle.
