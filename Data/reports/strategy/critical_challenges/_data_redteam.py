# Red-team attack on each bet: (strongest_case, evidence_text, claim_ids, must_be_true[list], kill[list], rating)
# rating: how exposed the bet is to the attack: HIGH / MEDIUM / LOW
RED = {}

RED["BET-01"] = (
 "A governance layer over a platform Takeda says it already has (a Databricks agent platform for 10,000+ employees, insourced digital factories) duplicates existing spend and will be judged by usage counts, the same failure visible in J&J's 47,000 course completions. No data layer at any company has an independent outcome, and the only Takeda outcome claim (about 30% shorter narcolepsy trial development) is one executive interview. If Takeda's estate is already governed, the incremental value is near zero and USD 200m is a sunk platform that is hard to stop.",
 "No independent outcome for ARCH, TuneLab, Polyphonic or the AISB model; the 'fragmented estate' premise is a NEEDS_MORE_RESEARCH hypothesis; platform maturity is vendor self-report; 63.4% workforce use is an adoption metric.",
 "CLM-011052 CLM-011055 CLM-005058 CLM-014073 CLM-014043 CLM-006022",
 ["IVB-001 shows production use is thin or fragmented, not already governed.", "Two decisions can be baselined before any model is applied.", "A second function adopts the standard within 12 months."],
 ["No decision baselined by 2027 H2 (the bet's own test), then stop and redirect to BET-08.", "Gate 3 (RM-015, 2027 H2) shows zero of two decisions with a measured effect on cycle time, hit rate or cost.", "Run cost exceeds measured benefit at scale gate."],
 "MEDIUM")

RED["BET-02"] = (
 "The thesis rests on three unproven links: that plasma is capacity-bound (but H1 FY2026 PDT revenue was -1.5% at constant rates), that Takeda's process data are unique (the comparison set has no plasma peers), and that a fixed-price outcome-linked automation vendor exists (NEEDS_MORE_RESEARCH; the SpaceX source says its cost gap is not isolated and every cargo partner had catastrophic failures). Takeda has no public robotics evidence, a prior warning letter and shortage, and USD 230m of expansion without commissioning data. The follow-on of USD 350m is committed on a 2% threshold that has no economic anchor.",
 "PDT revenue +8.5% AER and -1.5% CER; no yield or productivity figures; no evidence of manufacturing robotics; Hikari warning letter with a USD 505m award; plasma peers (CSL, Grifols, Octapharma and others) are not in the registry.",
 "CLM-005064 CLM-005060 CLM-005067 CLM-005020 CLM-011031 CLM-011006 CLM-011008 CLM-005065",
 ["IVB-006 shows yield or cost headroom above the pilot threshold that matters in money terms (ASM-031 must be re-based on cost per litre).", "At least one vendor prices fixed-price, outcome-linked terms for GMP automation.", "Validated change control does not trigger new inspection observations.", "Plasma is capacity-bound, so lower cost per litre converts to revenue."],
 ["Baseline headroom below ASM-031 (re-based) by 2027 H2.", "No vendor accepts outcome-linked terms at feasibility.", "Any new inspection observation attributable to the pilot.", "PDT revenue stays flat or negative at CER after the Los Angeles capacity is commissioned (signals demand-bound)."],
 "HIGH")

RED["BET-03"] = (
 "Takeda's record in the window is one in-house orexin success against a liver-safety stop (TAK-994), a Phase 3 miss (soticlestat) and an exited cell-therapy platform. Second-asset approval is a 5-30% proposition by the strategy's own range, payoff is 2038, and USD 500m is 17% of the balanced envelope. A platform does not protect a product (EYLEA -42% in 2025). Meanwhile the Entyvio window opens in 2031 and the capital arrives after it. An orexin discovery team already sits in base R&D, so the incremental USD 500m may fund work that would happen anyway.",
 "ASM-021 15%; RM-048 platform test 2038; TAK-994 liver signal; soticlestat Phase 3 miss and JPY 21.5bn impairment; no competitor orexin review; EYLEA -42%.",
 "CLM-005023 CLM-012119 CLM-012120 CLM-009083 CLM-011017 CLM-011037 CLM-005025",
 ["A second orexin asset with a clean safety profile exists by 2028.", "Competitors have no faster follower in the same indications.", "The USD 500m is additive to the Shonan base budget."],
 ["No second target clears safety by gate 1 (2028).", "IND-enabling package incomplete by 2031 (RM-030 target H1 2030).", "Phase 2 fails on placebo response or exposure (LES-18).", "Single approval only after 2040: withdraw the platform claim."],
 "HIGH")

