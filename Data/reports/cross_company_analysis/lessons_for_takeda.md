# Lessons for Takeda from Lilly, J&J and AbbVie

Cutoff 2026-11-21. Each lesson states what a competitor did (evidence IDs), a transferability verdict, why, the Takeda capability class from the [public baseline](../companies/takeda_public_baseline/capability_baseline/capability_baseline.md), the Takeda claims that anchor the baseline, and the internal-validation backlog item ([IVB list](../companies/takeda_public_baseline/internal_validation_backlog/backlog.md)) that must be checked with non-public data before acting. Verdicts are *(INTERPRETATION)* built on public evidence only. The same lessons are in `/Users/palrahma/Desktop/MEDICINE/strategy/data/takeda_lessons.json`.

Verdict key: **transfers** = mechanism applies on current evidence; **partially** = applies with a stated condition; **does_not_transfer** = structure or market differs. EVIDENCE_GAP means public evidence is missing, not that the capability is absent [CLM-005080]. Codes: LLY = Eli Lilly, JNJ = Johnson & Johnson, ABBV = AbbVie.

## Summary table

| ID | Area | Competitor | Verdict | Takeda baseline class | IVB |
|---|---|---|---|---|---|
| LES-01 | Manufacturing capacity as the binding constraint on a blockbuster | LLY | partially | EXISTING_STRENGTH (class 2: plasma network and PDT manufacturing) | IVB-006 |
| LES-02 | Cash-pay direct-to-patient channel | LLY | does_not_transfer | EVIDENCE_GAP (class 14: patient services and market access) | IVB-013 |
| LES-03 | Data-for-access platform (federated learning) | LLY | partially | EXISTING_BUT_UNDERDEVELOPED (class 9: enterprise data and AI platform, outcomes unproven) | IVB-001 |
| LES-04 | Owned robotic lab versus rented automation | LLY | transfers | EVIDENCE_GAP (class 11: lab automation and robotics) | IVB-002 |
| LES-05 | Growth concentration, price erosion and payer leverage | LLY | transfers | EXISTING_STRENGTH (class 1: GI and immunology franchise) | IVB-004 |
| LES-06 | Steady cadence of early-asset purchases versus a concentrated bet | LLY | partially | EXISTING_STRENGTH (class 5: external innovation and BD, deal flow); organisation EVIDENCE_GAP | IVB-007 |
| LES-07 | Successor sequencing before the cliff | JNJ | partially | EXISTING_BUT_UNDERDEVELOPED (class 7: LOE replacement) | IVB-005 |
| LES-08 | Debt-funded acquisition bridge | JNJ | partially | EXISTING_BUT_UNDERDEVELOPED (class 16: cost transformation) with class 5 deal flow | IVB-012 |
| LES-09 | Claimed pharma and MedTech synergy | JNJ | does_not_transfer | NOT_APPLICABLE (Takeda has no MedTech segment; six key business areas) | none |
| LES-10 | Inspection findings, not clinical data, behind approval delays | LLY | transfers | EXISTING_BUT_UNDERDEVELOPED (class 12: manufacturing quality, one documented failure) | IVB-011 |
| LES-11 | Litigation overhang and reserve volatility | JNJ | partially | NOT_APPLICABLE (legal exposure is not a baseline capability class) | IVB-012 |
| LES-12 | Self-reported AI metrics without baselines | JNJ | transfers | EXISTING_BUT_UNDERDEVELOPED (class 9: enterprise data and AI platform, outcomes unproven) | IVB-001 |
| LES-13 | Extend the successor across the incumbent's indications before the cliff | ABBV | transfers | EXISTING_BUT_UNDERDEVELOPED (class 7: LOE replacement) | IVB-005 |
| LES-14 | Contracting defence against PBM-driven biosimilar substitution | ABBV | partially | EVIDENCE_GAP (class 14: patient services and market access) with class 1 GI franchise | IVB-004 |
| LES-15 | Size acquisitions to survive a write-down | ABBV | transfers | EXISTING_STRENGTH (class 6: portfolio discipline, with write-down cost) | IVB-005 |
| LES-16 | Settlement-based IP to convert patent dates into entry dates | ABBV | partially | EXISTING_BUT_UNDERDEVELOPED (class 7: LOE replacement) | IVB-004 |
| LES-17 | Option and early-stage licence volume | ABBV | partially | EXISTING_STRENGTH (class 5: external innovation and BD, deal flow); organisation EVIDENCE_GAP | IVB-007 |
| LES-18 | High variance of first-in-class psychiatry and neuroscience assets | ABBV | partially | EXISTING_STRENGTH (class 3: rare disease and orexin science) | IVB-008 |
| LES-19 | Redesigning a patient or provider programme without a pilot | ABBV | does_not_transfer | EVIDENCE_GAP (class 14: patient services and market access) | IVB-013 |
| LES-20 | Packaging price concessions with tariff relief and investment pledges | LLY | partially | NOT_APPLICABLE (policy engagement is not a baseline capability class) | none |
| LES-21 | Home and subcutaneous administration as a growth and defence mechanism | JNJ | transfers | EXISTING_STRENGTH (class 1: GI and immunology franchise) | IVB-004 |

