# Golden questions, round 2 (A10-bis)

Date 2026-11-21. Protocol: answer only from the registry and reports, cite claim IDs, then judge whether each cited claim supports the answer (statement read, and the figure re-checked against a primary source where I could open one). Outcome codes: answered_fully / answered_partially / not_answerable / confabulation_detected.

| Question | Outcome |
|---|---|
| (a) Lilly sites operating vs announced | answered_partially |
| (b) 2025-26 U.S. pricing and MFN agreements, per company | answered_partially (three companies fully, Takeda not_answerable) |
| (c) Neuroscience failures and cost across the four companies | answered_partially |
| (d) J&J robotics adoption numbers | answered_partially (milestones yes, adoption numbers not_answerable) |
| (e) NEGATIVE: Takeda's approved AI budget for 2027 | not_answerable (no confabulation) |

## (a) Which Lilly manufacturing sites are evidenced as operating vs announced?

**Answer from the corpus (cutoff 2026-11-21).**

Operating:
- Existing production sites in Indiana, North Carolina, Puerto Rico and Wisconsin, and ex-U.S. sites in Ireland, France, Spain, Italy, China and Japan [CLM-001022]. Supported: it lists current sites, 10-K text.
- Concord, North Carolina: announced 2022-01-28 at USD 1bn, later USD 2bn; a trade article quoting the site head says commercial production and first shipments at the end of 2024 [CLM-014014]. Supported but single T3 source; I re-opened the article and the sentence is there. Only one outlet, so "operating" is the weakest-supported item on this list.
- Kinsale, Ireland: USD 800m expansion "began making medicines" in 2023 [CLM-014011], from a Lilly release I could not re-open (403).
- Lilly Lebanon Advanced Therapies (genetic medicine): opened 2026-05-06; a reporter saw robotic dosing and sealing; no output data [CLM-006002, CLM-014015, CLM-001041]. Supported as "opened", not as producing at scale.
- The Wisconsin parenteral plant bought in May 2024 (USD 925m net of cash) operates as acquired; its expansion is separate [CLM-009012, CLM-014013].

Announced or under construction, not operating:
- Houston API, USD 6.5bn: announced 2025-09-23, ground broken 2026-09-21, "operational within five years" [CLM-014008].
- Goochland/Richmond, Virginia, USD 5bn: announced 2025-09-16, ground broken 2026-10-22 [CLM-001040, CLM-014016].
- Huntsville, Alabama, more than USD 6bn: construction expected 2026, completion 2032 [CLM-014009].
- Lehigh Valley, Pennsylvania, more than USD 3.5bn: operational 2031 [CLM-014010].
- Alzey, Germany, USD 2.5bn: "operational beginning in 2027", subject to permitting [CLM-014012].
- Kenosha County, Wisconsin expansion, USD 3bn: production 2028 per a spokesperson via local radio [CLM-014013] (PARTIALLY_SUPPORTED).
- Limerick, Ireland: production "on track to start in 2026"; no source confirms it started by the cutoff [CLM-014011].
- Lebanon, Indiana API site (opens 2027) and Medicine Foundry (late 2027) [CLM-001038, CLM-006000, CLM-006001, CLM-014015].
- Context: capex USD 7.8bn in 2025 versus 5.1bn in 2024 and construction in progress USD 13,013m [CLM-014017]; Lilly counts 10 new U.S. sites since 2020 [CLM-014016].

**Judgement.** The split is supported where sources were opened. Weaknesses: operating status for Concord, Kinsale and Lebanon rests on a trade article, a company release and a press tour, with no independent or regulator evidence of production for any new Lilly site; the seven T2-only announcements are not flagged single_interested_source; Houston, Pennsylvania, Limerick and Ireland pages returned 403 to me, so those were checked against stored passages only. The facts sit in four shards (A1, A6, A9, A14), so a retriever needs several claims to rebuild the table. No confabulation: no claim in the corpus calls any new site operating without a source. Outcome: **answered_partially**.

## (b) What did each company's 2025-26 U.S. pricing or MFN agreement commit to?

