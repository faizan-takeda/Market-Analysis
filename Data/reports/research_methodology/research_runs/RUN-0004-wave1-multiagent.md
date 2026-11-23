# RUN-0004 — Wave 1 multi-agent deep research (2026-11-21, session 2)

**Question.** Can parallel specialist agents (A1 Lilly, A2 J&J, A3 AbbVie, A5 Takeda, A6 AI/robotics, A8 policy, A9 partnerships, A12 pipeline/regulatory) produce evidence-grade, shard-isolated research on the eight briefs in `briefs/WAVE1_*.md` that survives the fixed rubric?
**Hypothesis.** Company agents on on-disk 10-K/20-F text + primary web sources will reach ≥30 sources / ≥70 claims each with 0 validation errors; horizontals will reach ≥25 / ≥50.
**Search strategy.** On-disk filings first (grep + line locators), then EDGAR exhibits, FDA/CT.gov/PubMed APIs, company newsrooms, T3 corroboration; explicit failure/contradiction queries.

## Outcome
| Agent | Sources (retrieved) | Claims | Validation | Notes |
|---|---|---|---|---|
| A1 Lilly | 36 (36) | 70 | 0 errors | cut at tool cap after steer; several `~` locators need audit |
| A2 J&J | 38 (32+5 api) | 76 | 0 errors | first run killed at 100-call cap AFTER writing all files; dashboard retry added 6/10 |
| A3 AbbVie | 39 (20+7 api) | 91 | 0 errors | corrected brief errors (Cerevel impairment USD 4.5bn Q4-2024; USD 100bn pledge) |
| A5 Takeda | 40 (31) | 83 | 0 errors | capability baseline + IVB backlog produced |
| A6 AI/robotics | 36 (28) | 60 | 0 errors | 14 mechanism cards; every claim maturity-tagged |
| A8 policy | 36 (22) | 55 | 0 errors | runs 1 and 2 died at the cap with nothing saved; run 2 completed after Director steer |
| A9 partnerships | 23 (11) | 102 | 0 errors | audited 10-K deal notes; venture-arm scale not found |
| A12 pipeline | 117 (38+79 api) | 153 | 0 errors | 21 CDER novel approvals as FACT claims; 19 setbacks |
| **Merged** | **431** | **1,165** | canonical PASS | via `scripts/merge_shards.py`; 1 status downgrade logged (CLM-006019) |

## New evidence vs reused
Reused: 20 on-disk annual reports (SRC-000003..000028) cited by line; 286 session-1 claims. New: 396 sources, 879 claims.

## Contradictions found (kept, not deleted)
Morphic headline USD 3.2bn vs audited IPR&D charge 2.55bn; Lilly FY2021 IPR&D 874.9 vs 970.1 (restated comparative); Takeda restructuring cost 150/160/170bn JPY across sources; AbbVie Ventures founding 2009 vs ~2015; Strateos lab start 2017 vs ~2020; Lilly 2024 lobbying USD 7.89m vs 8.43m; Medicare obesity access "as early as 2026-04-01" vs 10-K "by 2026-07-01"; CT.gov status lag for VERONA and EXCLAIM-2.

## Evaluation (rubric, Director's provisional; A10 audit pending)
Source authenticity high (T1 share high; FDA/CT.gov/EDGAR records); coverage uneven (leadership interviews, lobbying totals, venture-arm scale, CBER products missing); independence of corroboration moderate (company releases dominate AI claims); temporal accuracy good (periods explicit); traceability good (locators; `~` approximations flagged).

## Decision
**ACCEPT with REVISE items** → wave 2: independent audit (A10), gap-fill (A14), commercial horizontal (A7), policy second pass declined (A8 coverage adequate; gaps recorded).

## Process findings (keep)
- Subagent default tool-call cap is 100, not 1000; two runs lost all work. Fix: `max_turns` raised to 400 and save-as-you-go in every brief.
- Agents reading on-disk filings produced the most reliable numeric claims; web-only agents produced more metadata_only records.
- Horizontal/company overlap (AI, deals) produced duplicate sources with different IDs → alias records; acceptable, but the auditor should check for conflicting statements about the same event.
