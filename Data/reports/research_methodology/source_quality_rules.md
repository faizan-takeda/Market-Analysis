# Source quality rules

## Hierarchy
| Tier | What | Treat as |
|---|---|---|
| T1_primary_official | SEC/EDGAR filings (10-K, 10-Q, 8-K, 20-F, proxy), FDA/EMA/PMDA records, ClinicalTrials.gov, peer-reviewed journals, patents, court records, government lobbying disclosures | Fact for what the document states |
| T2_company_technical | Company technical blogs, R&D-day decks, earnings transcripts, published operating results, executive interviews (verbatim) | Fact that the company said it; outcome claims need T1/T3 corroboration |
| T3_independent_reputable | Reuters, FT, WSJ, Bloomberg, STAT, Endpoints, Fierce, Nature/Science news, NBER/university research, recognised consultancies | Reportage; check for reliance on the same press release |
| T4_expert_commentary | Analyst notes, expert blogs, podcasts | Interpretation, labelled |
| T5_speculative | Forums, unverified social media, rumour | Never fact; may motivate a search |

## Rules
1. Inspect before citing. Store a verbatim passage (<= 600 chars) and locator.
2. One original = one source. Syndicated repeats of a press release do not add independence.
3. Interested-party claims are flagged. "Company says X improved Y%" is a FACT about the statement, INTERPRETATION about the outcome unless independently corroborated.
4. Numbers carry period, currency, accounting basis (GAAP/non-GAAP/IFRS; continuing vs total operations). J&J pre/post-Kenvue (Aug 2023) and AbbVie post-Allergan (May 2020) are not comparable without adjustment.
5. Dates: distinguish event date, publication date, access date.
6. Access: `retrieved` (opened), `api_json` (machine-read), `metadata_only` (known to exist, not opened), `paywalled`, `blocked` (403/robot), `unavailable` (404/down). Never bypass paywalls/logins; respect robots and rate limits (>= 1 s/host).
7. Preserve conflicts in `conflicts.jsonl` with both source IDs and a resolution note (or `unresolved`).
8. Lawful storage: full copies only for public records (SEC, FDA, CT.gov, government). Otherwise metadata + short excerpt + own notes.
9. Causality: two events in sequence are not cause and effect. Mark `causal: asserted_by_company | corroborated | unknown`.
10. Failure search is mandatory: for every company and domain, run at least one query for discontinued/failed/delayed/recall/lawsuit/criticism.