## LES-01 Manufacturing capacity as the binding constraint on a blockbuster (LLY)

- **What they did.** Lilly raised capex from USD 1.3bn (FY2021) to USD 7.8bn (FY2025) and announced more than USD 50bn of U.S. commitments after tirzepatide supply fell short; the FDA removed tirzepatide from the shortage list on 2024-10-02. Most announced sites are still pre-operating, with operating evidence only for Concord, Kinsale and the Lebanon genetic-medicine plant. [CLM-000168] [CLM-000172] [CLM-001039] [CLM-001066] [CLM-014017] [CLM-014008] [CLM-014014]
- **Transferability: partially.** Takeda's plasma-derived therapies are capacity-bound (collection centres and fractionation) and it has a USD 230m Los Angeles expansion, so the capacity logic transfers. The lesson to copy is to track operating capacity, not announced capacity. Takeda's FY2025 capex of JPY 426.9bn includes intangible assets and is not comparable with Lilly's property, plant and equipment capex. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_STRENGTH (class 2: plasma network and PDT manufacturing). Anchoring Takeda claims: [CLM-005063] [CLM-005065] [CLM-005007]
- **Internal validation needed.** IVB-006

## LES-02 Cash-pay direct-to-patient channel (LLY)

- **What they did.** Lilly launched LillyDirect on 2024-01-04, sold Zepbound self-pay vials from August 2024 and cut prices on 2025-12-01 to USD 299 / 399 / 449. The company says over 1 million patients accessed treatments through it in 2025; the 10-K gives no dollar share, and copay-accumulator and anti-kickback limits restrict combining discounts with insurance. [CLM-001042] [CLM-007002] [CLM-007004] [CLM-007005] [CLM-007010]
- **Transferability: does_not_transfer.** Cash-pay scaled in an uninsured-gap category (obesity). Takeda's main products are infused or specialty-distributed biologics and plasma therapies sold through payer coverage and hubs, so a cash channel fits poorly. Home and subcutaneous conversion (LES-21) is the better-evidenced mechanism. *(INTERPRETATION)*
- **Takeda baseline class.** EVIDENCE_GAP (class 14: patient services and market access). Anchoring Takeda claims: [CLM-005072] [CLM-007037]
- **Internal validation needed.** IVB-013

## LES-03 Data-for-access platform (federated learning) (LLY)

