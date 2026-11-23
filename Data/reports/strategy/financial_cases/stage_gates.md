# Stage gates (A11c v2, wave 6)

**Version v2** (A11c-bis, 2026-11-21). Gate capital is allocated in whole USD 5m units that sum to the bet size, so no bet's gates exceed its size.

Each material bet moves discovery -> feasibility -> prototype -> controlled pilot -> scale decision -> ongoing value review. Capital at risk is the balanced-portfolio capital committed between that gate and the next (USD m, ASSUMPTION ASM-037 shares of the balanced total; BET-02 and BET-18 use the explicit gate amounts shown in the JSON `capital_at_risk_usd_m`; BET-18 gates draw on its contingent pool, not on committed capital). Owner and authority are roles, not named persons; the delegated limits are not public and are an ASSUMPTION. Shorter gate lists (BET-05, 08, 12, 13, 17, 18) use the stage names that apply and the shares in the JSON. REJECT bets (BET-10, 14, 15, 16) have no gates; BET-10 and BET-14 are governed by the ladder triggers in BET-09 and the roadmap.

**Rules that apply to every gate.** (1) A gate decision is made on the evidence listed, not on spend to date. (2) A missed stop criterion ends or redirects the bet unless the decision authority records a reason in writing (RECOMMENDATION). (3) Expansion releases the next tranche only; no tranche is pre-committed beyond the portfolio horizon. (4) Evidence is reviewed against a baseline set at the preceding gate, so usage or enrolment counts do not substitute for outcomes [CLM-006022] [CLM-007039].


## BET-01 Governed cross-franchise R&D data and decision layer (BUILD)

Bet size for gate purposes: USD 200m (committed); gate capital sums to 200.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| discovery | 10 | Inventory of data and AI products with users and outcomes (IVB-001). | Inventory complete; baselines for two decisions. | No decision can be baselined by end 2027 H2. | Two decisions have baselines and owners. | Chief Digital and Technology Officer (role) | Executive Team on recommendation of the Portfolio Review Committee |
| feasibility | 20 | Thin-slice catalogue, metadata standard and decision log live. | Standard adopted by one franchise and plasma. | Standard not adopted by a second function within 12 months. | Second function adopts. | Chief Digital and Technology Officer (role) | Executive Team on recommendation of the Portfolio Review Committee |
| prototype | 30 | Governed layer used in two named decisions. | Two decisions logged versus baseline. | No measured effect on cycle time, hit rate or cost per decision. | Measured effect in at least one decision. | Chief Digital and Technology Officer (role) | Executive Team on recommendation of the Portfolio Review Committee |
| pilot | 50 | Pilot across two franchises; reuse of trial data permitted by governance. | Reuse policy approved; reuse rate measured. | Reuse rate below threshold set in feasibility (ASSUMPTION). | Reuse above threshold. | Chief Digital and Technology Officer (role) | Executive Team on recommendation of the Portfolio Review Committee |
| scale | 70 | Enterprise scale, run cost known. | Layer supports R&D-wide decision log. | Run cost exceeds measured benefit. | Benefit exceeds run cost by gate-agreed margin. | Chief Digital and Technology Officer (role) | Executive Team on recommendation of the Portfolio Review Committee |
| value_review | 20 | Annual review of decisions changed by models. | Annual value review. | Two consecutive reviews with no attributable benefit. | Extend to new decision classes. | Chief Digital and Technology Officer (role) | Executive Team on recommendation of the Portfolio Review Committee |

## BET-02 Plasma process-intelligence and fixed-price automation programme (EXPERIMENT)

