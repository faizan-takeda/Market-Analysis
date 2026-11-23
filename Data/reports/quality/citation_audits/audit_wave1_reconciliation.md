# A10 audit: numeric reconciliation (Task 2)

Date 2026-11-21. Machine-readable proposals: `New_mediciine/evidence_library/conflicts_proposed_A10.jsonl` (14 records).

## (a) RUN-0001 XBRL claims versus A4_financial shard
All A4 claims whose metric has an XBRL counterpart (revenue, R&D, net income, operating cash flow, capex, pre-tax income, operating income, acquisitions cash, acquired IPR&D, IPR&D payments) were joined to RUN-0001 by company, concept and fiscal year and compared in USD m / JPY bn.

- 151 pairs compared; 146 agree to rounding (Lilly 45/45, J&J 37/37 (incl. FY2021 52-week-end 2022-01-02 mapped to FY2021), Takeda 24/24, AbbVie 40/45).
- 5 differences, all AbbVie net income and all definitional: RUN-0001 uses consolidated net earnings (11,549 / 11,845 / 4,873 / 4,286 / 4,233), A4 uses net earnings attributable to AbbVie (11,542 / 11,836 / 4,863 / 4,278 / 4,226). Verified in the 10-Ks (FY2021 lines 1178-1180; FY2025 lines 1306-1308). Neither is wrong; each needs a basis note.
- A4 metrics with no XBRL counterpart (dividends paid, buybacks, ctgov counts) were not compared. A4 holds four Takeda fiscal years for several metrics where RUN-0001 holds four as well, so no gap.
- No restatement was found between the original and later filings for these metrics. Two classification changes were found: Lilly FY2021 acquired IPR&D 874.9 (FY2021 10-K) versus 970.1 (FY2022 10-K, line item widened to include development milestones); J&J FY2021 segment recast (Pharmaceutical 52,080 -> 51,680; Consumer Health 14,635 -> 15,035).
- **Error found in RUN-0001:** the 10 AbbVie and J&J "long-term debt (noncurrent)" claims (CLM-000066..000070, CLM-000128..000132) use tag `LongTermDebt`, which includes the current portion. AbbVie FY2025: 64,503 total vs 58,941 non-current; J&J FY2025: 41,438 subtotal vs 39,438 non-current. Lilly uses `LongTermDebtNoncurrent` and is correct. The label error propagates to CLM-003042 and the AbbVie business model.

## (b) Narrative numbers in dossiers versus the claims they cite
Reviewed: four `master_report.md` files and the three existing `business/business_model.md` files (Lilly, J&J, AbbVie). **Takeda has no `business/business_model.md`** (the directory is empty); its master report does not link one.

