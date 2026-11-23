# Scenarios 2027-2040 (A11c v2, wave 6)

**Version v2** (A11c-bis, 2026-11-21). The published robustness table is the council's re-rating; the author's v1 rating is kept in a second table. An early-entry stress case (S-A) is added.

Research cutoff 2026-11-21. These are SCENARIOs, not forecasts and not probability-weighted. Each lists the drivers that would signal it and the claim IDs that anchor the driver. The robustness table classifies every bet as robust (value holds or rises), fragile (value falls or spend is stranded), option value (low-cost position that pays only if the scenario occurs) or neutral. The classification is an INTERPRETATION built on the bet design and on competitor evidence; Takeda internal data (IVB-004, IVB-005, IVB-006, IVB-012) could change it.

## Scenarios


### SCN-1 AI materially accelerates R&D

SCENARIO: by about 2031 independent evidence shows AI-planned discovery and development cutting cycle time or raising hit rate at several companies; first-in-human data from AI-designed molecules are positive; compute and models commoditise further.

Drivers and signals:
- Positive first-in-human data from AI-designed molecules (Nabla expected in one to two years) [CLM-006039]
- Independent result from the Lilly-NVIDIA lab [CLM-000281]
- FDA credibility framework finalised [CLM-006046]
- Commodity compute and shared models [CLM-006056]


### SCN-2 AI incremental

SCENARIO: AI delivers productivity gains in documents, operations and decision support but no step change in probability of success or cycle time; no independent outcome appears for platform investments.

Drivers and signals:
- AI-origin Phase 2 success about the same as conventional (secondary citation) [CLM-006049]
- Platform pipelines keep ordinary attrition [CLM-006047]
- No independent outcome for any data platform [CLM-011052]


### SCN-3 Pricing, regulatory and biosimilar pressure intensifies

SCENARIO: Medicare negotiation, most-favoured-nation pricing and PBM private-label biosimilars compress net price faster; Entyvio erosion lands at the high end of ASM-024; Takhzyro and others face negotiated prices.

Drivers and signals:
- Entyvio Medicare price from January 2028 [CLM-007026]
- PBM template formularies preferring biosimilars (CVS Stelara template from 1 July 2026) [CLM-007015]; formulary exclusion can directly reduce usage [CLM-007025]
- Lilly realised prices -15% in Q3 2026 [CLM-014003]
- Government pricing agreements [CLM-008037] [CLM-008015]


### SCN-4 New modalities, care models and tech-native competitors reshape value

SCENARIO: in-vivo cell therapy, siRNA and gene editing move into the clinic; home and digital care models change where value accrues; AI-native biotechs and tech platforms (Isomorphic-type) win partnerships; platforms do not protect single products.

Drivers and signals:
- AbbVie Capstan and ADARx; Lilly Verve; J&J Ambrx at early clinical or concept [CLM-009058] [CLM-009061] [CLM-009010] [CLM-009035]
- Isomorphic raised outside capital [CLM-011014]
- Regeneron EYLEA -42% despite platform [CLM-011017]
- Pear Therapeutics failure shows reimbursement limits for stand-alone digital care [CLM-007045]


### SCN-5 Combined downside

SCENARIO: SCN-2 and SCN-3 together, plus launch slippage for 2026 approvals (inspection findings, payer delays) and Amitiza cash outflow near the full provision; leverage stays near 3x and discretionary spend is cut.

Drivers and signals:
- Amitiza provision JPY 403.5bn, final amount and timing unknown [CLM-005014] [CLM-014048]
- Base revenue still falling at constant rates [CLM-005011]
- Inspection-driven approval delays occurred at Lilly and AbbVie [CLM-012134] [CLM-012112]
- Leverage 2.6x at March 2026, 3.1x at March 2024 [CLM-005005]


**SCN-5 construction.** SCN-5 is the combination of SCN-2 (AI incremental) and SCN-3 (pricing pressure), plus launch slippage and Amitiza cash near the full provision. It is the stress test for the capital-constrained portfolio.


### Stress case S-A: Early Entyvio biosimilar entry (2028-2029) with an Amitiza outcome at or above the provision

STRESS CASE (council-added, adopted in v2; not a forecast): first meaningful U.S. biosimilar entry in 2028-2029 (ASM-038) with the Amitiza outcome at or above the provision (ASM-034). ASM-025's central case (2031) is unchanged; its range is widened to 2028-2032.

