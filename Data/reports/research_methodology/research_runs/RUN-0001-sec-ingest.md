# RUN-0001 — SEC XBRL ingest (A4)
Question: What are the audited FY2021-FY2025 financials of LLY/JNJ/ABBV and FY2021-FY2024 of Takeda, with filing-level provenance?
Sources: data.sec.gov submissions + companyfacts for CIKs 59478, 200406, 1551152, 1395064.
Result: 28 sources, 238 FACT claims. Evaluation: authenticity PASS, temporal PASS (after fixes), traceability PASS. Decision: ACCEPT.
Failures kept: (1) J&J 52/53-week year-ends mislabelled → fixed with 10-day shift; (2) J&J ResearchAndDevelopmentExpense tag = IPR&D impairments, not R&D → fixed by best-coverage/largest-magnitude selection; (3) Lilly R&D tag switched in 2023 → multi-tag merge with flag.
Open: Takeda FY2025 absent from companyfacts.
