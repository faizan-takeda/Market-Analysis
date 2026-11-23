# A10 scorecard, wave 1 (Task 6)

Rubric: `research_methodology/evaluation_rubric.md`, ordinal scores 0/1/2 per axis, no numeric confidence. ACCEPT needs no zero and 12/16 or more. Data: [wave1_scorecard.json](wave1_scorecard.json).

| Shard | Auth | Rel | Cov | Indep | Temp | Contr | Trace | Signif | Total | Decision |
|---|---|---|---|---|---|---|---|---|---|---|
| A1_lilly | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 13/16 | **ACCEPT** |
| A2_jnj | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 14/16 | **ACCEPT** |
| A3_abbvie | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 12/16 | **ACCEPT** |
| A5_takeda | 1 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 11/16 | **REVISE** |
| A6_ai_robotics | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 9/16 | **REVISE** |
| A9_partnerships | 1 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 12/16 | **ACCEPT** |
| A4_financial + RUN-0001 XBRL | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 13/16 | **ACCEPT** |

Not scored (outside the A10 sample): A7_commercial, A8_policy, A12_pipeline, A14_gapfill.

Cross-shard pattern: no claim in any shard registers `independent_corroboration`, and `conflicts.jsonl` holds one entry (a status adjustment), so Independence and Contradiction handling cannot score 2 for any shard until corroboration and conflicts are recorded in the registry rather than in claim text.

## A1_lilly: ACCEPT (13/16)
Eli Lilly company shard: 70 claims, 36 sources (all retrieved)

- **source authenticity (2)**: All 36 sources retrieved; all 17 sampled A1 claims re-found in the 10-K text or registry source pages; no source failed to open.
- **relevance (2)**: Every claim maps to a company sub-question (financials, pipeline, policy, leadership, manufacturing).
- **coverage (2)**: Financials, pipeline, policy, leadership, manufacturing, commercial covered; AI and partnerships delegated to A6/A9; evidence_gaps.md present.
- **independence of corroboration (1)**: 67 of 70 claims rest on Lilly's own 10-K only; no claim registers independent corroboration; 13 flagged single_interested_source.
- **temporal accuracy (2)**: Fiscal years, partial 2026 periods and 9M/Q3 bases are explicit; CLM-001014 shows false decimal precision (3,008.0).
- **contradiction handling (1)**: Contrary evidence on 7 claims (Alimta, COVID impairment, CRL, shortage); FY2021 IPR&D 874.9 vs 970.1 not registered in conflicts.jsonl (resolved by A10).
- **traceability (2)**: Every claim has a source and locator; 9 locators are "~" approximations and 1 points to the wrong section (CLM-001009).
- **significance (1)**: Mechanism cards exist but durability and competitive response are INTERPRETATION or "not assessed"; outcomes quantified for manufacturing and launches.
- **Required repairs**: Fix 12 approximate or wrong locators (list in audit_wave1_reinspection.md); Add basis label to IPR&D claims (expense vs cash); Register FY2021 IPR&D definition change in conflicts.jsonl.
- Note: Sample result: 17 claims re-inspected, 17 correct on figures (12 needed a locator fix).

## A2_jnj: ACCEPT (14/16)
Johnson & Johnson company shard: 76 claims, 38 sources

- **source authenticity (2)**: 32 of 38 sources retrieved, 5 API, 1 metadata_only; sampled J&J figures matched the 10-Ks.
- **relevance (2)**: Claims map to segments, LOE (Stelara), talc, MedTech, pipeline, leadership.
- **coverage (2)**: Segments, products, talc, Kenvue, acquisitions, robotics, FY2026 YTD covered; gaps listed.
- **independence of corroboration (1)**: 18 claims rest on J&J releases only and 8 of them are not flagged single_interested_source; regulatory milestones for OTTAVA/VELYS/MONARCH come from J&J releases, not FDA records.
- **temporal accuracy (2)**: Fiscal calendar (52/53 weeks), recast FY2021/FY2022 segments and partial FY2026 explicitly handled.
- **contradiction handling (1)**: Talc (company vs plaintiff-counsel estimates) and recasts are noted in claims; none entered in conflicts.jsonl.
- **traceability (2)**: Each claim has a source and locator; OTTAVA "first install" wording is stronger than the source (CLM-000284).
- **significance (2)**: Capability cards (Tremfya successor, MedTech) tie investment to outcome with numbers (e.g. Tremfya offsets about one third of the Stelara decline).
- **Required repairs**: Flag 8 T2-only claims as single_interested_source; Reword OTTAVA installation claims; cite FDA database records for 510(k)s; Add Impella/Varipulse FDA links to the MedTech status table.
- Note: Sample result: 13 claims re-inspected, 13 PASS.

