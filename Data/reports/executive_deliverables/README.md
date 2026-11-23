# Deliverables: MEDICINE 2040

Cutoff 2026-11-21. These five documents are the executive output of the project. They summarise, and do not replace, the evidence library and the strategy files. They cite strategy v2, which is the v1 strategy as amended by the [Director decision record](../strategy/critical_challenges/DIRECTOR_DECISION_RECORD.md). The v1 strategy files are not yet rewritten to match (pending the A11c-bis pass), so read the deliverables where the two differ.

| File | What it is | For whom | Evidence lives in |
|---|---|---|---|
| [executive_summary.md](executive_summary.md) | The ten-step storyline (what is changing, who is winning, why, what is defensible, what Takeda has, where the opportunity is, what to build, invest, execute, measure), reader notes for CEO, CFO, R&D, CTO and commercial leaders, and a box on what we could be wrong about | Executive team, Board | [executive_strategy_narrative.md](../strategy/takeda_future_2030_2040/executive_strategy_narrative.md), [counterarguments](../strategy/critical_challenges/counterarguments_and_uncertainty.md) |
| [competitor_comparison.md](competitor_comparison.md) | Answers to the ten comparison questions on Lilly, J&J, AbbVie and Takeda, the valid comparison tables, and the comparisons refused and why | Strategy, corporate development, R&D leadership | [master_comparison.md](../New_mediciine/cross_company_analysis/master_comparison.md), [matrices and lessons](../New_mediciine/cross_company_analysis/map.md), four [company dossiers](../New_mediciine/companies/) |
| [takeda_strategy.md](takeda_strategy.md) | Capability baseline, seven transformation domains, 18 bets with v2 decisions and moat mechanisms, sequencing, what not to do | Executive team, R&D, digital, commercial | [strategic_bets.md](../strategy/investment_theses/strategic_bets.md), [future_of_pharma](../strategy/future_of_pharma/map.md), [capability baseline](../New_mediciine/companies/takeda_public_baseline/capability_baseline/capability_baseline.md) |
| [investment_roadmap.md](investment_roadmap.md) | Three portfolios plus the v2 balanced portfolio, stage gates, half-year roadmap, scenario robustness, sensitivity | CFO, portfolio review committee | [capital_allocation.md](../strategy/financial_cases/capital_allocation.md), [stage_gates.md](../strategy/financial_cases/stage_gates.md), [roadmap](../strategy/strategic_roadmap/roadmap_2027_2040.md), [scenarios](../strategy/scenarios/scenarios_2027_2040.md), [stress test](../strategy/critical_challenges/scenario_stress_test.md) |
| [recommendations.md](recommendations.md) | First 12 months, what to avoid, scale criteria, success metrics, open questions needing Takeda-internal data | Executive team, bet owners | [stage_gates.md](../strategy/financial_cases/stage_gates.md), [internal-validation backlog](../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md) |

Not owned by this set: [OPEN_APPLICATION.md](OPEN_APPLICATION.md) and [MEDICINE_2040_Hub.html](MEDICINE_2040_Hub.html) (the application and hub).

## Rules these documents follow

- Every material sentence cites a claim (CLM-), bet (BET-) or assumption (ASM-) ID, or is labelled INTERPRETATION, HYPOTHESIS, SCENARIO or RECOMMENDATION.
- Claim values were looked up in the [claims registry](../New_mediciine/evidence_library/claims_registry.jsonl); the 42 claims that carry a `correction` field are cited with the correction applied.
- Every dollar figure for a bet is an ASSUMPTION. Takeda's budget, forecasts and internal data are not public. No NPV is reported.
- Scenarios (SCN-1 to SCN-5) are conditional futures, not forecasts.
- Comparisons the audit marks invalid are not made; they are listed in the competitor comparison.
- Where a bet's decision or size differs between the v1 bets file and the Director record, the deliverables say "v2 per Director decision record".

## Known limits

- The bet-level v2 sizes for BET-02 and BET-07, and the v2 horizon split beyond H1, are not in the Director record; the deliverables use the council memo's arithmetic and say so.
- The constrained and ambitious portfolios are v2 figures (rescaled by A11c-bis).
- BET-18's A-M template is not yet written.
- Takeda's Gate 1 verdict was FAIL (repairable); v1.1 repairs are applied and a re-audit is pending.

## How to regenerate

1. Update the evidence: `python3 scripts/validate_registries.py` (expect PASS at 524 sources and 1,401 claims) after any registry change; new claims go through the append-only registry process, not through these files.
2. Update the strategy: run the A11c-bis pass so the strategy files in `strategy/` match the Director record; refresh [strategy/data](../strategy/) if the contract requires it.
3. Re-run the A16 brief ([WAVE5_A16_deliverables.md](../research_methodology/briefs/WAVE5_A16_deliverables.md)) against the updated inputs. Respect the word limits (summary 1,800; comparison 2,500; strategy 3,000; roadmap 2,500; recommendations 1,500).
4. Check links with `python3 scripts/check_links.py` and re-count distinct claim IDs against the registry.

## How to read / evidence standard

524 sources, 1,401 claims, cutoff 2026-11-21. Audit results: Gate 1 passed Lilly, conditionally passed J&J and AbbVie, and failed Takeda as repairable ([verdicts](../quality/citation_audits/gate1_verdicts.md)). Wave-1 scorecard: A1 Lilly 13/16, A2 J&J 14/16, A3 AbbVie 12/16, A9 12/16 and A4 13/16 accepted; A5 Takeda 11/16 and A6 9/16 marked REVISE ([wave 1](../quality/evaluation_results/wave1_scorecard.md)). Wave-2/3 scorecard: A12 13/16 and A14 13/16 accepted; strategy shard 12/16 accepted; A8 policy 9/16 and A7 commercial 11/16 marked REVISE ([wave 2](../quality/evaluation_results/wave2_scorecard.md)). Independent corroboration is recorded on 2 of 1,401 claims, and most company claims rest on a single interested source. The challenge record ran 119 council verdicts (45 support, 64 conditional, 10 oppose) and a 95-item uncertainty register.