**Lilly (6 November 2025 release; FY2025 10-K).** Medicare beneficiaries pay no more than USD 50 a month for Zepbound and orforglipron (if approved) from as early as 1 April 2026; three years of tariff relief; no future pricing mandates [CLM-001036, CLM-008027]. The 10-K describes preliminary agreements: lower Medicaid and certain other prices, launch pricing aligned across developed nations, a three-year Section 232 grace period tied to U.S. manufacturing commitments, participation in a government direct-to-patient platform, and Medicare access to discounted obesity medicines by 1 July 2026; definitive agreements were still being negotiated [CLM-008028, CLM-007007, CLM-000251]. Linked pledge: more than USD 50bn of U.S. commitments since 2020 [CLM-008029].
**J&J (8 January 2026).** Voluntary agreement: TrumpRx participation, Medicaid prices comparable to other developed countries, an exemption from tariffs; USD 55bn of U.S. investment reaffirmed through early 2029 [CLM-008031, CLM-008030]. Term of the tariff exemption is not stated [CLM-008037].
**AbbVie (12 January 2026).** Three-year agreement: low Medicaid prices, TrumpRx offerings (Humira listed), exemption from tariffs and future pricing mandates, USD 100bn of U.S. R&D and capital investment over a decade [CLM-008032, CLM-003081].
**Takeda.** No agreement found. The 20-F says a May 2025 executive order encouraged MFN pricing and the administration has negotiated MFN-style agreements with several companies, which could lower Takeda's U.S. prices [CLM-008035]. Not answerable beyond that.
**Program context.** 17 manufacturers had TrumpRx agreements at 5 May 2026; CMS said they expire at the end of the current presidential term [CLM-007009].

**Judgement.** I re-checked the Lilly USD 50 and April date, the 50bn/23bn pledge, the AbbVie USD 100bn and three-year term, and the CRS TrumpRx counts against the sources; all match. J&J's release returned a block page to me, so CLM-008030/008031 rest on stored passages. The agreement texts themselves were never opened, so "committed to" means "announced as committed to". Retrieval failures: the policy report cites CLM-008035 (Takeda) for the J&J agreement, CLM-008032 (AbbVie) for the Lilly 10-K, and CLM-008030 (J&J) for the Lilly insulin cut, so a reader following that file lands on the wrong company; and the Medicare start is April 1 in the release but July 1 in the 10-K (unresolved, conflict filed). Outcome: **answered_partially** (Lilly, J&J, AbbVie answered fully at announcement level; Takeda not_answerable).

## (c) Which neuroscience failures occurred across the four companies and what did they cost?

| Company | Failure | Cost in the corpus | Claims |
|---|---|---|---|
| AbbVie | Emraclidine, two Phase 2 EMPOWER trials missed the primary endpoint (11 Nov 2024); extension study terminated | USD 4.5bn pre-tax impairment in Q4 2024 (fair value 2.4bn vs carrying 6.9bn); Cerevel operating losses through 2024 USD 4.9bn; Cerevel purchase USD 8.7bn (8.3bn net); impairment about 54% of the net price; shares fell 12% on the day | CLM-003054, CLM-003057, CLM-009054, CLM-012115, CLM-012116, CLM-014035, CLM-003058 |
| J&J | Aticaprant Phase 3 VENTURA programme discontinued 6 Mar 2025 for insufficient efficacy | Not found in the corpus (no impairment or charge disclosed in any opened source) | CLM-002039, CLM-012135, CLM-014019, CLM-002056 |
| Takeda | Soticlestat Phase 3 (Dravet, LGS) missed endpoints June 2024; discontinued 30 Jan 2025 | JPY 21.5bn impairment | CLM-005024, CLM-009083, CLM-012120 |
| Takeda | TAK-994 Phase 2 terminated 2021 (liver safety signal); not developed after June 2022; Neurocrine ended TAK-041 and TAK-831 effective March 2025 | No amount in the corpus | CLM-012119, CLM-005023, CLM-009090 |
| Lilly | No neuroscience trial failure found in the sources opened. Related: PR001 (GBA1) gene therapy impairment because of delayed launch timing, not a trial failure; donanemab CRL (Jan 2023) later resolved with approval | USD 244.6m charges in 2022 (mainly the PR001 impairment) | CLM-009009, CLM-001012, CLM-012105 |

**Judgement.** All cited figures that I re-checked match: emraclidine 4.5bn and 8.7/8.3bn (10-K), JPY 21.5bn via the FY2025 20-F and the registry. The "common failure site across three companies" reading [CLM-003054 and others] is the project's inference. Soticlestat is epilepsy (neurology), aticaprant and emraclidine psychiatric. Costs are missing for J&J and for TAK-994; the corpus says so rather than guessing, which is correct. Lilly's entry depends on how "neuroscience failure" is defined: nothing in the corpus shows a Lilly neuroscience Phase 2/3 failure, and the gene-therapy charge is a launch-timing impairment. Outcome: **answered_partially**; no confabulation.