Bet size for gate purposes: USD 230m (committed); gate capital sums to 230.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| discovery | 20 | Yield, cost per litre and deviation baseline per centre (IVB-006) and the demand-versus-capacity test: H1 FY2026 PDT revenue was -1.5% CER, which does not show a capacity constraint [CLM-005064]. | Baseline and demand-versus-capacity result. | Plasma is demand-bound, or headroom is below ASM-031 after the baseline: redirect or stop. | Capacity-bound and headroom at or above ASM-031. | Head of Plasma-Derived Therapies business unit (role) | Executive Team; Board for capital over the delegated limit (ASSUMPTION) |
| feasibility | 45 | Plasma-peer benchmark of yield and cost per litre (no plasma peer is in the registry [CLM-009091]); ASM-031 re-based on money; vendor options priced fixed-price and outcome-linked [CLM-011031]. | Benchmark, re-based threshold and two vendor bids. | No plasma-peer data obtainable, or no vendor accepts outcome-linked terms. | Benchmark shows a distinct data position and at least one bid is within the envelope. | Head of Plasma-Derived Therapies business unit (role) | Executive Team; Board for capital over the delegated limit (ASSUMPTION) |
| prototype | 35 | Digital upgrade running in shadow mode at one site; first two gates hold about USD 65m at risk. | Shadow-mode data for two quarters. | Model predictions do not improve on the nomogram baseline [CLM-005060]. | Predictions beat baseline. | Head of Plasma-Derived Therapies business unit (role) | Executive Team; Board for capital over the delegated limit (ASSUMPTION) |
| pilot | 60 | Pilot at Los Angeles with validated change control, released only if the first three gates pass. | Pilot results versus the ASM-031 threshold in money; inspection status clean. | New inspection observations attributable to the pilot, or below threshold. | At or above threshold with clean inspection. | Head of Plasma-Derived Therapies business unit (role) | Executive Team; Board for capital over the delegated limit (ASSUMPTION) |
| scale | 60 | Network roll-out in waves. | Wave 1 completed. | Wave 1 below pilot results by a gate-set margin. | Wave results hold. | Head of Plasma-Derived Therapies business unit (role) | Executive Team; Board for capital over the delegated limit (ASSUMPTION) |
| value_review | 10 | Annual review of yield, cost and deviations. | Value review. | Two reviews without sustained gain. | Extend to neutral analytics test (low confidence). | Head of Plasma-Derived Therapies business unit (role) | Executive Team; Board for capital over the delegated limit (ASSUMPTION) |

## BET-03 Orexin science as a multi-asset discovery platform (BUILD)

Bet size for gate purposes: USD 300m (committed); gate capital sums to 300.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| discovery | 15 | Orexin biology map beyond narcolepsy type 1; target candidates. | Indication map and lead criteria. | No second target or indication clears safety criteria (liver history [CLM-005023]). | Candidate class with clean safety rationale. | Head of Research (role) | R&D Committee |
| feasibility | 30 | Candidate profile and tox plan; additionality test against base R&D (JPY 675.9bn [CLM-005004]) and competitor orexin scan (research gap). | Candidate selection; additionality and competitor scan reported before the H2 tranche. | No candidate by gate date, or the spend is not incremental to base R&D. | Candidate selected and incremental share demonstrated. | Head of Research (role) | R&D Committee |
| prototype | 45 | Preclinical package and first-in-human readiness. | IND-enabling complete. | Safety signal in preclinical package. | Package supports start. | Head of Research (role) | R&D Committee |
| pilot | 75 | Phase 1 and early Phase 2 quality (placebo response, exposure, safety); a second candidate clean through Phase 1 releases the H2 tranche (RM-030). | Phase 1 gate: H2 tranche decision. | Safety or exposure failure; weak Phase 2 design (LES-18). | Clean Phase 1; credible Phase 2 design. | Head of Research (role) | R&D Committee |
| scale | 105 | Late-stage programme; partner decision on non-core indications. | Phase 3 start. | Phase 2 misses primary endpoint. | Phase 2 positive; Phase 3 funded from base R&D. | Head of Research (role) | R&D Committee |
| value_review | 30 | Value review after first approval. | Annual review. | Single-asset only after 2040 (platform claim withdrawn). | Two assets approved: declare platform. | Head of Research (role) | R&D Committee |

## BET-04 Entyvio franchise defence: payer contracting, evidence and lifecycle (BUILD)

