# A11e — Strategic Council challenge, red team and counterarguments (wave 5; fresh context, independent)

Allowed writes: `/Users/palrahma/Desktop/MEDICINE/strategy/critical_challenges/**`, `/Users/palrahma/Desktop/MEDICINE/strategy/data/council_reviews.json`, `/Users/palrahma/Desktop/MEDICINE/strategy/data/counterarguments.json`. You may NOT edit the bets, portfolios or roadmap — you challenge them; the Director decides what changes.

## Inputs
`strategy/DATA_CONTRACT.md` (council_reviews / counterarguments shapes); `strategy/investment_theses/strategic_bets.md` + `strategy/data/strategy_bets.json`; `strategy/financial_cases/*.md`; `strategy/scenarios/*.md`; `strategy/strategic_roadmap/*.md`; `strategy/data/assumptions.json`; Takeda baseline (`New_mediciine/companies/takeda_public_baseline/**`); competitor evidence via `New_mediciine/cross_company_analysis/master_comparison.md` and the registry (grep claim IDs); `industry_transformation/ai_data_robotics/autonomous_lab_reality_check.md`; `quality/evaluation_results/wave1_scorecard.md` and `New_mediciine/evidence_library/conflicts_proposed_A10.jsonl` (evidence weaknesses you can exploit).

## Councils (write each as its own section; each bet gets a verdict support / conditional / oppose with rationale and claim IDs; councils may disagree — record disagreements, do not harmonise)
Scientific (will it materially improve discovery/development/outcomes?), Technology (achievable with credible data/infrastructure? maturity evidence?), Commercial (economic value / durable differentiation?), Capital Allocation (appropriate use of scarce capital vs alternatives incl. buybacks/BD; opportunity cost), Regulatory & Ethics (compliance, patient safety, responsible AI), Competitive Red Team (why competitors win anyway; what Lilly/J&J/AbbVie/tech-native entrants do to this bet), Takeda Execution (compatible with publicly observable capabilities/priorities, incl. the JPY 200bn cost programme and the 2026 CEO transition?).

## Deliverables
- `critical_challenges/council_reviews.md` (7 councils × all bets; disagreements log; unresolved assumptions)
- `critical_challenges/red_team.md` (attack each bet: strongest case against; evidence; what would have to be true for the bet to survive; kill criteria)
- `critical_challenges/counterarguments_and_uncertainty.md` — the View-12 content: unsupported assumptions, unresolved questions, conflicting sources (from conflicts_proposed_A10 and registry `contrary_evidence`), public-knowledge gaps (IVB backlog), failed strategic hypotheses (incl. competitor failures that warn against a bet, e.g., Strateos lab divestment, emraclidine, Recursion terminations), alternative interpretations, caveats behind each recommendation.
- `critical_challenges/scenario_stress_test.md` — for each scenario in `scenarios.json`, which bets break; combined downside; what the "robust core" is.
- `strategy/data/council_reviews.json`, `strategy/data/counterarguments.json` (validate JSON; every claim id must exist — reuse `strategy/data/_check_ids.py`).
- `critical_challenges/decision_memo_to_director.md` — concrete proposed changes to decisions (e.g., "BET-07 BUILD → EXPERIMENT because …"), ranked, each with evidence.
- `map.md`.

## Rules
Independent: do not accept the bets' own evidence summaries; re-check claim IDs. Be specific, not generic ("AI is hyped" is not a critique; "no outcome evidence exists for any of the 14 A6 cards after ≥2 years" is). Budget 400 tool calls. Completion report: FILES WRITTEN / VERDICT MATRIX (bet × council) / TOP 10 CHALLENGES / PROPOSED DECISION CHANGES.