Drivers and signals:
- Two biosimilar BLAs under FDA review [CLM-014051]
- Takeda says earlier launches must address patent validity and infringement; some patents expire in 2032 and revocation actions are filed [CLM-005017] [CLM-014050]
- Amitiza provision JPY 403.5bn, outcome open [CLM-005014] [CLM-014048]

| Bet | Rating under S-A | Effect |
|---|---|---|
| BET-04 | neutral | Playbook RM-026 re-dated from 2029 H2 to 2028 H1 at no extra capital so it is not late. |
| BET-05 | robust | Becomes the only replacement in time; PsA readout (May 2027) and launch coverage carry more weight [CLM-005037]. |
| BET-03 | fragile | Payoff 2035-2038 misses the window. |
| BET-06 | fragile | First option-sourced approval 2035 (RM-043) misses the window; capital competes with the bridge. |
| BET-11 | fragile | SC migration before entry raises pharmacy-benefit exposure at the worst moment [CLM-007015]. |
| BET-15 | fragile | A USD 5bn bridge is infeasible at the leverage arithmetic (ASM-119); rejected in v2. |
| BET-18 | neutral | v2 author rating: the channel is the bridge that fits the balance sheet but only within the ASM-119 headroom; Amitiza at or above the provision can close it. |


Only BET-18's S-A rating is a v2 author rating; the others are the council's effects mapped to ratings. S-A is held in `scenarios.json` under `stress_cases`, not as a sixth scenario.

## Robustness by bet (published: council re-rating; author rating in brackets where different)

| Bet | Name | Decision | SCN-1 AI accelerates | SCN-2 AI incremental | SCN-3 pricing pressure | SCN-4 new modalities and models | SCN-5 combined downside | Author rationale |
|---|---|---|---|---|---|---|---|---|
| BET-01 | Governed cross-franchise R&D data and decision layer | BUILD | robust | robust | neutral | robust | **fragile** [neutral] | Cheap enabling layer; value rises with AI success, holds as productivity in SCN-2; neutral under price pressure because it does not defend revenue; vulnerable to being cut in SCN-5 though small. |
| BET-02 | Plasma process-intelligence and fixed-price automation programme | EXPERIMENT | robust | robust | **neutral** [robust] | neutral | **neutral** [robust] | Plasma is outside the biosimilar mechanism; cost per litre matters more when prices fall; independent of AI success. Depends on unvalidated headroom (IVB-006). |
| BET-03 | Orexin science as a multi-asset discovery platform | BUILD | robust | neutral | **neutral** [robust] | neutral | fragile | Diversifies away from Entyvio in SCN-3 and benefits from faster discovery in SCN-1; long-dated spend is first to be cut in the combined downside. |
| BET-04 | Entyvio franchise defence: payer contracting, evidence and lifecycle | BUILD | neutral | robust | **neutral** [robust] | neutral | robust | Directly addresses SCN-3; needed in every scenario with a biosimilar event; unaffected by AI outcomes. |
| BET-05 | Zasocitinib breadth and immunology successor evidence | INVEST | neutral | robust | neutral | neutral | **fragile** [neutral] | Core replacement revenue; robust to AI pace; exposed to class competition and payer terms [CLM-014049]. |
| BET-06 | Option-based external innovation engine incl. new-modality options | PARTNER | neutral | **neutral** [robust] | **neutral** [robust] | robust | **fragile** [robust] | Option structure caps loss, keeps access to new modalities; contingent payments cost nothing without data. |
| BET-07 | Milestone-gated AI-design partnerships (Nabla, Iambic and successors) | PARTNER | **option_value** [robust] | fragile | neutral | option_value | neutral | Pays off if AI works; wasted if AI is incremental; upfronts small; option value if tech-native competitors win. |
| BET-08 | Federated data consortium participation | PARTNER | robust | robust | neutral | neutral | robust | Cheap and reversible. |
| BET-09 | Rented automated data generation (CRO and cloud labs) with ladder triggers | PARTNER | robust | robust | **neutral** [robust] | neutral | robust | Service model avoids fixed cost; useful whatever AI does. |
| BET-10 | Owned autonomous discovery lab (stage 4-5) | REJECT | option_value | fragile | fragile | neutral | fragile | Would only pay off if SCN-1 with demonstrated autonomy; fragile otherwise; rejected now, retained as a trigger option. |
| BET-11 | Drug-device and home/SC administration platform | BUILD | neutral | robust | **fragile** [robust] | neutral | **neutral** [robust] | Convenience formats help retention under price pressure; effect after biosimilar entry unestablished [CLM-007053]. |
| BET-12 | Launch-pathway partnerships and patient-services outcome measurement | EXPERIMENT | neutral | **neutral** [robust] | **neutral** [robust] | **option_value** [robust] | neutral | Launch-pathway learning matters under pricing pressure and new care models. |
| BET-13 | Neutral rare-disease or plasma real-world data registry | DEFER | option_value | neutral | neutral | **option_value** [robust] | fragile | Option value on data value; fragile when capital is cut. |
| BET-14 | TuneLab-style productised external model platform | REJECT | option_value | fragile | fragile | fragile | fragile | Needs unmeasured advantage and external demand; fragile everywhere else. |
| BET-15 | Large asset purchase (USD 5bn or more) as LOE bridge | REJECT | neutral | **neutral** [robust] | **fragile** [option_value] | neutral | fragile | Needed as a bridge if replacement slips; option value under pricing pressure; fragile when leverage and Amitiza bind. |
| BET-16 | U.S. cash-pay direct-to-patient channel | REJECT | fragile | fragile | fragile | neutral | fragile | Poor structural fit; fragile where cash-pay rules tighten. |
| BET-17 | AI use-case measurement, decision support and reskilling | EXPERIMENT | robust | robust | neutral | neutral | robust | Cheap discipline that prunes spend in every scenario. |
| BET-18 | Phase 2/3 in-licensing channel | PARTNER | neutral | neutral | fragile | option_value | fragile | v2 addition rated by the author (not council-rated): neutral where AI pace is irrelevant, option value under new modalities, fragile when pricing pressure lowers free cash flow and when leverage binds. |


