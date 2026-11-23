# Johnson & Johnson — master dossier (v1.1)

## Dossier status
- Version: v1.1, 2026-11-21 (supersedes v1.0).
- Gate 1 verdict (A10): **CONDITIONAL PASS** (13/13 sampled figures correct; five required repairs, all applied in v1.1 except where noted in §22) [gate1_verdicts.md](../../../quality/citation_audits/gate1_verdicts.md); detail in [audit_wave1_reinspection.md](../../../quality/citation_audits/audit_wave1_reinspection.md) and [audit_wave1_status_discipline.md](../../../quality/citation_audits/audit_wave1_status_discipline.md).
- Claims in the registry tagged JNJ at 2026-11-21: 330 (313 FACT, 17 INTERPRETATION); shard A2_jnj holds CLM-002000..002075. Wave-2 gap-fill claims CLM-014018..014029, 014064..014066, 014069..014071 are integrated below.
- v1.1 changes: OTTAVA wording (announced installation site), derivation withdrawn, regulator-record labels, debt-basis wording, broken links fixed, single-interested-source flags, §8-13 horizontals. Repair list in §22.

Cut-off 2026-11-21. Claim IDs resolve in `../../evidence_library/claims_registry.jsonl` (CLM-000xxx) and `../../evidence_library/shards/A2_jnj/claims.jsonl` (CLM-002xxx). Fiscal years are 52 weeks ending on the Sunday nearest 31 December (FY2025 ended 2025-12-28; FY2026 has 53 weeks) [CLM-002005]. Q3 2026 data are a partial period [CLM-002060]. Sources are mostly company documents (interested party); regulator, court and registry sources are flagged.

## 1. Executive thesis
J&J is the only one of the three comparator companies with two operating segments after separating Consumer Health: Innovative Medicine (USD 60.4bn, +6.0%) and MedTech (USD 33.8bn) in FY2025 [CLM-000253]. Its distinctive FY2025 outcome is absorbing the largest loss of exclusivity in its portfolio: STELARA fell 41.3% to USD 6.1bn [CLM-000254] while DARZALEX (USD 14.4bn) [CLM-000255], TREMFYA [CLM-000256] and CARVYKTI [CLM-000257] grew, and group sales still rose 6.0% [CLM-000253]. Excluding STELARA, sales grew about 12%, about 1 point acquired [CLM-002075] *(INTERPRETATION)*. The cost was debt: net debt rose to USD 27.8bn [CLM-002014]. Vulnerabilities: talc [CLM-002062], DARZALEX concentration [CLM-002073], MedTech margin and growth [CLM-002004] [CLM-002060].

## 2. Business model
Two segments: Innovative Medicine 36.9% pre-tax margin and 19.6% R&D intensity; MedTech 12.2% and 8.4% [CLM-002004]. Segment series FY2021–25 [CLM-002000] [CLM-002001] [CLM-002002] [CLM-002003]. U.S. 57% of sales [CLM-002033]. Detail: [business/business_model.md](business/business_model.md).

## 3. Five-year timeline
See [timeline.md](timeline.md).

## 4. Financial evolution
Revenue, R&D, net income: [financials/xbrl_annual_facts.md](financials/xbrl_annual_facts.md); FY2025 net earnings USD 26,804m versus 14,066m in 2024 (litigation charges) [CLM-000261]. Net debt USD 2.1bn → 16.1bn (FY2022) → 27.8bn (FY2025) [CLM-002010] [CLM-002014]. Q3 2026 net earnings USD 210m after a special talc charge; FY2026 guidance USD 101.0–101.4bn [CLM-002060] [CLM-002061].

## 5. R&D model
Innovative Medicine R&D USD 11.8bn in FY2025 [CLM-002004]; 2023 prioritisation exited infectious disease/vaccines [CLM-002018]; IPR&D impairments USD 313m/211m/81m [CLM-002031]. R&D is complemented by acquisitions [CLM-002012] [CLM-002013].

## 6. Pipeline
Approvals and late-stage assets: [pipeline/late_stage_assets.md](pipeline/late_stage_assets.md); registry inventory [pipeline/ctgov_inventory.md](pipeline/ctgov_inventory.md). Icotrokinra approved 2026 [CLM-002065] with PsA/UC/CD Phase 3 [CLM-002055]. Aticaprant failed [CLM-002039].

## 7. Science and platforms
Cell therapy (CARVYKTI), bispecifics, ADC (Ambrx), RIPTAC (Halda), oral IL-23 peptide [CLM-002012] [CLM-002013] [CLM-002065]. Deeper scientific review not performed (gap).

