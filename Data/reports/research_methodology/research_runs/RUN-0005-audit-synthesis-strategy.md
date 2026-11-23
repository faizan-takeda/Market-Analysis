# RUN-0005 — Waves 2–5: audit, gap-fill, synthesis, strategy, council, hub (2026-11-21, session 2)

**Questions.** (a) Does the wave-1 evidence survive independent re-inspection? (b) Can a fresh-context synthesis layer and a Takeda strategy be built only on accepted claims? (c) Does an independent council change the strategy?
**Hypotheses.** Audit will find locator drift and announcement-vs-regulator date errors but few numeric errors; the synthesis will need to refuse several cross-company rankings; the council will cut long-horizon spend.

## What ran
| Wave | Agents | Output |
|---|---|---|
| 2 | A10 audit · A7 commercial · A8 policy (3rd attempt) · A14 gap-fill · A13 app v2 | 99-claim re-inspection; +26/59, +36/55, +50/75 shard records; 12 views on real data |
| 3 | A11a comparison · A11b future-of-pharma + analogies · A15 dossier integrator · A13 hub (white/red, reader, Q&A, single file) | 13 comparison files, 21 lessons; 7 domains, 7 analogies, moat taxonomy; dossiers v1.1; hub v3 |
| 4 | A11c bets/capital · A10-bis audit round 2 | 17 bets, 3 portfolios, 67 gates, 5 scenarios, 50 milestones; 88-claim re-inspection + 46 FDA dates + 43 CT.gov statuses |
| 5 | A11e council/red team · A13 final · A11c-bis strategy v2 · A16 deliverables | 119 verdicts, 95 counterarguments; strategy v2 (18 bets); 6 deliverables |

## Results vs hypotheses
- (a) **Confirmed.** Numeric accuracy high (all reachable numbers matched in round 2); defects were labels (debt basis), dates taken from announcements instead of FDA records (3), mis-cited IDs (4), unsupported link (Strateos), maturity over-tagging (6 + 24 missing). All applied with audit trail; statements never edited.
- (b) **Confirmed.** `master_comparison.md` refuses five rankings; A11c built strategy only from registry claims + explicit ASM ids (0 unknown IDs).
- (c) **Confirmed and stronger than expected.** Council cut the balanced envelope 2,950 → 1,920 committed (+1,030 contingent), rejected the USD 5bn purchase as framed, moved plasma to EXPERIMENT, and re-rated 19/85 robustness cells. The Director accepted 10 changes and declined 2 (recorded).

## New vs reused evidence
+129 sources / +291 claims in waves 2–3 (total 524 / 1,401); reused: all wave-1 shards and the 20 filings on disk.

## Contradictions found (kept)
Juvmo 09-25 vs 09-28; OTTAVA De Novo 07-21 vs 07-22 and receipt 2025-12-18 vs announcement 2026-01-07; Imaavy 04-29 vs 04-30; AbbVie IPR&D 5,016 vs 4,808 (definitional); bermekimab 0.6 vs 0.8bn (estimate vs final); CUDA developers 7.5m (10-K) vs 11m (blog); Lilly lobbying 7.89 vs 8.43m (open); Medicare obesity start Apr vs Jul 2026 (open).

## Evaluation
Coverage up (commercial, policy, gap-fill); traceability high; independence still weak structurally (`independent_corroboration` empty); contradiction handling now recorded (110 conflict records). Decision: **ACCEPT**; next research directions in `quality/final_validation.md` §4.

## Process findings (keep)
- Fresh-context auditors found errors the authors could not see (announcement dates, mis-cited IDs). Keep one audit round per wave.
- Builder-script regeneration (A11c's `_a11c_*.py`) made the v2 revision cheap and consistent across Markdown and JSON.
- Agents must never derive durations/counts in prose without a claim ("11 months", "nine months", "29 entries" errors).
