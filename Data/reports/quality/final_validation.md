# Final system validation — MEDICINE 2040 (session 2 close, 2026-11-21 ~20:15 IST)

Director (A0) sign-off against the master prompt's gates (§17) and quality standard (§25). Every check below was executed in this session; commands are given so a future agent can re-run them. "PASS" means the automated check passed; judgement calls are labelled as such.

## 1. Automated checks (re-runnable)

| Check | Command | Result |
|---|---|---|
| Registry schema, ID uniqueness, referential integrity, period discipline, T4/T5-only FACT rule | `python3 scripts/validate_registries.py` | **PASS** — 524 sources / 1,401 claims, 0 errors (warnings listed in `quality/citation_audits/registry_validation_2026-11-21.json`) |
| Shard-level validation (12 shards) | `~/.local/share/mise/installs/python/3.12/bin/python3 tools/evidence.py validate --shard <s> --path <file>` | 0 errors on every merged shard at merge time (`quality/citation_audits/shard_merge_2026-11-21.json`) |
| Every `[CLM-…]` cited in 192 Markdown files resolves | inline check (see RUN-0005) | **PASS** — 0 unknown references |
| Strategy JSON vs `strategy/DATA_CONTRACT.md`; every CLM/ASM/BET/RM/IVB id resolves | `python3 strategy/data/_check_ids.py` | **PASS** — 18 bets, 37 assumptions, 69 gates, 54 milestones, 5 scenarios; 0 unknown IDs |
| Council JSON (119 verdicts, 95 counterarguments) | `python3 strategy/critical_challenges/_check_council.py` | **PASS** (BET-18 explicitly listed as not independently reviewed) |
| Relative Markdown links | `python3 scripts/check_links.py` | **PASS** (report in `quality/coverage_reports/link_check_2026-11-21.json`) |
| Data pipeline (encyclopedia → 22 app datasets; fails on any unknown ID) | `python3 scripts/build_app_data.py` | **PASS** — 9/9 strategy files present |
| Application build + tests | `cd executive_application && npm run build && npm test` | **PASS** — 109 data-integrity + 145 route/Q&A tests, 0 failures |
| Single-file export | `python3 scripts/build_single_file.py` | **PASS** — `deliverables/MEDICINE_2040_Hub.html`, 8.5 MB, 22 datasets, verified loading from `file://` (screenshots in `quality/application_tests/screenshots/`) |
| Q&A negative tests | `tests/llm_probe.mjs` + route tests | **PASS** — "TuneLab revenue 2025" and "Takeda approved AI budget 2027" return the no-evidence state; retrieval-only and LLM paths both refuse to invent |
| Coverage ledger recomputed | `python3 scripts/update_coverage.py` | 85 computed company × source-family rows + 27 Director rows (`New_mediciine/research_coverage/coverage_summary.md`) |

## 2. Independent audits (not self-assessment)

| Audit | Scope | Outcome |
|---|---|---|
| A10 round 1 (`quality/citation_audits/audit_wave1_*.md`, `gate1_verdicts.md`, `quality/evaluation_results/wave1_scorecard.md`) | 99 claims re-inspected; 151 XBRL pairs reconciled; 7 controlled questions | 72 pass, 25 locator fixes, 1 label error (debt), 1 not-found (Strateos link); 146/151 reconcile (5 definitional); Gate 1: Lilly PASS, J&J / AbbVie CONDITIONAL PASS, Takeda FAIL (repairable) |
| A10-bis round 2 (`*_wave2.md`) | 88 claims + all 46 FDA approval dates + 43 CT.gov statuses re-checked live; ≥120 synthesis citations | All reachable numbers matched; 4 mis-cited IDs, 3 announcement-vs-regulator dates, 2 derived-number errors found; A12/A14/A11 ACCEPT, A7/A8 REVISE; `master_comparison.md` decision-grade with conditions |
| Director application | `scripts/apply_audit.py`, `scripts/apply_audit2.py` | 27 proposals accepted into `conflicts.jsonl` (110 records total); 82 claim amendments with `audit_history` (statements immutable); 2 new debt claims; policy/synthesis text repaired; dossiers v1.1 (A15) applied the Gate 1 repairs incl. Takeda's missing files |
| Strategic Council / Red Team (`strategy/critical_challenges/`) | 7 councils × 17 bets | 45 support / 64 conditional / 10 oppose; 17 disagreements; 19/85 robustness cells re-rated; 10 decision changes accepted by the Director (`DIRECTOR_DECISION_RECORD.md`) → strategy v2 |