## 8. AI and data
Horizontals: [landscape](../../industry_transformation/ai_data_robotics/ai_data_robotics_landscape.md), [maturity matrix](../../industry_transformation/ai_data_robotics/maturity_matrix.md), [mechanism cards](../../industry_transformation/ai_data_robotics/capability_mechanism_cards.md). Every metric below is self-reported by J&J executives (single interested source, no baselines).
- Enterprise gen-AI: nearly 900 use cases reviewed and a move from proofs of concept to deployment (pilot to operational) [CLM-006018]; 10-15% of use cases drive about 80% of value (relayed; partially supported) [CLM-006019]; "up to 2.6x" trial-site enrolment at better-performing sites, baseline and method undisclosed (retagged pilot, self-reported) [CLM-006020]; quality-control answers in minutes instead of weeks [CLM-006021]; 47,000 employees completed a required gen-AI course (a training metric, not a deployment) [CLM-006022].
- Duato (Bernstein, 2026-05-27): AI used in molecule design and clinical operations, with no named programmes or metrics [CLM-014071].
- Polyphonic digital surgery: early access "to select hospitals only" (2025-10-27) [CLM-006030]; Abu Dhabi deployment announced 2026-05-21 and expected, not operating (concept) [CLM-006031]. J&J is a founding member of the federated AISB OpenFold3 consortium (pilot) [CLM-006042].
- The FY2025 10-K gives a generic AI statement and risk language, with no OTTAVA or MONARCH text [CLM-006025].

