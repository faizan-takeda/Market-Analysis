# Strategic bets for Takeda, 2027-2040 (A11c v2, wave 6)

**Version v2** (A11c-bis, 2026-11-21): revised to the Director's decision record [DIRECTOR_DECISION_RECORD.md](../critical_challenges/DIRECTOR_DECISION_RECORD.md). v1 sizes, decisions and labels are listed in the Changes section below.

Research cutoff 2026-11-21. Takeda fiscal years run April-March (FY2025 = April 2025 to March 2026); Takeda amounts stay in JPY unless converted at ASM-001 for sizing only. This file proposes candidates; it does not endorse any of them. Eighteen candidates are assessed on a common template A-M (BET-18 is a v2 addition, council-proposed); five carry a decision other than BUILD, PARTNER, INVEST or EXPERIMENT (four REJECT, one DEFER) so the reader can see the alternatives that were considered and set aside.

**Labels.** FACT (registry claim), INTERPRETATION (reading of facts), HYPOTHESIS (reasoned, needs non-public data), SCENARIO (conditional future), RECOMMENDATION (proposed action). ASSUMPTION marks any number that is not a registry claim; each carries an ASM- id defined in [assumptions_register.md](../financial_cases/assumptions_register.md) and `strategy/data/assumptions.json`. Takeda's budget, headcount and internal data are not public (IVB-014); no figure here is a Takeda budget.

**Audit corrections honoured.** Takeda cell-therapy impairment is JPY 58.2bn (JPY 58.0bn was the earlier expectation) [CLM-005025]; the restructuring-cost series is about JPY 150bn, 170.0bn, then 160.0bn [CLM-005078]; Morphic headline USD 3.2bn versus audited charge 2.55bn [CLM-009002]; OTTAVA installation is announced, not shown complete [CLM-000284]; the Strateos link and 2020 date for Lilly's lab are unsupported [CLM-006017]; the 'no independent outcome' claim is worded more strongly than its sources support [CLM-006054]; J&J AI metrics are self-reported [CLM-006020] [CLM-006022]; AbbVie ImmunoGen is USD 9.2bn net of cash [CLM-003086]. **Invalid comparisons not used:** the share of FY2025 revenue from post-2021 molecules is not used as a productivity ranking; deal values across companies are not summed; Takeda capex including intangibles is not compared with Lilly property, plant and equipment capex; a Takeda revenue-share-from-new-molecules figure is not computable [CLM-012013] [CLM-009098] [CLM-005007].

## Summary


| ID | Bet | Decision | Confidence | Baseline class | Horizon | Balanced USD m 2027-40 (ASSUMPTION) | Hard prerequisites |
|---|---|---|---|---|---|---|---|
| BET-01 | Governed cross-franchise R&D data and decision layer | BUILD | hypothesis | EXISTING_BUT_UNDERDEVELOPED | H1 | 200 | none |
| BET-02 | Plasma process-intelligence and fixed-price automation programme | EXPERIMENT | hypothesis | EXISTING_STRENGTH | H1 | 230 | none |
| BET-03 | Orexin science as a multi-asset discovery platform | BUILD | hypothesis | EXISTING_STRENGTH | H2 | 300 | none |
| BET-04 | Entyvio franchise defence: payer contracting, evidence and lifecycle | BUILD | hypothesis | EXISTING_STRENGTH | H1 | 140 | none |
| BET-05 | Zasocitinib breadth and immunology successor evidence | INVEST | hypothesis | EXISTING_BUT_UNDERDEVELOPED | H1 | 180 | none |
| BET-06 | Option-based external innovation engine incl. new-modality options | PARTNER | hypothesis | EXISTING_STRENGTH | H2 | 300 | none |
| BET-07 | Milestone-gated AI-design partnerships (Nabla, Iambic and successors) | PARTNER | hypothesis | EVIDENCE_GAP | H2 | 80 | BET-01, BET-09 |
| BET-08 | Federated data consortium participation | PARTNER | hypothesis | EXISTING_BUT_UNDERDEVELOPED | H1 | 35 | none |
| BET-09 | Rented automated data generation (CRO and cloud labs) with ladder triggers | PARTNER | hypothesis | EVIDENCE_GAP | H1 | 95 | none |
| BET-10 | Owned autonomous discovery lab (stage 4-5) | REJECT | hypothesis | EVIDENCE_GAP | H3 | 0 | BET-01, BET-09, BET-07 |
| BET-11 | Drug-device and home/SC administration platform | BUILD | hypothesis | EXISTING_STRENGTH | H1 | 190 | none |
| BET-12 | Launch-pathway partnerships and patient-services outcome measurement | EXPERIMENT | hypothesis | EVIDENCE_GAP | H1 | 50 | none |
| BET-13 | Neutral rare-disease or plasma real-world data registry | DEFER | hypothesis | POTENTIAL_NEW_CAPABILITY | H2 | 0 | BET-01, BET-12 |
| BET-14 | TuneLab-style productised external model platform | REJECT | hypothesis | POTENTIAL_NEW_CAPABILITY | H3 | 0 | BET-01 |
| BET-15 | Large asset purchase (USD 5bn or more) as LOE bridge | REJECT | hypothesis | EXISTING_BUT_UNDERDEVELOPED | H2 | 0 | none |
| BET-16 | U.S. cash-pay direct-to-patient channel | REJECT | hypothesis | EVIDENCE_GAP | H1 | 0 | none |
| BET-17 | AI use-case measurement, decision support and reskilling | EXPERIMENT | hypothesis | EXISTING_BUT_UNDERDEVELOPED | H1 | 120 | none |
| BET-18 | Phase 2/3 in-licensing channel (v2 addition (council-proposed)) | PARTNER/INVEST | hypothesis | EXISTING_STRENGTH | H2 | 0 (+1,030 contingent) | none |


Balanced total 1,920; constrained 1,130; ambitious 3,155 (USD m, cumulative 2027-2040, ASM-002 to ASM-004; v1: 2,950 / 1,590 / 4,975). The balanced total is committed at gates; about USD 1,030m of contingent headroom is reserved for BET-18 (ASM-118) and is not a saving. BET-15 is rejected and outside every envelope.

## Sequencing: does data infrastructure have to come first? *(HYPOTHESIS argued from evidence)*

Three positions are possible: (a) data infrastructure first, then automation; (b) a bounded lab-automation initiative that seeds its own data foundation; (c) both in parallel with a defined hand-off. The evidence supports (c) with a hard gate at stage 3.

- Stages 1-2 of the automation ladder (assisted and scripted high-throughput work) are operational and commodity, and the continuing model is a service: Arctoris runs the former Lilly platform as a CRO and sells data generation to AI customers [CLM-006013] [CLM-006016] [CLM-011062]. A rented initiative (BET-09) therefore produces data without Takeda owning robots, and it can seed a structured assay dataset if a minimal schema is enforced from the first contract. This is a thin slice of BET-01, not the full layer.
- Stage 3 and above (AI planning tied to wet labs) has no independent demonstration [CLM-011062]. Judging it needs a decision log and baselines (BET-01), because without them a vendor claim such as Nabla's three to four week loop cannot be tested against a conventional comparator [CLM-006040]. Zymergen paired automation and ML and sold at about one-tenth of its IPO-era valuation after USD 1.2bn of cumulative net losses [CLM-006051]. (INTERPRETATION)
- The data layer is cheap relative to the cost of automating without it: AbbVie's ARCH was built by fewer than ten full-time staff plus contractors [CLM-006032]. This is one company's example, so the point is about order of magnitude, not a Takeda cost (see ASM-101).
- Plasma operations are the exception: nomogram and process data already exist at site level [CLM-005060], so BET-02 can seed its own data foundation and does not wait for BET-01.

**Dependency chain (hard):** BET-01 and BET-09 (H1 2027) -> BET-07 benchmarking (needs both; RM-020 now depends on RM-015 and RM-018) -> stage-3 pilot only if three triggers fire (independent Lilly-lab result, Nabla first-in-human data, measured CRO cost) [CLM-011066] -> any owned-lab reconsideration (BET-10, rejected now). BET-13 needs BET-01 and BET-12. BET-14 needs BET-01 and a measured advantage. BET-18 is released only after the leverage test (ASM-033, IVB-012) and takes sizing input from BET-05 launch curves. **Soft dependencies:** BET-02 on BET-01 standards from 2028; BET-12 on BET-17.

## Template

A thesis; B future market change; C problem; D evidence (claim IDs); E moat mechanism; F practical architecture; G investment (balanced and the other portfolios, ranges per ASM-036); H time to value; I measurable outcomes; J risks; K strategic options; L decision; M evidence and confidence (known / assumed / needs Takeda internal validation).


---

## BET-01 Governed cross-franchise R&D data and decision layer

**Decision: BUILD** | Horizon H1 | Baseline class: EXISTING_BUT_UNDERDEVELOPED | Confidence: hypothesis

**A. Thesis.** Make Takeda's own trial, real-world, assay and plasma data reusable under one governed layer so that a small number of named decisions (target choice, trial design, supply planning) can be measured against a pre-agreed baseline. (RECOMMENDATION, conditional on IVB-001.)

**B. Future market change.** Competitors are building proprietary data assets and opening them internally: AbbVie ARCH holds 124 TB and opened de-identified data from 2,000+ trials to all R&D; Lilly TuneLab rests on data Lilly estimates cost over USD 1bn [CLM-006032] [CLM-006034] [CLM-000280]. Compute and third-party models are purchasable by rivals, so proprietary data is the one defensible input [CLM-006055]. (INTERPRETATION)

**C. Problem.** Takeda's public record shows a platform and an aspiration but no quantified AI or data outcome [CLM-006045] [CLM-011053]. Without an inventory of products, users and outcomes, spending cannot be linked to value (IVB-001). Whether Takeda's data estate is fragmented as AbbVie's was is unknown (HYPOTHESIS) [CLM-011055].

**D. Evidence.**

- FACT: ARCH was built by fewer than ten full-time staff plus contractors; a governance decision opened trial data to all R&D [CLM-006032] [CLM-006034]. Outcome evidence is a preprint not opened by A6.
- FACT: across ARCH, TuneLab, Polyphonic and the AISB model, none has independent outcome evidence [CLM-011052] [CLM-006054 as corrected by the audit: wording stronger than sources support].
- FACT: Takeda reports 63.4% of workforce using gen-AI tools; this is a usage measure, as are J&J's course completions and unbaselined enrolment multiple [CLM-014043] [CLM-006022] [CLM-006020].
- HYPOTHESIS: one governed layer raises reuse of Takeda's own trial and real-world data if the estate is fragmented [CLM-011055].
- FACT (risk): FDA's January 2025 draft guidance proposes risk-based credibility for AI used in regulatory decisions, so model evidence must be documented [CLM-006046]; Takeda's own 20-F warns models may be flawed or trained on inadequate data [CLM-005054].

*Takeda baseline.* Class 9, enterprise data and AI platform: a Databricks-hosted agent platform for 10,000+ employees exists, outcomes unproven [CLM-005058] [CLM-005080]. Maturity must be assessed first (IVB-001), so this bet extends and governs an existing platform; it does not start a new one.

*Competitor analogues.* ABBV: [CLM-006032] [CLM-006034]; LLY: [CLM-000280] [CLM-006008]

**E. Moat mechanism.** data, learning, workflow_integration. Data and learning: decision-linked data that is costly to regenerate improves each later model and trial design; workflow integration comes from embedding the layer in named decisions. It compounds only if each decision is logged against a baseline so the layer learns from outcomes (INTERPRETATION) [CLM-011082].

**F. Practical architecture.** Build: Governance, data catalogue, decision log and metrics on the existing platform; Reuse policy for de-identified trial and real-world data. Buy: none. License: Commodity data tooling from the existing Databricks relationship [CLM-005058]. Partner: Federated consortia for pooled tasks (BET-08).

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-101).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 40 (30-50) | 50 (30-70) | 30 (20-40) | 120 |
| balanced | 60 (45-75) | 80 (50-110) | 60 (35-85) | 200 |
| ambitious | 90 (70-110) | 130 (80-180) | 120 (70-170) | 340 |