- **What they did.** Lilly launched TuneLab on 2025-09-09, giving selected biotechs access to Lilly-trained ADMET and safety models in exchange for federated data contributions, with Benchling distribution to more than 1,300 customers opt-in later in 2026. No uptake, retraining count or scientific outcome is disclosed. [CLM-000280] [CLM-006008] [CLM-014055] [CLM-014056] [CLM-006055]
- **Transferability: partially.** Takeda is already in a multi-pharma federated consortium (AISB) and could be a data-for-models participant, which is a cheaper position than building a rival platform. The platform's value is unproven, so participation should wait for independent results. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_BUT_UNDERDEVELOPED (class 9: enterprise data and AI platform, outcomes unproven). Anchoring Takeda claims: [CLM-005058] [CLM-005049] [CLM-006042]
- **Internal validation needed.** IVB-001

## LES-04 Owned robotic lab versus rented automation (LLY)

- **What they did.** Lilly built a remote robotic laboratory (Life Sciences Studio) and divested it to the CRO Arctoris in 2024; the reason is undisclosed. Zymergen, an owned biofoundry, was sold at about one-tenth of its IPO-era valuation. The NVIDIA-Lilly co-innovation lab announced in January 2026 is at concept stage. [CLM-006013] [CLM-006017] [CLM-006052] [CLM-006051] [CLM-000281]
- **Transferability: transfers.** The evidence favours buying automation as a service and gating AI-biotech deals on first-in-human data rather than owning a robotic lab. Takeda has no public lab-automation evidence, so there is nothing to retreat from. *(INTERPRETATION)*
- **Takeda baseline class.** EVIDENCE_GAP (class 11: lab automation and robotics). Anchoring Takeda claims: [CLM-005067] [CLM-005080] [CLM-014041]
- **Internal validation needed.** IVB-002

## LES-05 Growth concentration, price erosion and payer leverage (LLY)

- **What they did.** Tirzepatide reached 56.0% of Lilly's FY2025 revenue (15.6% in FY2023). Realised prices fell 5% in Q4 2025 and 15% in Q3 2026 while volume rose 46% and 53%; CVS Caremark removed Zepbound from its template formularies for 15 months (1 July 2025 to 1 October 2026); Trulicity and Verzenio face Medicare-set prices from 2028. [CLM-001003] [CLM-014003] [CLM-014004] [CLM-007011] [CLM-007013] [CLM-008015]
- **Transferability: transfers.** Entyvio is 21% of Takeda's revenue, faces Medicare negotiation from 2028 and a coming biosimilar event. Lilly's record shows that volume growth in a dominant franchise comes with net-price pressure and PBM leverage, so Takeda should plan for price erosion in its core franchise, not only for volume loss. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_STRENGTH (class 1: GI and immunology franchise). Anchoring Takeda claims: [CLM-005009] [CLM-005017] [CLM-008022]
- **Internal validation needed.** IVB-004

## LES-06 Steady cadence of early-asset purchases versus a concentrated bet (LLY)

- **What they did.** Lilly expensed USD 3.8bn, 3.3bn and 2.9bn of acquired IPR&D in 2023-2025 (Morphic USD 2,548.5m, DICE USD 1,915.5m); none of those assets had been approved in the sources reviewed, and DICE's lead asset was discontinued in 2024. [CLM-014058] [CLM-009095] [CLM-009000] [CLM-009002] [CLM-009003]
- **Transferability: partially.** A cadence of purchases keeps options open but had produced no approval by cutoff. Takeda's one large asset purchase (Nimbus, February 2023) reached an accepted NDA in September 2026, so the two models have different risk profiles; Takeda's organisation for external innovation is not documented publicly. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_STRENGTH (class 5: external innovation and BD, deal flow); organisation EVIDENCE_GAP. Anchoring Takeda claims: [CLM-009098] [CLM-005036] [CLM-005035] [CLM-005052]
- **Internal validation needed.** IVB-007

## LES-07 Successor sequencing before the cliff (JNJ)