| Dossier statement | Cited claim(s) | Result |
|---|---|---|
| Lilly revenue 28.3bn -> 65.2bn; tirzepatide 56% | CLM-000133/137, CLM-000242, CLM-001003 | Match; shares recomputed (15.6 / 36.6 / 56.0%). |
| Lilly net income 5.6 -> 20.6bn; op. cash flow 7.3 -> 16.8bn; capex 1.3 -> 7.8bn; LT debt 15.3 -> 40.9bn | CLM-000153/157/163/167/168/172/198/202 | Match (Lilly debt is the non-current line, filing lines 1003 and 1111). |
| Lilly FY2023 growth included ~2.0bn one-time rights sales | CLM-001002 | Match (579.0m Baqsimi + ~1.45bn olanzapine). |
| AbbVie Humira 21.2bn (2022) -> 4.5bn (2025); Skyrizi+Rinvoq 7.7 -> 25.9bn | CLM-003002, CLM-003014 | Match; recomputed from FY2023 and FY2025 10-K tables. |
| AbbVie Skyrizi+Humira+Rinvoq about 47% of 2024 revenue | CLM-003046 | Match (26,682 / 56,334 = 47.4%). |
| AbbVie operating margin 31.9% -> 16.2% -> 24.6% | CLM-003039 | Match. |
| AbbVie debt series (business_model L12) | CLM-003042 | **Mismatch of label**: figures are total debt incl. current portion, not non-current. |
| AbbVie "ImmunoGen (2024-02-12, 10.1bn)" (master L45) | CLM-003053 | 10.1bn is the announced total value; consideration transferred is 9.8bn (9.2bn net of cash). State both. |
| AbbVie "buy late-stage assets (18.5bn cash in 2024)" (Card 3) | CLM-003086 | 18.5bn = 9.8 + 8.7 consideration transferred; net of cash acquired 17.5bn. Not strictly "cash paid". |
| AbbVie acquired IPR&D 0.6bn (2023) -> 4.8bn (2025) | CLM-003075/3045 | Match (582 / 2,627 / 4,808, FY2025 10-K line 999). |
| J&J Innovation Medicine 60.4bn, MedTech 33.8bn; U.S. 53.8bn (+6.9%); intl 40.4bn | CLM-000253, CLM-002033 | Match. |
| J&J "Tremfya offset about one third of 2025 Stelara loss" | CLM-000256, CLM-000254 | Match (+1,485 vs -4,283 = 35%). |
| J&J MedTech ~ one third of IM margin on ~36% of sales | CLM-002004 | Match (12.2/36.9 = 33%; 33.8/94.2 = 35.9%). |
| J&J "OTTAVA ... first install 2026-11-19"; "about 24 months from IDE to first commercial install" | CLM-000284, CLM-002049 | Source says Memorial Hermann "will be the first hospital to install"; completed install not shown; date not in page text. |
| J&J debt 47.9bn (FY2025) | CLM-002014 | Consistent with 39,438 + 8,495 loans and notes payable = 47,933; differs from the XBRL claim CLM-000132 (41,438 labelled non-current). Three bases are in circulation. |
| Takeda revenue FY2021-25 3,569.0 ... 4,505.7; R&D 526.1 ... 675.9; capex 496.7/319.4/426.9; dividends 200/204 | CLM-005000/5004/5006/5007 | Match 20-F text. |
| Takeda H1 FY2026 revenue 2,407.0, core OP guidance 1,190 | CLM-005011 | Match (re-extracted PDF). |
| Takeda leverage 2.6x/3.1x/2.8x/2.6x | CLM-005005 | UNVERIFIED (value not located by grep in the 20-F text; table not read). |
| Takeda restructuring 150 / 160 / 170bn | CLM-005059/5078 | Reconciled: 150 (25-Mar-2026 estimate), 170.0 (original FY2026 forecast), 160.0 (revised forecast, Oct 2026). |

## (c) Known conflicts flagged by agents
| Conflict | A10 finding | Proposal |
|---|---|---|
| Morphic USD 3.2bn (Reuters) vs 2.55bn audited | Different measures. 10-K: IPR&D charge 2,548.5; 2024 cash paid for acquired IPR&D 3.35bn "primarily Morphic". 3.2bn headline is not in the filing text I searched. | Keep both, label measures. |
| Emraclidine impairment 4.5bn Q4-2024 | Confirmed 4.5bn, Q4 2024, fair value 2.4bn (FY2024 10-K lines 1010, 1721, 1878). The "~3.5bn in 2025" premise is contradicted. Total 2024 intangible impairment in cash flow is 4,476. | No conflict. |
| Lilly FY2021 IPR&D 874.9 vs 970.1 | Resolved: line item definition changed in FY2022 10-K (adds development milestones; +95.2). | Upgrade CLM-009022 to SUPPORTED with note. |
| Takeda restructuring 150/160/170bn | Resolved as a dated series, 170 is Takeda's own original forecast. | Edit CLM-005078. |
| Takeda cell-therapy impairment 58.0bn vs 58.2bn | Not a conflict: 58.0bn was the Oct-2025 expectation, 58.2bn is the amount recognised in the FY2025 20-F (lines 537, 1920). | Cite both with dates. |
| AbbVie Ventures 2009 vs 2015 | UNRESOLVED. Impact-report PDF is fetchable but text could not be extracted by A10; the web page returned 404 on the two URLs tried. | Keep INCONCLUSIVE; re-fetch with `--store-raw`. |
| Strateos start 2017 vs 2020 | 2017 is the Life Sciences Studio start (BiopharmaTrend). "Strateos" and "2020" are not in any opened source. | CLM-006017 NOT_FOUND_IN_SOURCE. |