## A3_abbvie: ACCEPT (12/16)
AbbVie company shard: 91 claims, 39 sources

- **source authenticity (1)**: 20 retrieved, 7 API, 8 metadata_only, 3 blocked, 1 unavailable; 16 claims re-inspected: 15 correct, 1 label error (CLM-003042).
- **relevance (2)**: Claims map to Humira LOE, successors, aesthetics, pipeline, BD, policy, leadership.
- **coverage (2)**: Humira, Skyrizi/Rinvoq, aesthetics, oncology, neuroscience, M&A, policy, AI; gaps listed (Aliada, Landos, Celsius).
- **independence of corroboration (1)**: 22 claims flagged single_interested_source; Humira contracting figures rely on T3 trade/IQVIA claims; none independently re-checked.
- **temporal accuracy (1)**: Basis error: CLM-003042 labels total debt incl. current portion as "non-current"; ImmunoGen 10.1bn vs 9.8bn and 18.5bn "cash paid" need basis labels.
- **contradiction handling (1)**: Emraclidine premise tested and recorded as CONTRADICTED (good); no entries in conflicts.jsonl.
- **traceability (2)**: All claims carry source and locator; 2 "~" locators were approximate.
- **significance (2)**: Successor-sequencing, contracting, BD-refill and settlement cards give problem, mechanism, outcome with numbers and limits.
- **Required repairs**: Correct CLM-003042 and the business-model line citing it; Label ImmunoGen/Cerevel amounts (announced / consideration / net of cash); Open or replace the 8 metadata_only sources.
- Note: Total is at the ACCEPT threshold (12/16); the repairs are needed before Gate 1.

## A5_takeda: REVISE (11/16)
Takeda public-baseline shard: 83 claims, 40 sources

- **source authenticity (1)**: 31 retrieved, 5 metadata_only, 3 blocked, 1 paywalled; one retrieved source has no local text file (H1 FY2026 PDF); Fierce page unreachable (137 roles).
- **relevance (2)**: Claims map to revenue, LOE, pipeline, restructuring, leadership, AI/plasma baselines.
- **coverage (1)**: No business/business_model.md exists; Ventures/CEI, patient-assistance, AI scale, manufacturing automation not found (listed, 7 INCONCLUSIVE).
- **independence of corroboration (1)**: 71 of 83 claims are flagged single_interested_source (accurate flagging); no claim carries independent corroboration; USD 10-20bn peak-sales range is a company statement only.
- **temporal accuracy (2)**: FY labels (FY2025 = Apr 2025-Mar 2026), partial H1 FY2026 and IFRS vs Core are explicit.
- **contradiction handling (1)**: Restructuring 150/160/170bn noted, but CLM-005078 mis-describes 170bn as trade-press only and orders the series wrongly; not in conflicts.jsonl.
- **traceability (2)**: Each claim has source and locator; 2 "~" locators; claim figures re-verified in 20-F and re-extracted H1 PDF.
- **significance (1)**: LOE exposure and replacement logic are set out; no mechanism cards with outcomes because the baseline is public-only.
- **Required repairs**: Create business/business_model.md; Rewrite CLM-005078 as a dated series (150 -> 170 -> 160); Store raw copy / passage for SRC-005015 and SRC-005018; Verify or drop "137 Massachusetts roles".
- Note: Total 11/16.

## A6_ai_robotics: REVISE (9/16)
AI, data and robotics shard: 60 claims, 36 sources