- **What they did.** J&J had TREMFYA (IL-23) on the market with Crohn's and UC labels and approved the oral IL-23 peptide ICOTYDE on about 2026-03-17. In FY2025 Tremfya grew USD 1,485m, offsetting about 35% of Stelara's USD 4,283m loss, yet Immunology still fell 11.8%. [CLM-002026] [CLM-002053] [CLM-002065] [CLM-000256] [CLM-012012]
- **Transferability: partially.** The mechanism requires a successor in the same prescriber base launched years before the loss. Takeda's zasocitinib is an oral TYK2 inhibitor in psoriasis, not a successor to Entyvio in gastroenterology, so it replaces revenue but not the franchise. J&J's record also shows that even a pre-launched successor offsets only part of the loss in the first year. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_BUT_UNDERDEVELOPED (class 7: LOE replacement). Anchoring Takeda claims: [CLM-005017] [CLM-005035] [CLM-005041]
- **Internal validation needed.** IVB-005

## LES-08 Debt-funded acquisition bridge (JNJ)

- **What they did.** J&J acquired businesses for USD 15.1bn (FY2024) and USD 17.5bn (FY2025) net of cash; net debt rose from USD 2.1bn (FY2021) to USD 27.8bn (FY2025) while it paid about USD 12.4bn of dividends and USD 6.0bn of buybacks in FY2025. [CLM-009049] [CLM-002010] [CLM-002014] [CLM-000105]
- **Transferability: partially.** J&J's bridge rests on USD 24.5bn of operating cash flow and a large MedTech and pharma base. Takeda stated no significant acquisitions in three years, carries a company-defined adjusted leverage ratio (2.6x, not verified by the audit) and has a JPY 403.5bn Amitiza provision, so its bridge capacity depends on legal cash timing that is not public. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_BUT_UNDERDEVELOPED (class 16: cost transformation) with class 5 deal flow. Anchoring Takeda claims: [CLM-005005] [CLM-005014] [CLM-009087]
- **Internal validation needed.** IVB-012

## LES-09 Claimed pharma and MedTech synergy (JNJ)

- **What they did.** J&J asserts that pairing Abiomed, Biosense Webster and Shockwave creates cardiovascular leadership, but no cross-segment revenue synergy is disclosed. MedTech earns a 12.2% segment margin against 36.9% for Innovative Medicine, and J&J announced the Orthopaedics separation on 2025-10-14. [CLM-002074] [CLM-002004] [CLM-002037]
- **Transferability: does_not_transfer.** Takeda has no MedTech segment, so the structure does not apply. The transferable point is to test a claimed combination synergy against segment margins and disclosed revenue links before building strategy on it. *(INTERPRETATION)*
- **Takeda baseline class.** NOT_APPLICABLE (Takeda has no MedTech segment; six key business areas). Anchoring Takeda claims: [CLM-005010]
- **Internal validation needed.** none; public evidence suffices or the topic is outside the backlog

## LES-10 Inspection findings, not clinical data, behind approval delays (LLY)

- **What they did.** Lilly's lebrikizumab CRL (October 2023) came from third-party manufacturer inspection findings, with no concern on clinical data, safety or label; lebrikizumab was approved as Ebglyss on 2024-09-13. AbbVie's second ABBV-951 CRL (June 2024) also cited third-party manufacturer observations. [CLM-012134] [CLM-001024] [CLM-001064] [CLM-012112]
- **Transferability: transfers.** Takeda's baseline already records a 2020 FDA warning letter at Hikari with a Leuprorelin supply shortage. Launch timing for its 2026 approvals and the zasocitinib NDA depends on site inspection status, including third-party sites. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_BUT_UNDERDEVELOPED (class 12: manufacturing quality, one documented failure). Anchoring Takeda claims: [CLM-005020] [CLM-005029] [CLM-005035]
- **Internal validation needed.** IVB-011

## LES-11 Litigation overhang and reserve volatility (JNJ)