**H. Time to value.** Near term: 12-24 months: production inventory, 2-3 decisions with baselines (closes IVB-001). Long horizon: 2030-2035: model-informed target and trial-design decisions with measured cycle-time or hit-rate effect; 2035-2040: compounding only if measured.

**I. Measurable outcomes.**

- Inventory of data and AI products in production with owner, users, baseline and measured benefit
- Named decisions where a model changed the outcome versus a pre-agreed baseline
- Share of trial data reusable across franchises

**J. Risks.**

- data: Estate may already be well governed, so the incremental value is small (IVB-001).
- regulatory: AI credibility documentation expectations [CLM-006046].
- adoption: Usage is mistaken for value, as in competitor metrics [CLM-006022].
- capital: Platform spend without outcome evidence is hard to stop once started.

**K. Strategic options.** expand, redirect, partner, stop. Expand if two decisions show measured gains by gate 3; redirect to federated use (BET-08) if Takeda data proves too sparse; stop if no baseline can be set.

**L. Decision: BUILD.** Small, ring-fenced and a prerequisite for stage-3 automation and for judging AI partnerships; the maturity assessment (IVB-001) gates the follow-on. Hard prerequisites: none. Sequencing: Start with a thin slice (metadata standards and decision log) in H1 2027 alongside BET-09; the full layer is a hard prerequisite for any stage-3 closed-loop pilot (HYPOTHESIS). Argument: AbbVie built ARCH with fewer than ten staff [CLM-006032], so the data layer costs little relative to running automation without it; Zymergen paired automation and ML and still failed commercially [CLM-006051].

**M. Evidence and confidence (hypothesis).** Known: Platform exists; competitors' data layers exist; no outcomes anywhere [CLM-005058] [CLM-011052]. Assumed: Cost and fragmentation level (ASM-101); that decisions can be baselined. Needs Takeda internal validation: IVB-001, IVB-010, IVB-014 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 7) Roadmap: RM-015 (decision log gate) is now a wired prerequisite of RM-020 (BET-07 stop-or-expand). Size unchanged.


---

## BET-02 Plasma process-intelligence and fixed-price automation programme

**Decision: EXPERIMENT** | Horizon H1 | Baseline class: EXISTING_STRENGTH | Confidence: hypothesis

**A. Thesis.** Test whether donor, yield and process data from the plasma network are a proprietary data class (no plasma peer is in the comparison set, so uniqueness is untested) by funding only a baseline, a demand-versus-capacity test, a plasma-peer benchmark and a one-site shadow-mode tranche before any fixed-price automation or network roll-out. (HYPOTHESIS) [CLM-011056] [CLM-011031]

**B. Future market change.** Plasma-derived therapies sit outside the biosimilar mechanism that threatens Entyvio; immunoglobulins were JPY 790.6bn (18% of FY2025 revenue) with PDT revenue +8.5% AER in H1 FY2026 (-1.5% CER), which does not show that capacity rather than demand binds [CLM-005064]. Lilly's record shows capacity bound a blockbuster until 2024, but that is an obesity-drug analogue, not plasma [CLM-001066] [CLM-000172]. (INTERPRETATION)

**C. Problem.** Whether plasma is a platform strength or only a large business depends on yield per centre and cost per litre, which are not public (IVB-006). Automation in GMP settings carries validation burden and Takeda has one documented warning letter and supply shortage [CLM-005020].

**D. Evidence.**

- FACT: nomogram programmes rolled out across 270+ centres; AI-powered donor tools reported in FY2025 [CLM-005060] [CLM-014046]; 170+ predictive-maintenance agents at Lessines with expansion planned by 2027 (company-reported, no outcome) [CLM-014041].
- FACT: NASA documents record Falcon 9 development at about USD 390m against model estimates of USD 1.7-4.0bn under fixed-price contracts, but the cause of the gap is not isolated and each cargo partner suffered catastrophic failures [CLM-011005] [CLM-011006] [CLM-011008]. Analogy only.
- FACT (counter-evidence): no public evidence of Takeda lab, continuous-manufacturing or manufacturing robotics [CLM-005067]; Lilly's Lebanon robotics were seen on a tour with no performance data [CLM-006002]; Medicine Foundry (USD 4.5bn) is concept [CLM-006000] [CLM-006001].
- HYPOTHESIS: a neutral-capacity or shared-analytics role could follow if spare capacity exists; sponsors guard process and liability [CLM-011041] [CLM-011040].
- FACT: PDT revenue was -1.5% at constant rates in H1 FY2026, so the public record does not show a capacity constraint; a demand-versus-capacity test is a gate [CLM-005064].
- INTERPRETATION: 'no competitor holds this data' holds only because the comparison set has no plasma peer; the registry holds none, so a plasma-peer benchmark is a gate [CLM-011056] [CLM-009091].
- FACT (counter-evidence): fixed-price vendor terms are a NEEDS_MORE_RESEARCH hypothesis and there is no fixed-price vendor evidence for plasma plants [CLM-011031].

*Takeda baseline.* Class 2, plasma network and PDT manufacturing: 233 to 275 centres (FY2022-FY2024), 270+ with adaptive nomograms, 99.6% on-time in-full, USD 230m Los Angeles fractionation expansion; yield and cost per litre are not public (IVB-006) [CLM-005063] [CLM-005060] [CLM-014046] [CLM-005065]. Class 12 manufacturing quality is EXISTING_BUT_UNDERDEVELOPED after the Hikari warning letter [CLM-005020]. This bet builds on a strength; it must first measure headroom.

*Competitor analogues.* LLY: [CLM-001066] [CLM-000172] [CLM-006002]

**E. Moat mechanism.** data, infrastructure, learning, regulatory_experience. Infrastructure and data: fractionation capacity takes years to copy and process data compounds with each batch; learning if yield models are retrained on every lot. Regulatory experience is the support layer: automated steps must be validated, which is slow for rivals and for Takeda (INTERPRETATION) [CLM-011085] [CLM-011039].

**F. Practical architecture.** Build: Process-data capture and yield models; Single-site (Los Angeles) pilot design and acceptance criteria. Buy: none. License: Nomogram and donor-tool vendors already used [CLM-005060]. Partner: Automation vendors on fixed-price, outcome-linked terms [CLM-011031].

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-102).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 25 (20-30) | 55 (35-75) | 45 (25-65) | 125 |
| balanced | 80 (60-100) | 100 (60-140) | 50 (30-70) | 230 |
| ambitious | 65 (50-80) | 170 (100-240) | 160 (95-225) | 395 |


**H. Time to value.** Near term: 2027-2029: yield and cost-per-litre baseline, demand-versus-capacity test, plasma-peer benchmark and a one-site shadow-mode run; remainder released only if all pass. Long horizon: 2030-2035: network roll-out if headroom is shown; 2035-2040: possible neutral analytics offer (low confidence).

**I. Measurable outcomes.**

- Yield per litre of plasma, deviation rate and cost per litre before and after pilot (company-defined)
- On-time in-full held at or above FY2025 99.6% [CLM-014046]
- Inspection record without new observations
- Demand-versus-capacity test result (is plasma demand- or capacity-bound?)
- Plasma-peer benchmark of yield and cost per litre against the ASM-031 threshold re-based on money

**J. Risks.**

- regulatory: GMP validation of automated steps; prior warning letter [CLM-005020].
- execution: Vendor fixed-price terms may not be available at plant complexity.
- data: Donor data capture may be inconsistent across centres (IVB-006).
- capital: Incremental to the base USD 230m expansion; double-counting risk [CLM-005065].
- competition: Plasma peers' data position is unbenchmarked; the uniqueness claim may fail [CLM-011056] [CLM-009091].
- adoption: Demand-bound, not capacity-bound, would remove the case for automation capex [CLM-005064].

**K. Strategic options.** expand, redirect, partner, stop. Expand to a pilot only if the baseline shows headroom and demand is capacity-bound; redirect to other core uses if demand-bound; stop if headroom is below the re-based ASM-031 threshold.

**L. Decision: EXPERIMENT.** Cheap baseline and shadow-mode tranche produces the data the council says is missing; the remainder of the programme is contingent on the demand-versus-capacity test, the plasma-peer benchmark and ASM-031 re-based on money (value of a gain per litre against pilot and run cost). Takeda-execution council dissent recorded: it supports BUILD because the CEO led the PDT unit and the network runs 270+ centres at 99.6% on-time in-full [CLM-005074] [CLM-005063] [CLM-014046]. The red team's call to reject any plasma spend is not accepted. Hard prerequisites: none. Sequencing: Baseline and shadow-mode tranche first (about USD 65m at risk in the first two gates, ASSUMPTION ASM-102); the pilot, roll-out and neutral-analytics decision are contingent. Nomogram and process data already exist at site level [CLM-005060], so the tranche does not wait for BET-01; soft dependency on BET-01 standards from 2028.

**M. Evidence and confidence (hypothesis).** Known: Network scale, capacity expansion, on-time in-full [CLM-005063] [CLM-005065] [CLM-014046]. Assumed: Yield and cost headroom (ASM-031); cost of upgrades (ASM-102). Needs Takeda internal validation: IVB-006, IVB-011, IVB-014 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 4) BUILD -> EXPERIMENT; balanced USD 430m -> 230m (baseline and shadow-mode tranche about USD 65m at risk, remainder contingent); ASM-031 re-based on money; demand-versus-capacity and plasma-peer tests added as gates; Takeda-execution council dissent recorded.


---

## BET-03 Orexin science as a multi-asset discovery platform

**Decision: BUILD** | Horizon H2 | Baseline class: EXISTING_STRENGTH | Confidence: hypothesis

**A. Thesis.** Run orexin biology as a platform with a second differentiated asset, funded at the constrained discovery size, with a Phase 1 gate before the H2 tranche, an additionality test against base R&D and a competitor orexin scan. (HYPOTHESIS) [CLM-011038]

**B. Future market change.** A platform does not protect a single product (Regeneron EYLEA net sales -42% in 2025), so the value of a platform is repeated assets (INTERPRETATION) [CLM-011017] [CLM-011037]. Neuroscience and psychiatry is the common failure site of the window across AbbVie, J&J and Takeda [CLM-003054] [CLM-002039] [CLM-012120].

**C. Problem.** After 2030 the six late-stage programmes carry the pipeline; refill depends on early depth that is not public (IVB-008). TAK-994 was stopped for liver safety, so a second asset is not assured [CLM-005023].

**D. Evidence.**

- FACT: oveporexton approved 2026-08-05 from in-house discovery; efficacy statements are company-reported [CLM-012149] [CLM-005048].
- FACT: TAK-994 stopped (liver-related signal); soticlestat Phase 3 missed (June 2024), JPY 21.5bn impairment [CLM-012119] [CLM-012120] [CLM-009083].
- FACT (analogue): Regeneron built VelociSuite and a genetics centre with over 3 million samples; contribution to approvals is not quantified [CLM-011015] [CLM-011016].
- INTERPRETATION: the lesson from AbbVie, J&J and Takeda is to gate CNS assets on Phase 2 quality and placebo response, and not to infer that orexin success transfers to other CNS bets [CLM-003057] [CLM-012135].
- INTERPRETATION: the orexin discovery team already sits in base R&D (JPY 675.9bn), so the incrementality of the spend cannot be tested without an additionality test [CLM-005004] [CLM-005048].
- FACT (research gap): competitor orexin programmes are not in the registry; a competitor scan is a gate [CLM-005029].

*Takeda baseline.* Class 3, rare disease and orexin science: oveporexton discovered in Shonan, FDA-approved 2026-08-05; Takeda calls itself world leader in orexin science [CLM-005048] [CLM-012149]. Pipeline refill beyond the six late-stage programmes is unknown (IVB-008) [CLM-005044].

