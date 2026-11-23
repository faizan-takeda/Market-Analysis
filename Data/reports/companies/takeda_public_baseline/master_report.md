# Takeda — public baseline (v1.1, A5)

## Dossier status
- Version: v1.1, 2026-11-21 (supersedes v1.0).
- Gate 1 verdict (A10): **FAIL (repairable)** at audit time: figures were correct (16/16, 24/24 XBRL pairs) but the timeline started in FY2022 and there was no business model or successes-and-failures file [gate1_verdicts.md](../../../quality/citation_audits/gate1_verdicts.md). v1.1 applies the eight required repairs (see §14); a re-audit is needed to change the verdict.
- Claims in the registry tagged TAK at 2026-11-21: 263 (243 FACT, 17 INTERPRETATION, 2 RECOMMENDATION, 1 HYPOTHESIS); shard A5_takeda holds CLM-005000..005083. Wave-2 gap-fill claims CLM-014041..014052, 014060..014062 and 014073..014074 are integrated below.
- New in v1.1: [business/business_model.md](business/business_model.md), [successes_failures/successes_failures.md](successes_failures/successes_failures.md), [evidence_notes/h1_fy2026_extracts.md](evidence_notes/h1_fy2026_extracts.md); timeline extended to FY2021 (Nov 2021 to Mar 2022) and FY2022; §13 policy and §14 repairs added.

Research cutoff 2026-11-21. Takeda fiscal years run April-March (FY2025 = April 2025 to March 2026). Claim IDs resolve in `New_mediciine/evidence_library/shards/A5_takeda/claims.jsonl`; `CLM-000xxx` IDs resolve in the canonical `claims_registry.jsonl`. Only public sources were used.

Sentences carry claim IDs; sentences marked *(INTERPRETATION)* or *(gap)* are the analyst's reading or a recorded evidence gap.

## 1. Financial position

**Established.**
- Revenue (IFRS, JPY bn): FY2021 3,569.0; FY2022 4,027.5; FY2023 4,263.8; FY2024 4,581.6; FY2025 4,505.7 [CLM-005000]. FY2025 fell 1.7% at actual exchange rates and 2.7% at constant rates; U.S. revenue fell 9.0% AER to JPY 2,164.8bn [CLM-005001].
- FY2025 geographic mix: U.S. about 48% of revenue, Japan about 10%, China about 4% (arithmetic on reported figures) [CLM-005002].
- Core Operating Profit (company non-IFRS): about 955 (FY2021, implied), 1,188.4, 1,054.9, 1,162.6, 1,172.5 [CLM-005003]. Reported operating profit fell to JPY 6.2bn in FY2025 after a JPY 403.5bn legal provision [CLM-005014] (see also CLM-000272, CLM-000273).
- R&D expense: 526.1, 633.3, 729.9, 730.2, 675.9 [CLM-005004].
- Leverage (adjusted net debt / adjusted EBITDA): 2.6x (Mar 2023), 3.1x (Mar 2024), 2.8x (Mar 2025), 2.6x (Mar 2026) [CLM-005005]. A10 could not locate these; they are now confirmed against the 20-F text: the 20-F for the year to March 2024 (file `TAK_20-F_2024-03-31_0001395064-24-000086.txt`, line 2803) shows 2.6x and 3.1x, and the 20-F for the year to March 2026 (file `TAK_20-F_2026-03-31_0001395064-26-000177.txt`, line 2353) shows 2.8x and 2.6x with adjusted EBITDA JPY 1,441.0bn and 1,457.2bn.
- Progressive dividend policy: JPY 200 per share in FY2025, JPY 204 intended for FY2026; dividends paid JPY 313.2bn in FY2025 [CLM-005006]. Capex JPY 496.7bn, 319.4bn, 426.9bn for FY2023-FY2025 [CLM-005007].
- Concentration: ENTYVIO JPY 958.0bn (21%), immunoglobulins JPY 790.6bn (18%), TAKHZYRO JPY 223.9bn (5%) [CLM-005009]; Growth & Launch Products were 43%, 48%, 51% of revenue in FY2023-FY2025 [CLM-005008].
- H1 FY2026 (Apr-Sep 2026, partial year): revenue JPY 2,407.0bn (+8.4% AER, -1.0% CER); FY2026 Core Operating Profit guidance JPY 1,190bn [CLM-005011]; ENTYVIO +2.7% CER [CLM-005012].