RED["BET-04"] = (
 "Humira is the best analogue and it argues against the premise: rebate-for-access held at least 97% of volume for 14 months, a co-brand route followed, and global Humira still fell 78.6% in three years. AbbVie and J&J already sell competing IBD products, and PBMs now prefer their own biosimilars (CVS Stelara template, July 2026). The January 2028 Medicare price is statutory and cannot be contracted away. Contracting levers work in the pharmacy benefit; Entyvio IV may largely sit outside it (not in the registry). USD 140m will not change an exposure of JPY 383-766bn a year, so the real risk is that the programme is a visible reassurance with no measurable lever.",
 "Humira -78.6% 2022-2025; US Humira -41% (2024) and -57% (2025); Skyrizi, Rinvoq and Tremfya hold IBD approvals; four of nine Stelara biosimilars are PBM-affiliated private labels; Entyvio selected for Medicare negotiation.",
 "CLM-003002 CLM-003007 CLM-003010 CLM-003016 CLM-002053 CLM-007015 CLM-007016 CLM-007026",
 ["IVB-004 shows a material pharmacy-benefit share of Entyvio that contracting can act on.", "A named lever moves net price or volume by a measurable amount against the ASM-024 low case.", "Patent posture (2032 patents, UK and Netherlands revocation actions) holds long enough for the playbook to matter."],
 ["IVB-004 (RM-003, 2027 H1) shows that most Entyvio volume is outside the contractable channel: redirect funds to provider and site-of-care strategy.", "Retained net revenue below the ASM-024 low case at the first annual review after the 2028 price.", "Biosimilar FDA approval and a launch date before RM-026 (playbook live 2029 H2): re-date the playbook."],
 "MEDIUM")

RED["BET-05"] = (
 "J&J's oral IL-23 peptide (Icotyde) was approved on 2026-03-17 with head-to-head superiority claims, so zasocitinib's head-to-head win over deucravacitinib is against the weaker comparator. Skyrizi and Tremfya hold psoriasis and IBD; Takeda would enter with a first launch under a new CEO, after 4,500 role reductions. The bet is correct to exist, but breadth is incremental money on a binary PsA readout in May 2027, and zasocitinib is not an Entyvio GI successor.",
 "Icotyde approval and head-to-head claims; PsA Phase 3 completion May 2027; milestones USD 1.0bn each at USD 4bn and 5bn net sales; USD 10-20bn peak is not probability-adjusted; inspection-driven CRLs at Lilly and AbbVie.",
 "CLM-012012 CLM-002065 CLM-005034 CLM-005037 CLM-009076 CLM-014049 CLM-012134 CLM-012112",
 ["PsA is positive and coverage at 6 and 12 months meets plan.", "Payers accept TYK2 oral therapy at parity with IL-23 oral and injectable products.", "NDA-supporting sites are inspection-clean."],
 ["PsA misses primary endpoint (2027).", "Coverage and uptake below plan at 12 months.", "FDA action slips beyond 2027 H2 on inspection grounds."],
 "MEDIUM")

RED["BET-06"] = (
 "No option from the window has produced an approved product, per-asset probability is 5-15%, and payoff is 2035 or later, so the engine does not bridge the 2031-34 Entyvio window. USD 700m over 14 years is smaller than one Takeda deal in 2025 (Innovent, USD 1.2bn upfront), so the 'engine' is sized to lose bidding contests to AbbVie (ADARx, Capstan) and Lilly (Verve), while the mid-size Phase 2/3 licences that actually produced Takeda's late-stage pipeline have no funded bet. Neuroscience, gene and cell therapy are where write-downs concentrate, and Takeda has just exited cell therapy at JPY 58.2bn.",
 "ASM-028 0.1; Innovent USD 1.2bn upfront; Denali and Neurocrine terminations; CEI and Ventures scope unknown; Lilly IPR&D expensed 2023-25 with no approval from those assets by cutoff.",
 "CLM-009097 CLM-009078 CLM-009089 CLM-009090 CLM-014052 CLM-009061 CLM-009010 CLM-009000 CLM-009084",
 ["Takeda's selection skill transfers from Phase 3 assets to Phase 1 options.", "Option fees stay within the scorecard bands.", "A separate funding line exists for Phase 2/3 licences."],
 ["No deal-outcome scorecard by 2027 H1 (RM-007).", "Counterparty terminates one of the first three options.", "Conversion below 5% at the three-year review (ASM-028 low), or impairment above 54% of deal value (the Cerevel benchmark)."],
 "HIGH")