The council re-rated 19 of 85 cells (22%) for BET-01 to BET-17; reasons are in `scenarios.json` (`council_notes`) and in [scenario_stress_test.md](../critical_challenges/scenario_stress_test.md). BET-18 is a v2 addition rated by the author only. The council's ratings describe the v1 decisions; the v2 decisions (BET-02 EXPERIMENT, BET-06 and BET-03 resized, BET-15 REJECT) address several of the flagged cells but the published ratings are not re-rated.

### Author rating (v1, kept for transparency)

| Bet | Name | SCN-1 | SCN-2 | SCN-3 | SCN-4 | SCN-5 |
|---|---|---|---|---|---|---|
| BET-01 | Governed cross-franchise R&D data and decision layer | robust | robust | neutral | robust | neutral |
| BET-02 | Plasma process-intelligence and fixed-price automation programme | robust | robust | robust | neutral | robust |
| BET-03 | Orexin science as a multi-asset discovery platform | robust | neutral | robust | neutral | fragile |
| BET-04 | Entyvio franchise defence: payer contracting, evidence and lifecycle | neutral | robust | robust | neutral | robust |
| BET-05 | Zasocitinib breadth and immunology successor evidence | neutral | robust | neutral | neutral | neutral |
| BET-06 | Option-based external innovation engine incl. new-modality options | neutral | robust | robust | robust | robust |
| BET-07 | Milestone-gated AI-design partnerships (Nabla, Iambic and successors) | robust | fragile | neutral | option_value | neutral |
| BET-08 | Federated data consortium participation | robust | robust | neutral | neutral | robust |
| BET-09 | Rented automated data generation (CRO and cloud labs) with ladder triggers | robust | robust | robust | neutral | robust |
| BET-10 | Owned autonomous discovery lab (stage 4-5) | option_value | fragile | fragile | neutral | fragile |
| BET-11 | Drug-device and home/SC administration platform | neutral | robust | robust | neutral | robust |
| BET-12 | Launch-pathway partnerships and patient-services outcome measurement | neutral | robust | robust | robust | neutral |
| BET-13 | Neutral rare-disease or plasma real-world data registry | option_value | neutral | neutral | robust | fragile |
| BET-14 | TuneLab-style productised external model platform | option_value | fragile | fragile | fragile | fragile |
| BET-15 | Large asset purchase (USD 5bn or more) as LOE bridge | neutral | robust | option_value | neutral | fragile |
| BET-16 | U.S. cash-pay direct-to-patient channel | fragile | fragile | fragile | neutral | fragile |
| BET-17 | AI use-case measurement, decision support and reskilling | robust | robust | neutral | neutral | robust |
| BET-18 | Phase 2/3 in-licensing channel | neutral | neutral | fragile | option_value | fragile |