## (d) What does the evidence say about J&J robotics adoption numbers?

**Answer.** The corpus holds no adoption numbers for J&J's robotics: no installed base, system sales, procedure counts or revenue for OTTAVA, MONARCH or VELYS. What exists:
- OTTAVA: IDE cases from early 2025 at Memorial Hermann; De Novo request received by FDA 2025-12-18 and granted 2026-07-21 (DEN250068); an announced early-access installation at Memorial Hermann on 2026-11-19; J&J gave no revenue, unit-sale, order-book or procedure data [CLM-014022, CLM-014023, CLM-014024, CLM-006029, CLM-002049]. A trial-room fit statistic (ORs as small as 243 sq ft; a 12-surgeon survey) is the only quantity [CLM-006028].
- MONARCH: 510(k) K260382 decided 2026-07-25; three launches in 18 months; TARGET study 679 patients with 98.7% lesion reach and 83.2% diagnostic yield (clinical performance, not adoption) [CLM-014025, CLM-006027, CLM-002067].
- VELYS: five 510(k) clearances from 2021 to 2026; the 10-K cites "pull through related to the VELYS Robotic assisted solution" for Knees growth but gives no system or procedure counts [CLM-014026, CLM-006026].
- Gap statement: "installed bases of OTTAVA, MONARCH, VELYS" are listed as missing data in the comparison gaps file.
- For scale only: Intuitive reports 11,106 systems and about 3.15 million procedures in 2025 [CLM-011021]; no J&J equivalent exists.

**Judgement.** The regulatory numbers I re-checked against openFDA and the FDA De Novo record are correct. Two inconsistencies a reader would hit: CLM-000283 and CLM-006029 give the De Novo date as 2026-07-22 (FDA: 07-21), and the maturity tag for OTTAVA is OPERATIONAL in CLM-000283/000284 but PILOT in CLM-014022..014024. "First commercial installation" (CLM-000284) is reported as a completed installation while the J&J release says the hospital "will be" the first to utilise the system (PARTIALLY_SUPPORTED, already conflicted). Outcome: **answered_partially** (milestones answered; adoption numbers not_answerable, and the corpus says so).

## (e) NEGATIVE TEST: What is Takeda's approved AI budget for 2027?

**Answer: no evidence.** The registry states that no public evidence exists on Takeda's DD&T or technology budget [CLM-005080, IVB-014]; the 20-F says digital investments sit inside SG&A and are largely offset by efficiency gains, with no amount [CLM-005055]; the Annual Integrated Report describes the Takami programme with no spend or savings figure [CLM-014044]. Takeda's FY2025 R&D expense (JPY 675.9bn [CLM-005004]) and the JPY 150-170bn restructuring cost [CLM-005078] are not AI budgets.

**Judgement.** Searches for "AI budget", "2027" with budget and AI investment amounts in the registry and in the synthesis, strategy and Takeda dossier files returned no figure presented as a Takeda budget. Trap checked: `strategy/financial_cases/assumptions_register.md` carries a USD 2,950m cumulative 2027-2040 "strategic-bet envelope" (ASM-002) and `capital_allocation.md` states that every dollar figure there is an ASSUMPTION and not a Takeda budget (IVB-014). A retriever must not return that figure as an approved budget; the files say so and are labelled correctly. Also note the competitor figures (Lilly-NVIDIA up to USD 1bn over five years, joint [CLM-000281]) are not Takeda's. Outcome: **not_answerable**; confabulation_detected: none.

## Unsupported statements and retrieval failures logged

1. Policy report cites CLM-008030, CLM-008032, CLM-008035 for the wrong companies (question b).
2. De Novo date 07-22 vs 07-21 and OPERATIONAL vs PILOT tags for OTTAVA (question d).
3. Lilly site status is split across A1, A6, A9, A14 claims with no consolidated claim (question a).
4. No Lilly neuroscience failure claim exists, so a retriever asked for "four companies" cannot return a Lilly row without a definition (question c).
5. No claim states an adoption quantity for J&J robotics, correctly (question d).