*Competitor analogues.* ABBV: [CLM-003054] [CLM-003057]; JNJ: [CLM-002039]

**E. Moat mechanism.** ip, learning, regulatory_experience. IP and learning: disease-biology depth is slow to buy and each asset's clinical data sharpens the next; regulatory experience from a first approval lowers review risk for follow-ons. Compounding requires a second asset and is unproven (HYPOTHESIS) [CLM-011036].

**F. Practical architecture.** Build: Discovery and early clinical team in Shonan with a multi-asset plan. Buy: none. License: Tools and models for design as needed. Partner: Academic and AI-design collaborators milestone-gated (BET-07).

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-103).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 40 (30-50) | 90 (55-125) | 50 (30-70) | 180 |
| balanced | 100 (75-125) | 150 (90-210) | 50 (30-70) | 300 |
| ambitious | 90 (70-110) | 240 (145-335) | 180 (110-250) | 510 |


**H. Time to value.** Near term: 2027-2029: lead-asset selection and indication map. Long horizon: 2032-2037: second asset in late-stage development; 2038-2040: platform proof only if two assets approve.

**I. Measurable outcomes.**

- Number of orexin-class clinical candidates and indications
- Phase 1 to Phase 2 transition rate versus conventional programmes
- Second-asset first-in-human by about 2030 (ASSUMPTION)
- Additionality result: share of the bet's spend that is incremental to base R&D (test design set at the feasibility gate)
- Competitor orexin scan completed before the H2 tranche

**J. Risks.**

- scientific: Orexin success may not generalise; liver safety history [CLM-005023].
- competition: Competitor orexin programmes are not in the registry (research gap, logged in evidence_gaps.md).
- capital: Long-dated and exposed in a downturn.

**K. Strategic options.** expand, redirect, partner, divest, stop. Expand on a clean second-asset Phase 1; partner out indications outside Takeda's depth; stop at gate 2 if no candidate beats a safety criterion.

**L. Decision: BUILD.** Builds on a proven in-house capability, sized at the constrained discovery size (v1 balanced was larger). The Phase 1 gate (second candidate clean through Phase 1, RM-030, target 2030 H1) releases the H2 tranche; an additionality test against base R&D and a competitor scan precede it. Removing BET-03 entirely is not accepted: orexin is Takeda's only evidenced in-house discovery success in the window [CLM-009076] [CLM-005048]. Hard prerequisites: none. Sequencing: Independent of BET-01 data layer; benefits from BET-07 design tools. Start in H1 (discovery to second-asset readiness takes years, INTERPRETATION); H2 tranche only after the Phase 1 gate and the additionality test.

**M. Evidence and confidence (hypothesis).** Known: First approval and in-house origin [CLM-012149] [CLM-005048]. Assumed: That a credible second asset exists (ASM-021, ASM-103). Needs Takeda internal validation: IVB-008, IVB-005 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 5) Balanced USD 500m -> 300m; Phase 1 gate before the H2 tranche (RM-030); additionality test against base R&D and competitor orexin scan added (new RM-052).


---

## BET-04 Entyvio franchise defence: payer contracting, evidence and lifecycle

**Decision: BUILD** | Horizon H1 | Baseline class: EXISTING_STRENGTH | Confidence: hypothesis

**A. Thesis.** Build payer-contracting and formulary-defence depth, outcomes evidence and lifecycle plans for Entyvio ahead of Medicare negotiation (January 2028) and biosimilar entry, to delay erosion and measure it. The outcome is 'delay and measure', not 'retain revenue': the January 2028 price is statutory and PBM private-label biosimilars route around contracts. (RECOMMENDATION) [CLM-011072] [CLM-007026] [CLM-007015]

**B. Future market change.** Entyvio loses regulatory exclusivity in the latter half of the decade, some patents expire in 2032 with revocation actions filed, two biosimilar BLAs are under FDA review, and Entyvio is selected for Medicare negotiation from January 2028 [CLM-005017] [CLM-014050] [CLM-014051] [CLM-007026]. PBM template changes decide outcomes: from 1 July 2026 CVS template formularies prefer interchangeable Stelara biosimilars [CLM-007015], and Takeda's 20-F says rebate details are undisclosed and formulary exclusion can directly reduce usage [CLM-007025].

**C. Problem.** Entyvio is the largest single exposure and Takeda's contracting depth is unknown. Humira lost 78.6% in three years even with rebate-for-access contracts and a co-brand route, and U.S. Humira fell 41% in 2024 and 57% in 2025 [CLM-003002] [CLM-003007] [CLM-003010] [CLM-007016].

**D. Evidence.**

- FACT: AbbVie kept at least 97% of volume to March 2024 through rebate-for-access, then supplied a co-branded Humira to CVS Cordavis after the April 2024 formulary change [CLM-003007] [CLM-003008] [CLM-003009].
- FACT: AbbVie's settlements put Rinvoq generic entry not before April 2037, four years after the 2033 composition patent [CLM-003021] [CLM-003087].
- FACT: Lilly realised prices fell 5% (Q4 2025) and 15% (Q3 2026) while volume rose 46% and 53% [CLM-014003] [CLM-014004]; CVS Caremark removed Zepbound for about 15 months (1 July 2025 to restoration on 1 October 2026) [CLM-007011] [CLM-007013].
- INTERPRETATION: plan for price erosion in the core franchise, not only volume loss [CLM-001003] [CLM-008022].
- FACT (gap): the registry has no Entyvio medical-benefit versus pharmacy-benefit split, so the contractable share of volume is unknown; this is the benefit-channel gate (IVB-004) [CLM-005072] [CLM-007016].

*Takeda baseline.* Class 1 GI and immunology is a strength (Entyvio JPY 958.0bn, 21% of revenue) but class 14 patient services and market access is an EVIDENCE_GAP (no public rebate or contracting data) and class 7 LOE replacement is EXISTING_BUT_UNDERDEVELOPED [CLM-005009] [CLM-005072] [CLM-005017]. Takeda already runs the SC pen and pediatric labels [CLM-005018]; the gap is payer defence, not product.

*Competitor analogues.* ABBV: [CLM-003007] [CLM-003008] [CLM-003021]; LLY: [CLM-014003] [CLM-007011]; JNJ: [CLM-002065] [CLM-000256]

**E. Moat mechanism.** workflow_integration, ip, regulatory_experience. Workflow integration (formulary position, patient hub and SC pen use) and IP posture. Both are removable (PBM template change, patent revocation), so this is defence, not a compounding moat (INTERPRETATION) [CLM-011086] [CLM-007015].

**F. Practical architecture.** Build: Payer analytics and contracting team capability; Entyvio real-world evidence and persistence study plan. Buy: none. License: none. Partner: Specialty distribution and PBM contracting partners as needed.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-104).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 40 (30-50) | 50 (30-70) | 30 (20-40) | 120 |
| balanced | 40 (30-50) | 60 (35-85) | 40 (25-55) | 140 |
| ambitious | 50 (40-60) | 90 (55-125) | 60 (35-85) | 200 |


**H. Time to value.** Near term: 2027 H1: benefit-channel gate (RM-003). 2028 H1: contracting posture ready for the January 2028 negotiated price and the biosimilar-event playbook live (RM-026, moved up from 2029 H2). Long horizon: 2030-2034: biosimilar-event playbook; value measured as net revenue retained versus ASM-024 erosion.

**I. Measurable outcomes.**

- Entyvio net price and persistence measured against the ASM-024 low case after the 2028 negotiation and any biosimilar entry (measured, not forecast)
- Benefit-channel split (medical versus pharmacy) known by 2027 H1 (IVB-004) and spend redirected if most volume is outside the contractable channel
- SC share of Entyvio patients (IVB-004)
- Time-to-erosion versus the AbbVie and J&J analogues

**J. Risks.**

- competition: Biosimilar or PBM private-label entry on a timetable Takeda does not control [CLM-014051].
- regulatory: Medicare negotiation and Part D redesign [CLM-007026].
- execution: Contracting capability is an EVIDENCE_GAP [CLM-005072].
- adoption: Patient-programme redesign without a pilot cost AbbVie share [CLM-003033] [CLM-003088].
- adoption: If most Entyvio volume sits outside the contractable pharmacy channel, contracting spend is misdirected (benefit-channel gate, RM-003).

**K. Strategic options.** expand, redirect, partner, stop. Expand to settlement-style IP posture if litigation allows; redirect spend to lifecycle if erosion is slower; no divest or stop option before 2032.

**L. Decision: BUILD.** Largest exposure, best-evidenced transferable mechanisms (LES-05, LES-14, LES-21); low capital relative to revenue at risk. v2: stays BUILD, with a hard benefit-channel gate at 2027 H1 and the outcome reframed to delay and measure because Humira held at least 97% of volume yet lost 78.6% in three years [CLM-003007] [CLM-003002]. Hard prerequisites: none. Sequencing: Time-boxed by dated external events: benefit-channel gate 2027 H1, January 2028 negotiation [CLM-007026], playbook live 2028 H1 (early-entry stress case), biosimilar BLA reviews [CLM-014051], 2032 patents [CLM-005017]. If the benefit-channel gate shows most volume outside the contractable pharmacy channel, redirect part of the balanced total to provider and site-of-care strategy. Cannot be postponed.

**M. Evidence and confidence (hypothesis).** Known: Dates, concentration and competitor mechanisms [CLM-005017] [CLM-007026] [CLM-003007]; load-bearing recommendation claim CLM-011072 is not fully supported, so the label is hypothesis. Assumed: Erosion curve and entry date (ASM-024, ASM-025); programme cost (ASM-104). Needs Takeda internal validation: IVB-004, IVB-013, IVB-012 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 6) Stays BUILD; benefit-channel gate at 2027 H1 (RM-003, IVB-004) with redirect rule; outcome reframed from 'retain 10 points of erosion' to 'delay and measure'; playbook RM-026 moved to 2028 H1 (row 2). (decision record row 10) Evidence_backed -> hypothesis; CVS Zepbound removal text corrected from about 11 months [CLM-007011] to about 15 months [CLM-007013].


---

## BET-05 Zasocitinib breadth and immunology successor evidence

**Decision: INVEST** | Horizon H1 | Baseline class: EXISTING_BUT_UNDERDEVELOPED | Confidence: hypothesis

**A. Thesis.** Extend zasocitinib across indications and with comparative data before the Entyvio cliff, copying the AbbVie pattern of indication breadth plus head-to-head evidence, and decide separately whether a GI-indication successor is credible. (RECOMMENDATION, partly already in Takeda's plan.)

**B. Future market change.** Skyrizi plus Rinvoq rose from USD 7,687m (2022) to USD 25,866m (2025) against Humira's USD 16,697m loss because they were marketed and extended across indications before the cliff; J&J's Tremfya offset only about 35% of Stelara's loss in year one [CLM-003014] [CLM-003084] [CLM-002065].

**C. Problem.** Takeda's successors are not yet marketed; the USD 10-20bn peak potential for six programmes is a company statement not adjusted for probability of success [CLM-005041] [CLM-014049]. Base revenue is still falling (H1 FY2026 -1.0% CER) [CLM-005011].

**D. Evidence.**

- FACT: Nimbus purchase USD 4.0bn upfront plus two USD 1.0bn sales milestones; NDA accepted [CLM-009076] [CLM-005035].
- FACT: AbbVie's successors covered Humira's major indications with head-to-head data [CLM-003084] [CLM-003016]; J&J's oral IL-23 peptide approved about 2026-03-17 [CLM-012012].
- INTERPRETATION: pre-launched successors in the same prescriber base offset only part of the loss in year one [CLM-002065] [CLM-002053].

*Takeda baseline.* Class 7 LOE replacement is EXISTING_BUT_UNDERDEVELOPED; class 4 late-stage execution is an EXISTING_STRENGTH: NDA accepted with Priority Review 2026-09-14, PsA Phase 3 running to May 2027, head-to-head win over deucravacitinib [CLM-005035] [CLM-005037] [CLM-005034]. Zasocitinib is not an Entyvio successor in gastroenterology; it replaces revenue, not the franchise (LES-07).

*Competitor analogues.* ABBV: [CLM-003014] [CLM-003084]; JNJ: [CLM-002065] [CLM-002026]

**E. Moat mechanism.** ip, regulatory_experience, workflow_integration. Regulatory experience and label breadth: each added indication increases the base on which a payer contract and prescriber habit can form; IP is the compound patent to be assessed internally (INTERPRETATION) [CLM-003084].

**F. Practical architecture.** Build: Incremental indication and comparative studies beyond the current plan. Buy: none. License: Further rights only if a GI-class gap is identified. Partner: none.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-105).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 50 (40-60) | 70 (40-100) | 10 (5-15) | 130 |
| balanced | 60 (45-75) | 100 (60-140) | 20 (10-30) | 180 |
| ambitious | 80 (60-100) | 140 (85-195) | 30 (20-40) | 250 |


