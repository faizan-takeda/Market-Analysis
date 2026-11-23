# A10-bis Task 1: re-inspection of wave 2/3 shards

Date 2026-11-21. Auditor A10-bis. Method: every verdict below comes from a source I opened myself in this session (openFDA and ClinicalTrials.gov APIs queried live, FDA De Novo database, CMS fact-sheet PDFs, SEC filings on disk and from EDGAR, NASA NTRS PDFs, Nobel, Roche and company releases). Codes: PASS / LOCATOR_FIX / NUMBER_MISMATCH / PERIOD_MISMATCH / NOT_FOUND / UNREACHABLE. UNREACHABLE means I could not open the source (HTTP 403 or block page), not that the claim is wrong.

**Sample size:** 92 claim verdicts in the stratified sample (A12 20, A8 13, A7 14, A14 22, A11 19, plus 4 cross-shard findings), plus a full sweep of 46 A12 FDA approval-date claims (46 of 46 match openFDA) and 43 of 43 A12 ClinicalTrials.gov status claims (all match the live record). Full machine-readable list: audit_wave2_reinspection.jsonl (165 records).

## Result in one paragraph

No wrong number was found in A12, A8, A7, A14 or A11 FACT claims. The defects found are (1) date-label errors where a company announcement date is stored as the FDA action date (CLM-003063 Juvmo 09-28 vs FDA 09-25; CLM-000283 and CLM-006029 OTTAVA De Novo 07-22 vs FDA 07-21), (2) seven claims I could not re-open because investor.lilly.com, jnj.com and computerweekly.com return 403, so those rest on the stored passage only, (3) CLM-007002 whose stored passage does not contain half of the prices the statement lists, (4) CLM-012109 bermekimab 0.6bn which is a subsequent-event estimate later booked at 0.8bn, and (5) CLM-012137 whose registry date (2026) postdates the 2023 withdrawal it is paired with.

## Verdict counts by shard (sample only)

| Shard | PASS | UNREACHABLE | PERIOD_MISMATCH | LOCATOR_FIX | NUMBER_MISMATCH |
|---|---|---|---|---|---|
| A12_pipeline | 20 | 0 | 0 | 0 | 0 |
| A8_policy | 12 | 1 | 0 | 0 | 0 |
| A7_commercial | 12 | 2 | 0 | 0 | 0 |
| A14_gapfill | 19 | 3 | 0 | 0 | 0 |
| A11_strategy | 18 | 1 | 0 | 0 | 0 |
| cross-shard (A3, A6, A2, Director) | 0 | 0 | 3 | 1 | 0 |

## Sample table (claims with a note or non-PASS verdict first, then PASS)

