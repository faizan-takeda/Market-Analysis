# WAVE 1 — common brief for every specialist research agent (read fully before any research)

Project root: `/Users/palrahma/Desktop/MEDICINE` (use absolute paths; your shell cwd is NOT the project).
Python for the evidence CLI: `PY=/Users/palrahma/.local/share/mise/installs/python/3.12/bin/python3`
Research cutoff: 2026-11-21. Primary window: 2021-11-21 → 2026-11-21 (lookback allowed to explain an advantage).

## 0. Start-up (do these first, in this order; ~5 minutes)
1. `cat /Users/palrahma/Desktop/MEDICINE/research_methodology/agent_protocols.md` — record formats, enums, rules.
2. `cat` your company/domain `map.md` if it exists; `ls -R` your allowed output directory.
3. `$PY /Users/palrahma/Desktop/MEDICINE/tools/evidence.py ids <your_shard>` — note your next free IDs.
4. `grep -c . /Users/palrahma/Desktop/MEDICINE/New_mediciine/evidence_library/claims_registry.jsonl` and grep it for your company/topic — REUSE existing claim IDs (CLM-000001..000286) by citing them; do not re-register facts already there (revenue/R&D/net income FY2021-25 are already in CLM-000001..000238 and in `companies/<co>/financials/xbrl_annual_facts.md`).
5. Only then begin retrieval.

## 1. Evidence rules (non-negotiable)
- The filesystem is the system of record. Save after every ~5 sources. Never end with unsaved findings.
- Every source you cite must have been OPENED by you (web_fetch, the CLI `fetch`, or a file on disk). `access_status: retrieved` REQUIRES a verbatim `inspected_passage` (≤600 chars) you actually saw. If you only saw a search snippet, register it as `metadata_only` and say so in `notes`.
- No invented URLs, page numbers, quotes, numbers, dates. If a locator is unknown write `"locator": "unknown — full text not paginated"`.
- Distinguish kinds: FACT (directly substantiated) / INTERPRETATION / HYPOTHESIS / SCENARIO / RECOMMENDATION. A company statement of intent is a FACT *that the statement was made*, not a FACT about outcome. Put your reading in `implication`, never in `statement`.
- Press release = announcement happened ≠ value realized. Multiple outlets repeating one release are NOT independent corroboration; a regulator record, filing, registry, peer-reviewed paper or an independent investigation is.
- Every AI / data / robotics / automation claim carries `maturity` ∈ concept|prototype|pilot|operational|scaled|demonstrated_outcome|unknown, with the evidence that justifies the level.
- For every major finding, search explicitly for contrary evidence (`failure`, `delay`, `discontinued`, `complete response letter`, `lawsuit`, `criticism`, `impairment`, `write-down`) and record it in `contrary_evidence` / `contrary_source_ids`.
- Reporting periods explicit (J&J fiscal years end late Dec/early Jan; Takeda FY ends 31 March — "FY2025" = Apr 2025–Mar 2026). Never present a partial 2026 period as a full year.
- Source hierarchy T1 (filings, regulators, registries, peer-reviewed) > T2 (company technical/IR) > T3 (Reuters, FT, STAT, Endpoints, Fierce, BioPharma Dive, Nature/Science news) > T4 (expert commentary) > T5 (speculative; never as fact).
- Neutral on policy: document lobbying/advocacy/litigation; never infer impropriety or causal influence without credible substantiation.

## 2. Retrieval mechanics
- Prefer the `web_fetch` tool for reading pages (it passes bot challenges that block curl: investor.lilly.com, investor.jnj.com, fiercepharma.com, lda.senate.gov, opensecrets.org). Use `web_search` for discovery, then OPEN the page.
- Use the CLI for bulk/primary documents when you also want a stored hash:
  `$PY tools/evidence.py fetch "<url>" --grep "<term>" --store-raw --context 400 --max-hits 8` (run from `/Users/palrahma/Desktop/MEDICINE`). It respects a 1 s sleep; keep ≥1 s between requests to one host; max 2 attempts per URL then record `blocked|unavailable|paywalled`.