**H. Time to value.** Near term: 2027-2028: PsA readout (May 2027 study end) and psoriasis launch. Long horizon: 2030-2035: breadth across additional immune indications (ASSUMPTION).

**I. Measurable outcomes.**

- Time to first prescription and payer coverage at 6 and 12 months
- Indications labelled by 2032
- Share of Entyvio revenue replaced (tracked, not forecast)

**J. Risks.**

- competition: Crowded psoriasis class with IL-23 and oral competitors (not researched here).
- regulatory: Launch timing tied to site inspection status incl. third-party sites [CLM-012134] [CLM-005029].
- execution: Class 8 launch execution is POTENTIAL_NEW_CAPABILITY [CLM-005074].
- capital: Milestones of USD 1.0bn each at USD 4bn and 5bn annual net sales [CLM-009076].

**K. Strategic options.** expand, redirect, partner, divest. Expand into additional immune indications on positive Phase 2; partner ex-US if capacity-limited; no stop before approval.

**L. Decision: INVEST.** Mostly inside the plan; the incremental decision is breadth and comparative evidence. Marked INVEST not BUILD because the asset already exists. Hard prerequisites: none. Sequencing: Time-boxed by regulatory dates and by the Entyvio timeline; must precede any BET-18 deal sizing because the replacement gap cannot be measured without launch curves (IVB-005).

**M. Evidence and confidence (hypothesis).** Known: NDA acceptance, Phase 3 design, deal terms [CLM-005035] [CLM-009076]. Assumed: Incremental spend and breadth success (ASM-105, ASM-022). Needs Takeda internal validation: IVB-005, IVB-011 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 10) Confidence relabelled evidence_backed -> hypothesis: a load-bearing claim is PARTIALLY_SUPPORTED or NEEDS_MORE_RESEARCH (CLM-011054, CLM-011065, CLM-011066, CLM-011072, CLM-011073, CLM-007053).


---

## BET-06 Option-based external innovation engine incl. new-modality options

**Decision: PARTNER** | Horizon H2 | Baseline class: EXISTING_STRENGTH | Confidence: hypothesis

**A. Thesis.** Use option and early-licence structures with small upfronts and gated exercise for one or two modalities adjacent to existing disease depth (for example RNAi next to fazirsiran), scorecard-first, at the strategy's own constrained size; the balance of the v1 size is contingent on the deal-outcome scorecard (RM-007) and the first two deals (RM-019). (HYPOTHESIS) [CLM-011061]

**B. Future market change.** AbbVie runs USD 0.6-1.0bn a year of early-stage upfronts and options (ADARx USD 335m upfront with up to USD 7.5bn milestones); Lilly expensed USD 3.8bn, 3.3bn and 2.9bn of acquired IPR&D in 2023-2025 with no approval from those assets by cutoff [CLM-009061] [CLM-009095] [CLM-009097] [CLM-009000].

**C. Problem.** Takeda needs pipeline depth after 2030 (IVB-008) and cannot rely on large cash purchases given leverage of 2.6x and the Amitiza provision [CLM-005005] [CLM-005014]. Acquiring modalities is not safer than building them [CLM-009003] [CLM-009054].

**D. Evidence.**

- FACT: Nimbus delivered (Phase 3 positive, NDA accepted) while AbbVie wrote down 54% of Cerevel's net price and Lilly discontinued DICE's lead asset [CLM-009076] [CLM-009054] [CLM-009003].
- FACT: Takeda-Innovent: USD 1.2bn upfront including USD 100m equity, up to USD 11.4bn; Denali and Neurocrine collaborations ended [CLM-009078] [CLM-009089] [CLM-009090].
- FACT: contingent value rights share risk (Prevail, Akouos, Verve, Abiomed, Nimbus) [CLM-009099].
- INTERPRETATION: no option from the window has produced an approved product, so durability is unproven [CLM-009097].

*Takeda baseline.* Class 5 external innovation and BD: deal flow is a strength (four of six late-stage programmes externally sourced); the organisation (Takeda Ventures, CEI scope) is an EVIDENCE_GAP [CLM-005050] [CLM-005052] [CLM-014052]. Takeda stated no significant acquisitions in three years to March 2026 [CLM-009087].

*Competitor analogues.* ABBV: [CLM-009061] [CLM-009062] [CLM-009054]; LLY: [CLM-009095] [CLM-009003]; JNJ: [CLM-009031] [CLM-009044]

**E. Moat mechanism.** ecosystem, network_effects, regulatory_experience. Ecosystem and selection skill: Takeda's late-stage execution and stop discipline (soticlestat, cell therapy) convert partner assets to approvals better than partners alone (INTERPRETATION) [CLM-005042] [CLM-005024] [CLM-005025]. Compounding only if deal outcomes are tracked.

**F. Practical architecture.** Build: Deal-outcome tracking and kill criteria. Buy: Only Phase 2+ assets, and only through the BET-18 channel rules. License: Early assets with option and CVR structures. Partner: Shared venture vehicles (BaseLaunch) [CLM-011077].

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-106).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 35 (25-45) | 50 (30-70) | 45 (25-65) | 130 |
| balanced | 80 (60-100) | 120 (70-170) | 100 (60-140) | 300 |
| ambitious | 105 (80-130) | 215 (130-300) | 195 (115-275) | 515 |


**H. Time to value.** Near term: 2027-2029: three to five option or licence deals; deal-outcome scorecard. Long horizon: 2033-2040: approvals from options (ASM-028 conversion range).

**I. Measurable outcomes.**

- Share of Phase 3 and filing assets sourced externally that reach approval versus in-house rate
- Impairments as % of deal value over three years versus AbbVie's 54% of Cerevel
- Contingent payments committed versus milestones achieved
- Scorecard approved by 2027 H1 before any deal beyond the first two

**J. Risks.**

- scientific: Neuroscience, gene and cell therapy concentrate value destruction [CLM-009100].
- execution: External-innovation organisation undocumented (IVB-007).
- competition: Others bid for the same assets.
- capital: Cumulative upfronts add up without a pipeline result.

**K. Strategic options.** expand, redirect, partner, divest, stop. Expand options that show Phase 1 data; redirect budget to Phase 2+ licences; divest or stop options at expiry.

**L. Decision: PARTNER.** Option structure limits capital at risk versus purchases, but no option from the window has an approved product and the first option-sourced approval is dated 2035 (RM-043), so it cannot bridge 2031-2034 [CLM-009097]. v2: scorecard-first at the constrained size; the remaining USD 400m of the v1 balanced size is contingent headroom (released only after RM-007 and the first two deals), not a saving. Hard prerequisites: none. Sequencing: Independent; sizing depends on IVB-008 pipeline-depth findings. Option exercise should follow Phase 1/2 data, not precede it. The contingent balance is released only after the scorecard (RM-007) and the first two deals (RM-019).

**M. Evidence and confidence (hypothesis).** Known: Deal structures and competitor outcomes [CLM-009061] [CLM-009054]. Assumed: Conversion rate and cost (ASM-028, ASM-106). Needs Takeda internal validation: IVB-007, IVB-008, IVB-014 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 3) Balanced USD 700m -> 300m (constrained size); scorecard-first; balance (USD 400m) contingent on RM-007 and the first two deals (RM-019).


---

## BET-07 Milestone-gated AI-design partnerships (Nabla, Iambic and successors)

**Decision: PARTNER** | Horizon H2 | Baseline class: EVIDENCE_GAP | Confidence: hypothesis

**A. Thesis.** Keep AI-design alliances but tie each scale-up to first-in-human or Phase 2 data with pre-agreed stop rules; do not pay for scale on vendor claims. (RECOMMENDATION) [CLM-011060] [CLM-006058]

**B. Future market change.** Generative design converges on shared models (OpenFold3, Boltz, Chai), weakening the model as a moat; Lilly-Isomorphic, AbbVie-BigHat and Takeda-Nabla are all prototype or earlier [CLM-006056] [CLM-006012] [CLM-006035] [CLM-006045].

**C. Problem.** Outcome evidence is limited and mixed: Recursion ended four of 11 programmes, Insilico's rentosertib Phase IIa showed a signal with seven liver-injury discontinuations, AI-origin Phase 2 success is cited as about the same as conventional (secondary citation, not one of the four companies) [CLM-006047] [CLM-006048] [CLM-006049].

**D. Evidence.**

- FACT: Nabla second collaboration (October 2025; double-digit millions upfront, over USD 1bn success-based) with first-in-human expected in one to two years (company statement) [CLM-006039] [CLM-006040].
- FACT: Iambic (February 2026; success-based payments could exceed USD 1.7bn) [CLM-006041].
- FACT: Lilly-Isomorphic USD 45m upfront, up to USD 1.7bn, concept stage, no candidate named [CLM-006012] [CLM-006007].
- INTERPRETATION: success-based payments are contingent liabilities, not demonstrated value [CLM-006039].

*Takeda baseline.* Class 10 AI-enabled discovery is an EVIDENCE_GAP: alliances exist (Nabla 2022 and 2025, Iambic 2026, BridGene, Charles River, MIT J-Clinic) with no disclosed outcome [CLM-005049] [CLM-006039] [CLM-006041]. An EVIDENCE_GAP is not a finding that the capability is absent [CLM-005080].

*Competitor analogues.* LLY: [CLM-006012] [CLM-006010]; ABBV: [CLM-006035] [CLM-006037]

**E. Moat mechanism.** learning, data, ecosystem. Learning and data only if Takeda feeds back proprietary assay and clinical data to partners under terms that keep ownership; otherwise partners compound, not Takeda (HYPOTHESIS) [CLM-006055] [CLM-011087].

**F. Practical architecture.** Build: Evaluation scorecard comparing AI-origin and conventional candidates. Buy: none. License: Model access under milestone terms. Partner: Nabla, Iambic, others on go/no-go terms.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-107).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 10 (10-10) | 20 (10-30) | 10 (5-15) | 40 |
| balanced | 20 (15-25) | 40 (25-55) | 20 (10-30) | 80 |
| ambitious | 35 (25-45) | 70 (40-100) | 60 (35-85) | 165 |


**H. Time to value.** Near term: 2026-2028: Nabla first-in-human data (company expectation). Long horizon: 2030-2038: share of Phase 1 starts from AI programmes and their Phase 2 transition rate.

**I. Measurable outcomes.**

- First-in-human data from Nabla-designed molecules versus conventional candidate quality
- Share of Phase 1 starts from AI or option programmes by FY2028 and their Phase 2 transition rate
- Contingent payments committed versus data-gated milestones achieved

**J. Risks.**

- scientific: AI-origin molecules may not outperform conventional [CLM-006049].
- data: Takeda data leaks into partner models.
- execution: Stop rules not honoured after sunk cost.
- regulatory: Draft FDA credibility framework [CLM-006046].