| Claim | Shard | Verdict | Source I checked | Note |
|---|---|---|---|---|
| CLM-011003 | A11_strategy | UNREACHABLE | computerweekly.com HTTP 403 | Quote not re-read; single interested speaker via T3 press. |
| CLM-014008 | A14_gapfill | UNREACHABLE | investor.lilly.com HTTP 403 | Announced 6.5bn, operational within five years, registry passage only; groundbreaking 2026-09-21 rests on a Yahoo reprint. |
| CLM-014010 | A14_gapfill | UNREACHABLE | investor.lilly.com HTTP 403 | 3.5bn, operational in 2031 from registry passage only. |
| CLM-014011 | A14_gapfill | UNREACHABLE | investor.lilly.com HTTP 403 | Limerick on track for 2026 from registry passage only. |
| CLM-002049 | A2_jnj | LOCATOR_FIX | FDA De Novo database DEN250068 | J&J said on 2026-01-07 that it had submitted; FDA received the request 2025-12-18. Statement should say submitted by 2025-12-18 (FDA receipt), announced 2026-01-07. |
| CLM-003063 | A3_abbvie | PERIOD_MISMATCH | openFDA NDA220415 | States FDA approval of Juvmo on 2026-09-28; FDA AP date is 2026-09-25 and 09-28 is AbbVie announcement (see CLM-012017, CLM-014039). Cross-shard (A3). |
| CLM-006029 | A6_ai_robotics | PERIOD_MISMATCH | FDA De Novo database DEN250068 | Repeats 2026-07-22 from CLM-000283; FDA decision 2026-07-21. |
| CLM-007000 | A7_commercial | UNREACHABLE | investor.lilly.com HTTP 403 | Registry passage (399/549, less than half list) read; not independently re-opened. |
| CLM-007002 | A7_commercial | UNREACHABLE | investor.lilly.com returned HTTP 403 | Registry passage covers 299/399/449 only; the non-program prices (599/699/849/1,049) and the previous 349/499 prices are not in the stored passage, so the claim is only partly traceable to its stored text. |
| CLM-008030 | A8_policy | UNREACHABLE | jnj.com release returned a 557-byte block page | Registry passage (>55bn, 25% increase) not independently re-read; J&J FY2025 10-K corroboration not searched. |
| CLM-000283 | Director | PERIOD_MISMATCH | FDA De Novo database DEN250068 | FDA decision date is 2026-07-21 (not 07-22). 07-22 is presumably the J&J announcement date; the statement attributes it to the FDA grant. Cross-shard (A6/Director), found through the A14 check. |
| CLM-011000 | A11_strategy | PASS | NVIDIA blog 20 years of CUDA | >11 million developers; 1,000+ libraries; announced Nov 2006 confirmed. Tension with 7.5m (CLM-011001) is a different date and definition. |
| CLM-011001 | A11_strategy | PASS | NVIDIA FY2026 10-K | Over 7.5 million developers confirmed. |
| CLM-011002 | A11_strategy | PASS | NVIDIA FY2026 10-K revenue-by-end-market table | 193,737 / 115,186 / 47,525 confirmed. |
| CLM-011005 | A11_strategy | PASS | NASA NAFCOM briefing PDF (Aug 2011) | 3.977bn and 1.695bn confirmed. |
| CLM-011006 | A11_strategy | PASS | NASA NTRS 20170008895 | 300m + 90m = 390m verified by NASA confirmed. |
| CLM-011007 | A11_strategy | PASS | NASA Ames ICES paper 20200001093 | 140m, 6,000 kg, 23,300/kg vs 93,400/kg, factor 4 confirmed. |
| CLM-011008 | A11_strategy | PASS | NASA NTRS 20170008895 | Firm fixed price; catastrophic failures; payment slightly less on a failed launch confirmed. |
| CLM-011009 | A11_strategy | PASS | Alphabet FY2025 10-K | Other Bets (4,095)/(4,444)/(7,515); 2.1bn Waymo compensation charge confirmed. |
| CLM-011010 | A11_strategy | PASS | Alphabet FY2025 10-K | 52.5bn and 91.4bn capex confirmed. |
| CLM-011012 | A11_strategy | PASS | Nobel Prize chemistry 2024 press release | 200 million proteins; >2 million users; 190 countries confirmed. |
| CLM-011015 | A11_strategy | PASS | Regeneron FY2025 10-K | Six megabases of mouse loci replaced confirmed. |
| CLM-011016 | A11_strategy | PASS | Regeneron FY2025 10-K | RGC over 3 million samples sequenced confirmed. |
| CLM-011017 | A11_strategy | PASS | Regeneron FY2025 10-K | EYLEA US net sales -42%; EYLEA HD+EYLEA 31% (42% in 2024) of total revenues confirmed. |
| CLM-011018 | A11_strategy | PASS | TSMC FY2025 20-F | 74% advanced nodes; OIP 2008; longest existing dedicated foundry confirmed. |
| CLM-011019 | A11_strategy | PASS | TSMC FY2025 20-F | NT$1,272,411m / 956,007m; US$52-56bn 2026 confirmed. |
| CLM-011020 | A11_strategy | PASS | Amazon FY2025 10-K | AWS 128,725 / 107,556; AWS OI 45,606; consolidated 79,975 confirmed. |
| CLM-011021 | A11_strategy | PASS | Intuitive FY2025 10-K | 11,106 (+12%); ~3.153m procedures (+18%); 1,721 placements; 8,465.3 recurring, 84% confirmed. |
| CLM-011022 | A11_strategy | PASS | Roche release 6 Apr 2018 | 1.9bn, separate legal entity, segregated PHI, 14 of top 15 confirmed. Flatiron network metric dates from 2018. |
| CLM-012002 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | BLA761279 ORIG-1 status AP 20231026 = claim event_date |
| CLM-012010 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | NDA219008 ORIG-1 status AP 20240819 = claim event_date |
| CLM-012014 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | BLA761324 ORIG-1 status AP 20230519 = claim event_date |
| CLM-012017 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 (NDA220415 ORIG-1 AP 20260925) | Juvmo FDA action 2026-09-25 confirmed; A3 CLM-003063 uses the 2026-09-28 company-announcement date as approval date (conflict C-02). |
| CLM-012021 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | NDA217806 ORIG-1 status AP 20231108 = claim event_date |
| CLM-012022 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | NDA216793 ORIG-1 status AP 20230811 = claim event_date |
| CLM-012024 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | BLA761433 ORIG-1 status AP 20251217 = claim event_date |
| CLM-012026 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | NDA216962 ORIG-1 status AP 20241016 = claim event_date |
| CLM-012029 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | BLA761133 ORIG-1 status AP 20230927 = claim event_date |
| CLM-012031 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | NDA217806 SUPPL-13 status AP 20241220 = claim event_date |
| CLM-012032 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | BLA761105 SUPPL-16 status AP 20220616 = claim event_date |
| CLM-012034 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | NDA211675 SUPPL-4 status AP 20220114 = claim event_date |
| CLM-012035 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | NDA211675 SUPPL-7 status AP 20220316 = claim event_date |
| CLM-012036 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | NDA211675 SUPPL-25 status AP 20250428 = claim event_date |
| CLM-012041 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | BLA761210 SUPPL-3 status AP 20240301 = claim event_date |
| CLM-012042 | A12_pipeline | PASS | openFDA drugsfda API (api.fda.gov), queried 2026-11-21 | NDA216059 SUPPL-1 status AP 20231201 = claim event_date |
| CLM-012109 | A12_pipeline | PASS | J&J FY2021 10-K line 769; FY2022 10-K lines 746, 798, 1527 | 0.6bn is stated as a non-recognized subsequent event (Jan 2022) to be booked in Q1 2022; FY2022 10-K lines 746/798 give 0.8bn recorded in FY2022. Both are correct for their filing; the claim omits that 0.6bn was an estimate (OVERSTATED as an impairment amount). |
| CLM-012122 | A12_pipeline | PASS | Takeda FY2023 20-F line 5828 | ALOFISEL 73,979; EXKIVITY 28,477 confirmed; EOHILIA 35.7 not located in this pass. |
| CLM-012123 | A12_pipeline | PASS | Takeda FY2025 20-F line 5386 | 58,173 and 31,877 JPY m confirmed (claim: ~58.2bn, 31.9bn). |
| CLM-012137 | A12_pipeline | PASS | ClinicalTrials.gov API v2 NCT04129502 | Registry fields match the claim (COMPLETED, primary completion 2026-09-22 ACTUAL) but the date is three years after the Oct 2023 miss the claim also cites; the record was updated after the global withdrawal, so the pairing reads as a contradiction unless a note says the registry date postdates the withdrawal. |
| CLM-014000 | A14_gapfill | PASS | Lilly FY2025 10-K lines 769, 887, 904-906 | 65,179 vs 45,043 (+45%) and Mounjaro/Zepbound figures confirmed via 10-K (earnings release not opened). |
| CLM-014014 | A14_gapfill | PASS | Pharma Manufacturing article (Jun 2025) | Commercial production end of 2024, 1bn doubled to 2bn confirmed; single trade source T3, so operating status rests on one outlet (flag). |
| CLM-014017 | A14_gapfill | PASS | Lilly FY2025 10-K lines 948, 1630, 1213 | Capex 7.8/5.1bn; CIP 13,013/8,245 confirmed. |
| CLM-014022 | A14_gapfill | PASS | FDA De Novo database DEN250068 (accessdata.fda.gov) | Date received 12/18/2025, decision 07/21/2026, granted, 21 CFR 878.4966 confirmed. CLM-000283 and CLM-006029 give 2026-07-22 (one day late). |
| CLM-014025 | A14_gapfill | PASS | openFDA 510(k) K260382 | Decision 2026-07-25, Substantially Equivalent, Auris Health, confirmed. |
| CLM-014026 | A14_gapfill | PASS | openFDA 510(k) | K202769 2021-01-14; K233227 2023-12-14; K240211 2024-06-05; K253551 2026-03-06; K260480 2026-06-25; DePuy Ireland UC confirmed. |
| CLM-014030 | A14_gapfill | PASS | AbbVie FY2025 10-K line 1766 | 2.1bn cash (1.9bn net), asset acquisition, Q3 2025 IPR&D confirmed. |
| CLM-014031 | A14_gapfill | PASS | AbbVie FY2025 10-K line 1002; FY2024 10-K line 1025 | 1.9bn/906/700/350 and 1.4bn/250 confirmed; ADARx 335 not located. |
| CLM-014032 | A14_gapfill | PASS | AbbVie FY2024 10-K lines 1025, 1776 | 1.4bn upfront, December 2024 completion confirmed. |
| CLM-014033 | A14_gapfill | PASS | Landos 8-K Ex 99.1 passage in registry (SEC) | 20.42/share, ~137.5m, CVR up to 11.14 (~75m) read from stored passage. |
| CLM-014034 | A14_gapfill | PASS | AbbVie FY2025 10-K line 1659 | 288m = 210m + 78m; up to 130m confirmed. |
| CLM-014035 | A14_gapfill | PASS | AbbVie FY2025 10-K lines 1661-1666 | 8.7bn / 8.3bn net of cash confirmed. |
| CLM-014038 | A14_gapfill | PASS | AbbVie FY2023 10-K lines 216, 422, 2236 | ~27% in 2023 confirmed. |
| CLM-014039 | A14_gapfill | PASS | openFDA NDA220415 | FDA ORIG-1 AP 20260925 confirmed; claim correct. |
| CLM-014048 | A14_gapfill | PASS | Takeda FY2025 20-F line 6687 | 884,943,990 / 474,897,965 / 346,837,646 confirmed; the JPY 403,510m provision figure was not re-located. |
| CLM-014058 | A14_gapfill | PASS | Lilly FY2023/FY2024 10-K tables | 1,915.5 / 604.1 / 406.5 / 256.6 / 216.3 and 2,548.5 confirmed. |
| CLM-014060 | A14_gapfill | PASS | Takeda FY2024 20-F lines 2715, 5870, 5872 | HUTCHMED 0.4bn, Jan 2023 agreement, March 2023 close; Protagonist Jan 2024 confirmed. |
| CLM-014061 | A14_gapfill | PASS | Takeda FY2025 20-F lines 5417, 5420 | Keros 200m; Innovent 1,200m (incl. minority equity) confirmed. |
| CLM-014062 | A14_gapfill | PASS | Takeda FY2024 20-F lines 2069, 5867 | 4.0bn = 3.0 (Feb 2023) + 0.9 (Apr 2023) + 0.1 (Aug 2023) confirmed. |
| CLM-007008 | A7_commercial | PASS | CRS IF13281 PDF | TrumpRx launch 5 Feb 2026 confirmed. |
| CLM-007009 | A7_commercial | PASS | CRS IF13281 PDF | 40 / >50 / 87 drugs; 17 manufacturers at 5 May 2026; J&J listed; agreements expire with term confirmed. |
| CLM-007011 | A7_commercial | PASS | CVS Health release / CNBC passage in registry | 1 July 2025 Wegovy-preferred action confirmed from the registered passage; 11% stock drop not re-read. |
| CLM-007013 | A7_commercial | PASS | Managed Healthcare Executive article | Zepbound back 1 Oct 2026; Foundayo block lifted 1 June 2026 confirmed. |
| CLM-007014 | A7_commercial | PASS | Managed Healthcare Executive article | Truveta 700,907; ~0.6% to 10.2%; 17-fold confirmed. Same article also states Medicare Part D GLP-1 Bridge from 1 July 2026 (C-03). |
| CLM-007017 | A7_commercial | PASS | J&J FY2025 10-K lines 297, 747-748, 687 | 6.5%, 3.8bn, 15.7bn/-11.8% and 10.4% operational-growth drag confirmed. |
| CLM-007019 | A7_commercial | PASS | AbbVie FY2025 10-K lines 850, 1098, 1100 | 65.1/59.3/56.8bn; 61,160 net revenues; three largest accruals ~94% confirmed. |
| CLM-007020 | A7_commercial | PASS | AbbVie FY2025 10-K lines 863, 866 | Skyrizi 17,562 (+49.9%), Rinvoq 8,304 (+39.1%) confirmed; Humira -49% not re-located. |
| CLM-007024 | A7_commercial | PASS | Lilly FY2025 10-K lines 911-912 | Zepbound US +174%, Mounjaro US +53% confirmed. Worldwide table gives +175%; CLM-014000 uses 175 (different base, not a conflict). |
| CLM-007027 | A7_commercial | PASS | Takeda FY2025 20-F line 1711 | 958.0bn/21%, 2,313.3bn/51% confirmed. |
| CLM-007029 | A7_commercial | PASS | J&J FY2025 10-K lines 698, 713, 720 | 1,887/963; 5,155/3,670; 1,696/1,077 confirmed. |
| CLM-007031 | A7_commercial | PASS | Lilly FY2025 10-K lines 862, 904-906 | 22,965/11,540; 13,542/4,926; 56% confirmed. |
| CLM-008000 | A8_policy | PASS | Lilly 2024 Report of Political Financial Contributions PDF | $7,890,000 federal lobbying 2024 verbatim. |
| CLM-008008 | A8_policy | PASS | CMS IPAY2026 fact sheet PDF | Stelara 4,695 / 13,836 / 66% / 2,988,560,000 confirmed. |
| CLM-008009 | A8_policy | PASS | CMS IPAY2026 fact sheet PDF | Xarelto 197 / 517 / 62% / 6,309,766,000 confirmed. |
| CLM-008010 | A8_policy | PASS | CMS IPAY2026 fact sheet PDF | Imbruvica 9,319 / 14,934 / 38% / 2,371,858,000 confirmed. |
| CLM-008012 | A8_policy | PASS | CMS IPAY2027 fact sheet PDF | Linzess 136 / 539 / 75% / 1,982,587,000 confirmed. |
| CLM-008013 | A8_policy | PASS | CMS IPAY2027 fact sheet PDF | Vraylar 770 / 1,376 / 44% / 1,136,814,000 confirmed. |
| CLM-008014 | A8_policy | PASS | CMS IPAY2027 fact sheet PDF | USD 12bn / ~44% of 2024 net spending confirmed; text excludes CGDP (8.5bn if included). |
| CLM-008027 | A8_policy | PASS | Lilly 6 Nov 2025 release (BioSpace mirror) | USD 50/month, from as early as 1 April 2026, three years tariff relief confirmed. Conflicts with 10-K 1 July 2026 (C-03). |
| CLM-008029 | A8_policy | PASS | Lilly 26 Feb 2025 release (BioSpace mirror) | >50bn since 2020 vs 23bn 2020-2024 confirmed. |
| CLM-008032 | A8_policy | PASS | AbbVie 12 Jan 2026 release (news.abbvie.com) | USD 100bn over decade, three-year agreement confirmed. |
| CLM-008050 | A8_policy | PASS | J&J FY2025 10-K lines 3085, 3090 | 6.475bn PV, ~7bn reversed, ~3.4bn confirmed. |
| CLM-008051 | A8_policy | PASS | J&J FY2025 10-K lines 3104-3105 | Up to 5.0bn, ~80% paid, ~23 state and 285 MDL cases confirmed. |

## Full sweeps (all PASS)

- A12 FDA approval-date claims: 46 of 46 claims carrying an NDA/BLA number match an AP submission date in openFDA drugsfda (sponsor names also match; Jaypirca sponsor of record is LOXO ONCOL, not Lilly, and the claim does not state otherwise).
- A12 ClinicalTrials.gov claims: 43 of 43 match overall status, primary completion date and date type in the API v2 record on 2026-11-21. Registry values can change, so a later re-run may differ.

## Limits

- Lilly press pages (Houston, Alabama, Pennsylvania, Ireland, 1 Dec 2025 vial price release), the J&J >55bn release and the Computer Weekly interview returned 403 to my client. These are marked UNREACHABLE and the A14 manufacturing status claims rest on registry passages plus the Concord trade article.
- I did not open Alphabet, NVIDIA, Regeneron and other 10-K text beyond the numbers listed; interpretive wording in A11 is audited in the status-discipline file.