# Capability baseline

Research cutoff 2026-11-21. Takeda fiscal years run April-March (FY2025 = April 2025 to March 2026). Claim IDs resolve in `New_mediciine/evidence_library/shards/A5_takeda/claims.jsonl`; `CLM-000xxx` IDs resolve in the canonical `claims_registry.jsonl`. Only public sources were used.

The capability-area list is this agent's taxonomy (the master-prompt section 11 list was not available to A5); the Director should map it to the canonical list. An EVIDENCE_GAP is not a finding that the capability is missing.

| # | Capability area | Class | Evidence | Internal validation needed |
|---|---|---|---|---|
| 1 | GI / immunology franchise | EXISTING_STRENGTH | [CLM-005009, CLM-005012] | Entyvio erosion curve (IVB-004) |
| 2 | Plasma network and PDT manufacturing | EXISTING_STRENGTH | [CLM-005063, CLM-005064, CLM-005065, CLM-005060] | Yield, cost per litre (IVB-006) |
| 3 | Rare disease / orexin science | EXISTING_STRENGTH | [CLM-005048, CLM-005029, CLM-005032] | Pipeline refill (IVB-008) |
| 4 | Late-stage development execution | EXISTING_STRENGTH | [CLM-005042, CLM-005028, CLM-005033] | Cycle times (IVB-009) |
| 5 | External innovation / BD | EXISTING_STRENGTH (deal flow); organisation EVIDENCE_GAP | [CLM-005050, CLM-005036, CLM-005043, CLM-005052] | Ventures / CEI scope (IVB-007) |
| 6 | Portfolio discipline (stop decisions) | EXISTING_STRENGTH, with write-down cost | [CLM-005025, CLM-005024, CLM-005022] | Kill criteria |
| 7 | LOE replacement / revenue depth | EXISTING_BUT_UNDERDEVELOPED | [CLM-005015, CLM-005016, CLM-005017] | Launch forecasts (IVB-005) |
| 8 | New-brand launch execution | POTENTIAL_NEW_CAPABILITY (to be proven) | [CLM-005069, CLM-005074, CLM-005045] | Launch readiness |
| 9 | Enterprise data and AI platform | EXISTING_BUT_UNDERDEVELOPED (outcomes unproven) | [CLM-005058, CLM-005055, CLM-005057, CLM-005056] | Production vs pilot (IVB-001) |
| 10 | AI-enabled discovery / development | EVIDENCE_GAP | [CLM-005049, CLM-005053] | IVB-001, IVB-010 |
| 11 | Lab automation and robotics | EVIDENCE_GAP | [CLM-005067] | IVB-002 |
| 12 | Manufacturing quality | EXISTING_BUT_UNDERDEVELOPED (documented failure, closed) | [CLM-005020] | Inspection record (IVB-011) |
| 13 | Supply-chain AI | EVIDENCE_GAP (executive claim only) | [CLM-005057] | Scope and benefits |
| 14 | Patient services / market access | EVIDENCE_GAP | [CLM-005072] | IVB-013 |
| 15 | Cell therapy | Exited | [CLM-005025] | Partnering outcome |
| 16 | Cost transformation | EXISTING_BUT_UNDERDEVELOPED (plan, not yet realised) | [CLM-005077, CLM-005059, CLM-005078] | Realised savings (IVB-003) |

## v1.1 update
Row 5 (external innovation): Takeda Ventures, Inc. is a 100%-owned subsidiary with no public fund size [CLM-014052]. Row 6: cell-therapy write-off recognised at JPY 58.2bn [CLM-009084]. Rows 9-13 (data, AI, automation): wave-2 evidence adds manufacturing AI agents and process pilots at operational or pilot maturity, still without outcome data [CLM-014041] [CLM-014042] [CLM-014043]; robotics remains EVIDENCE_GAP [CLM-005067]. Row 16: restructuring cost series 150bn → 170.0bn → 160.0bn [CLM-005078]. Row 14 transfer analysis: [transfer_to_takeda.md](../../../industry_transformation/commercial_patient/transfer_to_takeda.md).

## Reading notes
*(INTERPRETATION)* Evidenced strengths are franchise scale, plasma operations and delivery of three late-stage approvals or filings on a pre-announced timetable. The least-evidenced areas (AI outcomes, automation) are those later strategy modules may target, so recommendations there must be labelled ASSUMPTION until the backlog is validated.
