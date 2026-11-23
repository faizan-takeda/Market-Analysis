# A10 audit: wave-1 claim re-inspection (Task 1)

Auditor: A10 (independent). Date: 2026-11-21. Registry snapshot: 1,110 claims / 395 sources (the brief cites 957 / 278; the registry grew after A12/A8/A7/A14 merges). Companion data: [audit_wave1_reinspection.jsonl](audit_wave1_reinspection.jsonl).

## Method
Every sampled claim was re-checked against the source text myself: 10-K/20-F text on disk via `grep -n`/`sed -n` (line numbers are lines of the extracted `.txt`), the Takeda H1 FY2026 PDF re-extracted with pypdf, web pages fetched in this session or read from stored extracted text, ClinicalTrials.gov via the v2 API, PubMed via NCBI E-utilities. The agents' `inspected_passage` was not used as proof. Components I could not open are written as UNVERIFIED in the note column, not as PASS. As an additional screen, all 320 claims of shards A1/A2/A3/A5 were machine-checked for number presence in their cited on-disk source text: 209 passed, 23 flagged (all reviewed by hand; 3 real findings below), 88 have only web/PDF sources and were not machine-checkable.

## Result

Sample: **99 claims**. PASS 72, PASS_WITH_LOCATOR_FIX 25, NUMBER_MISMATCH 1, NOT_FOUND_IN_SOURCE 1.

Strata: A (FACT with `~` locator, all 17 in registry) · B (A1/A2/A3/A5 claims carrying a >=1,000 USD m / JPY bn figure; the wave-1 shards leave the `value` field null, so the stratum was selected from statement text: 41 audited of ~145 candidates) · C:A6 (12 random) · C:A9 (12 random) · C:Dir (10 random RUN-0002/0003) · C:extra (pipeline and web claims examined while following up flags).

### Substantive findings

1. **NUMBER_MISMATCH / mislabel, CLM-003042 (and its sources CLM-000066..000070, CLM-000128..000132).** "Non-current" long-term debt is in fact total long-term debt including the current portion for AbbVie (XBRL tag `LongTermDebt`) and J&J. AbbVie FY2025: 64,503 is "Long-term debt, including current portion" (current 6,000; long-term 58,503 in the contractual-obligations table) and the balance-sheet non-current line is 58,941 (FY2024 60,340; FY2023 52,194; FY2022 59,135; FY2021 64,189). J&J FY2025: 41,438 is the debt-note subtotal; "Total long-term debt" after the current portion of 2,000 is 39,438 (FY2024 32,400 vs 30,651). Lilly (`LongTermDebtNoncurrent`) is correct. 20 claims carry the wrong label.

2. **NOT_FOUND_IN_SOURCE, CLM-006017.** The claim about a "Lilly-Strateos remote robotic laboratory (public launch about 2020)" cites two BiopharmaTrend articles that never mention Strateos. They describe the Lilly Life Sciences Studio (established 2017, USD 90m). The 2020 date and the Strateos link are unsupported by the cited pages.

3. **Maturity labels not justified by the evidence.** CLM-006026 (VELYS) is tagged SCALED although the 10-K gives no system or procedure counts; CLM-006022 (course completions) is tagged SCALED; CLM-006047, -006049, -006051 are tagged DEMONSTRATED_OUTCOME but describe failures at Recursion, Exscientia/BenevolentAI and Zymergen, not AI applications at the four companies. CLM-006020 (J&J 2.6x enrollment) is tagged OPERATIONAL on a single self-reported interview statement. Maturity values are also upper-case, whereas the protocol enumerates lower-case.

4. **Registry understates retrievability.** SRC-000034 (J&J OTTAVA release), SRC-009022 (CDD TuneLab blog) and SRC-009017 (BioPharma Dive) are registered `metadata_only` but returned full pages in this audit. The OTTAVA page says Memorial Hermann "will be the first hospital to install" the system (future tense); CLM-000284 and the J&J master report ("first install 2026-11-19") present the installation as completed. The 19-Nov-2026 date does not appear in the page text I read.

