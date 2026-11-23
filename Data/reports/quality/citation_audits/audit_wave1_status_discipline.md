# A10 audit: status discipline (Task 3)

Date 2026-11-21. Scope: all 1,110 claims in `claims_registry.jsonl`. Proposals only; no registry edits.

## Summary

| Check | Count | Reading |
|---|---|---|
| FACT + SUPPORTED, every source T2, `single_interested_source` not set, no independent corroboration | 8 | Propose flag (all J&J). |
| FACT whose statement contains interpretive wording | 0 needing retype | 28 keyword hits were reviewed; all are quotations, source field names ("indications", "signals" in "no new safety signals") or attributed company statements. Wave-1 shards separate FACT and INTERPRETATION well (47 INTERPRETATION, 4 HYPOTHESIS, 3 RECOMMENDATION). |
| AI / robotics claims (domain `data_ai`, `robotics_automation`, or shard A6) with no `maturity` | 24 | Propose tags (below). |
| SUPPORTED claims whose only support is a `metadata_only` source | 0 | Agents already downgraded. 6 SUPPORTED/PARTIAL claims mix a metadata_only source with retrieved ones (below). |
| Maturity tags not justified by the cited evidence | 6 | Propose retag (below and conflicts_proposed_A10.jsonl). |
| Absence-of-evidence statements typed FACT | 9 | All INCONCLUSIVE or flagged in the statement; recommend a distinct `gap` record type instead of FACT. |
| Sources `retrieved` with neither `inspected_passage` nor a stored text file | 4 non-API (SRC-000029, -000031, -000032, -000035) | Protocol says `retrieved` requires `inspected_passage`. SRC-000031/-000035 have a raw HTML copy; SRC-000029 and -000032 have nothing preserved. |

## 1. FACT + SUPPORTED resting only on company (T2) sources, not flagged
These record that a company said or announced something (valid FACT about the statement), but any outcome-type wording relies on an interested party. Propose `single_interested_source: true`.