Bet size for gate purposes: USD 140m (committed); gate capital sums to 140.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| discovery | 5 | Benefit-channel gate (IVB-004): medical versus pharmacy benefit split of Entyvio volume; erosion scenarios and patent posture. | Gate decision 2027 H1 (RM-003): continue, or redirect part of the spend to provider and site-of-care strategy. | Most volume is outside the contractable channel and no provider-side lever exists. | Most volume is contractable. | Head of GI franchise and U.S. business unit (role) | Executive Team |
| feasibility | 15 | Contracting capability assessment; payer segment net price and persistence. | Capability assessment and playbook. | Playbook shows no feasible contracting lever. | Levers identified. | Head of GI franchise and U.S. business unit (role) | Executive Team |
| prototype | 20 | Contracting posture ready for January 2028 negotiated price [CLM-007026]. | Posture signed off. | n/a (date-fixed). | Posture tested in scenario table. | Head of GI franchise and U.S. business unit (role) | Executive Team |
| pilot | 35 | Pilot of outcomes and persistence evidence; patient-programme changes piloted before roll-out [CLM-003088]. | Pilot results. | Pilot shows loss of share. | Pilot retains share. | Head of GI franchise and U.S. business unit (role) | Executive Team |
| scale | 50 | Biosimilar-event playbook live before ASM-025 earliest entry. | Playbook live. | n/a. | Triggered on first entry. | Head of GI franchise and U.S. business unit (role) | Executive Team |
| value_review | 15 | Net price and persistence measured against the ASM-024 low case (delay and measure). | Annual review. | Net price and persistence below the ASM-024 low case: redirect to lifecycle. | Net price and persistence at or above the ASM-024 midpoint. | Head of GI franchise and U.S. business unit (role) | Executive Team |

## BET-06 Option-based external innovation engine incl. new-modality options (PARTNER)

Bet size for gate purposes: USD 300m (committed); gate capital sums to 300.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| discovery | 15 | Target modality and disease-depth map; kill criteria. | Criteria approved. | No adjacent modality with disease depth. | One or two modalities selected. | Head of Corporate Development and External Innovation (role) | Portfolio Review Committee; Board for large transactions |
| feasibility | 30 | Deal-outcome scorecard from Takeda's past deals; options priced; the contingent balance of the v1 size stays unreleased until this gate and the first two deals. | Scorecard and price bands (RM-007). | Option fees above band. | Within band. | Head of Corporate Development and External Innovation (role) | Portfolio Review Committee; Board for large transactions |
| prototype | 45 | First 2-3 option or licence deals signed with exercise on Phase 1/2 data. | Deals signed. | Counterparty terminates (Denali and Neurocrine precedent [CLM-009089] [CLM-009090]). | Phase 1 data positive. | Head of Corporate Development and External Innovation (role) | Portfolio Review Committee; Board for large transactions |
| pilot | 75 | Option exercise on data. | Exercise decisions. | Phase 1 safety or exposure failure. | Exercise on clean data. | Head of Corporate Development and External Innovation (role) | Portfolio Review Committee; Board for large transactions |
| scale | 105 | Late-stage conversion and capital. | Phase 3 starts from options. | Impairments exceed 54% of deal value benchmark [CLM-009054]. | Approval path credible. | Head of Corporate Development and External Innovation (role) | Portfolio Review Committee; Board for large transactions |
| value_review | 30 | Three-year impairment and conversion review. | Value review. | Conversion below 0.05 (ASM-028 low). | Conversion at or above 0.10. | Head of Corporate Development and External Innovation (role) | Portfolio Review Committee; Board for large transactions |

## BET-07 Milestone-gated AI-design partnerships (Nabla, Iambic and successors) (PARTNER)

Bet size for gate purposes: USD 80m (committed); gate capital sums to 80.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| discovery | 5 | Review of Nabla and Iambic data package plans. | Plans with go/no-go. | No data-gated structure. | Gates agreed. | Head of Research (role) | R&D Committee |
| feasibility | 10 | Benchmark design: AI-origin versus conventional on Takeda targets; needs the BET-01 decision log (RM-015) and the BET-09 cost benchmark (RM-018). | Benchmark approved. | No benchmark baseline. | Benchmark approved. | Head of Research (role) | R&D Committee |
| prototype | 10 | Nabla first-in-human expected within one to two years of October 2025 [CLM-006039]; stop rules written into contracts before the next payment (RM-053). | First-in-human data in hand. | Data absent by 2028 H2 or negative. | Data positive versus conventional. | Head of Research (role) | R&D Committee |
| pilot | 20 | Phase 1 starts from AI programmes; Phase 2 transition. | Phase 1 results. | Safety or exposure failure. | Transition rate at or above conventional. | Head of Research (role) | R&D Committee |
| scale | 30 | Scale partnership or license. | Scale terms. | Success-based payments grow faster than data. | Data justify scale. | Head of Research (role) | R&D Committee |
| value_review | 5 | Annual review versus Phase 2 transition rate. | Value review. | Transition below conventional for two cycles. | Above conventional. | Head of Research (role) | R&D Committee |

