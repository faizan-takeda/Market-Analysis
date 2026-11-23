# AbbVie Inc. — master dossier v1.1 (A3, cutoff 2026-11-21)

## Dossier status
- Version: v1.1, 2026-11-21 (supersedes v1.0).
- Gate 1 verdict (A10): **CONDITIONAL PASS** after repairs (15/16 sampled figures correct, one label error; financial reconciliation failed on the debt label and deal-size bases; evidence-gap report weak) [gate1_verdicts.md](../../../quality/citation_audits/gate1_verdicts.md). All four required repairs are applied in v1.1 (see §22).
- Claims in the registry tagged ABBV at 2026-11-21: 338 (316 FACT, 20 INTERPRETATION, 1 HYPOTHESIS, 1 RECOMMENDATION); shard A3_abbvie holds CLM-003000..003090. Wave-2 gap-fill claims CLM-014030..014040 and CLM-014072 are integrated below.
- v1.1 changes: debt basis, deal-size bases, Juvmo date resolution, expanded evidence gaps, single-interested-source flags, §12-17 horizontals.

Shard: `A3_abbvie` (39 sources, 91 claims). FACT/INTERPRETATION labelled; canonical financial claims CLM-000001..000270 reused. Unsourced sentences are marked (INTERPRETATION) or (gap). 2026 figures are partial periods (Q1-Q3), never full-year.

## 1. Executive thesis
AbbVie absorbed the largest U.S. loss of exclusivity in pharma by replacing Humira (global USD 21.2bn in 2022 to 4.5bn in 2025) with Skyrizi and Rinvoq (7.7bn to 25.9bn) [CLM-003002, CLM-003014]. Total revenue dipped 6.4% in 2023 and passed its 2022 peak only in 2025 (61.2bn) [CLM-003015]. The immunology engine is high quality; the diversification layer is mixed: emraclidine failed and cost a USD 4.5bn impairment [CLM-003057], aesthetics shrank [CLM-003031], while Vyalev, Elahere and Juvmo are real but small [CLM-003037, CLM-003036, CLM-003063].

## 2. Research question and scope
How AbbVie survived Humira LOE, what Allergan delivered, quality of the post-Humira engine, where capital was destroyed, and 2030+ positioning. Window 2021-11 to 2026-11. (gap) AI/robotics, policy and full deal inventory are left to A6/A8/A9.

## 3. Business architecture
Single segment; immunology, neuroscience, oncology, aesthetics, eye care. Skyrizi, Humira and Rinvoq were about 47% of 2024 revenue [CLM-003046]. Product tables: [business/business_model.md](business/business_model.md).