- SEC EDGAR for anything a company files: 8-K exhibits (earnings releases, deal announcements) via `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<CIK>&type=8-K&dateb=&owner=include&count=40` (CIKs: LLY 0000059478, JNJ 0000200406, ABBV 0001551152, Takeda 0001395064). Full-text search: `https://efts.sec.gov/LATEST/search-index?q="<phrase>"&forms=8-K` (JSON).
- 20 annual reports (FY2021–FY2025) are ALREADY on disk as plain text: `/Users/palrahma/Desktop/MEDICINE/New_mediciine/evidence_library/extracted_text/sec/*.txt` (500 KB–1 MB each). Use `grep -n -i "<term>" <file> | head` then `sed -n '<start>,<end>p'` to read the passage; cite `line N` as the locator. Their source records already exist in the canonical registry (`grep '"document_identifier"' …` or grep the accession number in `source_registry.jsonl`) — cite that `SRC-0000xx` rather than re-registering.
- ClinicalTrials.gov v2 API: `https://clinicaltrials.gov/api/v2/studies/<NCT>` (JSON). FDA: `https://www.accessdata.fda.gov/scripts/cder/daf/` and the yearly "Novel Drug Approvals" pages on fda.gov. PubMed: `https://pubmed.ncbi.nlm.nih.gov/?term=...`. EMA: `https://www.ema.europa.eu/en/medicines/...`.
- Do not bypass paywalls or logins. Paywalled: register `access_status: paywalled`, metadata only.

## 3. Writing your shard (your only registry write path)
Append JSON lines to `/Users/palrahma/Desktop/MEDICINE/New_mediciine/evidence_library/shards/<shard>/sources.jsonl` and `claims.jsonl` using your allocated ID range (sequential). Easiest: write small Python/JSON then
`$PY tools/evidence.py add-source --shard <shard> --json /path/to/src.json` and `add-claim` (they validate). Or append directly, then validate:
`$PY tools/evidence.py validate --shard <shard> --path New_mediciine/evidence_library/shards/<shard>/sources.jsonl` (0 errors required before you finish; same for claims.jsonl).
Field formats are in agent_protocols.md §2 (singular `domain`, lowercase `company` enums `eli_lilly|johnson_johnson|abbvie|takeda|industry|other`, `supporting_source_ids` as a list of IDs, `locator` string).
You MAY cite canonical IDs `SRC-0000xx` / `CLM-0000xx` in `supporting_source_ids` / report text; the validator accepts registry IDs.

## 4. Reports (Markdown, in your allowed directory only)
- Every material sentence ends with `[CLM-xxxxxx]` (one or more IDs). Sentences without an ID must be labelled *(INTERPRETATION)*, *(HYPOTHESIS)* or *(gap)*.
- Use relative links between your own files. Keep each file focused (one sub-domain per file). Headings: what is established / what is contested / what is unknown.
- Mandatory files: `map.md` (every file you wrote, one line each with link + one-line purpose), `evidence_gaps.md` (what you looked for and could not find/open: blocked URLs, unresolved questions, suggested next queries), plus the files named in your task.

## 5. Do NOT
- Write to: root `map.md`, `PROJECT_STATE.md`, `CONTINUE.md`, `COORDINATION.md`, `New_mediciine/map.md`, `New_mediciine/evidence_library/source_registry.jsonl` / `claims_registry.jsonl` / `conflicts.jsonl`, any other agent's shard or directory, `executive_application/`, `data/`, `strategy/`.
- Run `git commit`/`git add` (the Director commits). Do not delete or rewrite files you did not create, except where your task explicitly says you may replace `master_report.md`.
- Spend more than ~15 minutes on any single source. Loop on a blocked host. Pad with promotional content when primary questions remain open.

## 6. Budget and stop condition
Target 75–100 minutes of work. Stop when (a) your mandatory questions each have SUPPORTED / CONTRADICTED / INCONCLUSIVE status with evidence, or (b) you reach ~90% of budget — then write `evidence_gaps.md`, validate both shard files, and return the completion report in exactly this shape:

```
FILES WRITTEN: <relative paths, one per line>
SOURCES: <n> (retrieved <n>, metadata_only <n>, blocked/paywalled <n>)   CLAIMS: <n> (FACT <n>, other <n>)
VALIDATION: <paste the two validate output lines>
TOP 10 FINDINGS: <one line each, with claim IDs>
CONTRADICTIONS / FAILURES FOUND: <bullets with claim IDs>
EVIDENCE GAPS: <bullets>
RECOMMENDED NEXT RESEARCH: <bullets>
```
A completion report without validated shard files is a failed task.