- **What they did.** J&J's talc subsidiaries filed three Chapter 11 petitions (two dismissed, Red River not confirmed on 2025-03-31); J&J reversed about USD 7bn of reserve, held about USD 3.4bn at FY2025 end, then proposed a USD 5.5bn ovarian resolution on 2026-07-27 that needs 95% participation. Plaintiff counsel says the cost could reach USD 7bn or more. [CLM-002015] [CLM-002038] [CLM-002016] [CLM-002062] [CLM-002063]
- **Transferability: partially.** Talc is product liability and Takeda's AMITIZA case is pay-for-delay antitrust, so legal mechanics differ. The transferable point is that reserve and settlement estimates moved by billions within a year at J&J; Takeda's JPY 403.5bn provision follows a jury verdict it intends to appeal, and the final judgement and cash timing are not public. *(INTERPRETATION)*
- **Takeda baseline class.** NOT_APPLICABLE (legal exposure is not a baseline capability class). Anchoring Takeda claims: [CLM-005013] [CLM-005014] [CLM-014047]
- **Internal validation needed.** IVB-012

## LES-12 Self-reported AI metrics without baselines (JNJ)

- **What they did.** J&J's CIO reported nearly 900 gen-AI use cases reviewed, trial-site recommendations with 'up to 2.6x' enrolment, and 47,000 employees completing a gen-AI course. The enrolment figure has no baseline or method, and course completions are a training metric. The audit retagged both. [CLM-006018] [CLM-006019] [CLM-006020] [CLM-006022]
- **Transferability: transfers.** Takeda's own reported measures (63.4% of the workforce actively using gen-AI tools; a vendor-hosted agent platform) are also usage or self-report measures. Takeda should define outcome baselines (time saved, cycle time, cost) before treating usage as value. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_BUT_UNDERDEVELOPED (class 9: enterprise data and AI platform, outcomes unproven). Anchoring Takeda claims: [CLM-014043] [CLM-005058] [CLM-005057]
- **Internal validation needed.** IVB-001

## LES-13 Extend the successor across the incumbent's indications before the cliff (ABBV)

- **What they did.** Skyrizi and Rinvoq gained psoriatic arthritis, Crohn's, ulcerative colitis and atopic dermatitis labels between 2022 and 2025 and, with head-to-head data, covered Humira's major indications. Together they rose from USD 7,687m (2022) to USD 25,866m (2025) against a Humira loss of USD 16,697m. [CLM-003084] [CLM-003016] [CLM-003014] [CLM-003015]
- **Transferability: transfers.** Takeda has psoriatic arthritis Phase 3 studies for zasocitinib running to May 2027 and a head-to-head Phase 3 win over deucravacitinib, which is the same pattern of indication breadth and comparative data. The AbbVie successors were already marketed before the cliff; Takeda's are not yet. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_BUT_UNDERDEVELOPED (class 7: LOE replacement). Anchoring Takeda claims: [CLM-005037] [CLM-005034] [CLM-005018]
- **Internal validation needed.** IVB-005

## LES-14 Contracting defence against PBM-driven biosimilar substitution (ABBV)

- **What they did.** AbbVie kept at least 97% of adalimumab volume through March 2024 with rebate-for-access contracts, then supplied a co-branded Humira to CVS's Cordavis when Caremark removed Humira from template formularies on 2024-04-01; U.S. Humira revenue still fell 41% in 2024 and 57% in 2025. [CLM-003007] [CLM-003008] [CLM-003009] [CLM-003010] [CLM-007016]
- **Transferability: partially.** PBM private labels now handle large biosimilar events (nine Stelara biosimilars by July 2025, four from PBM-affiliated labels), so payer contracting depth matters as much as patents. Takeda has no public evidence on rebate or contracting structure, and two Entyvio biosimilar BLAs are under FDA review. *(INTERPRETATION)*
- **Takeda baseline class.** EVIDENCE_GAP (class 14: patient services and market access) with class 1 GI franchise. Anchoring Takeda claims: [CLM-007025] [CLM-005072] [CLM-014051]
- **Internal validation needed.** IVB-004

