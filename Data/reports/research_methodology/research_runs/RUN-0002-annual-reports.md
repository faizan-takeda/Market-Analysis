# RUN-0002 — FY2025 10-K / 20-F full-text mining (A1-A3, A4)
Question: What do the latest annual reports disclose about product concentration, LOE, M&A, capex and technology?
Method: download primary documents (public domain), convert to text, targeted grep by product/acquisition/patent/AI terms, read surrounding lines, record line-number locators.
Result: 41 claims (39 FACT, 1 INTERPRETATION, 1 PARTIALLY_SUPPORTED). Decision: ACCEPT, with audit pending (A10 should re-read each cited line).
Rejected direction: treating J&J `ResearchAndDevelopmentExpense` XBRL values as R&D (see RUN-0001).
