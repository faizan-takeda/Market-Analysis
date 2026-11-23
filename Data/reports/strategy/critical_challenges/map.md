# critical_challenges map (A11e, wave 5)

Research cutoff 2026-11-21. Independent Strategic Council and red team. Challenges the 17 bets in `strategy/data/strategy_bets.json`; does not edit bets, portfolios or roadmap. No registry writes.

| File | Purpose |
|---|---|
| [council_reviews.md](council_reviews.md) | Seven councils by 17 bets (119 verdicts with rationale, unresolved items and claim IDs), verdict matrix, disagreements log, unresolved assumptions. |
| [red_team.md](red_team.md) | Strongest case against each bet, evidence, what must be true to survive, kill criteria, exposure rating. |
| [counterarguments_and_uncertainty.md](counterarguments_and_uncertainty.md) | View 12 content: 95 items (CA-001 to CA-095) across unsupported assumptions, unresolved questions, conflicting sources, public-knowledge gaps, failed hypotheses, alternative interpretations and caveats. |
| [scenario_stress_test.md](scenario_stress_test.md) | Council re-rating of the five scenarios, which bets break, SCN-5 numbers, leverage arithmetic, three added stress cases, robust core, capital timing against the Entyvio window. |
| [decision_memo_to_director.md](decision_memo_to_director.md) | Ten ranked proposed decision changes with evidence, dissent and envelope effect. |
| `../data/council_reviews.json` | 119 reviews and 17 disagreements, contract shape in `DATA_CONTRACT.md`. |
| `../data/counterarguments.json` | 95 items, contract shape in `DATA_CONTRACT.md`. |

## Build and validation

- `_data_reviews.py`, `_data_redteam.py`, `_data_counter.py`: source text for the three JSON and markdown outputs.
- `_build.py`: writes `council_reviews.json`, `counterarguments.json`, `council_reviews.md`, `red_team.md`, `counterarguments_and_uncertainty.md`; fails if any CLM id is absent from `claims_registry.jsonl`, any ASM id is absent from `assumptions.json`, a bet is missing a council, or a verdict is invalid.
- `_build_stress.py`: writes `scenario_stress_test.md` from `scenarios.json`, `strategy_bets.json` and the council's re-rating table.
- `_check_council.py`: runs the strategy's `_check_ids.py` logic over these files as well (the shipped checker does not scan this directory).

## Conventions

- A verdict is the council's stance on the proposed decision as recorded; for REJECT and DEFER bets, 'support' endorses the REJECT or DEFER.
- 'Council arithmetic' marks calculations made here from registry values and ASM-001; they are not Takeda disclosures.
- Outside-registry knowledge (for example the statutory 12-year biologic exclusivity period, plasma-industry peers, orexin competitors) is labelled and treated as unverified.