### What breaks in each scenario (published ratings, v2 balanced sizes)

| Scenario | Fragile bets | Balanced USD m in fragile bets (ceiling) | Robust bets | Balanced USD m in robust bets |
|---|---|---|---|---|
| SCN-1 | BET-16 | 0 | BET-01, BET-02, BET-03, BET-08, BET-09, BET-17 | 980 |
| SCN-2 | BET-07, BET-10, BET-14, BET-16 | 80 | BET-01, BET-02, BET-04, BET-05, BET-08, BET-09, BET-11, BET-17 | 1,190 |
| SCN-3 | BET-10, BET-11, BET-14, BET-15, BET-16, BET-18 | 190 | none | 0 |
| SCN-4 | BET-14 | 0 | BET-01, BET-06 | 500 |
| SCN-5 | BET-01, BET-03, BET-05, BET-06, BET-10, BET-13, BET-14, BET-15, BET-16, BET-18 | 980 | BET-04, BET-08, BET-09, BET-17 | 390 |

### Capital-constrained portfolio under SCN-5 (published ratings, v2 constrained sizes)

| SCN-5 rating | Bets | Constrained USD m (of 1,130) | Share |
|---|---|---|---|
| robust | BET-04, BET-08, BET-09, BET-17 | 260 | 23% |
| neutral | BET-02, BET-07, BET-11, BET-12 | 310 | 27% |
| fragile | BET-01, BET-03, BET-05, BET-06, BET-10, BET-13, BET-14, BET-15, BET-16, BET-18 | 560 | 50% |
| option_value | none | 0 | 0% |


## Reading the table *(INTERPRETATION)*

- **SCN-3 (pricing, regulatory and biosimilar pressure):** under the published ratings no bet is robust. BET-04 is needed but its value holds only as delay: the January 2028 Medicare price is statutory and PBM private-label biosimilars route around contracts [CLM-007026] [CLM-007015]. BET-11 is fragile because SC moves patients into the pharmacy benefit.
- **SCN-2 (AI incremental) is the base case for AI spending:** no independent outcome exists for any AI platform [CLM-011052]. BET-07 is fragile there; its v2 size is small and its tranches are gated.
- **SCN-5 (combined downside):** about half of the v2 constrained envelope (50%) sits in bets the council rates fragile (table above); BET-03 and BET-05 stay funded as floors because they act inside or after the Entyvio window and nothing else replaces them.
- **Early entry (S-A):** BET-05 is the only replacement in time; BET-03 and BET-06 payoff misses the window; the playbook is moved to 2028 H1 (RM-026) and the bridge is BET-18 within the leverage headroom (ASM-119).
- **Option value:** BET-10 (rejected) only pays off if SCN-1 shows demonstrated autonomy; the operational trigger set keeps that option at zero capital [CLM-011066].

## Timing: what needs an early start and what can wait

**Early start (capability building takes years or dates are fixed):**

- BET-04 Entyvio franchise defence: payer contracting, evidence and lifecycle: Fixed external dates: benefit-channel gate 2027 H1, January 2028 negotiation [CLM-007026], biosimilar reviews and possible 2028-2029 entry [CLM-014051], 2032 patents [CLM-005017].
- BET-02 Plasma process-intelligence and fixed-price automation programme: Baseline, demand-versus-capacity test and plasma-peer benchmark take 2-3 years; the network decision should precede capacity commitments [CLM-005065].
- BET-03 Orexin science as a multi-asset discovery platform: Discovery to a second asset takes many years (INTERPRETATION); delay moves refill beyond 2035.
- BET-01 Governed cross-franchise R&D data and decision layer: Thin slice must exist before stage-3 automation or AI-design benchmarking.
- BET-17 AI use-case measurement, decision support and reskilling: Baselines must exist before any value claim; cheap.
- BET-05 Zasocitinib breadth and immunology successor evidence: Regulatory dates drive timing [CLM-005035] [CLM-005037].
- BET-06 Option-based external innovation engine incl. new-modality options: Option pipeline needs 5-10 years to show approvals [CLM-009097].
- BET-11 Drug-device and home/SC administration platform: Device development cycles and approvals [CLM-007042].
- BET-12 Launch-pathway partnerships and patient-services outcome measurement: Attach to the oveporexton launch (approved 2026-08-05 [CLM-005029]); a 2027 H2 pilot is late, so the start moves to 2027 H1.