**K. Strategic options.** expand, partner, stop. Expand on first-in-human success; redirect to licensed models; stop at first missed gate.

**L. Decision: PARTNER.** Matches A6 advice to partner-and-watch; spend is small and success-based. v2: sized at the constrained level, prerequisites re-wired in the roadmap, stop rules in contracts. Commercial and red-team councils oppose the differentiation claim; it is retained as a cheap option, not a moat [CLM-006047] [CLM-006048] [CLM-006049]. Hard prerequisites: BET-01, BET-09. Sequencing: Hard prerequisites BET-01 (decision log, RM-015) and BET-09 (cost benchmark, RM-018) are now wired into the roadmap: the stop-or-expand decision RM-020 (2028 H2) depends on both, and the H2 and H3 tranches are released only at RM-020. Stop rules are written into the Nabla and Iambic contracts before the next payment (new RM-053). Partnerships already running continue under these gates (HYPOTHESIS).

**M. Evidence and confidence (hypothesis).** Known: Deal terms and absence of outcomes [CLM-006039] [CLM-006045]. Assumed: Success odds (ASM-021) and spend (ASM-107). Needs Takeda internal validation: IVB-010, IVB-001 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 7) Stays PARTNER; balanced USD 180m -> 80m; prerequisites re-wired (RM-020 now depends on RM-015 and RM-018; RM-011 on the decision log and contract stop rules); H2/H3 tranche released only at RM-020; stop rules in contracts before next payment (new RM-053).


---

## BET-08 Federated data consortium participation

**Decision: PARTNER** | Horizon H1 | Baseline class: EXISTING_BUT_UNDERDEVELOPED | Confidence: hypothesis

**A. Thesis.** Participate in federated consortia where pooled models beat Takeda-only models on Takeda held-out data, instead of building a proprietary developer platform. (HYPOTHESIS) [CLM-011027] [CLM-011054]

**B. Future market change.** Five companies fine-tuned OpenFold3 on over 20,000 private structures and the organiser reports about 10 points better pose accuracy than the best public model (vendor-organised, not peer reviewed) [CLM-006043]. Rivals will cooperate under federation [CLM-006056].

**C. Problem.** Takeda lacks the data volume and developer pull to start a CUDA-style flywheel [CLM-011027]. A competitor-led platform strengthens that competitor's models as partners contribute [CLM-006055].

**D. Evidence.**

- FACT: AISB uses Apheris and an academic lab (Columbia) [CLM-006043].
- FACT: Lilly TuneLab: no uptake or outcome disclosed [CLM-000280] [CLM-006007].
- INTERPRETATION: participation should wait for independent results (LES-03) [CLM-006008].

*Takeda baseline.* Class 9: Takeda is an AISB member since 2025-10-01 but is not on the AISB Bind founding list [CLM-006042] [CLM-006044]. This bet extends existing membership; maturity of Takeda's contribution is unknown (IVB-001).

*Competitor analogues.* LLY: [CLM-000280] [CLM-006008]

**E. Moat mechanism.** network_effects, data, ecosystem. Network effects: pooled data improves everyone's model, but the advantage accrues to the participant that uses it best, so the moat is the internal decision layer (BET-01), not membership (INTERPRETATION) [CLM-011087].

**F. Practical architecture.** Build: Evaluation protocol on Takeda held-out data. Buy: none. License: none. Partner: AISB, Apheris, other federated consortia.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-108).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 10 (10-10) | 10 (5-15) | 5 (5-5) | 25 |
| balanced | 10 (10-10) | 15 (10-20) | 10 (5-15) | 35 |
| ambitious | 15 (10-20) | 20 (10-30) | 15 (10-20) | 50 |


**H. Time to value.** Near term: 2027-2028: measured gain on Takeda held-out targets. Long horizon: 2030-2035: participation in additional tasks if measured.

**I. Measurable outcomes.**

- Federated model gain on Takeda held-out data versus public models, method disclosed
- Raw data never leaves Takeda governance

**J. Risks.**

- data: Privacy and consent limit pooling [CLM-011054].
- competition: Rival-led platform lock-in [CLM-006055].
- adoption: Gain smaller than the organiser's benchmark.

**K. Strategic options.** expand, redirect, stop. Expand to more tasks if gain is measured; stop if gains do not exceed Takeda-only models.

**L. Decision: PARTNER.** Cheapest route to shared data advantage; consistent with competitor evidence. Hard prerequisites: none. Sequencing: Independent and cheap; value capture depends on BET-01.

**M. Evidence and confidence (hypothesis).** Known: Consortium exists and Takeda is a member [CLM-006042]. Assumed: Measured gain for Takeda tasks. Needs Takeda internal validation: IVB-001 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 10) Confidence relabelled evidence_backed -> hypothesis: a load-bearing claim is PARTIALLY_SUPPORTED or NEEDS_MORE_RESEARCH (CLM-011054, CLM-011065, CLM-011066, CLM-011072, CLM-011073, CLM-007053).


---

## BET-09 Rented automated data generation (CRO and cloud labs) with ladder triggers

**Decision: PARTNER** | Horizon H1 | Baseline class: EVIDENCE_GAP | Confidence: hypothesis

**A. Thesis.** Buy stage 1-2 automated data generation as a service, run one stage-3 pilot only on explicit triggers, and do not build an owned robotic lab. (RECOMMENDATION) [CLM-011065] [CLM-011066]

**B. Future market change.** Lilly's owned Life Sciences Studio was sold to the CRO Arctoris in 2024, reason undisclosed; Zymergen sold at about one-tenth of its IPO-era valuation after USD 1.2bn cumulative net losses on a different business model; the service model continues, with Arctoris expanding biophysics capacity ten-fold [CLM-006013] [CLM-006051] [CLM-006016]. The Lilly-NVIDIA lab (up to USD 1bn over five years, joint) reads as re-platforming rather than abandonment of automation; it is concept [CLM-000281].

**C. Problem.** Takeda needs wet-lab throughput for AI-design partnerships without taking owned-lab capital risk. Costs per data point and turnaround are unknown (IVB-002).

**D. Evidence.**

- FACT: the reason for Lilly's sale is undisclosed; the 'Strateos' link and 2020 date are unsupported [CLM-006017] [CLM-006014].
- FACT: stage 1-2 automation is operational and commodity; stage 4 not demonstrated in any source opened [CLM-011062].
- FACT: Ottava USD 0.9bn impairment shows robotics capital risk (device robotics) [CLM-009047].

*Takeda baseline.* Class 11 lab automation and robotics is an EVIDENCE_GAP (no public evidence at Shonan, Boston or Vienna; IVB-002) [CLM-005067]. Takeda lists Charles River as an alliance [CLM-005049]. This bet buys a service, so there is no existing capability to over-build.

*Competitor analogues.* LLY: [CLM-006013] [CLM-006016] [CLM-000281]; JNJ: [CLM-009047]

**E. Moat mechanism.** data, workflow_integration. Not the robots, which are purchasable: the moat is the structured data generated and the workflow that feeds models. It compounds only with a data standard from day one (HYPOTHESIS) [CLM-006052] [CLM-011063].

**F. Practical architecture.** Build: Data standards and acceptance tests. Buy: Automated assay capacity as a service. License: none. Partner: CRO and cloud-lab providers.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-109).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 15 (10-20) | 20 (10-30) | 15 (10-20) | 50 |
| balanced | 25 (20-30) | 40 (25-55) | 30 (20-40) | 95 |
| ambitious | 40 (30-50) | 80 (50-110) | 70 (40-100) | 190 |


**H. Time to value.** Near term: 2027-2028: cost per data point and turnaround versus internal baseline. Long horizon: 2030+: stage-3 pilot only on triggers.

**I. Measurable outcomes.**

- Cost per data point and turnaround from a CRO pilot versus internal baseline
- Prospective AI-planned versus human-planned experiments on the same target (stage-3 gate)

**J. Risks.**

- execution: Data quality and interface problems with vendors.
- data: IP and data ownership terms.
- capital: Vendor lock-in; commercially fragile model [CLM-006017].

**K. Strategic options.** expand, partner, stop. Expand to stage-3 pilot on triggers; redirect to a different CRO; stop at gate 2 if costs exceed internal baseline.

**L. Decision: PARTNER.** Renting is cheaper to reverse; no owned-lab success case exists in the set, but the causes of the competitor exits are largely undisclosed, so 'owned labs fail' is a HYPOTHESIS, not a finding [CLM-006052] [CLM-006017]. Hard prerequisites: none. Sequencing: Can seed its own data foundation for stages 1-2 if a minimal data schema is enforced from the start (a thin slice of BET-01). Stage-3 and above require BET-01 in full and the three triggers (independent Lilly-lab result, Nabla first-in-human, measured CRO cost) [CLM-011066].

**M. Evidence and confidence (hypothesis).** Known: Competitor exits and CRO continuation [CLM-006013] [CLM-006016]. Assumed: Takeda needs and cost (ASM-109). Needs Takeda internal validation: IVB-002, IVB-010 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 10) Confidence relabelled evidence_backed -> hypothesis: a load-bearing claim is PARTIALLY_SUPPORTED or NEEDS_MORE_RESEARCH (CLM-011054, CLM-011065, CLM-011066, CLM-011072, CLM-011073, CLM-007053). (decision record row —) Owned-labs-fail narrative softened: Lilly's sale reason is undisclosed, the Strateos link is unsupported [CLM-006017], the NVIDIA joint lab reads as re-platforming [CLM-000281]. (decision record row 7) Roadmap: RM-018 (CRO cost benchmark) is now a wired prerequisite of RM-020 (BET-07). Size unchanged.


---

## BET-10 Owned autonomous discovery lab (stage 4-5)

**Decision: REJECT** | Horizon H3 | Baseline class: EVIDENCE_GAP | Confidence: hypothesis

**A. Thesis.** Build an owned closed-loop autonomous lab. Not supported by evidence today; recorded as a rejected alternative with revisit triggers. (RECOMMENDATION: REJECT now.)

**B. Future market change.** Lilly and NVIDIA announced a co-innovation lab, concept stage; Medicine Foundry (USD 4.5bn) is concept [CLM-000281] [CLM-006000] [CLM-006001].

**C. Problem.** No independent demonstration of closed-loop autonomous discovery with clinical outcome exists in any source opened [CLM-011062]. One owned model (Lilly Studio) was sold with the reason undisclosed and one (Zymergen) failed commercially on a different model [CLM-006052] [CLM-006051] [CLM-006017].

**D. Evidence.**

- FACT: Lilly Studio divested to a CRO, reason undisclosed; the Strateos link and 2020 date are unsupported [CLM-006013] [CLM-006017]; Zymergen USD 1.2bn cumulative net loss without a commercial product [CLM-006051].
- INTERPRETATION: the Lilly-NVIDIA joint lab reads as re-platforming, not abandonment [CLM-000281]; stage 4 and above is an option on technology not yet shown to work [CLM-011062].

*Takeda baseline.* Class 11 EVIDENCE_GAP [CLM-005067]. No Takeda capability to extend; the bet would create a new one.

*Competitor analogues.* LLY: [CLM-006013] [CLM-000281]

**E. Moat mechanism.** data, learning, infrastructure. Would be data and learning, but the evidence shows owned-lab economics failing (HYPOTHESIS, low confidence).

**F. Practical architecture.** Build: Not proposed. Buy: none. License: none. Partner: Observe Lilly-NVIDIA lab outcomes.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-110).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| balanced | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| ambitious | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |


**H. Time to value.** Near term: None. Long horizon: Revisit when triggers fire (2030+).

**I. Measurable outcomes.**