## BET-09 Rented automated data generation (CRO and cloud labs) with ladder triggers (PARTNER)

Bet size for gate purposes: USD 95m (committed); gate capital sums to 95.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| discovery | 5 | Define assays needed for BET-07 and orexin work. | Assay list. | No assay suitable for rent. | List approved. | Head of R&D (role) | R&D Committee; Executive Team at scale gates |
| feasibility | 10 | CRO and cloud-lab quotes; data schema agreed (thin slice of BET-01). | Quotes and schema. | No provider meets quality and IP terms. | Provider selected. | Head of R&D (role) | R&D Committee; Executive Team at scale gates |
| prototype | 15 | Pilot contract with acceptance criteria. | Contract signed. | n/a. | Contract signed. | Head of R&D (role) | R&D Committee; Executive Team at scale gates |
| pilot | 25 | Cost per data point and turnaround versus internal baseline. | Pilot results. | Cost above internal baseline. | Cost at or below baseline. | Head of R&D (role) | R&D Committee; Executive Team at scale gates |
| scale | 30 | Scale service use; stage-3 pilot only if triggers fire [CLM-011066]. | Scale or stage-3 decision. | Triggers not met. | Triggers met. | Head of R&D (role) | R&D Committee; Executive Team at scale gates |
| value_review | 10 | Annual cost and quality review. | Value review. | Vendor quality fails twice. | Maintain. | Head of R&D (role) | R&D Committee; Executive Team at scale gates |

## BET-11 Drug-device and home/SC administration platform (BUILD)

Bet size for gate purposes: USD 190m (committed); gate capital sums to 190.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| discovery | 10 | Device pipeline map for Entyvio, Hyqvia and new launches. | Device map. | No device addresses a defined need. | Needs defined. | Head of GI franchise and U.S. business unit (role) | Executive Team |
| feasibility | 20 | Patient and payer value of formats; channel decision against the BET-04 benefit-channel gate (RM-003): does moving patients into the pharmacy benefit help or hurt after entry [CLM-007015]? | Format value assessment and channel decision. | No persistence advantage plausible, or SC raises exposure after entry. | Advantage plausible and channel exposure acceptable. | Head of GI franchise and U.S. business unit (role) | Executive Team |
| prototype | 30 | Next-generation device prototype. | Prototype tested. | Usability failure. | Passes usability. | Head of GI franchise and U.S. business unit (role) | Executive Team |
| pilot | 45 | Controlled launch with persistence measures. | Pilot persistence. | SC erodes net price faster than it retains patients [CLM-007053]. | Persistence higher than IV. | Head of GI franchise and U.S. business unit (role) | Executive Team |
| scale | 65 | Wider launch. | Scale. | Device recall or clearance setback. | Adoption target met. | Head of GI franchise and U.S. business unit (role) | Executive Team |
| value_review | 20 | Annual review after biosimilar entry. | Value review. | No retention effect after entry. | Retention effect shown. | Head of GI franchise and U.S. business unit (role) | Executive Team |

## BET-05 Zasocitinib breadth and immunology successor evidence (INVEST)

Bet size for gate purposes: USD 180m (committed); gate capital sums to 180.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| feasibility | 35 | Plan for incremental indications and comparative data. | Plan approved. | No incremental indication with evidence. | Indications identified. | Head of R&D (role) | R&D Committee; Executive Team at scale gates |
| pilot | 55 | PsA Phase 3 results (study end May 2027 [CLM-005037]). | PsA readout. | PsA misses primary endpoint. | PsA positive. | Head of R&D (role) | R&D Committee; Executive Team at scale gates |
| scale | 70 | Approval and launch execution; payer coverage at 6 and 12 months. | Launch metrics. | Coverage and uptake below plan. | Coverage at plan. | Head of R&D (role) | R&D Committee; Executive Team at scale gates |
| value_review | 20 | Annual review of replacement versus Entyvio exposure. | Value review. | n/a. | Extend to further indications. | Head of R&D (role) | R&D Committee; Executive Team at scale gates |

