# Wave 2/3 scorecard (A10-bis)

Date 2026-11-21. Fixed rubric (`research_methodology/evaluation_rubric.md`): 0 fails, 1 partial, 2 meets; ACCEPT needs no zero and a total of 12 or more out of 16. Ordinal scores only. Companion JSON: wave2_scorecard.json.

| Shard | Auth | Relev | Cover | Indep | Temporal | Contra | Trace | Signif | Total | Decision |
|---|---|---|---|---|---|---|---|---|---|---|
| A12_pipeline | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 13 | **ACCEPT** |
| A8_policy | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 9 | **REVISE** |
| A7_commercial | 1 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 11 | **REVISE** |
| A14_gapfill | 1 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 13 | **ACCEPT** |
| A11_strategy | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 12 | **ACCEPT** |

## A12_pipeline: ACCEPT (13/16)

- **source_authenticity** 2: 117 sources, 115 T1 regulator or registry records; 46 of 46 FDA approval dates and 43 of 43 ClinicalTrials.gov statuses re-checked live and match.
- **relevance** 2: Every source maps to approvals, CRLs, trials, publications or discontinuations in the four pipelines.
- **coverage** 2: FDA, openFDA, ClinicalTrials.gov, PubMed and 10-K discontinuations covered; CBER products and several CRLs listed as gaps.
- **independence_of_corroboration** 1: Regulator records are independent of the sponsors, but independent_corroboration is empty on all 153 claims and CRL or discontinuation claims rest on company filings alone.
- **temporal_accuracy** 2: Event dates are explicit and verified; the shard is the correct one where A3 (Juvmo) and A9 (Imaavy) carry announcement dates.
- **contradiction_handling** 1: The abemaciclib and EXCLAIM-2 tensions are described inside claims but none is in conflicts.jsonl.
- **traceability** 2: 153 of 153 claims have a locator and an ID; a reader can open each record.
- **significance** 1: Mostly an inventory of approvals and trial status; the interpretive claims on platform capability are PARTIALLY_SUPPORTED and not mechanism-level.
- **Required repairs:** (1) Record CLM-012136 and CLM-012137 tensions in conflicts.jsonl (proposed). (2) Fill independent_corroboration where an FDA record corroborates a company filing.

## A8_policy: REVISE (9/16)

- **source_authenticity** 1: 36 sources; the CMS, SEC, Federal Register and company-report numbers I opened all match, but 7 sources are metadata_only and 3 blocked (LDA, OpenSecrets, Senate pages).
- **relevance** 2: Prices, pledges, 340B and talc litigation, lobbying all bear on the four companies' policy exposure.
- **coverage** 1: Lobbying data is thin (LDA blocked), no Takeda pledge, no EU or Japan policy beyond NHI, court opinions not opened; gaps are listed.
- **independence_of_corroboration** 1: CMS T1 anchors the price claims, but pledges and litigation facts rest on company releases, 10-K text and T3 trade reports; independent_corroboration is empty.
- **temporal_accuracy** 1: 53 of 55 FACT claims have no event_date or reporting_period field although the statement text gives dates; no wrong date found in what I checked.
- **contradiction_handling** 1: Lilly lobbying 7.89m vs 8.43m and the April vs July Medicare date are caveated in text but not in conflicts.jsonl.
- **traceability** 1: Four IDs in the policy reports point at the wrong claim (CLM-008030, 008032 and 008035 in the pledge file; CLM-008021 in the IRA file); the claims themselves have the right numbers.
- **significance** 1: Documents what was announced and litigated; explicitly draws no causal link, so little mechanism.
- **Required repairs:** (1) Correct the four IDs. (2) Store primary records for the D.C. Circuit, Supreme Court and HRSA claims or downgrade them to PARTIALLY_SUPPORTED. (3) Add event_date to FACT claims. (4) Open LDA with a working client or keep the gap.

## A7_commercial: REVISE (11/16)

- **source_authenticity** 1: 26 sources, 22 retrieved; I re-opened the 10-K, CRS and trade-article figures and all match; 2 metadata_only and 2 blocked sources back four claims that are already not SUPPORTED.
- **relevance** 2: Pricing, access, payer, patient-program and launch-model evidence maps to the commercial sub-questions.
- **coverage** 1: Patient-support outcomes, decentralised trials, Takeda hub detail and Zepbound self-pay share are not found and are listed as gaps.
- **independence_of_corroboration** 1: All 59 claims carry single_interested_source=true, including FDA REMS, CRS and 10-K claims, so the flag does not discriminate; independent_corroboration is empty.
- **temporal_accuracy** 2: Fiscal periods, quarter and announcement dates are explicit; the 174% vs 175% Zepbound figure is explained by scope.
- **contradiction_handling** 1: The April vs July 2026 Medicare start is present in two claims and not recorded as a conflict.
- **traceability** 2: Every claim has a locator; CLM-007002 lists prices that its stored passage does not contain.
- **significance** 1: Shows payer and channel mechanisms with numbers, but outcome evidence (adherence, persistence) is explicitly absent.
- **Required repairs:** (1) Recompute single_interested_source per claim (59 of 59 is not credible). (2) Store full text for the Lilly 1 December 2025 release (CLM-007002, CLM-007000). (3) Record the Medicare date conflict.

## A14_gapfill: ACCEPT (13/16)