**Can be postponed (or is triggered):**

- BET-13 Neutral rare-disease or plasma real-world data registry: Needs BET-12 data; revisit 2029.
- BET-10 Owned autonomous discovery lab (stage 4-5): Triggers not yet fired.
- BET-14 TuneLab-style productised external model platform: No measured advantage.
- BET-07 Milestone-gated AI-design partnerships (Nabla, Iambic and successors): Scale only after first-in-human data; existing alliances continue.
- BET-09 Rented automated data generation (CRO and cloud labs) with ladder triggers: Stage-3 pilot waits on triggers; stage 1-2 can start now.
- BET-08 Federated data consortium participation: Cheap; can start any time but value rests on BET-01.
- BET-18 Phase 2/3 in-licensing channel: Triggered: no deal before the leverage test passes (ASM-033, IVB-012); policy and ceiling set 2027 H2.
- BET-15 Large asset purchase (USD 5bn or more) as LOE bridge: Rejected as framed; replaced by BET-18.


## Scenario signals to monitor (annual portfolio review)

| Signal | Scenario | Source of evidence |
|---|---|---|
| Nabla first-in-human data, positive or negative | SCN-1 vs SCN-2 | [CLM-006039] |
| Independent outcome from Lilly-NVIDIA lab or LillyPod | SCN-1 | [CLM-000281] [CLM-006007] |
| Entyvio biosimilar approvals and PBM template changes | SCN-3 | [CLM-014051] [CLM-007015] |
| Negotiated-price outcomes after January 2028 | SCN-3 | [CLM-007026] |
| First clinical outcomes of in-vivo CAR-T or siRNA programmes | SCN-4 | [CLM-009058] [CLM-009061] |
| Amitiza judgment and cash timing; leverage ratio | SCN-5 | [CLM-014048] [CLM-005005] |


## Changes from v1 (scenarios)

This file is **v2**. It implements strategy/critical_challenges/DIRECTOR_DECISION_RECORD.md (2026-11-21). Each change cites its decision-record row (row numbers 1-10 are the table rows; '—' rows are the unnumbered rows).

- Row 1: BET-15 DEFER -> REJECT as framed (fails the 3.0x leverage ceiling by council arithmetic, ASM-119); its stage gates are removed and its roadmap milestones move to BET-18.
- Row 1: New BET-18 'Phase 2/3 in-licensing channel' (PARTNER, secondary INVEST; USD 0.5-2bn contingent on IVB-012 and ASM-033; ASM-118 to ASM-120) with a complete A-M template labelled 'v2 addition (council-proposed)'; USD 0 committed, contingent pool 500 / 1,030 / 2,000.
- Row 2: ASM-025 range widened 2030-2032 -> 2028-2032 (central 2031 unchanged); ASM-038 early-entry stress case; stress case S-A added to scenarios; RM-026 moved 2029 H2 -> 2028 H1 and RM-031 to 2028 H2 (earliest window).
- Row 8: BET-11 stays BUILD; baseline first; BET-04 channel conflict stated and wired (RM-013 depends on RM-003); confidence -> hypothesis.
- Row 10: Six bets (BET-04, 05, 08, 09, 11, 16) relabelled evidence_backed -> hypothesis (BET-11 also in row 8).
- Row — (re-rating): Published robustness table is the council's re-rating (19 of 85 cells changed); the strategy author's v1 rating is kept as a second column.
- Row — (owned labs): 'Owned labs fail' narrative softened for BET-09 and BET-10: Lilly's reason undisclosed, the Strateos link unsupported, the NVIDIA joint lab reads as re-platforming; BET-10 stays REJECT with an operational trigger set (T1-T3).