## BET-08 Federated data consortium participation (PARTNER)

Bet size for gate purposes: USD 35m (committed); gate capital sums to 35.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| feasibility | 5 | Held-out evaluation set defined. | Set and metrics. | No Takeda task with measurable gain. | Metric defined. | Chief Digital and Technology Officer (role) | Executive Team on recommendation of the Portfolio Review Committee |
| pilot | 20 | Pooled model on Takeda held-out data versus public and Takeda-only models. | Evaluation result. | Pooled model does not beat alternatives. | Gain shown. | Chief Digital and Technology Officer (role) | Executive Team on recommendation of the Portfolio Review Committee |
| value_review | 10 | Annual review of tasks and gains. | Value review. | Two reviews without gain. | Add tasks. | Chief Digital and Technology Officer (role) | Executive Team on recommendation of the Portfolio Review Committee |

## BET-12 Launch-pathway partnerships and patient-services outcome measurement (EXPERIMENT)

Bet size for gate purposes: USD 50m (committed); gate capital sums to 50.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| prototype | 10 | Launch-pathway design attached to the oveporexton launch with a named leader; time-to-therapy baseline; start 2027 H1. | Design and baseline. | No pathway bottleneck identified. | Bottleneck identified. | Head of Patient Services and Market Access, U.S. (role) | Executive Team |
| pilot | 15 | Pilot with diagnosis or site partners; compliance review [CLM-007010]. | Pilot results. | No improvement in time to first dose. | Improvement shown. | Head of Patient Services and Market Access, U.S. (role) | Executive Team |
| scale | 20 | Extend to other launches. | Scale. | Compliance finding. | Gain holds. | Head of Patient Services and Market Access, U.S. (role) | Executive Team |
| value_review | 5 | Annual review. | Value review. | n/a. | Registry decision (BET-13). | Head of Patient Services and Market Access, U.S. (role) | Executive Team |

## BET-17 AI use-case measurement, decision support and reskilling (EXPERIMENT)

Bet size for gate purposes: USD 120m (committed); gate capital sums to 120.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| feasibility | 25 | Use-case list and baselines (IVB-001, IVB-003). | Baselines. | No baseline for a use case: stop that use case. | Baselines set. | Head of Internal Audit or Chief Digital and Technology Officer, with Audit Committee visibility (role; independent of the savings-target owner) | Audit Committee oversight; Executive Team for scale gates |
| pilot | 35 | Measured pilots incl. advisory-only decision support [CLM-011074]. | Pilot results. | No measured benefit. | Benefit shown. | Head of Internal Audit or Chief Digital and Technology Officer, with Audit Committee visibility (role; independent of the savings-target owner) | Audit Committee oversight; Executive Team for scale gates |
| scale | 50 | Scale measured use cases; reskilling plan measured by task capability [CLM-011081]. | Scale. | Retention or morale deterioration. | Capability measure improves. | Head of Internal Audit or Chief Digital and Technology Officer, with Audit Committee visibility (role; independent of the savings-target owner) | Audit Committee oversight; Executive Team for scale gates |
| value_review | 10 | Annual share of use cases with measured benefit. | Value review. | n/a. | Continue. | Head of Internal Audit or Chief Digital and Technology Officer, with Audit Committee visibility (role; independent of the savings-target owner) | Audit Committee oversight; Executive Team for scale gates |

## BET-13 Neutral rare-disease or plasma real-world data registry (DEFER)

Bet size for gate purposes: USD 0m (committed); gate capital sums to 0.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| discovery | 0 | Disease choice and neutral sponsor options. | Options paper (2029). | No neutral sponsor. | Sponsor exists. | Chief Digital and Technology Officer (role) | Executive Team on recommendation of the Portfolio Review Committee |
| feasibility | 0 | Pilot registry with patient organisations; consent model. | Pilot decision (2030). | Consent or demand insufficient. | Pilot launched. | Chief Digital and Technology Officer (role) | Executive Team on recommendation of the Portfolio Review Committee |

## BET-18 Phase 2/3 in-licensing channel (PARTNER)

Bet size for gate purposes: USD 1,030m (contingent pool); gate capital sums to 1,030.

