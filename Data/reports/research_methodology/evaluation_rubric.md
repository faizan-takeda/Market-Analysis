# Evaluation rubric (the fixed evaluator — do not edit to make a batch pass)

Score each axis 0 (fails), 1 (partial), 2 (meets). Write one sentence of justification per axis. A batch is ACCEPT if no axis is 0 and total >= 12/16; REVISE if total 9-11 or any single 0 that is repairable; RESEARCH_FURTHER if coverage or corroboration is 0; BLOCKED if sources are inaccessible.

| Axis | 0 | 1 | 2 |
|---|---|---|---|
| Source authenticity | invented or unverifiable sources | all sources exist, some metadata-only | all cited sources opened, passages stored |
| Relevance | material off-topic | mostly on question | each source maps to a sub-question |
| Coverage | mandatory source families missing | most families covered, gaps listed | all families attempted, gaps explained |
| Independence of corroboration | single interested source for key claims | key claims have 2 sources incl. one independent | key claims corroborated by T1/T3 |
| Temporal accuracy | periods mixed/wrong | minor ambiguity | period/currency/basis explicit |
| Contradiction handling | conflicts ignored | conflicts noted | conflicts recorded in conflicts.jsonl with resolution or `unresolved` |
| Traceability | claims lack IDs | most claims cite IDs | every material sentence cites CLM, each CLM cites SRC with locator |
| Significance | lists announcements | explains mechanism for some | explains problem->investment->capability->outcome->moat with evidence |

Hypothesis statuses: SUPPORTED / PARTIALLY_SUPPORTED / CONTRADICTED / INCONCLUSIVE / NEEDS_MORE_RESEARCH.
No numeric confidence percentages. Use the ordinal scores and the written rationale.

## Golden-question protocol
Answer only from the encyclopedia (registries + reports). For each answer list claim IDs. An auditor checks each cited claim's statement and source. Record: answered_fully / answered_partially / not_answerable / confabulation_detected. Negative tests (questions the corpus should not answer) must return not_answerable.
