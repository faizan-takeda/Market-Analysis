# A10-bis Task 2: citation consistency of the synthesis layer

Date 2026-11-21. Auditor A10-bis. Scope: `New_mediciine/cross_company_analysis/master_comparison.md` and `lessons_for_takeda.md`; the seven `strategy/future_of_pharma/domain*.md`; `strategy/platform_moats/analogies_platform_strategies.md` (lines 1-83 read in full); and the five `industry_transformation/policy/*.md` files that carry citations.

Method: for every cited line I printed the cited claim statements next to the sentence and judged support at sentence level. 788 citation occurrences were read this way (master 167, lessons 171, domain1-7 296, analogies about 80 in the lines read, policy 74). About 200 were compared number by number against the claim text. A script then listed every sentence containing a number that does not occur in any cited claim (74 hits, most are rounding, dates, table row numbers or computed values; the real ones are below). Every cited ID exists in the registry (0 dangling IDs).

Codes: OK, MISCITED (the cited claim says something else or lacks the number), OVERSTATED (sentence stronger than the claim), STALE (a later claim or fact supersedes the sentence).

## Verdict by file

| File | Citations read | MISCITED | OVERSTATED / STALE | Reading |
|---|---|---|---|---|
| master_comparison.md | 167 | 3 | 4 | Mostly sound; the debt-basis repair and two basis notes cite claims that do not carry the repaired numbers |
| lessons_for_takeda.md | 171 | 0 | 3 | Sound; one derived duration is wrong |
| domain1 data | 39 | 0 | 1 | Recommendation 1.1 labelled EVIDENCE_BACKED on weaker evidence |
| domain2 R&D | 65 | 0 | 2 | |
| domain3 robotics | 52 | 0 | 0 | Cleanest file; maturity and conflict notes are honest |
| domain4 care models | 38 | 1 (inherited date) | 0 | |
| domain5 commercial | 39 | 0 | 0 | |
| domain6 partnerships | 48 | 1 | 2 | Two wrong numbers carried from A9 claims |
| domain7 people | 35 | 0 | 0 | |
| analogies | about 80 | 1 | 0 | Table cells cite the hypothesis instead of the fact claim |
| policy/*.md | 74 | 4 | 0 | The alleged pledge mis-citations are real (see below) |

## The alleged policy mis-citations: confirmed, four in total

`industry_transformation/policy/pricing_tariffs_manufacturing_pledges.md` (the pledge IDs):

| Line | Sentence | Cites | Claim says | Correct ID |
|---|---|---|---|---|
| 12 | Lilly 1 March 2023 insulin 70% cut | CLM-008030 | J&J USD 55bn investment | CLM-008026 |
| 14 | Lilly FY2025 10-K preliminary agreements, three-year Section 232 grace | CLM-008032 | AbbVie USD 100bn agreement | CLM-008028 |
| 17 | J&J 8 January 2026 voluntary agreement, TrumpRx, USD 55bn reaffirmed | CLM-008035 | Takeda 20-F MFN statement | CLM-008031 |

`ira_negotiation_exposure.md` line 32: AbbVie USD 2.1bn Imbruvica impairment in Q3 2023 cites CLM-008021 (Lilly Jardiance 66% discount). Correct ID CLM-008019.

`cross_company_analysis/evidence_gaps.md` section 3 already admits the pledge-ID inconsistency ("for example CLM-008030 and CLM-008032 for Lilly 10-K points") and the OTTAVA 21/22 July difference, but the policy files were not corrected; I have located the exact lines. All four sentences are true; the IDs are shifted. The correct claims exist and I verified their numbers against primary sources (see audit_wave2_reinspection.md). Effect: a reader following the ID lands on a different company. All other lines of the five policy files match their claims, including the CMS price table, the pledge table rows 7-10 and the litigation list.

## Other findings (master, lessons, domains, analogies)

1. **master_comparison.md line 7 (MISCITED).** States non-current debt of USD 58,941m (AbbVie) and USD 39,438m (J&J) and cites CLM-000070, CLM-000132 and CLM-003042. Those claims carry 64,503, 41,438 and the 75,962 to 64,503 series, which are the figures the line says are wrong. The two non-current values are correct (AbbVie FY2025 10-K lines 1372, 2063; J&J FY2025 10-K lines 1203, 2038) but no registered claim contains them. CLM-003042 is still labelled "non-current" and still carries the mislabelled series, although Gate 1 required the correction. Fix: register two claims for 58,941 and 39,438 and relabel CLM-003042, CLM-000066..000070.
2. **master line 11 (MISCITED).** "3.35bn cash paid" cites CLM-009002, which contains 3.2bn and 2.55bn only. The 3.35bn is in the Lilly FY2024 10-K (line 1039) and in conflicts_proposed_A10, not in the cited claim. "AbbVie net income differs by basis" cites CLM-000026, a single XBRL value with no basis statement.
3. **master line 10 (MISCITED, partial).** "Cell-therapy impairment recognised is JPY 58.2bn, not 58.0bn" cites CLM-005025, which states the 58.0bn expectation. The recognised 58.2bn is CLM-009084 and CLM-009100 (verified: JPY 58,173m, Takeda FY2025 20-F line 5386).
4. **master line 28 (OVERSTATED).** "Of 29 company-level entries, 18 sit at concept, prototype or pilot" cites CLM-006054, which has no such count (the numbers appear only in data_ai_maturity_matrix.md line 25). My count from A6 FACT claims with a company and a maturity tag is 36 tagged claims (15 OPERATIONAL, 21 concept, prototype or pilot). Unit differs (entries vs claims); the matrix should state the unit.
5. **master line 52 (OVERSTATED).** "outcome trials read out 2029-2031" cites ClinicalTrials.gov records whose primary completion dates are estimates (2029-02, 2029-03, 2031-08). A primary completion estimate is not a readout date.
6. **master line 16 (OVERSTATED, minor).** "capex USD 1.3bn to 7.8bn" cites CLM-000172 (7.8bn only); the 1.3bn is CLM-000168, cited in lessons but not here.
7. **master line 12 and CLM-000286 (STALE).** The sentence correctly says completed installation is not shown, but CLM-000286, cited in the same sentence, still reads "regulator-verified milestone and a commercial installation".
8. **lessons line 63 (OVERSTATED, wrong number).** "CVS Caremark removed Zepbound for about 11 months". CLM-007011 gives removal from 1 July 2025 and CLM-007013 gives restoration effective 1 October 2026: 15 months. About 11 months is the time to the 28 May 2026 announcement.
9. **lessons line 35 (OVERSTATED).** "Operating evidence only for Concord, Kinsale and the Lebanon genetic-medicine plant" cites the Houston claim and the Concord claim; Kinsale (CLM-014011) and Lebanon (CLM-014015, CLM-006002) are not cited. Concord's operating status rests on one trade article (T3, CLM-014014 PARTIALLY_SUPPORTED).
10. **lessons line 175 (OVERSTATED).** "TREMFYA subcutaneous share gains accompanied USD 5,155m": the 10-K attributes growth to share gains and market growth (CLM-000256), and says nothing about the subcutaneous route.
11. **domain1 line 40 (OVERSTATED).** Recommendation 1.1 reads "EVIDENCE_BACKED: pooled models beat Takeda-only models on Takeda targets". The only evidence (CLM-006043) says a five-company model beat the best public model by about 10 points on pose accuracy, vendor-reported and not peer reviewed. No Takeda-only comparison exists in the corpus.
12. **domain2 line 22 (OVERSTATED).** "AbbVie's Cerevel purchase ended in discontinuation or large impairment, so acquiring is not safer than building". The same purchase delivered tavapadon, approved as Juvmo on 2026-09-25 (CLM-012017); the sentence omits it.
13. **domain2 line 18 (STALE).** "zasocitinib ... (NDA planned 2026)". CLM-005035 records FDA acceptance of the NDA with Priority Review on 14 September 2026.
14. **domain6 line 15 (wrong numbers).** "J&J Momenta (nipocalimab, 2025-04-30)": FDA approved Imaavy on 2025-04-29 (openFDA BLA761430; CLM-012011 is right, CLM-009044 uses the company announcement date). "CAPLYTA MDD, nine months after close": the acquisition closed 2025-04-02 and openFDA shows the efficacy supplement approved 2025-11-05, seven months.
15. **domain6 line 36 (STALE).** "A10 flags 2.6x as unverified". Takeda FY2025 20-F lines 2353 and 2669 show 2.8x (March 2025) and 2.6x (March 2026). The 2.6x (March 2023) and 3.1x (March 2024) values remain unchecked.
16. **domain4 line 10 and analogies line 67 (inherited error).** OTTAVA De Novo "2026-07-22" is taken from CLM-000283 and CLM-006029. The FDA De Novo database gives decision date 2026-07-21 and receipt 2025-12-18 (DEN250068). CLM-014022 has it right.
17. **analogies table rows 4 and 7 (MISCITED style).** "Flagship product still eroded 42%" and "Installed base drives 84% recurring revenue" cite the HYPOTHESIS claims (CLM-011038, CLM-011048). The numbers sit in CLM-011017 and CLM-011021. Table cells should cite the fact claim for a figure.

## OK, with notes

- The CMS price table, the Part D cost figures, the IRA cycle dates, the litigation list, and the AbbVie, J&J and Lilly revenue, R&D and capex rows of the master table match their claims.
- Computed values I recomputed and found correct: Humira -78.6% (21,237 to 4,540), Skyrizi plus Rinvoq +18,179m, Tremfya +1,485m offsetting 34.7% of Stelara's 4,283m loss, emraclidine 4.5bn as 54% of Cerevel's 8.3bn net price, AWS 57% of Amazon operating income, Alphabet Other Bets loss +3.1bn.
- Novel-approval counts in master line 40 (Lilly 8, J&J 5, AbbVie 5, Takeda 3) match the registry. AbbVie's five include Elahere (sponsor of record ImmunoGen) and Epkinly (sponsor Genmab), which the text calls "mostly acquired or partnered".
- Takeda's AMITIZA, Nimbus split, Keros and Innovent payments, Entyvio revenue share and Growth and Launch share were checked in the 20-F and agree.

## What this means for use

Citation hygiene is good: no invented IDs, no unsupported company-level number found in the policy, domain and analogy layers beyond items 1, 2, 4, 8, 11 and 14. The items most likely to mislead a reader are 1 (debt), 8 (11 months), 11 (EVIDENCE_BACKED on vendor evidence) and 14 (dates in the partnership domain).