RED["BET-07"] = (
 "The partner owns the model and Takeda owns an invoice. Lilly holds Isomorphic, Chai, OpenAI and NVIDIA compute; AbbVie holds BigHat and Valkai; five pharmas share the AISB fine-tune. Evidence that AI-origin molecules do better is absent (Recursion four of 11 ended; AI-origin Phase 2 about conventional; rentosertib liver discontinuations). Takeda's own gates are mis-sequenced, because the Nabla window opens before the comparator infrastructure exists. Success-based payments over USD 1bn per deal are liabilities that rise only if the science works.",
 "Nabla first-in-human is a company expectation; Iambic payments could exceed USD 1.7bn; Isomorphic raised a reported USD 600m; models converge on open weights.",
 "CLM-006047 CLM-006048 CLM-006049 CLM-006039 CLM-006041 CLM-006012 CLM-006010 CLM-006035 CLM-006043 CLM-006056",
 ["Nabla first-in-human data are positive against a conventional comparator.", "Takeda retains ownership of its assay and clinical data fed to partners.", "A benchmark exists before the data arrive."],
 ["Nabla first-in-human absent or negative by 2028 H2.", "Success-based payments committed grow faster than data-gated milestones achieved.", "Phase 2 transition below conventional for two review cycles."],
 "HIGH")

RED["BET-08"] = (
 "Cheap parity: Takeda is a follower in a consortium whose founding partners for the follow-on binding model are AbbVie, AstraZeneca, BMS and J&J. A pooled model that is 10 points better on a vendor-organised benchmark may not help Takeda targets, and the advantage accrues to whoever uses it best, which depends on the BET-01 decision layer that is itself unproven.",
 "AISB Bind lists AbbVie, AstraZeneca, BMS and J&J; the benchmark is vendor-organised and not peer reviewed.",
 "CLM-006044 CLM-006043 CLM-006056 CLM-006008",
 ["Held-out gain on Takeda targets beats public and Takeda-only models.", "Raw data never leaves Takeda governance."],
 ["Pooled model does not beat alternatives at RM-006 (2027 H1).", "Two annual reviews without gain."],
 "LOW")

RED["BET-09"] = (
 "Rented capacity is available to every rival, including AI-biotech entrants, so it yields parity not advantage. The evidence for renting over owning is a divestiture with an undisclosed reason plus an industrial-biotech failure; Lilly's later USD 1bn joint lab suggests the opposite lesson. The data-schema moat requires a standard that the roadmap delays behind a BET-17 inventory.",
 "Reason for Lilly's sale undisclosed; Strateos link unsupported; Zymergen is not a drug-discovery lab; Arctoris sells data generation to AI customers.",
 "CLM-006017 CLM-006014 CLM-006051 CLM-006016 CLM-000281 CLM-006052",
 ["CRO cost per data point is at or below Takeda's internal baseline.", "Data ownership and schema are enforceable in the contract."],
 ["Cost above internal baseline at RM-018 (2028 H1).", "Vendor quality fails twice.", "No trigger fires by the 2032 ladder review: stop stage-3 planning."],
 "LOW")

RED["BET-10"] = (
 "(Attack on the REJECT.) The rejection leans on 'two owned-model failures' that are really one divestiture of undisclosed cause and one company in another sector, while Lilly is investing up to USD 1bn jointly with NVIDIA and USD 4.5bn in a Medicine Foundry. If an owned closed-loop lab works in 2029-31 and Takeda has not built the data layer and CRO relationships, it will be years behind. The rejection is right for 2027 and wrong if the trigger set cannot be acted on.",
 "Lilly lab at concept; no independent outcome; triggers are NEEDS_MORE_RESEARCH.",
 "CLM-006017 CLM-006051 CLM-000281 CLM-006000 CLM-011066 CLM-006052",
 ["Triggers have dates, owners and a pre-agreed response.", "BET-01 and BET-09 exist so a stage-3 pilot can start within 12 months of a trigger."],
 ["Independent, audited cycle-time or hit-rate gain from the Lilly lab or any peer by 2029: reopen as a rented stage-3 pilot, not an owned build.", "Nabla first-in-human positive versus conventional: reopen."],
 "MEDIUM")

RED["BET-11"] = (
 "SC is table stakes: Tremfya, Skyrizi and Rinvoq are already convenient, and the biosimilars in review are IV. SC moves Entyvio patients into the pharmacy benefit, where PBM private-label biosimilar templates operate, so the pen could accelerate erosion after entry. Device IP does not outlive the drug's own protection, and Takeda has not shown persistence data.",
 "CLM-007053 is PARTIALLY_SUPPORTED yet the bet is labelled evidence_backed; PBM template from 1 July 2026; four of nine Stelara biosimilars are PBM-affiliated.",
 "CLM-007053 CLM-007015 CLM-007016 CLM-014051 CLM-007042 CLM-002026",
 ["SC users persist better after biosimilar entry than IV users.", "SC does not cannibalise IV before exclusivity loss."],
 ["SC erodes net price faster than it retains patients (stage-gate stop).", "No retention effect after entry (RM-040, 2033).", "Device recall or clearance setback."],
 "MEDIUM")