## 9. Robotics and automation
OTTAVA: FDA De Novo DEN250068 granted 2026-07-21 per the FDA grant letter (request received 2025-12-18) [CLM-014022]; J&J announced the authorization on 2026-07-22 [CLM-000283]. On 2026-11-19 J&J announced Memorial Hermann-Texas Medical Center as the **first hospital to install** OTTAVA under an early-access commercial programme [CLM-014024]; the release uses future tense, so this is an announced installation site and not a completed install [CLM-000284] *(contested wording, see conflicts_proposed_A10 #11)*. Maturity: pilot (regulator-authorised; no installed-base or procedure data) [CLM-014022]. MONARCH: QUEST 3 clearance announced 2026-08-17 [CLM-014025]; openFDA K260382 (decided 2026-07-25) and K243219 (auditor record) [CLM-014025] [CLM-000286]; TARGET data (company-sponsored) [CLM-002067]. VELYS: openFDA lists K260480 (2026-06-25) and K240211 (2024-06-05) among five clearances [CLM-014026]; VELYS Spine [CLM-002066]; the 10-K reports pull-through with no system or procedure counts, so VELYS is operational, not scaled [CLM-006026]. No installed-base figure exists for any platform *(gap)*. OTTAVA De Novo was granted earlier than Duato's stated expectation of "by the end of this year, beginning of next year" [CLM-014070]. Detail: [robotics_automation/medtech_robotics_status.md](robotics_automation/medtech_robotics_status.md); FDA record labelling: OTTAVA, MONARCH and VELYS milestones are now backed by FDA records (De Novo grant letter, openFDA 510(k)); other statements about adoption remain company-reported.

## 10. Commercial and market access
[commercial_market_access/commercial.md](commercial_market_access/commercial.md): Stelara biosimilars [CLM-002052], Tremfya conversion [CLM-002026], IRA [CLM-002021] [CLM-002054], 340B [CLM-002069] [CLM-002070]. Horizontals: [commercial models](../../industry_transformation/commercial_patient/commercial_models_comparison.md), [pricing and payer dynamics](../../industry_transformation/commercial_patient/pricing_access_and_payer_dynamics.md), [launch execution](../../industry_transformation/commercial_patient/launch_execution_evidence.md).
- Stelara: Optum Rx excluded it from two main formularies from 2025-07-01 with nine biosimilars on the market (partially supported, trade commentary) [CLM-007016]; CVS Caremark prefers Pyzchiva and Yesintek over Stelara from 2026-07-01 [CLM-007015]. U.S. Stelara sales were about USD 3.8bn in FY2025 and the decline cut Innovative Medicine growth [CLM-007017].
- Part D redesign reduced Erleada, Invega, Opsumit and Uptravi sales [CLM-007018].
- Launch curves FY2025: Carvykti USD 1,887m vs 963m (capacity-limited), Spravato USD 1,696m vs 1,077m (certified-setting restriction under its REMS), Tremfya USD 5,155m vs 3,670m [CLM-007029] [CLM-007030].
- No gross-to-net figure for J&J was found in the passages read [CLM-007024].

## 11. Patient care
J&J withMe (formerly Janssen CarePath), free, no income requirement for its savings programme [CLM-002071] [CLM-007035]; no adherence or time-to-therapy outcome data for any company's support programme [CLM-007039]. Horizontal: [patient programmes](../../industry_transformation/commercial_patient/patient_programs_and_care_delivery.md). *(gap)*

## 12. Partnerships and M&A
Abiomed [CLM-002009], Shockwave [CLM-002068], Ambrx/Proteologix/Numab/V-Wave [CLM-002012], Intra-Cellular [CLM-002041], Halda [CLM-002013]. Horizontals: [deal inventory](../../industry_transformation/partnerships_ecosystem/deal_inventory.md), [scorecard](../../industry_transformation/partnerships_ecosystem/deal_outcomes_scorecard.md), [external-innovation machinery](../../industry_transformation/partnerships_ecosystem/external_innovation_machinery.md).
- Capital: USD 15.1bn (FY2024) and USD 17.5bn (FY2025) of business acquisitions [CLM-009049]. Abiomed USD 17.1bn net with a CVR that was reduced in 2025 [CLM-009041] [CLM-009042]; Intra-Cellular USD 14.5bn, CAPLYTA MDD approved in Q4 2025, nine months after close [CLM-009030] [CLM-009031]; Shockwave USD 12.6bn [CLM-009033]; Halda about USD 3.05bn net [CLM-009032].
- Write-downs: Auris/OTTAVA partial impairment USD 0.9bn (FY2021) [CLM-009047]; bermekimab about USD 0.8bn (FY2022) [CLM-009046]; M710 (Momenta) about USD 0.2bn in each of 2023 and 2024 [CLM-009045]; Laminar pivotal study suspended 2025 after USD 0.4bn plus a USD 0.3bn milestone [CLM-009039] [CLM-009040]; NM26 interim analysis met early-termination criteria 2025, direction unknown [CLM-009037]. Momenta yielded IMAAVY (2025-04-30) [CLM-009044].
- Ecosystem: JLABS planned in 2016 at six sites with capacity for 225 companies [CLM-009051]; J&J withdrew from Toronto, Houston and Washington D.C. in 2025, leaving 11 sites in August 2025 [CLM-014064]; a snippet says New York is closing (not opened) [CLM-014065] [CLM-009052]. J&J claims more than 150 partnerships (company statement) [CLM-009050]. No JJDC portfolio count or fund size was found [CLM-014066].
- AbbVie's Aliada was co-founded by JJDC and built on J&J-created BBB-shuttle science before AbbVie bought it for USD 1.4bn [CLM-014032].

## 13. Policy and regulation
IRA negotiation [CLM-002021] [CLM-002054]; Part D redesign [CLM-002025]; 340B [CLM-002069] [CLM-002070]; opioid settlement [CLM-002032]. Neutral: activity and outcomes only, no causal inference about influence [CLM-008007]. Horizontals: [policy landscape](../../industry_transformation/policy/policy_landscape.md), [IRA exposure](../../industry_transformation/policy/ira_negotiation_exposure.md), [pricing and pledges](../../industry_transformation/policy/pricing_tariffs_manufacturing_pledges.md), [litigation](../../industry_transformation/policy/litigation_with_policy_dimension.md), [lobbying](../../industry_transformation/policy/lobbying_and_political_activity.md).
- Negotiated 2026 prices: Stelara USD 4,695 (-66% vs list), Xarelto USD 197 (-62%), Imbruvica USD 9,319 (-38%) [CLM-008008] [CLM-008009] [CLM-008010]; Stelara and Xarelto leave the programme from 2027 [CLM-008011]; Erleada is a third-cycle drug for 2028, price not located [CLM-008015]. Janssen's constitutional challenge ended when the Supreme Court denied certiorari on 2026-05-18 [CLM-008023] [CLM-008024].
- Pledges and agreements: more than USD 55bn of U.S. investment over four years (2025-03-21) [CLM-008030]; voluntary agreement of 2026-01-08 with TrumpRx participation, Medicaid pricing and a tariff exemption [CLM-008031].
- 340B: D.C. Circuit held on 2026-07-21 that rebate models need HRSA approval (consolidated appeal including J&J's 2024-11-12 suit) [CLM-008039]; Stelara and Xarelto are outside the 2027 HRSA rebate pilot cohort [CLM-008041].
- Talc: prepackaged plan about USD 6.475bn present value (May 2024), Red River bankruptcy (September 2024) dismissed in March 2025 [CLM-008050] [CLM-014027]; about USD 7bn of reserve reversed, no appeal, USD 3.4bn reserve at Q4 2025 [CLM-014028]; on 2026-07-27 a USD 5.5bn conditional resolution of about 76,000 ovarian claims (at least 95% participation; first payment at most USD 3bn in 2027), outcome unknown [CLM-014029]. Opioids: up to USD 5.0bn, about 80% paid by FY2025 end [CLM-008051].
- Lobbying: PhRMA dues above USD 500,000 in 2023 (about 8% used for federal lobbying); J&J PAC active 2022-2026 cycles; annual lobbying totals not obtained [CLM-008006] [CLM-008003].

## 14. Leadership
[leadership/leadership.md](leadership/leadership.md) [CLM-002035] [CLM-002064]. Duato (2026-05-27): 2026 guidance of 6.1% adjusted operational growth and more than USD 100bn of revenue [CLM-014069].

## 15. Successes
DARZALEX, CARVYKTI/bispecifics, Stelara absorption, Kenvue exit, cardiovascular M&A integration: [successes_failures/successes_failures.md](successes_failures/successes_failures.md).

## 16. Failures and weaknesses
Talc [CLM-002015] [CLM-002043], aticaprant [CLM-002039], RSV/COVID vaccine exits [CLM-002018] [CLM-002019], bermekimab [CLM-002020], Varipulse [CLM-002045] (FDA correction notice: 4 of 132 U.S. External Evaluation patients, about 3%, had stroke or TIA versus about 1% or less expected; Instructions for Use updated 2025-02-14 for all lots, a correction and not a removal [CLM-014018]), Impella recalls [CLM-002046] [CLM-002047]; aticaprant VENTURA stopped 2025-03-06 for insufficient efficacy, safety acceptable (company release only) [CLM-014019]; OTTAVA/Auris impairment of USD 0.9bn (FY2021) [CLM-009047].

## 17. Competitive advantages and moats
*(INTERPRETATION)* myeloma depth [CLM-002072]; dual platform unproven [CLM-002074]; M&A capacity. See [competitive_advantage/moats.md](competitive_advantage/moats.md).

## 18. Capability Mechanism Cards

### Card 1 — Replacing a lost franchise (Stelara → Tremfya/Icotyde)
- Problem: STELARA USD 10.4bn (FY2024) at loss of exclusivity [CLM-002022].
- Built/bought: TREMFYA IL-23 antibody with UC/Crohn's labels [CLM-002053]; oral icotrokinra approved [CLM-002065].
- Enablers: earlier launch of a successor; head-to-head data vs STELARA in Crohn's per J&J [CLM-002053].
- Pilot vs production: production; TREMFYA +40.5% [CLM-000256].
- Outcome: offset about one third of the 2025 Stelara loss [CLM-002026]; Immunology still -11.8%.
- Cost: not disclosed. Defensibility: depends on IL-23 competitors *(gap)*. Maturity: demonstrated_outcome (partial).

### Card 2 — Cardiovascular device roll-up (Abiomed + Shockwave + Biosense Webster)
- Problem: need for higher-growth MedTech segments [CLM-002037] (company release only: single interested source). Orthopaedics separation targets completion 18-24 months after the 2025-10-14 announcement; FY2025 Orthopaedics sales USD 9.3bn (+1.1%) [CLM-014020] [CLM-014021].
- Bought: Abiomed USD 17.1bn net [CLM-002009]; Shockwave at USD 335/share [CLM-002011].
- Outcome: Cardiovascular USD 8.9bn (+15.8%), Abiomed 1.75bn, Shockwave 1.15bn [CLM-002027] [CLM-002011]; offset: PFA competition and Varipulse pause [CLM-002028] [CLM-002045]; Impella recalls [CLM-002046].
- Defensibility: safety record and competition are the risk; synergy with pharma not evidenced [CLM-002074]. Maturity: scaled (Abiomed/Shockwave), mixed (EP).

### Card 3 — Surgical robotics (OTTAVA/MONARCH/VELYS)
- Problem: lack of a soft-tissue robot; competitor incumbency *(INTERPRETATION)*.
- Built: OTTAVA from IDE (2024-11) to De Novo (2026-07) and an announced first installation site (2026-11; not a completed install) [CLM-002048] [CLM-002049] [CLM-000283] [CLM-000284] [CLM-014022] [CLM-014024]; MONARCH with 679-patient dataset [CLM-002067]; VELYS Spine [CLM-002066].
- Pilot vs production: one announced early-access installation site (Memorial Hermann) only; no completed-install evidence. Outcome: no adoption or clinical-superiority evidence. Cost: not disclosed. Maturity: pilot for OTTAVA (regulator-authorised, no installed base); operational, not scaled, for MONARCH and VELYS [CLM-006026] [CLM-014025].

## 19. Contradictions and uncertainty
Impella recalls vs continued growth [CLM-002046] [CLM-002027]; company attribution of Varipulse events to use [CLM-002045]; talc total cost USD 5.5bn+ (company) vs 7bn+ (plaintiff counsel) vs reserve USD 3.4bn at FY2025 [CLM-002062] [CLM-002063] [CLM-002016]; 2026-03-17 ICOTYDE date from company release only [CLM-002065] (FDA novel-approvals record lists Icotyde on 2026-03-17 [CLM-012012]). OTTAVA De Novo date: FDA grant letter 2026-07-21 [CLM-014022] versus J&J announcement 2026-07-22 [CLM-000283]; De Novo filing date: J&J said it submitted in January 2026 (2026-01-07) [CLM-002049] versus FDA record of receipt on 2025-12-18 [CLM-014022] *(contested; the FDA letter is the regulator record)*. Segment recast: FY2021 Pharmaceutical 52,080 and Consumer Health 14,635 versus 51,680 and 15,035 in the FY2022 comparatives (conflicts_proposed_A10 #9) [CLM-002000] [CLM-002001].

**Single-interested-source flags (A10).** These claims rest only on J&J-issued documents; treat any outcome wording in them as company-reported: CLM-002037 (Orthopaedics separation), CLM-002039 (aticaprant), CLM-002040 (Kenvue exchange results), CLM-002041 (Intra-Cellular accretion statement), CLM-002044 (Varipulse pause; partly corroborated by FDA's correction notice [CLM-014018]), CLM-002060 (Q3 2026 results), CLM-002061 (FY2026 guidance), CLM-002064 (Taubert retirement). Aticaprant is corroborated by a registry record [CLM-012135]; the separation intent is corroborated in the 10-K [CLM-014021].

## 20. Implications (INTERPRETATION / HYPOTHESIS)
J&J's playbook is successor launch plus bolt-on M&A, funded with debt; durability depends on DARZALEX [CLM-002073], talc settlement uptake [CLM-002062] and MedTech execution [CLM-002060].

## 21. Lessons for Takeda (HYPOTHESIS)
LOE can be absorbed when successors are launched before the cliff (TREMFYA/ICOTYDE); acquisitions bridge gaps but raise net debt [CLM-002014]; an earlier draft derived "about 24 months from IDE to first commercial install" from [CLM-002049]; that derivation is withdrawn because the release describes an announced installation site, not a completed install [CLM-000284].

## 22. Evidence register and gaps
Shard A2_jnj: 38 sources (32 retrieved, 5 api_json, 1 metadata_only), 76 claims (72 FACT, 4 INTERPRETATION). See [evidence_gaps.md](evidence_gaps.md) and [map.md](map.md).

### v1.1 audit repairs applied (A10 Gate 1: CONDITIONAL PASS)
1. **OTTAVA wording** (§9, Card 3, §21, [timeline.md](timeline.md), [robotics status](robotics_automation/medtech_robotics_status.md)): "announced Memorial Hermann as first installation site", not a completed install; the "about 24 months from IDE to first commercial install" derivation removed (the registry correction on CLM-000284 and CLM-002049's arithmetic remain; the registry text was not edited).
2. **Regulator-record labels:** MONARCH (openFDA K260382, K243219), VELYS (K260480, K240211) and the OTTAVA De Novo (DEN250068 grant letter) now cite FDA records [CLM-014025] [CLM-014026] [CLM-014022]; adoption and installed-base claims stay company-reported. "Regulator-verified" wording in CLM-000286 and CLM-006054 is treated as company-reported for anything beyond the FDA record itself.
3. **Single-interested-source flags** on the eight T2-only claims (§19). The registry field `single_interested_source` is not edited here.
4. **Debt basis** (CLM-000128..000132): see [business model](business/business_model.md): non-current USD 39,438m, debt-note subtotal USD 41,438m including the current portion of USD 2,000m, and USD 47.9bn including loans and notes payable [CLM-000132] [CLM-002014].
5. **Broken relative links** in [business/business_model.md](business/business_model.md) fixed (three).
6. Maturity retags relevant here: CLM-006026 VELYS SCALED to operational; CLM-006020 OPERATIONAL to pilot (self-reported); CLM-006022 not a deployment [CLM-006026] [CLM-006020] [CLM-006022]. Registry retags are pending; the dossier uses the corrected values.