## LES-15 Size acquisitions to survive a write-down (ABBV)

- **What they did.** AbbVie recorded a USD 4.5bn impairment in Q4 2024 after emraclidine failed, 54% of the USD 8.3bn Cerevel net price. The same year's ImmunoGen purchase supplied a growing product (Elahere) and Cerevel's tavapadon was approved as Juvmo in September 2026. [CLM-009054] [CLM-003057] [CLM-003086] [CLM-003090]
- **Transferability: transfers.** Takeda's largest purchase (Nimbus, USD 4.0bn upfront) has the same single-asset risk profile and has so far delivered. Takeda's baseline already shows that stop decisions and write-downs (cell therapy, soticlestat) are absorbed; the lesson is to size any next large purchase so one failure does not breach leverage or dividend policy. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_STRENGTH (class 6: portfolio discipline, with write-down cost). Anchoring Takeda claims: [CLM-005036] [CLM-005025] [CLM-009084]
- **Internal validation needed.** IVB-005

## LES-16 Settlement-based IP to convert patent dates into entry dates (ABBV)

- **What they did.** AbbVie's September 2025 settlements with all Rinvoq generic filers mean no generic tablet entry is expected before April 2037, four years after the 2033 composition patent; Humira biosimilar entry was negotiated to 2023. [CLM-003021] [CLM-003087] [CLM-014036]
- **Transferability: partially.** Entyvio patents expire in some cases in 2032 and third parties filed UK and Netherlands revocation actions in early 2026, so Takeda faces litigation rather than settled entry dates. What is transferable is the posture; the outcome depends on Takeda's litigation position, which is not public. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_BUT_UNDERDEVELOPED (class 7: LOE replacement). Anchoring Takeda claims: [CLM-014050] [CLM-005017] [CLM-014051]
- **Internal validation needed.** IVB-004

## LES-17 Option and early-stage licence volume (ABBV)

- **What they did.** AbbVie runs a yearly stream of USD 0.6bn to 1.0bn of early-stage upfronts and option deals (ADARx USD 335m upfront with up to USD 7.5bn of milestones; Gubra USD 350m; Ichnos USD 700m). None had produced an approved product by cutoff. [CLM-009061] [CLM-009062] [CLM-009060] [CLM-009069] [CLM-009097]
- **Transferability: partially.** Takeda's Innovent arrangement (USD 1.2bn upfront including USD 100m equity, with an option) is the same shape on a smaller number of deals. The evidence does not show that volume produces approvals, and Takeda's external-innovation organisation is not documented in primary sources. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_STRENGTH (class 5: external innovation and BD, deal flow); organisation EVIDENCE_GAP. Anchoring Takeda claims: [CLM-009078] [CLM-005050] [CLM-005052]
- **Internal validation needed.** IVB-007

## LES-18 High variance of first-in-class psychiatry and neuroscience assets (ABBV)

- **What they did.** AbbVie's emraclidine Phase 2 missed its primary endpoint in November 2024; J&J stopped aticaprant on insufficient efficacy in March 2025; Takeda's soticlestat Phase 3 missed in June 2024. Neuroscience and psychiatry is the common failure site across three companies in the window. [CLM-003054] [CLM-003057] [CLM-002039] [CLM-012135] [CLM-012115] [CLM-012120]
- **Transferability: partially.** Takeda's oveporexton succeeded in a different neuroscience area (orexin, with discovery in Shonan) after TAK-994 was stopped in 2022 for liver safety. The lesson is to gate psychiatry and CNS assets on Phase 2 quality and placebo response, and not to infer that orexin success transfers to other CNS bets. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_STRENGTH (class 3: rare disease and orexin science). Anchoring Takeda claims: [CLM-005024] [CLM-005048] [CLM-005029] [CLM-005023]
- **Internal validation needed.** IVB-008

