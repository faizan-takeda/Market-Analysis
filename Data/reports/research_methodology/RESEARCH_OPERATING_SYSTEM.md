# RESEARCH OPERATING SYSTEM — MEDICINE 2040

Status: v1.0, initialized 2026-11-21 (Phase 0). Owner: A0 Research Director.
This document is the constitution of the project. Every agent reads it (via `.kiro/steering/`) before working.

## 1. What this system is for

A long-horizon, source-grounded intelligence system about three competitors (Eli Lilly, Johnson & Johnson, AbbVie), a public baseline for Takeda, and a forward strategy for Takeda 2027-2040. The filesystem under `~/Desktop/MEDICINE/` is the system of record; conversation context is scratch memory.

## 2. Principles adopted, and where they came from

| Principle | Origin (inspected 2026-11-21) | How we implement it |
|---|---|---|
| Fixed evaluation, mutable experiment. Keep what improves the metric, discard what does not, log everything. | Karpathy, `autoresearch/program.md`: fixed `prepare.py` eval vs. mutable `train.py`; `results.tsv` with keep/discard/crash per commit | `research_methodology/evaluation_rubric.md` is the fixed evaluator; each research pass is an "experiment" logged in `research_runs/research_experiments.jsonl` with status keep/revise/reject. Failed directions are kept in the log, never deleted. |
| Simplicity criterion: an improvement that adds ugly complexity is not worth it. | Karpathy | Zero-dependency Python tooling; no custom agent framework; plain JSONL registries. |
| Orchestrator-worker; subagents as parallel "intelligent filters" with isolated contexts; the lead synthesizes. Token spend drives quality; parallelize breadth-first work. | Anthropic, *How we built our multi-agent research system* | A0 (this session) delegates bounded research to specialist subagents via Kiro Crew `spawn_run`; each writes to its own directory + ID-ranged shard; A0 merges (single writer). |
| Persist the plan outside the context window; compress through written artifacts. | Anthropic (Memory in LeadResearcher; context > 200k truncation) | `PROJECT_STATE.md`, `CONTINUE.md`, `map.md`, shards on disk after every batch. |
| Long-running agents: initializer sets up environment + feature list marked failing; later sessions do one increment, leave clean state, commit with messages; never mark done without end-to-end test. | Anthropic, *Effective harnesses for long-running agents* | Phase 0 = initializer. `.kiro/specs/medicine-2040/tasks.md` is the feature list (all tasks start `[ ]`). Git commits per batch. Application gate requires scripted tests, not eyeballing. |
| Citation agent pass separate from writing; verify claims against documents. | Anthropic | A10 Independent Evidence Auditor runs on completed batches; `evidence.py linkcheck` + passage re-inspection. |
| Decompose the question, bound delegation, ground synthesis in sources, guardrails, re-check conclusions. | OpenAI *Deep research* and *Practical guide to building agents* (summarised from prior knowledge; pages not re-fetched this session — recorded as a limitation) | Every delegation carries: question, scope, source IDs, output dir, evidence standard, completion criteria, handoff artifacts (see `agent_protocols.md`). |
| Use native capabilities instead of building a framework. | Kiro docs: `kiro.dev/docs/crew/features/subagents/` (inspected): subagents are isolated sessions, up to 3h / 1000 tool calls, auto-sized concurrency, durable queue, delegation gate reasons (`parent_parallel`, `bulk_data`, `fresh_context`, `specialist`, `user_requested`) | Delegation uses `spawn_run` with `tasks[]`. Steering files in `.kiro/steering/`. Spec in `.kiro/specs/medicine-2040/`. |

## 3. The research loop (operational form of Karpathy's loop)

```
frame question -> source hierarchy -> broad search -> open primary -> extract+normalize (shard)
   -> challenge (contrary evidence) -> evaluate (rubric) -> decide status -> persist -> next
```

Hypothesis status vocabulary: `SUPPORTED / PARTIALLY_SUPPORTED / CONTRADICTED / INCONCLUSIVE / NEEDS_MORE_RESEARCH`.
Batch status vocabulary: `ACCEPT / REVISE / RESEARCH_FURTHER / BLOCKED`.
Claim kind vocabulary (never collapsed): `FACT / INTERPRETATION / HYPOTHESIS / SCENARIO / RECOMMENDATION`.
Stop rule: continue a loop only when another pass can materially change an answer (information gain), not because more web pages exist.

## 4. Evidence standard (summary; full rules in `source_quality_rules.md`)

1. A cited source was actually opened; the record stores a verbatim `inspected_passage` (<= 600 chars) and a locator (section/table/page/timestamp).
2. Source hierarchy T1 (filings, regulators, registries, peer review) > T2 (company technical) > T3 (independent reputable) > T4 (expert commentary) > T5 (speculative, never fact).
3. Press releases prove an announcement happened, not that value was realized. Multiple outlets repeating one press release = one source.
4. Single-interested-party claims are flagged `single_interested_source: true`.
5. Conflicts are preserved in `conflicts.jsonl`, never silently resolved.
6. Numeric claims carry the reporting period; FY2026 is never treated as a full year.
7. No invented URLs, pages, numbers, quotes, or transcripts. If inaccessible: `access_status: blocked|paywalled|unavailable|metadata_only` and move on.

## 5. Evaluation criteria (the fixed evaluator)