**Gate status at close.** Gate 0 (operating system) PASS. Gate 1: Lilly PASS; J&J, AbbVie CONDITIONAL PASS with repairs applied in v1.1; Takeda repairs applied in v1.1 but **not re-audited** — formally still FAIL (repairable) until a third audit round confirms. Gate 2 (Takeda baseline + gaps documented) PASS — 16 capability areas classified, 14-item internal-validation backlog. Gate 3 (only accepted evidence feeds conclusions): the deliverables cite 184 claims, all SUPPORTED/PARTIALLY_SUPPORTED or used only for "no evidence" statements; INCONCLUSIVE claims are not used as facts. Application gate PASS.

## 3. Judgement against the §25 standard (Director's honest assessment)

| Question | Assessment |
|---|---|
| Research — what companies did vs their ambitions | Strong on financials, approvals, deals, LOE and policy (filings, FDA, CT.gov, courts). AI/robotics evidence is mostly company-reported by nature of the subject; the system says so (no demonstrated outcome at any of the four companies). |
| Evidence traceability | Every number in dossiers, comparisons, strategy and deliverables resolves to a claim → source → locator; 294 T1 sources. |
| Comparison — explains *why*, not ranks | `master_comparison.md` explains mechanisms and lists the rankings it refuses (LOE score, approvals per R&D dollar, margin/leverage, ecosystem "defensibility"). |
| Science | Approval dates, CRL reasons and trial statuses verified against regulator/registry records; peer-reviewed readouts read at abstract level only (limitation). |
| Business | Mechanisms (Humira contracting, incretin capacity, Stelara→Tremfya, Allergan synergies) are evidence-backed with numbers. |
| Technology maturity | 110 maturity-tagged claims; retags applied where the auditor disagreed; autonomous-lab reality check separates commodity stages from undemonstrated ones. |
| Strategy grounded in Takeda's position | Every bet carries a baseline class and IVB pointers; council challenge changed 10 decisions. |
| Capital allocation | Three portfolios with ranges and 37 explicit assumptions; no NPV (needs Takeda forecasts) — stated rather than faked. |
| Multiple futures | 5 scenarios + early-entry stress case; robustness published with council re-ratings. |
| Product | 11-pillar hub; insight → claim → source navigation; 197 reports in-app; Q&A grounded, zero-cost by default. |
| Persistence | `map.md`, `PROJECT_STATE.md`, `CONTINUE.md`, run logs, experiments log, briefs for every agent, 29 commits. |

## 4. Known gaps and limitations (carried forward, not hidden)
1. **Takeda Gate 1 re-audit pending** (repairs applied in v1.1, not independently re-checked).
2. **A7 (commercial) and A8 (policy) shards rated REVISE**: single-interested-source flag over-applied in A7; lobbying totals for J&J/AbbVie missing because the Senate LDA and OpenSecrets block scripted access; FEC totals not obtained (DEMO_KEY rate limit).
3. **Independent corroboration field is empty on almost all claims** — independence was assessed in prose and tiers, not recorded structurally; the rubric's "independence" dimension cannot exceed 2 until this is back-filled.
4. **Peer-reviewed sources read at abstract level**; no full-text safety tables.
5. **Leadership interviews**: only metadata and a handful of inspected transcripts.
6. **Unresolved conflicts** (kept, not forced): AbbVie Ventures founding date; Lilly robotic-lab start (2017 vs ~2020) and the Strateos link; Lilly 2024 lobbying (7.89m vs 8.43m); Medicare obesity access start (April vs July 2026); Entyvio statutory exclusivity date.
7. **No evidence found for**: installed bases of OTTAVA/MONARCH/VELYS; TuneLab uptake; NVIDIA–Lilly lab operating status; venture-arm fund sizes; competitor orexin landscape; Takeda Ventures/CEI scale.
8. **BET-18 (licensing channel)** is council-proposed and not independently reviewed.
9. **Strategy numbers are assumptions**: Takeda's actual budget, PTS and forecasts are not public; portfolios are proposals.
10. **Mobile layout** verified only by CSS review and headless Chrome at ≥1024 px; **LLM path from `file://`** requires `OLLAMA_ORIGINS=*` and was not browser-tested.
11. Subagent default tool-call cap (100) cost two wave-1 runs; later waves used 400 with save-as-you-go. Recorded in `research_methodology/research_runs/RUN-0004-wave1-multiagent.md`.

## 5. Verdict
The system is **usable, auditable and maintainable**: a future agent can open `map.md`, run the four validators above, and extend any shard without re-reading the encyclopedia. It is **not** finished research: items 1–8 above are the next session's queue (see `CONTINUE.md`).