## 4. Financial evolution
Revenue 56.2bn (2021), 58.1bn, 54.3bn, 56.3bn, 61.2bn (2025) [CLM-000001..000005]. GAAP operating margin 31.9% to 16.2% (2024) to 24.6% (2025) (INTERPRETATION, arithmetic) [CLM-003039]. GAAP net income 4.2bn in 2025 is depressed by 7.4bn amortization and a 6.5bn contingent-consideration charge [CLM-003040, CLM-003041]. **Debt basis (Gate 1 relabel).** Total long-term debt *including the current portion* fell from USD 75,962m (2021) to 59,245m (2023), then rose to 66,841m (2024) after USD 15.0bn of notes for ImmunoGen/Cerevel, and was 64,503m at end-2025 (63,128m in 2022) [CLM-003042] [CLM-000066] [CLM-000067] [CLM-000068] [CLM-000069] [CLM-000070]. The balance-sheet non-current series is lower: 64,189 / 59,135 / 52,194 / 60,340 / 58,941 (2021-2025) [CLM-003042]. The earlier word "non-current" for the first series was wrong (XBRL tag `LongTermDebt`); the registry correction fields on these claims say the same. Net income basis: consolidated net earnings 4,233m (2025) versus 4,226m attributable to AbbVie; the A4 and RUN-0001 series differ only by this definition (conflicts_proposed_A10 #8) [CLM-000030] [CLM-004152]. Dividends 11.7bn paid in 2025; buybacks small [CLM-003043, CLM-003044].

## 5. Timeline summary
See [timeline.md](timeline.md).

## 6. Humira loss of exclusivity
U.S. exclusivity ended 2023-01-31; nine biosimilars launched in 2023 [CLM-003000, CLM-003006]. The 2017-2022 settlements licensed biosimilars from 2023 in the U.S. (2018 in Europe); terms are undisclosed [CLM-014036]. The 2019 indirect-purchaser antitrust class actions were dismissed in June 2020 and appealed [CLM-014037]; the Seventh Circuit affirmed dismissal of the patent-thicket complaint on 2022-08-01 [CLM-008048]; a January 2025 payor class action over rebating is pending [CLM-007021]. Humira was about 27% of 2023 net revenue [CLM-014038]. Humira kept at least 97% of volume to March 2024 [CLM-003007] *(T3 IQVIA/trade source, not re-opened by the auditor; single-interested-source flag, §22)*; CVS Caremark excluded Humira from major template formularies from 2024-04-01 while AbbVie supplied a co-branded Humira to Cordavis [CLM-003008]. U.S. Humira revenue: 18.6bn (2022), 12.2bn, 7.1bn, 3.1bn (2025) [CLM-003001]. Steepest falls came after the PBM change (association, not proven causation) [CLM-003010].

## 7. Skyrizi and Rinvoq ramp
Indication breadth covers Humira's uses [CLM-003016]. Rinvoq carries a JAK boxed warning since 2021 [CLM-003017] yet grew every year [CLM-003013]. Patents run to 2033; no Rinvoq generic expected before April 2037 [CLM-003021]. 2027 target of more than 31bn combined [CLM-003022]; nine-month 2026 already 23.1bn [CLM-003023].

## 8. Allergan integration
Closed 2020-05-08 [CLM-003048]. USD 2.5bn cost synergies targeted and reported realized in 2022 [CLM-003049]. Revenue side weaker: Botox Therapeutic grew (2.5bn to 3.8bn) [CLM-003030] but Botox Cosmetic and Juvederm declined from 2024 [CLM-003031]; 2029 aesthetics target cut from 9bn to above 7bn [CLM-003034].

## 9. Neuroscience
Vraylar 3.6bn, Botox Therapeutic 3.8bn, Ubrelvy and Qulipta growing [CLM-003028, CLM-003037]. Vyalev approved 2024-10 after two CRLs [CLM-003061]; Juvmo approved by FDA on 2026-09-25 per the FDA novel-approvals record; AbbVie announced it on 2026-09-28 (the earlier 09-25 versus 09-28 question is resolved as FDA action versus company release) [CLM-012017] [CLM-014039] [CLM-003063]. NDA submitted September 2025 [CLM-014040]. Emraclidine failed [CLM-003054].

## 10. Oncology
Imbruvica declining (5.4bn to 2.9bn) and IRA-selected [CLM-003025, CLM-003026]; Venclexta 2.8bn but two Phase 3 misses [CLM-003027]; Elahere growing [CLM-003036]; Emrelis accelerated approval on 35% ORR [CLM-003066]; Epkinly DLBCL missed OS [CLM-003067] (company-reported; Phase 3 PFS improved, OS not statistically significant per the 10-K [CLM-012118]).

## 11. Pipeline quality
About 90 programs, 60 mid/late [CLM-003047]. Details: [pipeline/late_stage_assets.md](pipeline/late_stage_assets.md). (HYPOTHESIS) breadth outside immunology is thin on proven peak sales [CLM-003089]. FDA novel approvals 2022-2026: Elahere (2022-11-14, ImmunoGen sponsor), Epkinly (2023-05-19, Genmab sponsor), Emrelis (2025-05-14), Decnupaz (2026-05-27), Juvmo (2026-09-25) [CLM-012013] [CLM-012014] [CLM-012015] [CLM-012016] [CLM-012017]. Setbacks: ABBV-951 CRLs (March 2023 device; June 2024 third-party manufacturer inspection, approved Oct 2024), Imbruvica accelerated approvals withdrawn (May 2023), navitoclax TRANSFORM-2 stopped (April 2024), emraclidine Phase 2 miss (November 2024), Venclexta VERONA OS miss (June 2025), Epkinly Phase 3 PFS win with non-significant OS (January 2026) [CLM-012111] [CLM-012112] [CLM-012113] [CLM-012114] [CLM-012115] [CLM-012117] [CLM-012118]. Horizontals: [pipeline quality assessment](../../industry_transformation/pipeline_regulatory/pipeline_quality_assessment.md), [setbacks](../../industry_transformation/pipeline_regulatory/setbacks_crls_withdrawals.md), [late-stage snapshot](../../industry_transformation/pipeline_regulatory/late_stage_pipeline_snapshot.md).

## 12. Commercial and patient
[commercial_market_access/commercial.md](commercial_market_access/commercial.md). Horizontals: [commercial models](../../industry_transformation/commercial_patient/commercial_models_comparison.md), [pricing and payer dynamics](../../industry_transformation/commercial_patient/pricing_access_and_payer_dynamics.md), [launch execution](../../industry_transformation/commercial_patient/launch_execution_evidence.md), [patient programmes](../../industry_transformation/commercial_patient/patient_programs_and_care_delivery.md).
- Rebate and chargeback provisions USD 65.1bn (2025), 59.3bn (2024), 56.8bn (2023) against 2025 net revenue of USD 61.2bn [CLM-007019].
- Skyrizi USD 17,562m (+49.9%) and Rinvoq USD 8,304m (+39.1%); Humira -49% [CLM-007020]. The 10-K gives share-uptake language only for the drivers.
- Humira contracting: CVS Caremark removal from template formularies (2024-04-01) with co-branded Cordavis Humira [CLM-003008] [CLM-003009]; the percentage figures rest on trade sources (flagged, §22).
- Patient support: Allē had over six million members across 19,000 practices (January 2024); the October 2024 redesign was reversed in early 2025 [CLM-007036] [CLM-003033]. No adherence or time-to-therapy outcomes for any company [CLM-007039].

## 13. R&D model and external innovation
External innovation is an explicit strategy pillar; acquired IPR&D charges rose from 0.6bn (2023) to 4.8bn (2025) [CLM-003075, CLM-003045]. Yearly early-stage upfronts of USD 0.6-1.0bn [CLM-009069]; AbbVie Ventures founding date unresolved (2009 versus about 2015) [CLM-009074] (see §14).

## 14. Partnerships and M&A
**Deal-size bases (Gate 1 relabel).** ImmunoGen (closed 2024-02-12): USD 10.1bn is the announced total value, 9.8bn is consideration transferred and 9.2bn is net of cash acquired [CLM-003053] [CLM-009056]. Cerevel (closed 2024-08-01): USD 8.7bn consideration, 8.3bn net of cash [CLM-009053] [CLM-014035]. The "18.5bn cash paid" in 2024 is consideration transferred for the two (9.8 + 8.7); net of cash acquired it is 17.5bn [CLM-003086] *(conflicts_proposed_A10 #10)*. Capstan: USD 2.1bn cash paid (1.9bn net of cash acquired), expensed as IPR&D in 2025; lead asset Phase 1 [CLM-014030] [CLM-009058] (CLM-003072's "up to 2.1bn" is the announcement wording). Gubra obesity: USD 350m upfront [CLM-003073]; Apogee closed in 2026 [CLM-003070].
- Other terms: Aliada USD 1.4bn cash (announced 2024-10-28, closed December 2024), co-founded by J&J's JJDC [CLM-014032] [CLM-009063]; Landos USD 20.42 a share (about USD 137.5m) plus a CVR worth up to about USD 75m [CLM-014033]; Nimble USD 288m (USD 210m upfront plus contingent consideration; up to USD 130m further) [CLM-014034] [CLM-009057]; Celsius USD 250m [CLM-009064]. FY2025 upfronts: Gilgamesh USD 906m, Ichnos Glenmark USD 700m, Gubra USD 350m, ADARx option USD 335m; FY2024: Aliada USD 1.4bn, Celsius USD 250m [CLM-014031].
- Cerevel assumed a Pfizer licence with up to USD 1.6bn of milestones [CLM-014035]. Horizontals: [deal inventory](../../industry_transformation/partnerships_ecosystem/deal_inventory.md), [scorecard](../../industry_transformation/partnerships_ecosystem/deal_outcomes_scorecard.md), [external-innovation machinery](../../industry_transformation/partnerships_ecosystem/external_innovation_machinery.md).
- Outcomes: ImmunoGen contributed USD 578m revenue and a USD 682m operating loss through 2024 [CLM-009056]; Cerevel's emraclidine failed Phase 2 in November 2024 with a USD 4.5bn impairment, about 54% of the net price (the horizontal's arithmetic, 4.5 of 8.3) [CLM-009054]. DJS (USD 287m, 2022), Syndesi (USD 130m), Soliton (USD 535m) are older bolt-ons [CLM-009065] [CLM-009066] [CLM-009067]. Calico extension (USD 500m AbbVie share) and ADARx are option structures [CLM-009068] [CLM-009061]. Aliada, Landos, Celsius and Nimble were listed without terms in v1.0 [CLM-003074]; terms are now above. Unspecified smaller arrangements: USD 602m / 975m / 582m upfronts in 2025 / 2024 / 2023 [CLM-009069]. AbbVie Ventures founding is 2009 (web page) versus about 2015 (impact report): unresolved [CLM-009074] *(conflicts_proposed_A10 #5)*; one source is sponsored content [CLM-009075]. AbbVie is a BaseLaunch partner [CLM-009094].

## 15. Policy and regulatory
IRA selections: Imbruvica, Vraylar, Botox [CLM-003080]; January 2026 U.S. agreement with 100bn pledge [CLM-003081] (company announcement; single interested source); the brief's USD 10bn 2025 pledge was not found [CLM-003082]. Neutral: activity and outcomes only, no causal inference about influence [CLM-008007]. Horizontals: [policy landscape](../../industry_transformation/policy/policy_landscape.md), [IRA exposure](../../industry_transformation/policy/ira_negotiation_exposure.md), [pricing and pledges](../../industry_transformation/policy/pricing_tariffs_manufacturing_pledges.md), [litigation](../../industry_transformation/policy/litigation_with_policy_dimension.md), [lobbying](../../industry_transformation/policy/lobbying_and_political_activity.md).
- Negotiated prices: Linzess USD 136 (-75%) and Vraylar USD 770 (-44%) from 2027; Imbruvica USD 9,319 (-38%, shared with J&J) from 2026; Botox selected for 2028, price not located [CLM-008012] [CLM-008013] [CLM-008010] [CLM-008015] [CLM-008018]. USD 2.1bn pre-tax Imbruvica impairment in Q3 2023 after selection (fair value 1.9bn vs carrying 4.0bn) [CLM-008019].
- January 2026 agreement: three-year voluntary agreement with USD 100bn of U.S. R&D and capital investment over a decade, low Medicaid prices, TrumpRx offerings and tariff exemption [CLM-008032]. From 2025 the Part D coverage-gap discount became a 10% manufacturer discount [CLM-008020].
- Litigation: Humira antitrust history in §6 [CLM-008048] [CLM-008049]. Lobbying totals not obtained; AbbVie PAC active 2022-2026 cycles [CLM-008004].

## 16. Leadership
Gonzalez to Michael (CEO 2024-07-01, chairman 2025-07-01) [CLM-003076]; internal, continuity heavy [CLM-003079]. See [leadership/leadership.md](leadership/leadership.md).

## 17. AI and data
Horizontals: [landscape](../../industry_transformation/ai_data_robotics/ai_data_robotics_landscape.md), [maturity matrix](../../industry_transformation/ai_data_robotics/maturity_matrix.md), [mechanism cards](../../industry_transformation/ai_data_robotics/capability_mechanism_cards.md).
- Valkai (2026-09-29): announcement only, concept [CLM-003083] [CLM-000285] [CLM-006037].
- ARCH knowledge graph (conceived 2020; fewer than ten FTE plus contractors; over 124 TB; graph of over 30 million nodes and nearly 2 billion relationships): maturity operational; no outcome beyond a preprint; the head of AI said the first version was built "quick, not cheap, not right [or final]" (company speaker relayed by trade press; single interested source) [CLM-006032] [CLM-006033] [CLM-006034]. The source describes a knowledge graph, not generative AI.
- BigHat collaboration (2023-12-05): USD 30m upfront, up to about USD 325m milestones; prototype [CLM-006035]. Founding member of the AISB OpenFold3 consortium (pilot; vendor benchmark, not peer-reviewed) and AISB Bind (concept) [CLM-006042] [CLM-006043] [CLM-006044].
- The 10-K discloses AI skills investment and an adoption-failure risk, with no outcomes [CLM-006036]. Michael (Q4 2025 call): record USD 61.2bn ex-IPR&D revenue despite nearly USD 16bn of U.S. Humira erosion [CLM-014072].

## 18. Successes (top 5) and failures (>=5)
See [successes_failures/successes_failures.md](successes_failures/successes_failures.md).

## 19. Moats (INTERPRETATION)
See [competitive_advantage/moats.md](competitive_advantage/moats.md) and the cards below.

## 20. Capability Mechanism Cards (INTERPRETATION)
**Card 1: successor sequencing.** Problem: 37% of revenue exposed to LOE. Built/bought: Skyrizi/Rinvoq expanded across Humira indications, plus head-to-head data. Enablers: immunology sales force, IL-23/JAK science. Outcome: 25.9bn in 2025. Replicate: launch the successor 3-5 years before the cliff [CLM-003084, CLM-003016].
**Card 2: contracting defence.** Problem: biosimilar entry. Mechanism: rebate-for-access kept >=97% volume to March 2024, then co-branded Humira via Cordavis took 23% of switchers vs 60% for co-promoted Hyrimoz. Limit: 2025 U.S. -57% [CLM-003085].
**Card 3: BD&L refill.** Problem: pipeline gap. Mechanism: buy late-stage/commercial assets (18.5bn consideration transferred in 2024 for ImmunoGen and Cerevel; 17.5bn net of cash acquired). Outcome: one 4.5bn write-down, Elahere growth, Juvmo approval; returns not yet demonstrated [CLM-003086].
**Card 4: settlement-based IP.** Rinvoq entry deferred to 2037 after 2025 settlements; Humira history unverified [CLM-003087].
**Card 5: aesthetics channel (risk).** Loyalty redesign cut share and price; reversed within months [CLM-003033, CLM-003088].

## 21. Lessons for Takeda (HYPOTHESIS/RECOMMENDATION)
Pre-build successors in the same franchise; expect PBM structure to matter as much as patents; size acquisitions to survive a write-down; treat first-in-class psychiatry BD as high variance [CLM-003090].

## 22. Evidence register and gaps
39 sources (20 retrieved, 7 registry API, 8 metadata-only, 3 blocked, 1 unavailable), 91 claims. Gaps: [evidence_gaps.md](evidence_gaps.md) (expanded in v1.1 to list each metadata-only and blocked source). Brief premises tested: impairment ~3.5bn in 2025 CONTRADICTED (4.5bn in Q4 2024) [CLM-003058]; USD 10bn pledge INCONCLUSIVE [CLM-003082].

### v1.1 audit repairs applied (A10 Gate 1: CONDITIONAL PASS)
1. **Debt basis** (CLM-003042 and CLM-000066..000070): the series 75,962 / 63,128 / 59,245 / 66,841 / 64,503 is total long-term debt including the current portion; balance-sheet non-current is 64,189 / 59,135 / 52,194 / 60,340 / 58,941. Corrected in §4, [business model](business/business_model.md) and the Card 3 context [CLM-003042] [CLM-000070].
2. **Deal-size bases** (CLM-003086; master Card 3 and the §14 ImmunoGen line): ImmunoGen 10.1bn announced total value, 9.8bn consideration, 9.2bn net of cash; 18.5bn is consideration transferred for ImmunoGen plus Cerevel (17.5bn net of cash acquired) [CLM-003053] [CLM-003086] [CLM-009056] [CLM-009053].
3. **Evidence gaps** expanded: the eight metadata-only sources, three blocked sources, one unavailable source and the Ventures founding-date conflict are now listed in [evidence_gaps.md](evidence_gaps.md) [CLM-009074].
4. **Single-interested-source flags.** The registry marks 22 AbbVie-tagged claims as single_interested_source (company releases, 10-K text used for outcomes, trade or sponsored sources). Where a flagged claim carries a strategic conclusion in this dossier it is marked in text: Humira contracting percentages [CLM-003007] [CLM-003009] [CLM-003085] (T3 IQVIA/trade sources not re-opened by the auditor); CVS exclusion [CLM-003008]; 2027 Skyrizi plus Rinvoq target and nine-month 2026 figures [CLM-003022] [CLM-003023]; aesthetics slowdown and Allē [CLM-003032] [CLM-003033] [CLM-003034]; Allergan synergies [CLM-003049]; the January 2026 U.S. agreement [CLM-003081]; deal announcements [CLM-003052] [CLM-003072] [CLM-003073]; Valkai and ARCH [CLM-000285] [CLM-006032] [CLM-006033] [CLM-006035]; sponsored-content Ventures claim [CLM-009075]. Single-source conclusions are *(INTERPRETATION)* until independently corroborated.
5. **Juvmo date:** FDA action 2026-09-25 (FDA novel-approvals record), company announcement 2026-09-28 [CLM-012017] [CLM-014039].
6. **Emraclidine impairment:** 4.5bn emraclidine charge (Q4 2024) and the 2024 total intangible impairment of 4,476m are consistent within rounding; no registry conflict (conflicts_proposed_A10 #2) [CLM-003057] [CLM-003059]. The brief's 3.5bn in 2025 remains CONTRADICTED [CLM-003058].
7. **Net income basis** note in §4 (conflicts_proposed_A10 #8).