A research batch is scored on 8 axes in `evaluation_rubric.md`: source authenticity, relevance, coverage, independence of corroboration, temporal accuracy, contradiction handling, traceability, significance. Scores are ordinal (0-2) with written justification; no fabricated numeric confidence.

Golden questions (independently seeded, `quality/evaluation_results/golden_questions_seed.json`, 26 items) are answered from the encyclopedia only; each answer is checked against its cited claim IDs. Negative tests ask questions the corpus should NOT be able to answer, to catch confabulation.

## 6. Architecture decisions (with reasons)

| Decision | Choice | Why |
|---|---|---|
| Registry format | JSONL shards per agent + canonical JSONL registries; optional SQLite index built by pipeline | Append-only, diff-able in git, parallel-safe via ID ranges, zero dependencies |
| ID ranges | SRC/CLM-001000.. Lilly, 002000.. J&J, 003000.. AbbVie, 004000.. EDGAR, 005000.. Takeda, 006000.. AI/robotics, 008000.. policy, 010000.. audit, 011000.. strategy | Prevents collisions without locks |
| Single writer | Only A0 runs `evidence.py merge`; only A0 edits `map.md`, `PROJECT_STATE.md`, registries | Avoids corrupted shared files under parallel execution |
| Deterministic extraction first | SEC XBRL (`tools/edgar_financials.py`) and ClinicalTrials.gov v2 API (`tools/ctgov_pipeline.py`) run as scripts, not LLM reading | Highest-value facts with zero hallucination surface |
| Application stack | Static HTML + ES-module JavaScript + vendored D3 v7, data as generated JSON, Python `http.server` launcher bound to 127.0.0.1; **no build step** | Installed env: Node 20/24, Python 3.12, no Playwright. React/TS/Vite was considered and rejected for this phase: a 300 MB `node_modules` and a build toolchain reduce the chance that a future agent can reopen the project months later and run it. Upgrade path documented in `executive_application/README.md`. |
| Python interpreter | `~/.local/share/mise/installs/python/3.12/bin/python3` (the `python3` shim fails under Rosetta/xcrun on this host) | Recorded so continuation sessions do not re-debug |
| Git | `arch -arm64 /usr/bin/git` (shell runs as i386 under Rosetta; git needs arm64) | Same |

## 7. Environment capability record (inspected 2026-11-21 16:50 IST)

- Host: macOS 26.7.3, Apple silicon (14 CPU, 48 GB), shell under Rosetta (`arch` = i386).
- Kiro: `kiro-cli 3.5.0`, Kiro Crew / MeshClaw 3.4.0 dashboard runtime; subagents via `spawn_run`; lead model claude-fable-5.1 (recorded by the runtime as the current model).
- Reachable: SEC EDGAR (`data.sec.gov` 200), ClinicalTrials.gov v2 API (200), npm registry (200), jsdelivr CDN (200), general web via `web_fetch`/`web_search`.
- Blocked/limited: `investor.lilly.com` returns 403 to scripted clients (use SEC 8-K exhibits and lilly.com newsroom); `lda.senate.gov` API returns Access Denied without a registered key (lobbying totals must come from alternative public sources and be flagged); openFDA sponsor-name search needs exact registrant strings.
- Not available: Playwright browser automation (UI tests are scripted data/link/structure tests, plus manual check instructions).

## 8. Gates

- Gate 0 (this doc + schemas + maps + state): PASSED when `PROJECT_STATE.md` says so.
- Gate 1: company dossier accepted only with verified source records, 5-year timeline, financial reconciliation to EDGAR, balanced success/failure analysis, evidence-gap report.
- Gate 2: Takeda baseline + information gaps documented before capital allocation recommendations.
- Gate 3: only evidence-accepted material feeds executive conclusions and the application.
- Application gate: scripted checks in `quality/application_tests/` pass; no placeholder data.

## 9. Known limitations of this operating system (honest list)

- Subagents cannot be forced to open every source; the auditor samples and link-checks, so some records may be metadata-only. They are labelled as such.
- The Senate LDA API block means lobbying figures are second-hand unless the House disclosure site is reachable; treat as T3 and flag.
- The 2026 study-window end (2026-11-21) includes partial-year disclosures only.
- Evaluation is partially self-generated; the 26 golden questions were seeded by an earlier scaffold, not by this session, which gives some independence but not full independence.


## 10. Amendments adopted in session 2 (2026-11-21)
**Status amendment rule.** A claim's `statement` is immutable. The Director may amend `status`, `maturity`, `basis`, `event_date`, `single_interested_source`, `implications` and add a `correction` ONLY when (a) an independent auditor proposed it in a `conflicts_proposed_*.jsonl` file, (b) the change is applied by a script (`scripts/apply_audit*.py`) that appends an `audit_history` entry to the record and a line to `conflicts.jsonl`. Contradictory new evidence still goes in as a new claim linked through `conflicts.jsonl`.
**Multi-agent operation.** Shard-isolated specialist agents (ID ranges in `agent_protocols.md`), single-writer merge (`scripts/merge_shards.py`), one independent audit round per wave, fresh-context synthesis and council. Subagent default tool-call cap is 100 — briefs must raise it and require save-as-you-go.
**No derived numbers in prose.** Durations, counts and percentages computed by an author must either be registered as a claim or be labelled INTERPRETATION with the inputs' claim IDs (three such errors were caught by audit round 2).
**Announcement ≠ regulator date.** Approval dates are taken from FDA/EMA records; company announcement dates are recorded separately (three corrections in round 2).