- **source authenticity (1)**: 28 retrieved, 7 metadata_only, 1 paywalled; sampled pages exist and match, but CLM-006017 cites pages that do not mention Strateos.
- **relevance (2)**: All sources relate to AI/data/robotics at the four companies or industry comparators.
- **coverage (1)**: Discovery, compute, MedTech, partners, federated learning covered; AbbVie ARCH page 403, Takeda internal AI absent; gaps explained.
- **independence of corroboration (1)**: 42 of 60 claims flagged single_interested_source; 28 rest on company or vendor sources only; the outcome claims (2.6x, minutes vs weeks) have no independent source.
- **temporal accuracy (1)**: Dates mostly explicit; "public launch about 2020" for Strateos is unsupported; 2026 events labelled as announcements.
- **contradiction handling (1)**: Several INCONCLUSIVE/NEEDS_MORE_RESEARCH records and explicit counter-evidence, but nothing in conflicts.jsonl; the 2017 vs 2020 lab-start conflict was not resolved.
- **traceability (1)**: 16 claims use locator "see source record"; 24 AI claims lack maturity; maturity values upper-case against the lower-case protocol.
- **significance (1)**: Maturity ladder is the right device but six tags are not justified (SCALED, DEMONSTRATED_OUTCOME); no application with an independent outcome exists to explain.
- **Required repairs**: Retag maturity (6 claims) and add missing tags (24); Replace "see source record" locators; Rewrite or drop CLM-006017; Normalise maturity case.
- Note: Total 9/16.

## A9_partnerships: ACCEPT (12/16)
Partnerships and ecosystem shard: 102 claims, 23 own sources plus canonical 10-K sources

- **source authenticity (1)**: 11 of 23 own sources metadata_only (3 of them retrievable); 10-K-based claims (T1) all re-found in text; all 14 sampled claims correct on figures (4 locator fixes).
- **relevance (2)**: Deals, impairments, venture arms and write-downs map to the ecosystem questions.
- **coverage (2)**: M&A, licences, venture arms, write-downs for all four companies; gaps stated.
- **independence of corroboration (1)**: 79 claims T1-only (10-K), 11 flagged; no independent corroboration registered; headline deal values from press are PARTIALLY_SUPPORTED.
- **temporal accuracy (2)**: Deal dates, windows and lookback (Prevail Jan 2021) explicit; cash vs expense bases not labelled.
- **contradiction handling (1)**: Morphic 3.2 vs 2.55bn, IPR&D 874.9 vs 970.1, AbbVie Ventures 2009 vs 2015 recorded inside claims; none in conflicts.jsonl; two are resolved by A10.
- **traceability (2)**: Claims cite SRC and locator; 2 locator fixes (CLM-009000, CLM-009086); synthesis claims cite six sources with a generic locator.
- **significance (1)**: Synthesis claims (windows, write-downs, ecosystem arms) describe mechanisms but are PARTIALLY_SUPPORTED interpretations with no outcome ranking.
- **Required repairs**: Upgrade 3 retrievable metadata_only sources (SRC-000034, -009022, -009017); Add basis labels (expense / cash / headline); Record conflicts in conflicts.jsonl.
- Note: Total 12/16, at threshold.

## A4_financial + RUN-0001 XBRL: ACCEPT (13/16)
Financial series: 189 A4 claims + 238 RUN-0001 XBRL claims, 31 + 8 API sources

- **source authenticity (2)**: Raw companyfacts JSON stored; 151 metric-year pairs re-compared across two independent extractions; 146 agree, 5 definitional.
- **relevance (2)**: Revenue, R&D, income, cash flow, capex, debt, IPR&D for all four companies.
- **coverage (2)**: Five years for three companies and four Takeda 20-F years; XBRL-free metrics (buybacks, dividends) only in A4.
- **independence of corroboration (2)**: Two separate pipelines (XBRL and A4) and the 10-K text agree for the sampled values.
- **temporal accuracy (1)**: Debt basis error: 10 AbbVie/J&J "non-current" claims are totals including current portion (tag LongTermDebt).
- **contradiction handling (1)**: Net income consolidated vs attributable difference undocumented; no conflict records.
- **traceability (2)**: Every claim has accession-level locator and API source.
- **significance (1)**: Data series only; the mechanism links are made in dossiers.
- **Required repairs**: Relabel CLM-000066..70 and CLM-000128..132; add non-current claims; Add basis note on AbbVie net income pairs.
- Note: Financial values themselves are accurate; the defect is a label.