**Contested.** Core measures exclude items such as the Amitiza provision, so reported and core figures diverge in FY2025. Takeda disputes the verdict and intends to appeal [CLM-005013].

**Unknown.** Buyback amounts, FX hedging policy and the FY2021 leverage ratio were not extracted *(gap)*.

## 2. LOE exposure
See [loe_risk/loe_exposure.md](loe_risk/loe_exposure.md). VYVANSE fell from JPY 423.2bn to 203.2bn in two years [CLM-005015]; TRINTELLIX faces generics after December 2026 [CLM-005016]; ENTYVIO loses regulatory exclusivity in the latter half of the decade, with 2032 patents [CLM-005017]. Takeda's replacement plan is the late-stage pipeline, with a stated USD 10-20bn combined peak potential [CLM-005041]. That range is a **company statement (T2)**: the 2024 R&D Day footnote says it is not adjusted for probability of technical and regulatory success and "should not be considered a forecast or target" [CLM-014049]. Entyvio: some patents expire in 2032 and UK/Netherlands revocation actions were filed February-April 2026 [CLM-014050]; two biosimilar BLAs (Alvotech AVT16, Fresenius/Polpharma) were accepted for FDA review, exclusivity status unconfirmed [CLM-014051].

## 3. Pipeline
See [pipeline/late_stage_assets.md](pipeline/late_stage_assets.md). Oveporexton was approved by the FDA on 5 August 2026 [CLM-005029]; rusfertide on 28 August 2026 [CLM-005032]; the zasocitinib NDA was accepted under Priority Review on 14 September 2026 [CLM-005035]. Failures in the window: soticlestat [CLM-005024], cell therapy exit [CLM-005025], ALOFISEL/EXKIVITY write-downs [CLM-005022], TAK-994 [CLM-005023]. The cell-therapy impairment was announced on 2025-10-01 as an expected JPY 58.0bn [CLM-005025]; the FY2025 20-F recognises JPY 58.2bn on the gamma delta T-cell platform, plus JPY 31.9bn on ALUNBRIG [CLM-009084] [CLM-012123] *(not a contradiction: estimate versus recognised amount; conflicts_proposed_A10 #14)*. Full list with successes: [successes_failures/successes_failures.md](successes_failures/successes_failures.md). FDA novel approvals: Fruzaqla 2023-11-08, Orzeyful 2026-08-05, Mimrylo 2026-08-28 [CLM-012018] [CLM-012019] [CLM-012020]; platform view [CLM-012149] [CLM-012150] [CLM-012151] *(INTERPRETATION)*. Horizontals: [pipeline quality](../../industry_transformation/pipeline_regulatory/pipeline_quality_assessment.md), [FDA approvals](../../industry_transformation/pipeline_regulatory/fda_approvals_2022_2026.md), [setbacks](../../industry_transformation/pipeline_regulatory/setbacks_crls_withdrawals.md), [scientific platforms](../../industry_transformation/pipeline_regulatory/scientific_platforms.md).

## 4. R&D operating model
Takeda describes a modality-diversified, partnership-driven model [CLM-005046], with sites in Massachusetts, Shonan and Vienna [CLM-005047]. Four of the six late-stage programs were licensed or acquired externally *(INTERPRETATION)* [CLM-005050]; oveporexton is an in-house discovery [CLM-005048]. The Nimbus acquisition (USD 4.0bn upfront) is the largest deal [CLM-005036]. Takeda Ventures, Inc. is a 100%-owned consolidated subsidiary; no fund size, portfolio count or Center for External Innovation description was found in primary sources [CLM-014052] [CLM-005052]; the Center's head (Alison Handley) sits on BaseLaunch's investment board [CLM-009091] and an aggregator says Takeda Ventures sits under it (inconclusive) [CLM-009092] *(gap)*. Andrew Plump has led R&D since 2015 [CLM-005051].

## 5. Data, digital and AI
See [data_ai/digital_ai_baseline.md](data_ai/digital_ai_baseline.md). Public evidence is aspiration and platform statements, not outcomes [CLM-005053, CLM-005058, CLM-005057]. Horizontals: [landscape](../../industry_transformation/ai_data_robotics/ai_data_robotics_landscape.md), [maturity matrix](../../industry_transformation/ai_data_robotics/maturity_matrix.md), [autonomous-lab reality check](../../industry_transformation/ai_data_robotics/autonomous_lab_reality_check.md).
- Annual Integrated Report 2026 (FY2025; opened via pypdf, 55 pages; company document, single interested source): 63.4% of the workforce actively used generative AI at 31 March 2026 versus 46.6% a year earlier, and 30.9% took at least one data, digital and technology course [CLM-014043]; named AI partners Nabla Bio, TetraScience and APHERIS, with AI/ML in study design and operations [CLM-014045]; the Takami programme standardises end-to-end processes with qualitative benefits and no spend disclosed [CLM-014044].
- Manufacturing and supply AI: more than 170 AI-enabled predictive-maintenance agents at Lessines (maturity operational, self-reported) [CLM-014041]; One Day Batch Release completed six-site pilots in 2025, targeting 60% shorter release lead time by 2028 and global rollout by 2029 (pilot, target) [CLM-014042]; on-time in-full 99.6% in FY2025, with personalised plasma-donation nomograms and Smart Donor Care rolled out at BioLife [CLM-014046].
- Partner deals (prototype): Nabla Bio second collaboration, October 2025, with over USD 1bn of success-based payments and first-in-human data expected in one to two years (company statements) [CLM-006039]; Iambic, February 2026, payments that could exceed USD 1.7bn [CLM-006041]; AISB OpenFold3 member since October 2025 [CLM-006042].
- Leadership statements: Weber (Semafor, January 2026) aims to double research productivity with AI and cites about 30% shorter narcolepsy development time (single source, partially supported) [CLM-014073]; Kim's May 2026 letter sets "two horizons" and an AI-heavy reorganisation [CLM-014074].
- No first-party deployment with outcome metrics was found for discovery AI [CLM-006045]; lab and manufacturing robotics remain an evidence gap [CLM-005067].

## 6. Manufacturing and plasma network
Plasma centers grew from 233 to 275 over FY2022-FY2024 [CLM-005063]; a USD 230m Los Angeles expansion adds up to 2 million litres/year of fractionation capacity [CLM-005065]; a 2020 FDA warning letter at Hikari led to a supply shortage and a USD 505m award to AbbVie [CLM-005020]. Automation and continuous manufacturing are an evidence gap [CLM-005067], apart from the Lessines predictive-maintenance agents and One Day Batch Release pilots in §5 [CLM-014041] [CLM-014042]. BioLife plasma centres: 233 (FY2022), 260 (FY2023), 275 (FY2024) [CLM-005063].

## 7. Commercial reach
U.S., International and Japan business units [CLM-005069]. Japan JPY 433.1bn and China JPY 195.1bn in FY2025 [CLM-005071]. QDENGA revenue JPY 40.8bn [CLM-005045]. The "~80 markets" figure could not be verified [CLM-005070]; patient-assistance detail is limited to Help at Hand, which reports more than 100,000 patients cumulatively (company-stated) [CLM-007037] [CLM-005072]. Horizontals: [commercial models](../../industry_transformation/commercial_patient/commercial_models_comparison.md), [pricing and payer dynamics](../../industry_transformation/commercial_patient/pricing_access_and_payer_dynamics.md), [launch execution](../../industry_transformation/commercial_patient/launch_execution_evidence.md), [transfer to Takeda](../../industry_transformation/commercial_patient/transfer_to_takeda.md).
- Entyvio is 21% of revenue (JPY 958.0bn) and Growth & Launch Products 51% [CLM-007027]; the subcutaneous Entyvio pen (UC September 2023, Crohn's April 2024) drives uptake, with FDA application records on 2023-09-27 (SC) and 2024-04-18 (pen) [CLM-007033] [CLM-007041] [CLM-012029] [CLM-012030]. Rebate details are not public; formulary exclusion directly reduces usage [CLM-007025].
- Entyvio selected for Medicare negotiation effective January 2028; Part D redesign expected to reduce profit; May 2025 MFN executive order [CLM-007026]. The HYHUB needle-free Hyqvia transfer device received 510(k) clearance in July 2025 (clearance, not adoption) [CLM-007042]. Call summary credits Entyvio pen adoption and formulary wins and Qdenga +22.1% (aggregator, partially supported) [CLM-007043].
- *(INTERPRETATION)* Transfer logic: subcutaneous/home conversion is the best-evidenced transferable mechanism; a cash-pay DTC channel fits poorly [CLM-007053] [CLM-007052] [CLM-007054] [CLM-007055] [CLM-007056] [CLM-007057] [CLM-007058].

## 8. Partnerships
In-licensing roster [CLM-005050]; Innovent oncology license [CLM-005043]; AI-oriented research alliances [CLM-005049]; Teva generics JV dissolution (JPY 18.9bn impairment, JPY 56.5bn proceeds) [CLM-005021] [CLM-009085]. Horizontals: [deal inventory](../../industry_transformation/partnerships_ecosystem/deal_inventory.md), [scorecard](../../industry_transformation/partnerships_ecosystem/deal_outcomes_scorecard.md), [external-innovation machinery](../../industry_transformation/partnerships_ecosystem/external_innovation_machinery.md).
- Upfronts (20-F): HUTCHMED USD 400m (April 2023; up to USD 730m more) and Protagonist USD 300m (April 2024) [CLM-014060]; Keros USD 200m (February 2025) and Innovent USD 1.2bn (December 2025) [CLM-014061]; Nimbus USD 4.0bn (paid USD 3.0bn February 2023, 0.9bn April 2023, 0.1bn August 2023) with two USD 1.0bn sales milestones [CLM-014062] [CLM-009076]; AC Immune USD 100m [CLM-014062]. Innovent: US$1.2bn including equity, up to US$11.4bn in total [CLM-009078] [CLM-009079].
- Takeda states there were no significant acquisitions in the three years to March 2026 [CLM-009087]. Terminations: Denali collaboration ended April 2026; Neurocrine terminated TAK-041/TAK-831 in March 2025 [CLM-009089] [CLM-009090]. Write-offs of earlier purchases: Maverick JPY 27.8bn, soticlestat JPY 21.5bn, gamma delta T-cell JPY 58.2bn [CLM-009083] [CLM-009084]. Takeda holds an AbbVie licence for mirvetuximab in Japan [CLM-009093]. BaseLaunch partner alongside AbbVie and J&J [CLM-009091].

## 9. Leadership and organisation
Julie Kim became President and CEO on 24 June 2026; Christophe Weber retired [CLM-005073]. Kim's background is PDT and U.S. commercial [CLM-005074]. Three external directors joined, including Paul Stoffels [CLM-005075]. Milano Furuta is CFO and Gabriele Ricci CDTO [CLM-005076, CLM-005056]. Restructuring: May 2024 program [CLM-005077]; March 2026 transformation targeting over JPY 200bn gross annual savings by FY2028 [CLM-005059]. **Restructuring-cost series (Gate 1 rewrite of CLM-005078):** about JPY 150bn (Takeda release, 25 March 2026) → JPY 170.0bn (original FY2026 forecast, May 2026) → JPY 160.0bn (revised forecast, H1 FY2026 report, October 2026); the 170bn is Takeda's own forecast, not only a press figure [CLM-005078] [CLM-005011] (conflicts_proposed_A10 #4). The H1 report text is preserved in [evidence_notes/h1_fy2026_extracts.md](evidence_notes/h1_fy2026_extracts.md). "About 4,500 roles" is a trade-press figure [CLM-005078]; the "137 Massachusetts roles" element could not be verified and is not used [CLM-005025]. Dual listing in Tokyo and on the NYSE [CLM-005079]. Weber's January 2026 and Kim's May 2026 statements are in §5 [CLM-014073] [CLM-014074].

## 10. Capability baseline
Detail in [capability_baseline/capability_baseline.md](capability_baseline/capability_baseline.md).

| Capability area | Class | Evidence |
|---|---|---|
| GI / immunology franchise | EXISTING_STRENGTH | [CLM-005009, CLM-005012] |
| Plasma network and PDT manufacturing | EXISTING_STRENGTH | [CLM-005063, CLM-005064, CLM-005065] |
| Late-stage pipeline delivery | EXISTING_STRENGTH | [CLM-005042, CLM-005029, CLM-005032, CLM-005035] |
| Orexin / rare-disease science | EXISTING_STRENGTH | [CLM-005048, CLM-005027] |
| LOE replacement (revenue depth) | EXISTING_BUT_UNDERDEVELOPED | [CLM-005015, CLM-005017, CLM-005016] |
| External innovation / BD | EXISTING_STRENGTH (deals); organisation EVIDENCE_GAP | [CLM-005050, CLM-005036, CLM-005052] |
| Enterprise data and AI platform | EXISTING_BUT_UNDERDEVELOPED (outcomes unproven) | [CLM-005058, CLM-005055, CLM-005053] |
| AI-enabled discovery | EVIDENCE_GAP | [CLM-005049, CLM-005053] |
| Lab / manufacturing automation, robotics | EVIDENCE_GAP | [CLM-005067] |
| Manufacturing quality | EXISTING_BUT_UNDERDEVELOPED (one documented failure) | [CLM-005020] |
| Patient services / market access | EVIDENCE_GAP | [CLM-005072] |
| New-brand launch execution | POTENTIAL_NEW_CAPABILITY (to be proven) | [CLM-005069, CLM-005074] |

## 11. Internal-validation backlog
See [internal_validation_backlog/backlog.md](internal_validation_backlog/backlog.md).

## 12. Evidence register and gaps
Shard `A5_takeda`: 40 sources (31 retrieved, 5 metadata-only, 3 blocked, 1 paywalled), 83 claims. See [evidence_gaps.md](evidence_gaps.md). The Annual Integrated Report PDF body was not read in v1.0 [CLM-005081] and was opened in wave 2 [CLM-014041]; the takeda.com pipeline asset table was not read [CLM-005082].

## 13. Policy and regulation
Neutral: activity and outcomes only, no causal inference about influence [CLM-008007]. Horizontals: [policy landscape](../../industry_transformation/policy/policy_landscape.md), [IRA exposure](../../industry_transformation/policy/ira_negotiation_exposure.md), [pricing and pledges](../../industry_transformation/policy/pricing_tariffs_manufacturing_pledges.md), [litigation](../../industry_transformation/policy/litigation_with_policy_dimension.md).
- Entyvio, Takeda's highest-selling product in FY2025, was selected by CMS for negotiation effective January 2028; CMS announced on 2026-03-13 that the manufacturers of all 15 third-cycle drugs chose to participate [CLM-008022] [CLM-008015] [CLM-008016]; third-cycle prices were not located [CLM-008017].
- A May 2025 executive order encouraged Most Favored Nation pricing, which could lower Takeda's U.S. prices; Takeda made no U.S. manufacturing pledge in the 20-F text searched [CLM-008035]. Japan's annual NHI price revisions since April 2021 have brought more frequent downward revisions, with a surcharge on long-listed originator drugs from 2026-06-01 [CLM-008036].
- AMITIZA antitrust: jury verdict of 2026-05-18 for USD 884.9m single damages (wholesaler class and individual retailers, subject to trebling for two groups); Takeda booked a JPY 403.5bn provision and plans post-trial motions and an appeal; the final judgment amount and post-trial status are unverified [CLM-005013] [CLM-005014] [CLM-014047] [CLM-014048].
- The 2020 Hikari warning letter and the USD 505m award to AbbVie [CLM-005020].

## 14. v1.1 audit repairs applied (A10 Gate 1: FAIL, repairable)
1. **Timeline** extended to FY2021 (Nov 2021 to Mar 2022) and FY2022 events already in the registry: [timeline.md](timeline.md) [CLM-009086] [CLM-012119].
2. **Business model** created: [business/business_model.md](business/business_model.md).
3. **Successes and failures** created: [successes_failures/successes_failures.md](successes_failures/successes_failures.md).
4. **Restructuring series** rewritten in §9 (150bn → 170.0bn → 160.0bn) [CLM-005078].
5. **Impairment:** recognised JPY 58.2bn (FY2025 20-F) cited beside the October 2025 estimate of 58.0bn (§3) [CLM-009084] [CLM-012123] [CLM-005025].
6. **Evidence preservation:** the H1 FY2026 report (SRC-005015) has no extracted text file in the registry; the passages A10 and this task re-read are copied to [evidence_notes/h1_fy2026_extracts.md](evidence_notes/h1_fy2026_extracts.md). SRC-005018 (BioSpace, about JPY 170bn) was not re-opened; the 170bn figure is anchored to Takeda's own forecast instead. "137 Massachusetts roles" is dropped (Fierce returned 403) [CLM-005025].
7. **Leverage** (CLM-005005): verified against the 20-F text (see §1).
8. **USD 10-20bn** treated as a company statement (T2) in §2, [loe_risk/loe_exposure.md](loe_risk/loe_exposure.md), [pipeline/late_stage_assets.md](pipeline/late_stage_assets.md) and the backlog [CLM-014049].
9. Gate 1 tier note: the H1 FY2026 Kessan Tanshin (SRC-005015) is a company results document; the auditor suggests T2 for earnings releases and T1 for audited statements and regulator-filed forms. Registry retag pending.