## LES-19 Redesigning a patient or provider programme without a pilot (ABBV)

- **What they did.** AbbVie launched a revised Alle loyalty programme in October 2024 and reinstated the original in early 2025 after providers found the new one too complex; U.S. Botox Cosmetic revenue fell 11% in 2025 on pricing from programme changes, lower share and lower demand. [CLM-003033] [CLM-003032] [CLM-003088]
- **Transferability: does_not_transfer.** Takeda has no aesthetics business, and Alle is a consumer loyalty scheme. The narrower point, that a support-programme redesign can cost share within months and should be piloted, applies to Takeda's Help at Hand and EntyvioConnect programmes, which have no public outcome data. *(INTERPRETATION)*
- **Takeda baseline class.** EVIDENCE_GAP (class 14: patient services and market access). Anchoring Takeda claims: [CLM-007037] [CLM-007038] [CLM-005072]
- **Internal validation needed.** IVB-013

## LES-20 Packaging price concessions with tariff relief and investment pledges (LLY)

- **What they did.** Lilly (2025-11-06), J&J (2026-01-08) and AbbVie (2026-01-12) each announced a voluntary agreement pairing price or access concessions with tariff relief and a U.S. investment pledge (Lilly more than USD 50bn since 2020, J&J more than USD 55bn over four years, AbbVie USD 100bn over a decade). [CLM-001036] [CLM-008031] [CLM-008032] [CLM-008029] [CLM-008030] [CLM-008037]
- **Transferability: partially.** Takeda's 20-F records MFN pricing and Japan's annual price revisions as risks and the registry holds no Takeda pledge or agreement. Whether such a package is available or advisable for Takeda cannot be judged from public evidence; the competitor agreements are company announcements, and their terms and realised value are not independently verified. *(INTERPRETATION)*
- **Takeda baseline class.** NOT_APPLICABLE (policy engagement is not a baseline capability class). Anchoring Takeda claims: [CLM-008035] [CLM-008036] [CLM-008022]
- **Internal validation needed.** none; public evidence suffices or the topic is outside the backlog

## LES-21 Home and subcutaneous administration as a growth and defence mechanism (JNJ)

- **What they did.** TREMFYA subcutaneous share gains accompanied USD 5,155m of FY2025 sales (+40.5%); Zepbound moved to vials and a KwikPen with self-pay pricing from USD 299. [CLM-007029] [CLM-007044] [CLM-000256] [CLM-007053]
- **Transferability: transfers.** This is the best-evidenced transferable mechanism for Takeda: the ENTYVIO subcutaneous pen is approved for UC (September 2023) and Crohn's disease (April 2024), the 20-F says it continues to drive uptake, and HYHUB needle-free Hyqvia transfer received FDA 510(k) clearance in July 2025. Effect on net price and erosion after biosimilar entry is not established. *(INTERPRETATION)*
- **Takeda baseline class.** EXISTING_STRENGTH (class 1: GI and immunology franchise). Anchoring Takeda claims: [CLM-005018] [CLM-007041] [CLM-007042] [CLM-005012]
- **Internal validation needed.** IVB-004

## Cross-lesson reading *(INTERPRETATION)*

- The lessons bearing most directly on Entyvio (21% of revenue) are LES-05, LES-14 and LES-21 [CLM-005009] [CLM-007016] [CLM-007053].
- AI-infrastructure lessons (LES-03, LES-04) point to partnering and renting: competitor evidence shows no outcome and one divestment [CLM-006007] [CLM-006013].
- No lesson rests on an independently verified AI outcome; the only regulator-verified items are device records [CLM-006054].
- Takeda's 2026 integrated-report evidence post-dates the capability baseline and should update classes 9, 11 and 13 at the next refresh [CLM-014041] [CLM-014042] [CLM-014043].