RED["BET-12"] = (
 "No company publishes persistence or time-to-therapy outcomes, so the bet has no benchmark and the hypothesis that pathways govern launch speed is untested. Oveporexton was approved on 2026-08-05; the pilot starts in 2027 H2 and reports in 2028 H2, after the launch curve forms. Pear's failure shows payers, not evidence, decide.",
 "Help at Hand is an enrolment count; Spravato and Carvykti constraints were certification and capacity; AbbVie's Allē change reversed within months.",
 "CLM-007039 CLM-007037 CLM-011070 CLM-007045 CLM-007046 CLM-003033 CLM-005029",
 ["Oveporexton uptake is pathway-limited.", "Hub data can be owned and measured."],
 ["No pathway bottleneck identified at the prototype gate.", "No improvement in time to first dose in the pilot.", "Any compliance finding."],
 "MEDIUM")

RED["BET-13"] = (
 "(Attack on the DEFER.) A neutral registry is a different business from anything Takeda runs. Flatiron worked because Roche kept it separate and it had oncology EHR scale. DEFER with USD 80m in the envelope is a placeholder that will be spent by inertia.",
 "Flatiron regulatory-use claim is a vendor snippet; no Takeda network.",
 "CLM-011022 CLM-011049 CLM-011050 CLM-011023 CLM-005072",
 ["A neutral sponsor and patient-organisation partners exist."],
 ["No neutral sponsor at the 2029 options paper (RM-028)."],
 "LOW")

RED["BET-14"] = (
 "(Attack on the REJECT.) The only credible counter is that rivals will own the interface to biotechs (Lilly via Benchling to 1,300+). Takeda has no measured internal advantage, so it has nothing to sell.",
 "No TuneLab uptake disclosed; NVIDIA warns of customers replacing platform layers.",
 "CLM-006008 CLM-009027 CLM-011004 CLM-000280",
 ["A measured Takeda advantage and external demand."],
 ["Revisit only if BET-01 produces a measured advantage and a biotech customer asks."],
 "LOW")

RED["BET-15"] = (
 "(Attack on the DEFER.) Both ways. If Takeda waits for 2031 triggers, AbbVie and J&J have already bought bridges (USD 17.5bn net each in 2024 and 2025) and the best Phase 2/3 assets are gone. If Takeda buys at USD 5bn, adjusted leverage is about 3.1x before Amitiza and about 3.4x with it, against a 3.0x ceiling the strategy itself set, and a Cerevel-type write-down (54% of price) would be JPY 400bn. The binary USD 5bn framing leaves the middle (USD 0.5-2bn licences, the Nimbus and Innovent pattern) unfunded.",
 "Leverage 2.6x at March 2026; Amitiza provision JPY 403.5bn; progressive dividend JPY 313.2bn paid in FY2025; no significant acquisitions in three years.",
 "CLM-005005 CLM-005014 CLM-005006 CLM-003086 CLM-009049 CLM-009054 CLM-009087",
 ["Free cash flow after dividends deleverages Takeda below the ceiling within 24 months.", "A named Phase 2+ asset passes the write-down test."],
 ["Any unmet trigger: no deal (the bet's own rule).", "Leverage above 3.0x after Amitiza clarity: remove BET-15 from the roadmap."],
 "MEDIUM")

RED["BET-16"] = (
 "(Attack on the REJECT.) Nothing material; the only open point is whether government pricing agreements (TrumpRx, MFN) will force a direct-price posture on Takeda anyway.",
 "TrumpRx agreements expire with the presidential term; Takeda's status is not in the registry.",
 "CLM-007009 CLM-008037 CLM-007010 CLM-007052",
 ["Takeda's categories stay specialty."],
 ["A Takeda pricing agreement that requires a direct channel: reopen."],
 "LOW")

RED["BET-17"] = (
 "The bet can become a reporting ritual. Measurement is owned by the CFO who owns the JPY 200bn savings target, role cuts are proceeding in parallel, and J&J's own numbers (10-15% of use cases drive 80% of value) come from one interview. The reskilling plan needs credibility with employees who are losing roles.",
 "J&J metrics are self-reported; Takeda 63.4% is usage; the savings target mixes technology with headcount.",
 "CLM-006019 CLM-006020 CLM-006022 CLM-014043 CLM-005059 CLM-005078",
 ["Baselines can be set per use case.", "Measurement is independent of the savings owner."],
 ["No baseline for a use case: stop that use case (stage gate).", "At the FY2028 checkpoint (RM-023) technology share of savings cannot be separated."],
 "LOW")