- **source_authenticity** 1: 50 sources; 7 metadata_only snippets and 2 blocked pages back claims that are marked PARTIALLY_SUPPORTED or INCONCLUSIVE; every deal-term, FDA and 10-K number I re-checked is correct.
- **relevance** 2: Fills the Lilly manufacturing, J&J device, AbbVie and Takeda deal and AI-operations gaps that wave 1 left.
- **coverage** 2: Manufacturing, FDA device records, deal terms, litigation, AI operations and ecosystem arms attempted; unreachable items stated (Strateos, JJDC, Takeda Ventures).
- **independence_of_corroboration** 1: 28 claims flagged single-interested but seven T2-only site announcements are not; Concord operating status rests on one trade article; independent_corroboration empty.
- **temporal_accuracy** 2: Dates are explicit and correct (OTTAVA De Novo 07-21 and receipt 12-18; Juvmo FDA 09-25 vs 09-28 announcement); manufacturing claims separate announced from operating.
- **contradiction_handling** 1: Juvmo dates are reconciled inside the claim, the OTTAVA correction against A6 is not recorded in conflicts.jsonl.
- **traceability** 2: 75 of 75 claims have locators; the 10-K and 20-F figures trace to line numbers.
- **significance** 2: Announced-versus-operating treatment of Lilly sites and the neuroscience and deal-term evidence gives usable problem-investment-outcome chains.
- **Required repairs:** (1) Flag CLM-014008..014012, 014015, 014020 as single_interested_source. (2) Retag CLM-014073 (DEMONSTRATED_OUTCOME), CLM-014043 (SCALED), CLM-014030 (PROTOTYPE). (3) Store the Lilly pages that returned 403 to me.

## A11_strategy: ACCEPT (12/16)

- **source_authenticity** 1: 17 sources, 13 retrieved; all 19 FACT claims I re-opened match NASA, SEC and Nobel primary text; 4 sources are snippets and their claims are PARTIALLY_SUPPORTED.
- **relevance** 2: Eight analogies (NVIDIA, SpaceX, Alphabet, Regeneron, TSMC, AWS, Intuitive, Roche) map to named Takeda design questions.
- **coverage** 2: The brief's analogy families are covered; Roche realised value and Google Health detail listed as gaps.
- **independence_of_corroboration** 1: Analogy numbers rest on T1 filings and NASA, which are independent of Takeda, but the CUDA cost claim is one interested speaker and no analogy has a second independent test.
- **temporal_accuracy** 2: Fiscal years and dates are explicit in every analogy number.
- **contradiction_handling** 1: Developer count 7.5m vs 11m is noted in text, not in conflicts.jsonl.
- **traceability** 1: Domain tables cite HYPOTHESIS claims for figures that sit in FACT claims (42%, 84%); seven recommendations are labelled EVIDENCE_BACKED but registered PARTIALLY_SUPPORTED.
- **significance** 2: Each analogy follows mechanism, evidence strength, prediction, where it breaks, hypothesis, which is the rubric's chain, and is labelled HYPOTHESIS.
- **Required repairs:** (1) Relabel or upgrade the seven EVIDENCE_BACKED recommendations. (2) Cite fact claims in table cells. (3) Reword CLM-011045 and CLM-011066.

## Synthesis layer verdict: DECISION_GRADE_WITH_CONDITIONS

master_comparison.md is decision-grade for the financial, loss-of-exclusivity and capital-deployment comparisons, which are anchored in audited filings and regulator records and state their bases. It is not decision-grade for a ranking of ecosystems, AI investments or partnership durability, and it says so itself. Citation hygiene is good (no dangling IDs, no invented figures) but about 17 specific defects must be fixed before external use.

**Supported comparisons**

- Why Lilly grows (sections 1 and 11): revenue, margin, capex and tirzepatide share are filing-based
- How AbbVie absorbed Humira (section 3): sales, successor products, contracting and patents are traced
- J&J pharma and MedTech: segment margins and the unevidenced synergy
- Capital deployment table (section 11) with basis labels, after the AbbVie IPR&D basis note

**Unsupported or hypothesis-only**

- Who has the most defensible technology ecosystem (section 5): HYPOTHESIS, no outcome evidence for any company
- Which AI investments are operationally meaningful (section 6): 'operational' means launched, no effect on cost, cycle time or revenue is shown
- Partnership durability (section 8): no option from the window has produced an approved product; value comparisons across bases are invalid
- Positions in 2035 (section 10): hypothesis by design
- Any ranking of R&D productivity (section 4): the file itself calls it invalid
- Takeda five-year timeline: FY2021 and Nov 2021 to Mar 2022 events remain thin

**Defects to fix before use**

- Debt basis values 58,941 and 39,438 not in any claim; CLM-003042 and CLM-000066..000070 not relabelled
- 'About 11 months' of Zepbound exclusion should be 15 months (1 Jul 2025 to 1 Oct 2026)
- OTTAVA De Novo date 07-22 should be 07-21; Imaavy 04-30 should be 04-29; Juvmo 09-28 is the announcement date
- The 29 and 18 AI maturity counts are not in the cited claim
- Four mis-cited IDs in the policy files
- EVIDENCE_BACKED label on seven PARTIALLY_SUPPORTED recommendations, and Recommendation 1.1 overstated

## Cross-shard observations

- independent_corroboration is empty on all 442 claims in these five shards, so the Independence axis cannot reach 2 on any shard until the field is filled; this repeats the wave 1 finding.
- Conflicts: none of the tensions found in these shards sits in conflicts.jsonl; 13 proposals are filed in conflicts_proposed_A10b.jsonl.