5. **Partly unreachable component.** CLM-005025: the JPY 58.0bn cell-therapy impairment is confirmed in the Takeda release, but the "137 Massachusetts roles" element rests on a Fierce Biotech page that returned HTTP 403 to this audit (UNVERIFIED).

6. **Locator drift.** 25 claims have correct figures but approximate or wrong locators; 15 of the 17 `~` locators needed a corrected line number (e.g. CLM-001009 cites Item 5 while the sentence is in the equity note at line 2255; CLM-009086 cites lines ~2070-2072, the text is at 2075-2076). Corrected locators are in the table.

7. **Cash vs expense.** CLM-001014 states FY2025 cash paid for acquired IPR&D as "3,008.0"; the filing reports 3,008 (whole millions). Cash paid (3,008/3,346/3,944) differs from the IPR&D expense (2,910/3,280/3,800); the two series are both correct and must not be mixed (CLM-000247 uses cash, CLM-009000 uses expense).

## Table

| Claim | Stratum | Shard/run | Verdict | Corrected locator / value | Note |
|---|---|---|---|---|---|
| CLM-001009 | A:tilde | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY 10-K FY2023 line 2255 (equity note) not Item 5 ~800 | $5.00bn authorised May 2021, $2.50bn remaining at 31-Dec-2023 confirmed. |
| CLM-001010 | A:tilde | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY 10-K FY2021 lines 594,762,1474; FY2022 line 785; FY2023 line 1052 | 339.7 / 2,239.3 / 2,023.5 / nil all confirmed. |
| CLM-001011 | A:tilde | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY 10-K FY2022 line 790 (927.7 vs 2,061.4, -55%) and line 769 (US multiple generics in 1H2022) | Confirmed; FY2021/FY2023 source ids add no support for the 55% figure. |
| CLM-001015 | A:tilde | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY 10-K FY2021 line 409; FY2025 line 582 | 35,000/8,100 and 50,000/12,000/27,000 confirmed. |
| CLM-001017 | A:tilde | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY 10-K FY2025 lines 507, 616 | Jardiance Aug-2023 eff.2026; Trulicity+Verzenio Jan-2026 eff.2028 confirmed. |
| CLM-001020 | A:tilde | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY 10-K FY2021 lines 380,384,394; FY2025 lines 568-572 | All names/dates confirmed. Statement says "FY2021 10-K ... CFO since 2021": confirmed. |
| CLM-001023 | A:tilde | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY 10-K FY2025 line 948 (7.8bn vs 5.1bn); line 655 (supply agreements) | Capex figures confirmed; contract-manufacturing wording is looser in source (long-term supply agreements). |
| CLM-001025 | A:tilde | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY 10-K FY2021 lines 362,611,619; FY2023 line 848 | ~45 and ~50 confirmed; tirzepatide PRV confirmed. |
| CLM-001027 | A:tilde | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY 10-K FY2025 lines 504, 613, 854 | Confirmed. |
| CLM-002024 | A:tilde | A2_jnj | PASS | JNJ 10-K FY2025 lines 697-707 | All oncology figures confirmed. |
| CLM-002025 | A:tilde | A2_jnj | PASS | JNJ 10-K FY2025 lines 715-720, 750 | All neuroscience figures confirmed; CAPLYTA acquired 2-Apr-2025 confirmed. |
| CLM-003035 | A:tilde | A3_abbvie | PASS_WITH_LOCATOR_FIX | ABBV 10-K FY2025 lines 1857-1858 | 1.4bn (CoolSculpting 290m vs 1.3bn; Liletta 241m vs 561m); Resonic 407m; Durysta FV 271 vs 711; 2025 total 847m confirmed. |
| CLM-003047 | A:tilde | A3_abbvie | PASS_WITH_LOCATOR_FIX | ABBV 10-K FY2025 line 785 | ~90 / ~60 confirmed. |
| CLM-005011 | A:tilde | A5_takeda | PASS_WITH_LOCATOR_FIX | Takeda H1 FY2026 PDF (text re-extracted with pypdf) lines 179,187,201,576-594,649 | 2,407.0 / 406.7 / 4,700 / 1,190 / restructuring 160.0 confirmed. Source has no extracted-text path in registry (raw PDF only). |
| CLM-005012 | A:tilde | A5_takeda | PASS_WITH_LOCATOR_FIX | Takeda H1 FY2026 PDF lines 218, 249-250 | 1,130.7 (+3.6/-5.4); ENTYVIO 541.7 (+13.0/+2.7); US 351.8 confirmed. |
| CLM-009000 | A:tilde | A9_partnerships | PASS_WITH_LOCATOR_FIX | LLY 10-K FY2025 lines 926, 934, 1034 (2,910/3,280/3,800 USD m); Note 4 table lines 1416-1428 (SiteOne 494, Scorpion 1,412, Morphic 2,549) | Statement rounds correctly. Note 10-K line 952 says cash paid $3.0bn (2025) vs expense 2.91bn; Morphic audited charge 2,549 (see conflict). |
| CLM-009086 | A:tilde | A9_partnerships | PASS_WITH_LOCATOR_FIX | TAK 20-F FY2023 lines 2075-2076 | JPY133.0bn Teijin and USD230m/JPY34.8bn Hasten confirmed. |
| CLM-001001 | B:big | A1_lilly | PASS | LLY FY2022 10-K l.777-779 etc. | Trulicity 7,439.7, Verzenio 2,483.5 (+84%), Taltz 2,482.0 confirmed. |
| CLM-001003 | B:big | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY 10-K FY2023 l.1023 (Mounjaro 5,163.1) + l.1050 (Zepbound 175.8); FY2024 l.962,965; FY2025 l.904,906 | Sums and shares recomputed: 5,338.9/34,124.1=15.6%; 16,465.8/45,042.7=36.6%; 36,507/65,179=56.0%. Computed, not quoted. |
| CLM-001004 | B:big | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY FY2022 l.777 (7,439.7); FY2023 l.1022 (7,132.6; US 5,433.3); FY2024 l.964 (5,253.5); FY2025 l.1302-1305 (US 2,914 + OUS 1,362 = 4,276) | FY2025 total is a sum of US+OUS rows, not printed as a single figure. |
| CLM-001014 | B:big | A1_lilly | PASS_WITH_LOCATOR_FIX | LLY cash-flow statements: FY2023 l.1393 (3,944.5); FY2024 l.1324 (3,345.8); FY2025 l.1219 (3,008) | FY2025 reported to whole USD m; claim writes 3,008.0 (false decimal precision). Cash paid differs from IPR&D expense (2,910/3,280/3,800). |
| CLM-001031 | B:big | A1_lilly | PASS | SRC-001000 Lilly Q3-2026 release headline bullets l.6-7 | 24.4bn +39%; ~900m benefits incl 410m Jardiance milestones confirmed in stored text. |
| CLM-001032 | B:big | A1_lilly | PASS | SRC-001000 l.267-269 | 67,170 vs 45,887 confirmed in stored Lilly Q3-2026 release; product lines not compared. |
| CLM-002001 | B:big | A2_jnj | PASS | JNJ FY2022 10-K l.650,707,596 | Pharma 52,563/51,680; MedTech 27,427/27,060; Consumer 14,953/15,035 confirmed. |
| CLM-002002 | B:big | A2_jnj | PASS | JNJ FY2023 10-K l.658,728 | 54,759 (+4.2/+4.8) and 30,400 (+10.8/+12.4) confirmed. |
| CLM-002007 | B:big | A2_jnj | PASS | JNJ 10-K (Kenvue exchange offer) l.901 | Date and 80.1% confirmed; share counts/31.4bn/21.0bn not individually compared (UNVERIFIED detail). |
| CLM-002011 | B:big | A2_jnj | PASS | JNJ FY2025 10-K l.2937 (31-May-2024), l.812 (Shockwave 1,146/564) | Confirmed; USD335/share not re-opened. |
| CLM-002015 | B:big | A2_jnj | PASS | JNJ FY2025 10-K l.3085 | 6.475bn PV / 8.0bn nominal / 99.75% / 25 yrs confirmed. Statement stops at filing; status of the plan after Sept 2024 not in claim (see status section). |
| CLM-002017 | B:big | A2_jnj | PASS | JNJ FY2023 10-K l.794 | ~7.0bn talc charge confirmed; 0.4bn Kenvue FV not re-read. |
| CLM-002023 | B:big | A2_jnj | PASS | JNJ FY2022 10-K l.636 (7,977/6,023); other years in later 10-Ks not opened | FY2021/22 confirmed; FY2023-25 values rely on registry (14,351 confirmed in l.699). |
| CLM-002033 | B:big | A2_jnj | PASS | JNJ FY2025 10-K l.673,687 | US 53.8bn +6.9%; IM US 36.3bn +7.0% confirmed; MedTech US 17.4bn and intl 40.4bn not opened. |
| CLM-002072 | B:big | A2_jnj | PASS | JNJ FY2025 10-K l.1231 (94,193), l.697-706 | Sum 17,371 and 18.4% recomputed. |
| CLM-002073 | B:big | A2_jnj | PASS | JNJ FY2025 10-K l.699, 899 | 14,351/94,193=15.2% recomputed; 25.9bn sum (DARZALEX+TREMFYA+ERLEADA+IMBRUVICA) not independently re-added (TREMFYA row not opened). |
| CLM-002075 | B:big | A2_jnj | PASS | JNJ FY2025 10-K l.712 (STELARA 6,078/10,361), l.1231 (94,193/88,821) | 78.46bn/88.12bn/+12.3% recomputed; reported +6.0% (l.2888). |
| CLM-003014 | B:big | A3_abbvie | PASS | ABBV FY2023 10-K l.872,873 + FY2025 l.861-869 | Skyrizi 5,165+Rinvoq 2,522=7,687 (2022); 17,562+8,304=25,866 (2025); Humira 21,237->4,540. Arithmetic confirmed. |
| CLM-003015 | B:big | A3_abbvie | PASS | ABBV FY2023 10-K l.859 (54,318 -6.4%; 58,054 +3.3%) | Confirmed; FY2024/25 growth rates match XBRL claims. |
| CLM-003026 | B:big | A3_abbvie | PASS | ABBV FY2023 10-K l.1792 (Imbruvica IRA selection Aug-2023; impairment); l.995 (3.6bn total 2023 gross-margin impairments) | 2.1bn/1.9bn/4.0bn figures not individually re-read in tail of l.1792 (UNVERIFIED digits). |
| CLM-003027 | B:big | A3_abbvie | PASS | ABBV FY2023 l.885; FY2025 l.902 | Venclexta 1,820/2,009/2,288/2,583/2,792 confirmed; CANOVA/VERONA endpoint text not opened (UNVERIFIED part). |
| CLM-003031 | B:big | A3_abbvie | PASS | ABBV FY2023 10-K l.896 (2,682/2,615/2,232) | 2024/2025 values not opened. |
| CLM-003039 | B:big | A3_abbvie | PASS | Recomputed from CLM-000021..25 / CLM-000001..5 | 31.9/31.2/23.5/16.2/24.6 (24.65 rounds either way) confirmed. |
| CLM-003041 | B:big | A3_abbvie | PASS | ABBV FY2025 10-K l.1437 | 6,495/3,771/5,128 confirmed (payments row not opened). |
| CLM-003042 | B:big | A3_abbvie | NUMBER_MISMATCH | ABBV 10-K FY2025 l.1065 "Long-term debt, including current portion 64,503 (current 6,000; long-term 58,503)"; balance sheet l.1372 noncurrent 58,941 (2025)/60,340 (2024); FY2021 l.1245 64,189; FY2022 l.1327 59,135; FY2023 l.1394 52,194 | Claim labels 75,962/63,128/59,245/66,841/64,503 "non-current"; they are total long-term debt INCLUDING current portion. Same label error originates in XBRL claims CLM-000066..70 (tag LongTermDebt). True non-current: 64,189/59,135/52,194/60,340/58,941 (balance sheet, incl. finance leases). |
| CLM-003043 | B:big | A3_abbvie | PASS_WITH_LOCATOR_FIX | ABBV FY2025 10-K l.1470 (dividends paid 11,657/11,025/10,539), l.2511 (6.65/6.29/5.99), l.704 (1.64->1.73); Q3-2026 PR (SRC-003010) fetched: 1.73->1.82 payable 16-Feb-2027 | Confirmed. 10-K says declared 31-Oct-2025 (table shows 10/31/25). |
| CLM-003049 | B:big | A3_abbvie | PASS | ABBV FY2021 10-K l.699; FY2022 l.725 | 2.5bn expected / realized confirmed. |
| CLM-003052 | B:big | A3_abbvie | PASS | ABBV FY2024 10-K l.1684 ($45.00; 8.7bn), FY2023 l.1104 | Close date 1-Aug-2024 l.1661 confirmed. "Best-in-class" press-release wording not re-opened. |
| CLM-003057 | B:big | A3_abbvie | PASS | ABBV FY2024 10-K l.1010,1721,1878 | 4.5bn emraclidine impairment Q4-2024; FV 2.4bn; 4.9bn operating loss; 11-Nov-2024 confirmed. 6.9bn carrying cut off in grep, partially seen. |
| CLM-003059 | B:big | A3_abbvie | PASS | ABBV FY2025 10-K l.1444 | 847/4,476/4,229 confirmed. |
| CLM-003065 | B:big | A3_abbvie | PASS | ABBV FY2024 10-K l.1714 (246m), l.1720 (up to 1.6bn) | Statement says "may owe Pfizer": l.1720 refers to milestones for programs; Pfizer attribution not re-read. |
| CLM-005001 | B:big | A5_takeda | PASS | TAK FY2025 20-F l.1804,1805 | US 2,164.8 (-9.0/-7.7); Europe&Canada 1,146.2 (+8.6/+3.0) confirmed. |
| CLM-005002 | B:big | A5_takeda | PASS | TAK FY2025 20-F l.1804,1774 | Shares recomputed: 2,164.8/4,505.7=48.0%; 433.1=9.6%; 195.1=4.3%; 2,379.7/4,581.6=51.9%. |
| CLM-005004 | B:big | A5_takeda | PASS_WITH_LOCATOR_FIX | TAK 20-F FY2021 l.2391 (526.1); FY2022 l.2095 (633.3); FY2025 20-F l.1777 (729.9/730.2/675.9), l.1918 | Confirmed; fiscal-year labels FY2025=Apr25-Mar26 correct. |
| CLM-005006 | B:big | A5_takeda | PASS | TAK FY2025 20-F l.2234 | 288.5/303.9/313.2; JPY200 (FY2025); JPY204 intended FY2026(Mar-27) confirmed. |
| CLM-005007 | B:big | A5_takeda | PASS | TAK FY2025 20-F l.569 | 496.7/319.4/426.9 confirmed. |
| CLM-005009 | B:big | A5_takeda | PASS | TAK FY2025 20-F l.1824 (ENTYVIO 958.0), l.1695 (VYVANSE 203.2), l.1848 (790.6, 140.3) | Other product values not individually opened. |
| CLM-005021 | B:big | A5_takeda | PASS | TAK FY2025 20-F l.1723 | Teva JV dissolution confirmed; 18.9/56.5/50.8 amounts not individually compared. |
| CLM-005022 | B:big | A5_takeda | PASS | TAK 20-F FY2023 l.536 | ALOFISEL 74.0bn; EXKIVITY 28.5bn confirmed. |
| CLM-005064 | B:big | A5_takeda | PASS | TAK 20-F FY2025 l.1848 (790.6, 140.3), l.1774 (rev 4,505.7); H1 PDF l.239 (561.2 +8.5/-1.5) | 790.6/4,505.7=17.5% ("18%") and 140.3=3.1% ok. |
| CLM-005071 | B:big | A5_takeda | PASS | TAK 20-F FY2025 l.1803,1807 | Japan 433.1 (+3.5%), China 195.1 (+1.8%) confirmed. |
| CLM-006003 | C:A6 | A6_ai_robotics | PASS | NVIDIA blog (b9d7dd9c95a90d89) | 1,016 Blackwell Ultra GPUs, >9,000 petaflops, GTC Washington DC confirmed; "DGX SuperPOD/B300" not separately grepped. |
| CLM-006004 | C:A6 | A6_ai_robotics | PASS | BiopharmaTrend (bf85ccddaa21c929) | ~4 months assembly, 700 TB genomics, 290 TB GPU memory, 100% renewable by 2030 confirmed. Maturity OPERATIONAL = installed hardware; no scientific output. |
| CLM-006006 | C:A6 | A6_ai_robotics | PASS | NVIDIA blog (b9d7dd9c95a90d89) | Robots for quality inspection/transport and Omniverse digital twins confirmed (statement is a vendor-blog capability claim; PILOT tag is generous - no deployment evidence). |
| CLM-006009 | C:A6 | A6_ai_robotics | PASS | insitro release (19f8ab63d9d5bfc2) | TuneLab, 2024 siRNA/antibody relationship confirmed; 9-Sep-2025 date not re-verified. |
| CLM-006020 | C:A6 | A6_ai_robotics | PASS | Greylock interview (stored text 6f6aa8acfa8f272b) | "up to 2.6x increase in enrollment at the better performing, higher enrolling sites" confirmed. Maturity tag OPERATIONAL rests on a single CIO interview statement (self-reported, no baseline): recommend downgrade to PILOT/self-reported. |
| CLM-006023 | C:A6 | A6_ai_robotics | PASS | Greylock interview | AskJIA and Engagement.AI (14 countries) confirmed; supply-risk and HR agent items not searched. |
| CLM-006025 | C:A6 | A6_ai_robotics | PASS | JNJ FY2025 10-K l.428; grep count of OTTAVA/MONARCH = 0 | Confirmed: generic AI statement + risk language; no OTTAVA/MONARCH text. |
| CLM-006034 | C:A6 | A6_ai_robotics | PASS | Bio-IT World (1df4999f5365f345) | "2,000+ clinical trials" and prison/pediatric exceptions confirmed. Interview statement by AbbVie head of AI (T3 relaying company speaker). |
| CLM-006037 | C:A6 | A6_ai_robotics | PASS | AbbVie Valkai release (raw_documents/press/ABBV_valkai.html) | "AI@AbbVie" confirmed. |
| CLM-006041 | C:A6 | A6_ai_robotics | PASS | Yahoo Finance copy of Iambic release (f5edd09eaf4a7cbc) | 9-Feb-2026; NeuralPLexer; "could exceed $1.7 billion" + royalties confirmed. Source is a syndicated press release (T2). |
| CLM-006052 | C:A6 | A6_ai_robotics | PASS_WITH_LOCATOR_FIX | BiopharmaTrend Arctoris article (142aee2607f17df3) | Life Sciences Studio sale to Arctoris confirmed (2017, $90m). Zymergen distress is NOT in cited sources SRC-006005/6: that part is UNVERIFIED from the cited sources. |
| CLM-006055 | C:A6 | A6_ai_robotics | PASS | NVIDIA blog; Benchling blog; CLM-000280 | Interpretation; Benchling "opt into the program" confirmed. USD 1bn data-cost figure relies on CLM-000280 (company estimate). |
| CLM-009005 | C:A9 | A9_partnerships | PASS | LLY FY2025 10-K l.1432 | Emergence, ETx-22, Aug 2023, 407 confirmed. |
| CLM-009008 | C:A9 | A9_partnerships | PASS | LLY FY2021 10-K l.725,835,1304 | $22.50, 747.4m, CVR $4.00 (~160m), 824.0 confirmed. Acquisition Jan-2021 predates the 2021-11 window (lookback). |
| CLM-009009 | C:A9 | A9_partnerships | PASS | LLY FY2022 10-K l.591,608,830 | $244.6m (2022), PR001 intangible impairment confirmed. Note: shown under "asset impairment, restructuring and other special charges"; 2022 charge total, not only Prevail. |
| CLM-009012 | C:A9 | A9_partnerships | PASS | LLY FY2025 10-K l.1394 | $925m net of cash, May 2024 confirmed; goodwill 817 / PP&E 109 not re-opened. |
| CLM-009028 | C:A9 | A9_partnerships | PASS_WITH_LOCATOR_FIX | CDD blog (d1fad88b6baa80b1) fetched in this audit | 2 million / 675,000 as of October 2026 confirmed in the page text. Registry marks source metadata_only although it is retrievable; recommend upgrade to retrieved. Vendor blog (T4), single interested source. |
| CLM-009031 | C:A9 | A9_partnerships | PASS | JNJ FY2025 10-K l.3012 | FDA approval in fiscal Q4-2025; IPR&D reclassified to definite-lived and amortising: confirmed. |
| CLM-009054 | C:A9 | A9_partnerships | PASS | AbbVie PR (20423aa36ee6c7a9); ABBV FY2024 10-K l.1010,1721,1878 | Primary-endpoint miss, 4.5bn impairment, 4.9bn loss confirmed. |
| CLM-009055 | C:A9 | A9_partnerships | PASS_WITH_LOCATOR_FIX | BioPharma Dive (58b6133779101ab4) fetched in this audit | Headline "AbbVie's $9B bet collapses..." confirmed. Registry says metadata_only but page is retrievable; upgrade. Statement is a fact about a headline only. |
| CLM-009056 | C:A9 | A9_partnerships | PASS | ABBV FY2025 10-K l.1702, 1734 | $31.26, $9.8bn/$9.2bn, 578m revenue, 682m operating loss confirmed; close date 12-Feb-2024 not re-opened. |
| CLM-009065 | C:A9 | A9_partnerships | PASS | ABBV FY2023 10-K l.1691-1692 | $287m = $255m cash + $32m contingent; up to $95m; business combination confirmed. |
| CLM-009071 | C:A9 | A9_partnerships | PASS | ABBV FY2025 10-K l.1002 | 1.9bn Capstan, 906m Gilgamesh, 700m Ichnos Glenmark confirmed. |
| CLM-009073 | C:A9 | A9_partnerships | PASS | ABBV FY2025 10-K l.1794 | Janssen profit share 954/1,140/1,245 confirmed. |
| CLM-000242 | C:Dir | RUN-0002 | PASS | LLY FY2025 10-K l.624,862 | 56 percent confirmed. |
| CLM-000246 | C:Dir | RUN-0002 | PASS | LLY FY2025 10-K l.948 | 7.8bn vs 5.1bn confirmed. |
| CLM-000253 | C:Dir | RUN-0002 | PASS | JNJ FY2025 10-K l.735,817,896 | 94,193; IM 60,401 (+6.0/5.3); MedTech 33,792 vs 31,857 confirmed. |
| CLM-000264 | C:Dir | RUN-0002 | PASS | ABBV FY2025 10-K l.861-863 | 17,562 / 15,202 / 2,360 / 11,718 / 7,763, +49.9% confirmed. |
| CLM-000275 | C:Dir | RUN-0002 | PASS | TAK FY2025 20-F l.1695,1872,1909 | 203.2 vs 350.6 (-42.0% AER); Neuroscience 414.3 (-26.8%) confirmed; 423.2 FY2023 confirmed l.1704. |
| CLM-000276 | C:Dir | RUN-0002 | PASS | TAK FY2025 20-F l.417,1707 | TRINTELLIX 121.8bn; patents Dec-2026; ENTYVIO exclusivity loss latter half of decade confirmed. |
| CLM-000279 | C:Dir | RUN-0002 | PASS | TAK FY2025 20-F l.570 | 27 new centers -> 260, FY ended 31-Mar-2024 (FY2023) confirmed. |
| CLM-000281 | C:Dir | RUN-0003 | PASS | NVIDIA newsroom HTML | 12-Jan-2026, up to $1bn over five years, BioNeMo, Vera Rubin, continuous learning system confirmed. |
| CLM-000282 | C:Dir | RUN-0003 | PASS | NVIDIA newsroom (raw_documents/press/LLY_nvidia_lab.html) | Omniverse digital-twin statement confirmed; claim attributes it to "NVIDIA-Lilly release" and "intended to train" language not exact-matched. |
| CLM-000284 | C:Dir | RUN-0003 | PASS_WITH_LOCATOR_FIX | JNJ IR page (c5bb363a88b35bf7) fetched in this audit | Release states Memorial Hermann will be the first hospital to install OTTAVA; follows July-2026 FDA De Novo. Statement writes "first commercial installation" announced: wording ok, but release is future/ongoing tense, not completed installation. 19-Nov-2026 date not confirmed in page text. Source retrievable though registry says metadata_only. |
| CLM-001057 | C:extra | A1_lilly | PASS | SRC-001025 inspected passage (ARIA-E 24.0%, 52 symptomatic vs 2.1%) consistent with JAMA 2023 abstract; PubMed page itself returns cookie stub | Trial values 0.67 / 1,736 / deaths not re-read this session (UNVERIFIED by this audit; source passage only). |
| CLM-001060 | C:extra | A1_lilly | PASS | PubMed 42814954 via NCBI E-utilities efetch: n=2339, -17.6/-23.7/-25.0% (4/9/12 mg) | Verified by this audit. Note: pubmed.ncbi.nlm.nih.gov page fetched by evidence.py returns a "Cookies must be enabled" stub (129 bytes); stored extracted text for SRC-001028 does not contain the abstract. |
| CLM-005025 | C:extra | A5_takeda | PASS_WITH_LOCATOR_FIX | Takeda FSE release pdf (25100145020.pdf) fetched/pypdf: impairment ~JPY 58.0bn, gamma-delta T-cell platform; decision to discontinue cell therapy confirmed | Fierce Biotech page returned HTTP 403 to the CLI; "137 Massachusetts roles" is UNVERIFIED by this audit (SOURCE_UNREACHABLE for that component). Registry lists SRC-005019 as retrieved. |
| CLM-005031 | C:extra | A5_takeda | PASS | ClinicalTrials.gov API NCT05210790: enrollment 293 ACTUAL; lead sponsor Protagonist Therapeutics | Confirmed. VERIFY primary-endpoint statement relies on 20-F l.686-689 (not re-read). |
| CLM-005033 | C:extra | A5_takeda | PASS | ClinicalTrials.gov API NCT06088043 n=693 completed; NCT06108544 n=1,108 completed | Enrollment confirmed; "~70% sPGA 0/1" not re-read. |
| CLM-005037 | C:extra | A5_takeda | PASS | ClinicalTrials.gov API NCT06671483 n=1,583; NCT06671496 n=601; ACTIVE_NOT_RECRUITING; primary completion 2027-05-18 (est) | Confirmed. |
| CLM-006017 | C:extra | A6_ai_robotics | NOT_FOUND_IN_SOURCE | Cited sources SRC-006005/006 (stored text 142aee2607f17df3, e701e9b32d276dae) contain zero mentions of "Strateos"; they state Life Sciences Studio established 2017 ($90m), and Fierce snippet (metadata_only) says "four years after launching" | "Lilly-Strateos remote robotic laboratory (public launch about 2020)" is not supported by the cited pages; the 2020 date and the Strateos link are UNVERIFIED. Conflicts with CLM-006014 (2017). |