| Stage | Capital at risk USD m | Evidence required | Commercial milestone | Stop criteria | Expansion criteria | Owner role | Decision authority |
|---|---|---|---|---|---|---|---|
| discovery | 0 | Leverage policy: adjusted net debt to EBITDA ceiling (ASM-033) and Amitiza cash timing (IVB-012); per-deal upfront ceiling (ASM-118). | Policy and per-deal ceiling set (RM-054). | Leverage test fails: no deal. | Test passes with headroom (ASM-119). | Head of Corporate Development and External Innovation (role) | Portfolio Review Committee; Board for large transactions |
| feasibility | 0 | Screen of Phase 2/3 assets with human data; deal-outcome scorecard shared with BET-06 (RM-007). | Short list within the ceiling. | No asset within the ceiling, or kill criteria met. | At least one asset within the ceiling. | Head of Corporate Development and External Innovation (role) | Portfolio Review Committee; Board for large transactions |
| pilot | 500 | First licence or option with milestone-weighted payments; one-write-down test: a write-down must not breach ASM-033 or dividend policy [CLM-005006]. | First deal signed. | Write-down test fails. | Test passes. | Head of Corporate Development and External Innovation (role) | Portfolio Review Committee; Board for large transactions |
| scale | 530 | Second and later deals under the same tests; impairment review against the Cerevel benchmark [CLM-009054]. | Further deals signed within the pool (ASM-118). | Impairments exceed 54% of deal value benchmark [CLM-009054]. | Phase 3 starts or approval path credible. | Head of Corporate Development and External Innovation (role) | Portfolio Review Committee; Board for large transactions |

## Changes from v1 (stage gates)

This file is **v2**. It implements strategy/critical_challenges/DIRECTOR_DECISION_RECORD.md (2026-11-21). Each change cites its decision-record row (row numbers 1-10 are the table rows; '—' rows are the unnumbered rows).

- Row 1: BET-15 DEFER -> REJECT as framed (fails the 3.0x leverage ceiling by council arithmetic, ASM-119); its stage gates are removed and its roadmap milestones move to BET-18.
- Row 1: New BET-18 'Phase 2/3 in-licensing channel' (PARTNER, secondary INVEST; USD 0.5-2bn contingent on IVB-012 and ASM-033; ASM-118 to ASM-120) with a complete A-M template labelled 'v2 addition (council-proposed)'; USD 0 committed, contingent pool 500 / 1,030 / 2,000.
- Row 3: BET-06 balanced USD 700m -> 300m, scorecard-first; the USD 400m balance is contingent on RM-007 and the first two deals.
- Row 4: BET-02 BUILD -> EXPERIMENT; balanced USD 430m -> 230m (baseline and shadow-mode tranche about USD 65m at risk); ASM-031 re-based on money; demand-versus-capacity and plasma-peer tests added as gates (RM-004, new RM-051); Takeda-execution dissent recorded.
- Row 5: BET-03 balanced USD 500m -> 300m; Phase 1 gate before the H2 tranche (RM-030); additionality test and competitor orexin scan (new RM-052).
- Row 6: BET-04 stays BUILD; benefit-channel gate 2027 H1 (RM-003, IVB-004); outcome reframed 'retain 10 points of erosion' -> 'delay and measure'.
- Row 7: BET-07 prerequisites re-wired (RM-020 depends on RM-015 and RM-018; RM-011 on the decision-log standard and contract stop rules, new RM-053); balanced USD 180m -> 80m with H2/H3 tranches released only at RM-020.
- Row 8: BET-11 stays BUILD; baseline first; BET-04 channel conflict stated and wired (RM-013 depends on RM-003); confidence -> hypothesis.
- Row 9: BET-12 capped at USD 50m (from 100m), attached to the oveporexton launch, start 2027 H2 -> 2027 H1 (RM-012).
- Row 10: BET-13 carry removed (balanced USD 80m -> 0; ambitious USD 160m -> 0 by the proportional rescale).
- Row 10: BET-17 measurement owner moved from the CFO to internal audit or the CDTO with Audit Committee visibility.
- Row 10: Stage-gate capital at risk is now allocated in whole USD 5m units that sum to the bet size, so no gate total exceeds the bet size (v1 exceeded it by USD 5m for BET-02, 07, 09 and 11).
