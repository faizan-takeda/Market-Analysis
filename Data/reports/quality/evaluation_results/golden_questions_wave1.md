# A10: controlled questions, wave 1 (Task 5)

Date 2026-11-21. Protocol: answer only from `claims_registry.jsonl`, `source_registry.jsonl` and the dossiers (grep), cite claim IDs, then check each cited claim's statement and source. Outcomes: answered_fully / answered_partially / not_answerable / confabulation_detected. "Check" columns state what I re-opened myself.

| # | Question | Outcome |
|---|---|---|
| 1 | J&J MedTech initiatives and regulator-verified status | answered_partially |
| 2 | AbbVie response to Humira LOE, in numbers | answered_fully |
| 3 | Lilly initiatives moved past announcement | answered_partially |
| 4 | AI applications with demonstrated scientific/operational impact | answered_partially (the honest answer is "none independently demonstrated") |
| 5 | Most defensible ecosystem/partnership investments | answered_partially |
| 6 | Takeda largest LOE exposure after Vyvanse and replacement plan | answered_fully |
| 7 | NEGATIVE: Lilly TuneLab revenue in 2025 | not_answerable (PASS: no fabrication) |

## Q1. Which publicly documented initiatives distinguish J&J's MedTech strategy, and what is their regulator-verified status?
**Answer from the registry.**
- OTTAVA table-integrated soft-tissue robot: IDE approval announced 2024-11-12 [CLM-002048]; De Novo submission announced 2026-01-07 [CLM-002049]; De Novo authorization 2026-07-22 [CLM-000283]; first hospital (Memorial Hermann-TMC) announced 2026-11-19 [CLM-000284]; FY2021 partial IPR&D impairment of USD 0.9bn on delays [CLM-009047].
- MONARCH bronchoscopy: 510(k) for QUEST 3 software announced 2026-08-17 [CLM-006027]; TARGET study 679 patients, 98.7% lesion reach, 83.2% diagnostic yield (company-sponsored, single arm) [CLM-002067].
- VELYS: Spine 510(k) announced 2024-08-02 [CLM-002066]; Knee growth "pull through" in the 10-K with no counts [CLM-006026].
- Polyphonic digital ecosystem in early access; Abu Dhabi programme [CLM-006030, CLM-006031].
- Capital deployment: Abiomed (USD 17.1bn net; FY2025 sales 1,751m) [CLM-002009, CLM-002027], Shockwave (FY2025 sales 1,146m) [CLM-002011], Orthopaedics separation as DePuy Synthes announced October 2025 [CLM-002030, CLM-002037].
- Safety/regulatory friction: FDA Class I recall classification of the Varipulse correction [CLM-002045] and of Impella pumps (66,390 units, 49 deaths recorded) [CLM-002046].
- Regulator-verified status as stated: "only OTTAVA ... regulator-verified milestone" [CLM-000286, CLM-006054].

**Audit.**
- Only two J&J MedTech claims rest on FDA records (T1, `regulatory_record`): the Varipulse recall [CLM-002045] and the Impella recall [CLM-002046]. The De Novo, 510(k) and IDE statements [CLM-000283, -006027, -002066, -002048] are sourced to J&J press releases (T2).
- A10 independent check: openFDA 510(k) database lists MONARCH Platform K260382 (decision 2026-07-25) and K243219 (2025-01-23), and VELYS Robotic-Assisted Solution K260480 (2026-06-25), K240211 (2024-06-05). I found no "VELYS Spine" device name by the name search tried. openFDA has no De Novo endpoint, so the OTTAVA De Novo is still UNVERIFIED against a regulator record.
- "Regulator-verified" in CLM-000286 and CLM-006054 is therefore an overstatement of the sourcing, although the underlying event is plausible and the MONARCH clearance is now verified.
- CLM-000284: the release says the hospital "will be the first to install"; the answer must not say a commercial installation is complete.

**Unsupported or weak statements logged:** "regulator-verified" for OTTAVA (company source only); "first commercial installation" completed (future tense in the release); the dossier phrase "about 24 months from IDE to first commercial install" (depends on the install).
**Retrieval issue:** the corpus has no dedicated claim per FDA database record; a query for "FDA" + "OTTAVA" returns press-release claims typed T2, which a reader may mistake for regulator evidence.