- Operational trigger set, reviewed annually (RM-027, RM-038): T1 an independent, published operating result from the Lilly-NVIDIA lab [CLM-000281] (not a press statement); T2 Nabla first-in-human data against a conventional comparator [CLM-006039]; T3 measured CRO cost per data point from BET-09 [CLM-006016]. All three plus BET-01 in full are required before any stage-3 pilot; owner: Head of R&D (role).

**J. Risks.**

- capital: Distressed outcomes documented [CLM-006051].
- scientific: Reproducibility and failure modes.
- regulatory: Unsettled for submission use [CLM-006046].

**K. Strategic options.** partner, stop. Partner; stop. Option value retained at zero capital via triggers.

**L. Decision: REJECT.** No evidence of value; no owned-lab success case in the set; rented model available (BET-09). The competitor exits are weak evidence because their causes are largely undisclosed [CLM-006017]. Zero spend, with an operational trigger set. Hard prerequisites: BET-01, BET-09, BET-07. Sequencing: If ever reconsidered, requires BET-01 in full, BET-09 evidence and BET-07 first-in-human data. Revisit annually at the portfolio review.

**M. Evidence and confidence (hypothesis).** Known: Competitor outcomes [CLM-006051] [CLM-006013]. Assumed: That triggers can be observed within 12-24 months [CLM-011066]. Needs Takeda internal validation: IVB-002 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row —) Stays REJECT (zero spend); owned-labs-fail narrative softened; operational trigger set T1-T3 defined with owner and review dates.


---

## BET-11 Drug-device and home/SC administration platform

**Decision: BUILD** | Horizon H1 | Baseline class: EXISTING_STRENGTH | Confidence: hypothesis

**A. Thesis.** Extend drug-device combinations (pens, needle-free transfer, home infusion) as the cheaper Intuitive-style pull-through, instead of surgical or lab robotics. (HYPOTHESIS) [CLM-011048]

**B. Future market change.** Tremfya SC share gains accompanied USD 5,155m FY2025 sales (+40.5%); Zepbound moved to vials and KwikPen [CLM-007029] [CLM-007044] [CLM-000256]. Intuitive derives 84% of revenue from recurring instruments and service [CLM-011021].

**C. Problem.** Effect on net price and erosion after biosimilar entry is not established [CLM-007053]. Cannibalisation of IV ahead of exclusivity loss is a risk (IVB-004). Conflict with BET-04: SC pens move patients into the pharmacy benefit, which is where PBM private-label biosimilar templates operate, so scaling SC before the benefit-channel gate could raise exposure at the worst moment [CLM-007015] [CLM-007016].

**D. Evidence.**

- FACT: SC pen described as driving uptake [CLM-007041].
- FACT (counter-example): J&J robotics cost USD 0.9bn impairment; OTTAVA installation is announced, not shown complete [CLM-009047] [CLM-000284].
- INTERPRETATION: device features are tied to the product and its patents, so advantage is proprietary but not independent of the drug's LOE [CLM-007042].

*Takeda baseline.* Class 1 and class 2: Entyvio SC pen approved for UC (September 2023) and Crohn's (April 2024); HYHUB needle-free Hyqvia transfer received FDA 510(k) clearance in July 2025 (clearance, not adoption) [CLM-007041] [CLM-007042] [CLM-005018]. The capability exists; the bet extends it.

*Competitor analogues.* JNJ: [CLM-000256] [CLM-007029]; LLY: [CLM-007044]

**E. Moat mechanism.** ip, workflow_integration, learning. IP (device patents) and workflow integration (patient habit on a pen); learning if device data feeds adherence evidence. Persistence after biosimilar entry is the test (INTERPRETATION) [CLM-011046].

**F. Practical architecture.** Build: Next-generation devices and connected features. Buy: none. License: Device components. Partner: Device manufacturers.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-111).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 40 (30-50) | 50 (30-70) | 30 (20-40) | 120 |
| balanced | 50 (40-60) | 80 (50-110) | 60 (35-85) | 190 |
| ambitious | 70 (50-90) | 120 (70-170) | 100 (60-140) | 290 |


**H. Time to value.** Near term: 2027-2029: share of Entyvio patients on SC; HYHUB home use. Long horizon: 2030-2035: persistence of SC users after biosimilar entry.

**I. Measurable outcomes.**

- Share of Entyvio patients on SC and of Hyqvia patients on device-assisted home use
- Persistence after any biosimilar entry versus IV

**J. Risks.**

- adoption: SC share grows without protecting net price [CLM-007053].
- regulatory: Device clearance and REMS-style designs [CLM-007030].
- capital: Device capex competes with core.
- competition: SC migration before biosimilar entry increases pharmacy-benefit exposure (conflict with BET-04) [CLM-007015] [CLM-007016].

**K. Strategic options.** expand, redirect, partner, stop. Expand to additional products; stop if SC does not retain share after entry.

**L. Decision: BUILD.** Existing capability; modest capital; but the supporting interpretation is PARTIALLY_SUPPORTED and the effect after entry is not established [CLM-007053], so spend is baseline-first and the BET-04 channel conflict is a stated gate. Hard prerequisites: none. Sequencing: Baseline first (RM-013), then device spend. Before scaling SC, decide whether moving patients into the pharmacy benefit helps or hurts after biosimilar entry, using the BET-04 benefit-channel gate (RM-003, IVB-004); the roadmap now wires RM-013 to RM-003.

**M. Evidence and confidence (hypothesis).** Known: Approvals and clearance [CLM-007041] [CLM-007042]. Assumed: Value after biosimilar entry; spend (ASM-111). Needs Takeda internal validation: IVB-004, IVB-013 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 10) Confidence relabelled evidence_backed -> hypothesis: a load-bearing claim is PARTIALLY_SUPPORTED or NEEDS_MORE_RESEARCH (CLM-011054, CLM-011065, CLM-011066, CLM-011072, CLM-011073, CLM-007053). (decision record row 8) Stays BUILD; baseline first; BET-04 channel conflict stated and wired (RM-013 depends on RM-003); confidence evidence_backed -> hypothesis.


---

## BET-12 Launch-pathway partnerships and patient-services outcome measurement

**Decision: EXPERIMENT** | Horizon H1 | Baseline class: EVIDENCE_GAP | Confidence: hypothesis

**A. Thesis.** Attach a diagnosis and certified-site pathway pilot to the oveporexton (Orzeyful) launch with a named leader, starting 2027 H1, and measure time-to-therapy and persistence before any redesign. Capped at USD 50m. (HYPOTHESIS) [CLM-011070] [CLM-005029]

**B. Future market change.** Site certification governed Spravato (USD 1,696m, site-limited) and capacity governed Carvykti (USD 1,887m) [CLM-007029] [CLM-007030]. Three Takeda launches fall within 12 months of June 2026 [CLM-005074].

**C. Problem.** No company publishes adherence, persistence or time-to-therapy outcomes [CLM-007039]; AbbVie's revised Alle programme was reinstated within months and Botox Cosmetic fell 11% [CLM-003033] [CLM-003032] [CLM-003088].

**D. Evidence.**

- FACT: Pear Therapeutics filed Chapter 11 after payers could deny payment [CLM-007045] [CLM-007046].
- INTERPRETATION: attach support to the drug instead of standalone digital therapeutics [CLM-011069].

*Takeda baseline.* Class 14 patient services and market access is an EVIDENCE_GAP [CLM-005072] and class 8 launch execution is POTENTIAL_NEW_CAPABILITY [CLM-005074]. Help at Hand reports over 100,000 patients cumulative, an enrolment count, not an outcome [CLM-007037] [CLM-007039]. Assess first (IVB-013).

*Competitor analogues.* JNJ: [CLM-007030] [CLM-007029]; ABBV: [CLM-003033]

**E. Moat mechanism.** workflow_integration, regulatory_experience, ecosystem. Workflow integration in diagnosis and site networks; replicable by vendors unless measured outcomes exist (INTERPRETATION) [CLM-011067].

**F. Practical architecture.** Build: Outcome measurement for existing programmes. Buy: none. License: none. Partner: Diagnosis and certified-site networks, health systems.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-112).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 10 (10-10) | 10 (5-15) | 5 (5-5) | 25 |
| balanced | 30 (20-40) | 10 (5-15) | 10 (5-15) | 50 |
| ambitious | 20 (15-25) | 30 (20-40) | 25 (15-35) | 75 |


**H. Time to value.** Near term: 2027 H1: pilot attached to the launch; 2028 H2: baseline gate (RM-021). Long horizon: 2030-2035: outcome evidence supports contracting.

**I. Measurable outcomes.**

- Time from prescription to first dose and persistence at 12 months by channel
- Site activation rate and payer coverage at 6 and 12 months

**J. Risks.**

- regulatory: Anti-kickback and copay accumulator rules [CLM-007010].
- adoption: Redesign without pilot [CLM-003088].
- data: Hub data not owned by Takeda (IVB-013).

**K. Strategic options.** expand, redirect, partner, stop. Expand if pathway data show time-to-therapy gain; stop otherwise.

**L. Decision: EXPERIMENT.** Hypothesis that launch pathways govern speed is untested for narcolepsy type 1. v2: approval was 2026-08-05 [CLM-005029], so a 2027 H2 pilot is late; capped at USD 50m and attached to the launch. The options paper for BET-13 (USD 25m) is funded inside this cap. Hard prerequisites: none. Sequencing: Starts 2027 H1 with a named launch leader (role; the owner organisation also carries three launches and the January 2028 Entyvio price [CLM-005074] [CLM-007033]); further tranches wait for RM-021 evidence. Soft dependency on BET-17 measurement discipline.

**M. Evidence and confidence (hypothesis).** Known: Competitor launch constraints [CLM-007029] [CLM-007030]. Assumed: That oveporexton is pathway-limited (ASM-112). Needs Takeda internal validation: IVB-013, IVB-005 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 9) Capped USD 100m -> 50m; attached to the oveporexton launch with a named leader; start moved 2027 H2 -> 2027 H1 (RM-012).


---

## BET-13 Neutral rare-disease or plasma real-world data registry

**Decision: DEFER** | Horizon H2 | Baseline class: POTENTIAL_NEW_CAPABILITY | Confidence: hypothesis

**A. Thesis.** Build or buy a neutral registry with patient organisations and health systems so competitors will contribute data (Flatiron analogue). (HYPOTHESIS, low confidence) [CLM-011051]

**B. Future market change.** Roche paid USD 1.9bn for Flatiron and kept it neutral; Flatiron partnered with 14 of the top 15 oncology companies in 2018 [CLM-011022].

**C. Problem.** Flatiron is oncology-specific and built in US community oncology; Takeda's areas lack such a network [CLM-011050].

**D. Evidence.**

- FACT: regulatory-use claim is a vendor snippet [CLM-011023].
- INTERPRETATION: ownership by one pharma works only if neutrality is protected [CLM-011049].

*Takeda baseline.* No Takeda data network is public; class 14 is an EVIDENCE_GAP [CLM-005072]. This would be a new capability.

*Competitor analogues.* LLY: [CLM-009027]

**E. Moat mechanism.** data, network_effects, ecosystem. Data and network effects only with neutrality; unproven.

**F. Practical architecture.** Build: Registry governance. Buy: Possible neutral entity. License: Data access. Partner: Patient organisations and health systems.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-113).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| balanced | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| ambitious | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |


**H. Time to value.** Near term: None before 2030. Long horizon: 2033-2040.

**I. Measurable outcomes.**

- Registry enrolment and contributing companies (if started)

**J. Risks.**

- data: Consent and neutrality.
- competition: Existing registries.
- capital: Low differentiation.

**K. Strategic options.** partner, stop. Partner via patient organisations; stop if no neutral sponsor.

**L. Decision: DEFER.** Needs BET-12 evidence and a disease choice; revisit in 2029. v2: the balanced carry is removed (a DEFER bet was funded while BET-15 was not); the USD 25m options paper (RM-028) is funded inside the BET-12 cap. Hard prerequisites: BET-01, BET-12. Sequencing: After BET-01 governance and BET-12 pathway data.