| Claim | Statement (start) |
|---|---|
| CLM-002037 | On 2025-10-14 J&J announced its intent to separate its Orthopaedics business as a standalone company, DePuy Synthes, citing a shift of MedTech toward  |
| CLM-002039 | On 2025-03-06 J&J announced it would discontinue the Phase 3 VENTURA programme of aticaprant (adjunctive MDD) 'due to insufficient efficacy in the tar |
| CLM-002040 | On 2023-08-23 J&J announced final results of the Kenvue exchange offer: 800,449,685 J&J shares were tendered, 190,955,436 accepted (proration factor 2 |
| CLM-002041 | J&J stated at closing of Intra-Cellular (2025-04-02) that the deal would add approximately USD 0.7bn of 2025 sales (about +0.8% growth), dilute 2025 a |
| CLM-002044 | J&J MedTech paused all U.S. VARIPULSE (pulsed field ablation) cases on 2025-01-05 after four neurovascular events in the U.S. External Evaluation (mor |
| CLM-002060 | In Q3 2026 (quarter reported 2026-10-13) J&J's reported sales were USD 25,399m (+5.9%; operational +6.0%): Innovative Medicine USD 16,757m (+7.7%; STE |
| CLM-002061 | J&J raised its FY2026 guidance on 2026-10-13 to estimated reported sales of USD 101.0-101.4bn (midpoint USD 101.2bn, +7.4%) and adjusted EPS of USD 11 |
| CLM-002064 | J&J announced on 2026-08-04 that Jennifer Taubert (EVP, Worldwide Chairman Innovative Medicine since 2018) will retire and be succeeded effective 2026 |

Note on tiering consistency: Takeda's H1 FY2026 Kessan Tanshin (SRC-005015, company results filed with the exchange) is tiered T1, while J&J's Q3 2026 earnings release (CLM-002060/2061) is T2. Both are company-issued results documents. Apply one rule (suggest T2 for earnings releases, T1 for audited statements and regulator-filed forms).

## 2. Interpretive language typed as FACT
No claim needs retyping. Borderline cases that should keep the quotation marks in the statement: CLM-003052 ("best-in-class" attributed to the announcement), CLM-009050 (J&J "claims more than 150 partnerships"), CLM-006025 ("competitive advantage" inside a risk-factor paraphrase). Three claims whose FACT type is correct but whose downstream use is interpretive: CLM-006026 (VELYS pull-through), CLM-006020 (2.6x enrollment) and CLM-000286 (only OTTAVA regulator-verified).

## 3. AI / robotics claims without a maturity tag

| Claim | Shard | Proposed maturity | Basis |
|---|---|---|---|
| CLM-000246 | RUN-0002 | not_applicable | capex, not an AI claim (domain mis-assigned) |
| CLM-000252 | RUN-0002 | unknown | statement only lists initiatives/risk language; no deployment evidence |
| CLM-000278 | RUN-0002 | concept | statement only lists initiatives/risk language; no deployment evidence |
| CLM-000279 | RUN-0002 | not_applicable | plasma centres, not AI |
| CLM-000286 | RUN-0003 | operational | only OTTAVA has regulator-verified milestone |
| CLM-006015 | A6_ai_robotics | unknown | statement only lists initiatives/risk language; no deployment evidence |
| CLM-006025 | A6_ai_robotics | unknown | statement only lists initiatives/risk language; no deployment evidence |
| CLM-006036 | A6_ai_robotics | unknown | statement only lists initiatives/risk language; no deployment evidence |
| CLM-006045 | A6_ai_robotics | concept | statement only lists initiatives/risk language; no deployment evidence |
| CLM-006046 | A6_ai_robotics | not_applicable | regulatory draft guidance |
| CLM-006050 | A6_ai_robotics | pilot | statement only lists initiatives/risk language; no deployment evidence |
| CLM-006053 | A6_ai_robotics | not_applicable | comparison/interpretation |
| CLM-006054 | A6_ai_robotics | operational | statement only lists initiatives/risk language; no deployment evidence |
| CLM-006057 | A6_ai_robotics | not_applicable | deal-cost summary |
| CLM-006058 | A6_ai_robotics | not_applicable | recommendation |
| CLM-006059 | A6_ai_robotics | not_applicable | recommendation |
| CLM-005049 | A5_takeda | prototype | statement only lists initiatives/risk language; no deployment evidence |
| CLM-005054 | A5_takeda | concept | statement only lists initiatives/risk language; no deployment evidence |
| CLM-005062 | A5_takeda | unknown | statement only lists initiatives/risk language; no deployment evidence |
| CLM-005063 | A5_takeda | not_applicable | plasma centres |
| CLM-005065 | A5_takeda | not_applicable | plasma site expansion |
| CLM-005066 | A5_takeda | not_applicable | site list |
| CLM-005067 | A5_takeda | not_applicable | absence of evidence |
| CLM-005068 | A5_takeda | not_applicable | plasma supply statement |

Several of these were tagged by the domain list rather than by content (plasma, capex). Proposal: remove `data_ai`/`robotics_automation` from CLM-000246, CLM-000279, CLM-005063, CLM-005065, CLM-005066, CLM-005068, or tag them `not_applicable`.

## 4. Maturity tags to change

| Claim | Current | Proposed | Why |
|---|---|---|---|
| CLM-006026 | SCALED | operational | 10-K reports VELYS "pull through" but no system/procedure counts |
| CLM-006022 | SCALED | not_applicable | training completions (30,000 / 47,000 of 130,000+), not an AI application at scale |
| CLM-006047 | DEMONSTRATED_OUTCOME | not_applicable | Recursion programme terminations; not one of the four companies |
| CLM-006049 | DEMONSTRATED_OUTCOME | not_applicable | industry analyses, discontinued programmes at Exscientia/BenevolentAI |
| CLM-006051 | DEMONSTRATED_OUTCOME | not_applicable | Ginkgo/Zymergen deal |
| CLM-006020 | OPERATIONAL | pilot (self-reported) | one interview figure, no baseline or method |
| CLM-006004 | OPERATIONAL | operational (hardware) | keep, but note: no scientific output disclosed |

Also: maturity values are stored upper-case (OPERATIONAL, PILOT, ...) whereas `agent_protocols.md` lists lower-case enums; normalise. The A1 claims CLM-001056..001060 carry DEMONSTRATED_OUTCOME for Phase 3 drug trial results: that is a clinical outcome, not AI maturity (the field was designed for AI/data/robotics). Consider `not_applicable`.

## 5. Claims citing metadata_only sources
No SUPPORTED claim relies on a metadata_only source alone. Mixed cases to re-read: CLM-006029, CLM-006059, CLM-009015, CLM-003072, CLM-003081, CLM-008040. Claims left PARTIALLY_SUPPORTED/INCONCLUSIVE solely because their source is metadata_only although the page is retrievable (A10 opened them): CLM-000284 (J&J OTTAVA), CLM-009028 (CDD TuneLab data points, confirmed), CLM-009055 (BioPharma Dive headline, confirmed). Propose re-registering SRC-000034, SRC-009022 and SRC-009017 as `retrieved` with the inspected passage and upgrading CLM-009028 and CLM-009055 to SUPPORTED (FACT about the vendor blog / headline only).

## 6. Absence claims
CLM-005052, -005067, -005070, -005072, -005080, -007039, -014057 record searches that found nothing. They are correctly INCONCLUSIVE. Typing them FACT mixes "a document says X" with "I could not find X"; use a gap record. CLM-014057 (no primary Strateos/Multiply Labs release) is consistent with this audit: CLM-006015 should stay NEEDS_MORE_RESEARCH.