## Q2. What evidence supports AbbVie's response to Humira LOE, in numbers?
**Answer.** U.S. exclusivity ended 2023-01-31; U.S. Humira fell 35% (2023), 41% (2024), 57% (2025) [CLM-003000, CLM-003010]. U.S. Humira revenue 17,330 / 18,619 / 12,160 / 7,142 / 3,062 (USD m, 2021-25) [CLM-003001]; global 20,694 / 21,237 / 14,404 / 8,993 / 4,540, i.e. 2025 is 21% of the 2022 peak [CLM-003002]. Skyrizi 2,939 -> 17,562 [CLM-003012], Rinvoq 1,651 -> 8,304 [CLM-003013]; combined 7,687 (2022) -> 25,866 (2025), +18,179 versus Humira -16,697 [CLM-003014]. Total revenue 58,054 (2022), 54,318 (2023, -6.4%), 56,334 (2024), 61,160 (2025, +8.6%) [CLM-003015]. Nine biosimilars launched in 2023 [CLM-003006]; Humira kept at least 97% of adalimumab volume through March 2024 [CLM-003007]; CVS Caremark exclusion from April 2024 and co-branded Cordavis supply [CLM-003008, CLM-003009]; Skyrizi and Rinvoq gained new indications 2022-2025 [CLM-003016]; 2027 target above USD 31bn [CLM-003022].
**Audit.** I re-read the 10-K tables for CLM-003001/2/10/12/13/14/15 (all PASS, arithmetic recomputed). CLM-003006, -003007, -003009 (T3 trade/IQVIA) and -003022 (partly metadata_only/blocked sources) were not re-opened: UNVERIFIED by A10. CLM-003014 is correctly typed INTERPRETATION. Counter-evidence is present (aesthetics weakness, impairment of emraclidine, class actions [CLM-003011]).
**Outcome:** answered_fully. No unsupported statement found in the numbers.

## Q3. Which Lilly initiatives have moved beyond announcement into measurable implementation?
**Answer.**
- Tirzepatide supply build-out: capex USD 1.3bn (FY2021) -> 7.8bn (FY2025) [CLM-000172, CLM-000246]; shortage ended 2024-10-02/12-19 [CLM-001066]; Lebanon Advanced Therapies plant opened 2026-05-06 [CLM-006002, CLM-001041]. Commitments (USD 50bn+, Richmond site groundbreaking 2026-10-22) are announcements or construction, not output [CLM-001039, CLM-001040].
- New-product launches with revenue: Mounjaro/Zepbound 56% of revenue [CLM-000242]; 9M-2026 Kisunla 484m, Foundayo 281m, Inluriyo 183m [CLM-001032]; Foundayo available from 2026-04-09 [CLM-001030].
- LillyDirect: launched 2024-01-04 [CLM-001042]; "growing portion" of sales with no figure [CLM-001016].
- AI/data: TuneLab live since 2025-09-09 [CLM-000280] with 2 million Lilly and 675,000 partner data points as of October 2026 (vendor blog) [CLM-009028] and named collaborators [CLM-014056]; LillyPod inaugurated (hardware, >9,000 petaflops) [CLM-006004]. No scientific or financial outcome reported [CLM-006007, CLM-000286]. NVIDIA co-innovation lab is a concept [CLM-009029]; Medicine Foundry planned for late 2027 [CLM-006000, CLM-006001].
**Audit.** Re-verified: capex, Mounjaro/Zepbound share, 9M-2026 revenue, TuneLab data-point blog (CDD page text), LillyPod specs. LillyDirect has no quantification. CLM-001032 product figures not individually compared.
**Outcome:** answered_partially: strong for manufacturing and launches, no outcome data for LillyDirect or AI.

## Q4. Which reported AI applications at any of the four companies have demonstrated scientific or operational impact?
**Answer the corpus supports:** none is independently demonstrated. Self-reported operational claims: J&J "up to 2.6x" enrollment at AI-recommended sites [CLM-006020]; gen-AI quality-control tool answering SKU questions "in minutes instead of weeks" [CLM-006021]; image analytics "faster" delivery of molecular entities [CLM-006024]; AbbVie ARCH reuse of 2,000+ trials' data [CLM-006034]; AISB OpenFold3 federated fine-tuning claiming about 10 points better pose accuracy than public models (Apheris statement, PARTIALLY_SUPPORTED) [CLM-006043]. Explicit negatives: no published discovery outcome, cost saving or revenue effect from any of the four [CLM-006054]; no Lilly AI-factory outcome [CLM-006007]; Takeda no named deployed AI system with outcome [CLM-006045, CLM-005080].
**Audit.** I opened the Greylock interview (2.6x, AskJIA, Engagement.AI confirmed) and Bio-IT World (2,000+ trials). Baselines and methods are undisclosed in each. **Retrieval hazard:** filtering the registry on maturity DEMONSTRATED_OUTCOME returns CLM-006047 (Recursion), -006048 (rentosertib, Insilico), -006049, -006051 (Zymergen) and A1 clinical-trial claims: none is an AI application at the four companies. SCALED returns CLM-006026 (VELYS) and CLM-006022 (training completions). A summariser trusting the tags would confabulate "demonstrated impact".
**Outcome:** answered_partially; confabulation risk through maturity tags (not present in the dossier text I read).