**M. Evidence and confidence (hypothesis).** Known: Roche precedent [CLM-011022]. Assumed: Neutrality and demand (ASM-113). Needs Takeda internal validation: IVB-013, IVB-007 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 10) Balanced carry removed (USD 80m -> 0; ambitious USD 160m -> 0 by proportional rescale); options paper funded from BET-12.


---

## BET-14 TuneLab-style productised external model platform

**Decision: REJECT** | Horizon H3 | Baseline class: POTENTIAL_NEW_CAPABILITY | Confidence: hypothesis

**A. Thesis.** Build a platform that offers Takeda-trained models to external biotechs in exchange for data (the TuneLab model). (RECOMMENDATION: REJECT now.) [CLM-011027]

**B. Future market change.** TuneLab launched 2025-09-09 with Benchling distribution to 1,300+ customers opt-in; no uptake, retraining or scientific outcome is disclosed [CLM-000280] [CLM-006008].

**C. Problem.** Takeda should not productise capabilities until a measured internal advantage exists [CLM-011045]. NVIDIA warns customers with in-house capability replace platform layers [CLM-011004].

**D. Evidence.**

- FACT: Lilly cites over USD 1bn data cost; vendor blog reports over 2 million Lilly and 675,000 partner data points (single vendor source) [CLM-000280] [CLM-009028].
- INTERPRETATION: customers are rivals [CLM-011044].

*Takeda baseline.* Class 9 is EXISTING_BUT_UNDERDEVELOPED and there is no measured internal advantage [CLM-005058] [CLM-006045]. Productising would extend an unproven capability.

*Competitor analogues.* LLY: [CLM-000280] [CLM-006008]

**E. Moat mechanism.** data, network_effects, ecosystem. Would be network effects; requires scale Takeda cannot show.

**F. Practical architecture.** Build: Not proposed. Buy: none. License: none. Partner: Federated participation (BET-08) instead.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-114).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| balanced | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| ambitious | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |


**H. Time to value.** Near term: None. Long horizon: Reconsider after BET-01 yields a measured advantage.

**I. Measurable outcomes.**

- None funded

**J. Risks.**

- competition: Lilly-scale data advantage [CLM-000280].
- adoption: Unknown demand [CLM-006008].
- capital: Platform build without outcome.

**K. Strategic options.** partner, stop. Participate (BET-08); revisit if advantage measured.

**L. Decision: REJECT.** Public record gives no measured internal advantage and no external demand evidence. Hard prerequisites: BET-01. Sequencing: Cannot precede BET-01 and a measured advantage.

**M. Evidence and confidence (hypothesis).** Known: TuneLab status [CLM-000280]. Assumed: Takeda data volume lower than Lilly's. Needs Takeda internal validation: IVB-001 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).


---

## BET-15 Large asset purchase (USD 5bn or more) as LOE bridge

**Decision: REJECT** | Horizon H2 | Baseline class: EXISTING_BUT_UNDERDEVELOPED | Confidence: hypothesis

**A. Thesis.** A single USD 5bn+ acquisition as the LOE bridge. (RECOMMENDATION: REJECT as framed; the bridge is a funded Phase 2/3 licensing channel, BET-18.)

**B. Future market change.** J&J acquired USD 17.5bn net of cash in FY2025 funded by USD 24.5bn operating cash flow; AbbVie's Cerevel purchase led to a USD 4.5bn impairment [CLM-009049] [CLM-002010] [CLM-009054].

**C. Problem.** Council arithmetic puts leverage at about 3.1x after a USD 5bn purchase and about 3.4x if the Amitiza provision is also debt-funded, against the strategy's own 3.0x ceiling (ASM-033, ASM-119) [CLM-005005] [CLM-005014]. Takeda's observed pattern is mid-size licensing, not USD 5bn purchases [CLM-009098] [CLM-009087].

**D. Evidence.**

- FACT: sizing rule from LES-15 is to survive a write-down [CLM-009054] [CLM-005036].
- INTERPRETATION: comparisons of deal values across companies are invalid across bases [CLM-009098].

*Takeda baseline.* Class 5 deal flow is a strength; Takeda's one large purchase (Nimbus, USD 4.0bn upfront) delivered so far; class 16 cost transformation and leverage constrain capacity [CLM-009076] [CLM-005005] [CLM-005014].

*Competitor analogues.* ABBV: [CLM-009054] [CLM-003086]; JNJ: [CLM-009049] [CLM-002010]

**E. Moat mechanism.** ip, regulatory_experience. Acquired assets bring IP; no compounding moat from the purchase itself.

**F. Practical architecture.** Build: none. Buy: Phase 2+ assets under trigger. License: none. Partner: none.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-115, ASM-033).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| balanced | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| ambitious | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |


**H. Time to value.** Near term: None. Long horizon: None.

**I. Measurable outcomes.**

- None funded; the bridge question is handled by BET-18 triggers

**J. Risks.**

- capital: Leverage and dividend [CLM-005006].
- scientific: Single-asset binary risk [CLM-009076].
- regulatory: Antitrust not researched.

**K. Strategic options.** expand, redirect, stop. Stop; see BET-18.

**L. Decision: REJECT.** The strategy's own leverage test fails by arithmetic (ASM-033, ASM-119) and Takeda's pattern is mid-size licensing (Nimbus, Innovent); the gap is covered by BET-18, not by a trigger-based purchase. Hard prerequisites: none. Sequencing: None. Superseded by BET-18; revisit only if leverage policy changes (IVB-012).

**M. Evidence and confidence (hypothesis).** Known: Competitor deal outcomes [CLM-009054] [CLM-009049]. Assumed: Leverage ceiling (ASM-033). Needs Takeda internal validation: IVB-005, IVB-012, IVB-014 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 1) DEFER -> REJECT as framed (fails the 3.0x leverage ceiling by arithmetic); stage gates removed; bridge replaced by BET-18.


---

## BET-16 U.S. cash-pay direct-to-patient channel

**Decision: REJECT** | Horizon H1 | Baseline class: EVIDENCE_GAP | Confidence: hypothesis

**A. Thesis.** Replicate LillyDirect. (RECOMMENDATION: REJECT.) [CLM-011073]

**B. Future market change.** Cash-pay scaled in an uninsured-gap category (obesity); Lilly says over 1 million patients used LillyDirect in 2025 but the 10-K gives no revenue share [CLM-001042] [CLM-007002] [CLM-007005].

**C. Problem.** Takeda products are infused, specialty or plasma-derived; copay-accumulator and anti-kickback limits restrict combining discounts with insurance [CLM-007010] [CLM-007052].

**D. Evidence.**

- INTERPRETATION: LES-02 does not transfer [CLM-007004].
- FACT: TrumpRx materiality unknown [CLM-007009].

*Takeda baseline.* Class 14 EVIDENCE_GAP [CLM-005072].

*Competitor analogues.* LLY: [CLM-001042] [CLM-007002]

**E. Moat mechanism.** workflow_integration. None evidenced for Takeda's categories.

**F. Practical architecture.** Build: Not proposed. Buy: none. License: none. Partner: none.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-116).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| balanced | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| ambitious | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |


**H. Time to value.** Near term: None. Long horizon: None.

**I. Measurable outcomes.**

- None funded

**J. Risks.**

- regulatory: Anti-kickback [CLM-007010].
- adoption: Poor fit.

**K. Strategic options.** stop. Stop.

**L. Decision: REJECT.** Structure differs; evidence supports home and SC conversion instead (BET-11). Hard prerequisites: none. Sequencing: None.

**M. Evidence and confidence (hypothesis).** Known: Product and channel structure [CLM-007052]. Assumed: Takeda product mix stays specialty. Needs Takeda internal validation: IVB-013 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 10) Confidence relabelled evidence_backed -> hypothesis: a load-bearing claim is PARTIALLY_SUPPORTED or NEEDS_MORE_RESEARCH (CLM-011054, CLM-011065, CLM-011066, CLM-011072, CLM-011073, CLM-007053).


---

## BET-17 AI use-case measurement, decision support and reskilling

**Decision: EXPERIMENT** | Horizon H1 | Baseline class: EXISTING_BUT_UNDERDEVELOPED | Confidence: hypothesis

**A. Thesis.** Measure a small set of AI use cases against pre-agreed baselines, prune early, pilot AI decision support that advises humans only, and publish a reskilling plan measured by task capability. (HYPOTHESIS) [CLM-011080] [CLM-011081] [CLM-011074]

**B. Future market change.** J&J reviewed nearly 900 gen-AI use cases; a CIO interview says 10-15% drive about 80% of value (single source) and AI ownership moved to departments [CLM-006018] [CLM-006019].

**C. Problem.** Usage and training metrics are not value [CLM-006022]; CEO transition, restructuring and several launches coincide [CLM-005073] [CLM-005074] [CLM-005078]; adoption-failure risk is disclosed by AbbVie [CLM-006036].

**D. Evidence.**

- FACT: J&J AskJIA and Engagement.AI have no usage or outcome data [CLM-006023] [CLM-006021].
- INTERPRETATION: do not conflate efficiency and AI in communication [CLM-011078] [CLM-011079].

*Takeda baseline.* Class 9 and class 16: 63.4% workforce gen-AI use, insourced digital factories, JPY 200bn savings plan with technology share unknown (IVB-003) [CLM-014043] [CLM-005057] [CLM-005059] [CLM-005078].

*Competitor analogues.* JNJ: [CLM-006018] [CLM-006019] [CLM-006023]

**E. Moat mechanism.** learning, workflow_integration. Learning: faster pruning of use cases; workflow integration; skills.

**F. Practical architecture.** Build: Baseline and measurement office; reskilling plan. Buy: none. License: Decision-support tools. Partner: none.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-117).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 25 (20-30) | 25 (15-35) | 15 (10-20) | 65 |
| balanced | 40 (30-50) | 50 (30-70) | 30 (20-40) | 120 |
| ambitious | 55 (40-70) | 70 (40-100) | 50 (30-70) | 175 |


**H. Time to value.** Near term: 2027-2028: use cases with baselines and results. Long horizon: 2030+: reskilled workforce share.

**I. Measurable outcomes.**

- AI use cases in production with owner, baseline and measured benefit at 12 months
- Share of savings attributed to technology (closes IVB-003)
- Retention and internal mobility in affected roles

**J. Risks.**

- adoption: Morale and capability loss [CLM-011078].
- regulatory: Compliance of outbound content [CLM-006046].
- execution: Load on organisation.

**K. Strategic options.** expand, redirect, stop. Expand to broader rollout only where measured; stop low-value use cases.

**L. Decision: EXPERIMENT.** Cheap, prerequisite for credibility of all other AI claims. Hard prerequisites: none. Sequencing: Start first; informs BET-01 and BET-12. Measurement owner is internal audit or the Chief Digital and Technology Officer with Audit Committee visibility (roles), independent of the owner of the JPY 200bn savings target, so that attribution of savings to technology is credible (IVB-003) [CLM-005059] [CLM-005078].

**M. Evidence and confidence (hypothesis).** Known: Competitor self-reports and Takeda usage [CLM-006018] [CLM-014043]. Assumed: Baselines can be set (ASM-117). Needs Takeda internal validation: IVB-001, IVB-003 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 10) Measurement owner moved off the CFO (owner of the JPY 200bn savings target) to internal audit or the CDTO with Audit Committee visibility.


---

## BET-18 Phase 2/3 in-licensing channel

**Decision: PARTNER/INVEST** | Horizon H2 | Baseline class: EXISTING_STRENGTH | Confidence: hypothesis | **v2 addition (council-proposed)**