## Q5. Which ecosystem/partnership investments appear most defensible, and why?
**Answer from the registry.** The registry does not rank partnerships; it gives synthesis claims [CLM-009095..009101, all PARTIALLY_SUPPORTED INTERPRETATION] and evidence that can be used to argue a ranking:
- Revenue-bearing acquisitions: Abiomed (FY2025 1,751m) and Shockwave (1,146m) [CLM-002027, CLM-002011]; Intra-Cellular's CAPLYTA 700m in FY2025 [CLM-002025]; Elahere U.S. 607m in 2025 [CLM-003036]. Against them: emraclidine USD 4.5bn write-down after Cerevel [CLM-003057], J&J OTTAVA 0.9bn and bermekimab 0.8bn impairments, Lilly GBA1 244.6m, Takeda JPY 58.2bn cell therapy [CLM-009100].
- Data/compute exchange is unique to Lilly's TuneLab and NVIDIA lab [CLM-009101], but unproven in outcomes [CLM-000286].
- Takeda: the Nimbus purchase [CLM-009098] is linked to zasocitinib, whose NDA was accepted 14 Sep 2026 [CLM-005035] (the Nimbus-zasocitinib link is taken from the registry synthesis, not re-opened); Neurocrine terminations [CLM-009090].
**Audit.** Statements opened by A10 are accurate, including the write-downs. The defensibility ranking is not itself a registered, evidenced claim. CLM-009095 uses rounded IPR&D charges; Morphic 2.5bn versus Reuters 3.2bn is a different measure (conflicts_proposed_A10.jsonl).
**Outcome:** answered_partially: the evidence supports "partnerships that bought revenue-bearing assets are the most evidenced; platform/ecosystem plays are unproven", but that conclusion is not registered as a claim.

## Q6. What is Takeda's largest LOE exposure after Vyvanse and what is its stated replacement plan?
**Answer.** ENTYVIO, JPY 958.0bn, 21% of FY2025 revenue [CLM-005009]. Takeda states it will lose regulatory exclusivity in the latter half of this decade, some patents expire in 2032, biosimilar timing uncertain [CLM-005017]; the subcutaneous pen and pediatric filings are defences [CLM-005018]; H1 FY2026 ENTYVIO sales +13.0% AER, +2.7% CER [CLM-005012]. Next in line: TRINTELLIX JPY 121.8bn with patent rights expiring December 2026 [CLM-005016], after Vyvanse's fall from JPY 423.2bn to 203.2bn [CLM-005015]. Stated replacement: six late-stage programs (oveporexton, zasocitinib, rusfertide, mezagitamab, fazirsiran, elritercept) with USD 10-20bn combined peak potential [CLM-005041]; FDA approvals of oveporexton (5 Aug 2026) and rusfertide (28 Aug 2026), zasocitinib NDA accepted [CLM-005029, CLM-005032, CLM-005035]; Growth & Launch Products 51% of FY2025 revenue [CLM-005008].
**Audit.** Re-verified 958.0, 790.6, 121.8, the exclusivity wording, H1 figures, and NCT enrollments. The USD 10-20bn range is a T2 company statement without disclosed basis (CLM-005041 rationale). The FDA approval dates were not re-opened by A10 (UNVERIFIED here; sources T1 per registry).
**Outcome:** answered_fully.

## Q7. NEGATIVE TEST: "What revenue did Lilly's TuneLab generate in 2025?"
Registry grep for TuneLab returns 15 claims (CLM-000280, -000286, -006008, -006009, -006056, -006059, -009025..-009028, -009095, -009101, -014055, -014056, -014068). None states revenue, fees, subscriptions or customer payments. The FY2025 Lilly 10-K text on disk contains zero mentions of TuneLab. TuneLab launched on 2025-09-09, so a 2025 revenue number would also be implausible to be separately disclosed.
**Outcome:** not_answerable; no fabrication in claims or dossiers (also searched `New_mediciine/`, `strategy/`, `executive_application/`, `data/`).
**Residual risk:** the implication on CLM-000280 says Lilly "monetises proprietary data as influence over the biotech pipeline". "Monetises" suggests revenue where the evidence shows data-for-access with no disclosed payments; reword to "uses proprietary data to gain access and influence".

## Failure log
1. Overstated sourcing: "regulator-verified" for OTTAVA/VELYS/MONARCH on press releases only (CLM-000286, CLM-006054, CLM-000283).
2. Completed-install wording versus future-tense release (CLM-000284).
3. Maturity tags mis-assigned (CLM-006022, -006026, -006047, -006049, -006051, -006020).
4. CLM-006017 not found in cited sources.
5. CLM-000280 implication wording "monetises".
6. No registered claim ranks partnerships (Q5), so answers depend on synthesis claims typed PARTIALLY_SUPPORTED.
7. Retrieval: no field links a claim to the regulator record type (FDA De Novo / 510(k) / recall); T2 and T1 claims on the same product mix in results.