**A. Thesis.** Hold a standing channel for Phase 2/3 in-licences and option-to-acquire deals with a per-deal upfront ceiling of USD 0.5-2bn (ASM-118), contingent on Amitiza cash (IVB-012) and the 3.0x leverage ceiling (ASM-033), so that the Entyvio refill gap (2031-2034) has a funded instrument that BET-06 (payoff 2035+) and BET-15 (fails the leverage test) cannot supply. (RECOMMENDATION, council-proposed, adopted by the Director in v2.)

**B. Future market change.** Takeda's refill pattern is mid-size licences: Nimbus USD 4.0bn upfront plus two USD 1.0bn sales milestones, Innovent USD 1.2bn upfront including USD 100m equity, plus Protagonist and Keros licences [CLM-009076] [CLM-009078] [CLM-009080] [CLM-009081]. AbbVie bought bridges of USD 9.2bn net (ImmunoGen) and J&J acquired USD 17.5bn net of cash in FY2025, funded by operating cash flow [CLM-003086] [CLM-009049]. (INTERPRETATION: Takeda's balance sheet does not allow that scale.)

**C. Problem.** Takeda needs pipeline depth after 2030 (IVB-008) and its only bridge in v1 (BET-15, USD 5bn or more) fails its own leverage test: adjusted net debt to EBITDA is 2.6x [CLM-005005]; council arithmetic gives about 3.1x after a USD 5bn purchase and about 3.4x if the Amitiza provision is also debt-funded (ASM-119) [CLM-005014]. No significant acquisitions in three years [CLM-009087]; the pipeline refill instrument that fits the balance sheet has no funded line.

**D. Evidence.**

- FACT: four of six late-stage programmes were externally sourced; Takeda licensed fazirsiran (Arrowhead), rusfertide (Protagonist, Phase 3 primary endpoint met) and elritercept (Keros) [CLM-005050] [CLM-009080] [CLM-005031] [CLM-009081] [CLM-005039].
- FACT: Nimbus delivered (Phase 3 positive, NDA accepted) while AbbVie wrote down 54% of Cerevel's net price; single-asset binary risk is the reason to cap per-deal upfronts [CLM-009076] [CLM-005035] [CLM-009054].
- INTERPRETATION (council arithmetic, ASM-119): debt headroom to the 3.0x ceiling is about JPY 554bn (about USD 3.7bn at ASM-001) before Amitiza and about JPY 150bn (about USD 1.0bn) if the Amitiza provision is debt-funded, which is why the balanced pool is about USD 1.0bn and a Nimbus-size upfront does not fit [CLM-005005] [CLM-005014].
- FACT: contingent consideration and sales milestones are the structures Takeda and AbbVie use to share risk (Nimble, DJS, Nimbus) [CLM-009099].
- FACT (limit): option and early-licence deals from the window have no approved product at cutoff, so the channel is for Phase 2/3 assets with human data, not early options (BET-06) [CLM-009097].

*Takeda baseline.* Class 5 external innovation and BD is a strength: four of six late-stage programmes were externally sourced (Arrowhead, Protagonist, Keros, Innovent) and Takeda's pattern is mid-size licensing after one flagship purchase (Nimbus, USD 4.0bn upfront); the organisation behind it is an EVIDENCE_GAP (IVB-007) [CLM-005050] [CLM-009098] [CLM-009076] [CLM-009078]. This bet funds an instrument Takeda already uses; it does not create a capability.

*Competitor analogues.* ABBV: [CLM-003086] [CLM-009054] [CLM-009061]; JNJ: [CLM-009049]

**E. Moat mechanism.** ecosystem, regulatory_experience. Ecosystem and selection skill: Takeda's late-stage execution and stop discipline convert licensed assets into approvals [CLM-005042] [CLM-005024]. No compounding moat from the purchase itself; value is the asset's IP and data (INTERPRETATION).

**F. Practical architecture.** Build: Channel policy: per-deal upfront ceiling, leverage test, kill criteria and a deal-outcome scorecard shared with BET-06. Buy: No acquisition of whole companies under this bet. License: Phase 2/3 in-licences and option-to-acquire structures with milestone-weighted payments. Partner: Co-development and regional-rights partners to hold the upfront down.

**G. Investment (USD m, cumulative by horizon, ASSUMPTION; ranges per ASM-036; ids ASM-118).**


| Portfolio | H1 2027-29 initial | H2 2030-34 follow-on | H3 2035-40 scaled | Total |
|---|---|---|---|---|
| capital_constrained | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| balanced | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |
| ambitious | 0 (0-0) | 0 (0-0) | 0 (0-0) | 0 |


*Contingent (not committed; ASM-118, released only if the leverage test passes):* constrained 500; balanced 1,030; ambitious 2,000. Per-deal upfront ceiling range USD 500-2,000m.


**H. Time to value.** Near term: 2027 H2: leverage policy and per-deal ceiling set after IVB-012 (RM-054). Long horizon: 2031-2036: first Phase 3 starts or approvals from licensed assets (ASSUMPTION ASM-120).

**I. Measurable outcomes.**

- Per-deal upfront ceiling and leverage test agreed (ASM-118, ASM-033) after IVB-012
- Share of Phase 2/3 licences reaching approval versus the ASM-120 range
- Leverage after each deal versus ASM-033

**J. Risks.**

- capital: Leverage and Amitiza cash timing; no deal if adjusted net debt to EBITDA would exceed ASM-033 (IVB-012) [CLM-005005] [CLM-005014].
- scientific: Single-asset binary risk, concentrated in neuroscience and gene therapy [CLM-009054] [CLM-009100].
- competition: AbbVie and J&J bid for the same assets with larger balance sheets [CLM-003086] [CLM-009049].
- execution: External-innovation organisation undocumented (IVB-007) [CLM-014052].
- regulatory: Antitrust not researched [CLM-009098].

**K. Strategic options.** expand, redirect, partner, stop. Expand the pool if IVB-012 shows headroom; redirect to BET-05 breadth or BET-06 options if leverage binds; stop if the leverage test fails for two reviews.

**L. Decision: PARTNER.** Funded, bounded and contingent: a licensing channel sized USD 0.5-2bn (ASM-118), released only if IVB-012 shows leverage headroom to the ASM-033 ceiling. The USD 1,030m contingent pool in the balanced portfolio is the headroom freed from the council's changes, not a saving. Dissent recorded: the capital council is conditional (nothing is funded now); the red team opposes waiting; Takeda execution is conditional on leverage policy and the new CEO [CLM-005073]. v2 addition, council-proposed. Hard prerequisites: none. Sequencing: Policy and per-deal ceiling in 2027 H2 (RM-054), after IVB-012; soft dependency on BET-05 launch curves (IVB-005) for sizing and on the BET-06 scorecard (RM-007) for selection discipline. No capital is committed until the leverage test passes.

**M. Evidence and confidence (hypothesis).** Known: Takeda's licensing pattern and deal terms [CLM-009076] [CLM-009078]; leverage 2.6x [CLM-005005]. Assumed: Ceiling and pool (ASM-118), headroom arithmetic (ASM-119), probability of approval (ASM-120). Needs Takeda internal validation: IVB-012, IVB-005, IVB-007, IVB-014 ([backlog](../../New_mediciine/companies/takeda_public_baseline/internal_validation_backlog/backlog.md)).

**v2 changes from v1.** (decision record row 1) New bet BET-18 added by the Director (council-proposed): PARTNER/INVEST, USD 0.5-2bn contingent on IVB-012 and ASM-033; A-M template completed by A11c-bis.


## Changes from v1 (strategic bets)

This file is **v2**. It implements strategy/critical_challenges/DIRECTOR_DECISION_RECORD.md (2026-11-21). Each change cites its decision-record row (row numbers 1-10 are the table rows; '—' rows are the unnumbered rows).

- Row 1: BET-15 DEFER -> REJECT as framed (fails the 3.0x leverage ceiling by council arithmetic, ASM-119); its stage gates are removed and its roadmap milestones move to BET-18.
- Row 1: New BET-18 'Phase 2/3 in-licensing channel' (PARTNER, secondary INVEST; USD 0.5-2bn contingent on IVB-012 and ASM-033; ASM-118 to ASM-120) with a complete A-M template labelled 'v2 addition (council-proposed)'; USD 0 committed, contingent pool 500 / 1,030 / 2,000.
- Row 2: ASM-025 range widened 2030-2032 -> 2028-2032 (central 2031 unchanged); ASM-038 early-entry stress case; stress case S-A added to scenarios; RM-026 moved 2029 H2 -> 2028 H1 and RM-031 to 2028 H2 (earliest window).
- Row 3: BET-06 balanced USD 700m -> 300m, scorecard-first; the USD 400m balance is contingent on RM-007 and the first two deals.
- Row 4: BET-02 BUILD -> EXPERIMENT; balanced USD 430m -> 230m (baseline and shadow-mode tranche about USD 65m at risk); ASM-031 re-based on money; demand-versus-capacity and plasma-peer tests added as gates (RM-004, new RM-051); Takeda-execution dissent recorded.
- Row 5: BET-03 balanced USD 500m -> 300m; Phase 1 gate before the H2 tranche (RM-030); additionality test and competitor orexin scan (new RM-052).
- Row 6: BET-04 stays BUILD; benefit-channel gate 2027 H1 (RM-003, IVB-004); outcome reframed 'retain 10 points of erosion' -> 'delay and measure'.
- Row 7: BET-07 prerequisites re-wired (RM-020 depends on RM-015 and RM-018; RM-011 on the decision-log standard and contract stop rules, new RM-053); balanced USD 180m -> 80m with H2/H3 tranches released only at RM-020.
- Row 8: BET-11 stays BUILD; baseline first; BET-04 channel conflict stated and wired (RM-013 depends on RM-003); confidence -> hypothesis.
- Row 9: BET-12 capped at USD 50m (from 100m), attached to the oveporexton launch, start 2027 H2 -> 2027 H1 (RM-012).
- Row 10: BET-13 carry removed (balanced USD 80m -> 0; ambitious USD 160m -> 0 by the proportional rescale).
- Row 10: BET-17 measurement owner moved from the CFO to internal audit or the CDTO with Audit Committee visibility.
- Row 10: Six bets (BET-04, 05, 08, 09, 11, 16) relabelled evidence_backed -> hypothesis (BET-11 also in row 8).
- Row 10: CVS Caremark Zepbound removal corrected from 'about 11 months [CLM-007011]' to about 15 months [CLM-007011] [CLM-007013].
- Row — (re-rating): Published robustness table is the council's re-rating (19 of 85 cells changed); the strategy author's v1 rating is kept as a second column.
- Row — (owned labs): 'Owned labs fail' narrative softened for BET-09 and BET-10: Lilly's reason undisclosed, the Strateos link unsupported, the NVIDIA joint lab reads as re-platforming; BET-10 stays REJECT with an operational trigger set (T1-T3).
- Row Net effect: Balanced USD 2,950m -> 1,920m committed-at-gates (plus about USD 1,030m contingent headroom for BET-18, not a saving); capital-constrained USD 1,590m -> 1,130m and ambitious USD 4,975m -> 3,155m by proportional rescale of the changed bets; core H1 2027-29 tranche USD 465m.


---

## Reading notes

- A BUILD decision on a capability whose baseline class is EXISTING_BUT_UNDERDEVELOPED (BET-01) means extend and measure an existing platform; it is not a new build.
- EVIDENCE_GAP in the baseline is a public-evidence gap, not an absence [CLM-005080]. BET-07, BET-09, BET-12 and BET-16 sit on EVIDENCE_GAP classes, so their decisions are the most dependent on IVB-001, IVB-002, IVB-010 and IVB-013.
- Owned-lab narrative (v2): the causes of Lilly's sale and Zymergen's failure are largely undisclosed, so 'owned labs fail' is a hypothesis; BET-10 stays REJECT with an operational trigger set [CLM-006017] [CLM-000281].
- Single-source and vendor claims (Nabla loop time, TuneLab data-point counts, AISB gain) are cited as claims of the source and not as outcomes [CLM-006040] [CLM-009028] [CLM-006043].
