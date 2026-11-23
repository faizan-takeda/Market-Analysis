#!/usr/bin/env python3
"""Director (A0) application of the A10-bis (round 2) audit. Same rules as apply_audit.py:
statement text immutable; status/maturity/basis/event_date/single_interested_source/correction amendable with
audit_history; proposals appended to conflicts.jsonl; two new FACT claims registered through registry.add_claim
(Director ID range) for the non-current debt figures the synthesis layer quotes without a claim.
"""
import datetime, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from registry import read_jsonl, CLM_PATH, EL, add_claim  # noqa

CONF = os.path.join(EL, "conflicts.jsonl")
PROPOSED = os.path.join(EL, "conflicts_proposed_A10b.jsonl")
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
REF = "A10bis-wave2-2026-11-21"

AMEND = {
    "CLM-003063": {"event_date": "2026-09-25", "correction": "A10-bis: FDA approval of Juvmo (tavapadon) is dated 2026-09-25 in the FDA record (CLM-012017); 2026-09-28 is AbbVie's announcement date."},
    "CLM-000283": {"event_date": "2026-07-21", "correction": "A10-bis: FDA De Novo DEN250068 decision date is 2026-07-21 (receipt 2025-12-18); 2026-07-22 is J&J's announcement date (see CLM-014022)."},
    "CLM-006029": {"event_date": "2026-07-21", "correction": "A10-bis: De Novo granted 2026-07-21 per FDA record; 2026-07-22 is the J&J announcement."},
    "CLM-002049": {"correction": "A10-bis: FDA received the OTTAVA De Novo submission on 2025-12-18; 2026-01-07 is the date of J&J's statement. The '24 months IDE-to-install' derivation is withdrawn (installation announced, not completed)."},
    "CLM-009044": {"event_date": "2025-04-29", "correction": "A10-bis: FDA approved IMAAVY (nipocalimab, BLA761430) on 2025-04-29 (CLM-012011); 2025-04-30 is the company announcement."},
    "CLM-000050": {"basis": "acquired IPR&D and milestones expense (upfronts 4,808 + milestones 208 = 5,016; XBRL)"},
    "CLM-003045": {"basis": "upfront charges only (4,808); excludes 208 of milestones included in the XBRL total 5,016 (CLM-000050)"},
    "CLM-012137": {"correction": "A10-bis: the ClinicalTrials.gov completion date postdates Takeda's October 2023 topline disclosure and withdrawal (CLM-012121); registry dates lag company decisions."},
    "CLM-012107": {"correction": "A10-bis: registry status lags the company decision; Lilly's FY2023 10-K lists the programme as discontinued (CLM-012136). Use the 10-K for status, the registry for dates."},
    "CLM-011000": {"basis": "unaudited company marketing figure (blog); the FY2026 10-K figure is 7.5 million (CLM-011001)"},
    "CLM-014073": {"maturity": "PILOT", "single_interested_source": True, "status": "PARTIALLY_SUPPORTED", "correction": "A10-bis: a former CEO's interview estimate (~30% shorter development) with no baseline or method; not a demonstrated outcome."},
    "CLM-014043": {"maturity": None, "correction": "A10-bis: usage/training percentages are adoption metrics, not a deployment maturity level (consistent with the round-1 retag of J&J course completions)."},
    "CLM-014030": {"maturity": None, "correction": "A10-bis: asset-acquisition accounting claim, not an AI/robotics capability."},
    "CLM-014025": {"maturity": "OPERATIONAL", "correction": "A10-bis: openFDA 510(k) shows substantial equivalence only; 'AI-powered' features are company marketing."},
    "CLM-000286": {"correction": "A10-bis (adds to round 1): 'regulator-verified milestone and a commercial installation' is stale — the installation is announced, not completed; the regulator record is the De Novo grant (2026-07-21)."},
    "CLM-008001": {"status": "PARTIALLY_SUPPORTED", "correction": "A10-bis: USD 8.43m (shareholder-proponent summary) vs 7.89m (company report, CLM-008000) unresolved until the Senate LDA database is opened."},
    "CLM-001036": {"correction": "A10-bis: '1 April 2026' is the earliest possible start stated in Lilly's 6 Nov 2025 release; the FY2025 10-K states 1 July 2026 (CLM-000251). Wording difference, not resolved."},
    "CLM-008027": {"correction": "A10-bis: see CLM-001036 — April (release, earliest) vs July (10-K) start date for Medicare obesity access."},
    "CLM-002020": {"basis": "final FY2022 charge for AD and HS (~USD 0.8bn); the FY2021 filing's ~0.6bn was the AD-only estimate (CLM-012109)"},
}
for cid in ["CLM-014008", "CLM-014009", "CLM-014010", "CLM-014011", "CLM-014012", "CLM-014015", "CLM-014020"]:
    AMEND.setdefault(cid, {})["single_interested_source"] = True

NEW_CLAIMS = [
    {"statement": "AbbVie's balance-sheet non-current long-term debt and finance lease obligations were USD 58,941 million at 2025-12-31 (USD 60,340 million at 2024-12-31), compared with total long-term debt including the current portion of USD 64,503 million (XBRL us-gaap:LongTermDebt).",
     "kind": "FACT", "companies": ["ABBV"], "domains": ["financials"], "entities": ["AbbVie"],
     "supporting_sources": [{"source_id": "SRC-000003", "locator": "Consolidated balance sheet and debt note; extracted_text/sec/ABBV_10-K_2025-12-31_0001551152-26-000008.txt lines 1372 and 2063"}],
     "independent_corroboration": [], "single_interested_source": False, "contrary_evidence": [], "value": 58941, "unit": "USD_millions",
     "reporting_period": "FY2025", "event_date": "2025-12-31", "basis": "non-current portion (balance sheet)", "status": "SUPPORTED",
     "confidence_rationale": "Audited balance-sheet line in the SEC-filed 10-K; registered by the Director after A10-bis found the synthesis layer quoting it without a claim.",
     "maturity": None, "last_verified": NOW[:10], "related_reports": ["New_mediciine/cross_company_analysis/master_comparison.md"], "implications": None,
     "added_by": "A0", "run_id": "RUN-0005-audit-repairs"},
    {"statement": "Johnson & Johnson's balance-sheet long-term debt (Note 7, non-current) was USD 39,438 million at 2025-12-28 (USD 30,651 million at 2024-12-29), compared with total long-term debt including the current portion of USD 41,438 million (XBRL us-gaap:LongTermDebt).",
     "kind": "FACT", "companies": ["JNJ"], "domains": ["financials"], "entities": ["Johnson & Johnson"],
     "supporting_sources": [{"source_id": "SRC-000010", "locator": "Consolidated balance sheet and Note 7; extracted_text/sec/JNJ_10-K_2025-12-28_0000200406-26-000016.txt lines 1203 and 2038"}],
     "independent_corroboration": [], "single_interested_source": False, "contrary_evidence": [], "value": 39438, "unit": "USD_millions",
     "reporting_period": "FY2025", "event_date": "2025-12-28", "basis": "non-current portion (balance sheet)", "status": "SUPPORTED",
     "confidence_rationale": "Audited balance-sheet line in the SEC-filed 10-K; registered by the Director after A10-bis found the synthesis layer quoting it without a claim.",
     "maturity": None, "last_verified": NOW[:10], "related_reports": ["New_mediciine/cross_company_analysis/master_comparison.md"], "implications": None,
     "added_by": "A0", "run_id": "RUN-0005-audit-repairs"},
]


def main():
    claims = read_jsonl(CLM_PATH)
    idx = {c["claim_id"]: c for c in claims}
    log, n = [], 0
    for cid, changes in AMEND.items():
        c = idx.get(cid)
        if not c:
            print("unknown", cid); continue
        hist = c.setdefault("audit_history", [])
        if any(h.get("audit_ref") == REF for h in hist):
            continue
        before = {k: c.get(k) for k in changes}
        if "correction" in changes and c.get("correction"):
            changes["correction"] = c["correction"] + " " + changes["correction"]
        c.update(changes); c["last_verified"] = NOW[:10]
        hist.append({"audit_ref": REF, "at": NOW, "by": "A0", "changed": {k: {"from": before[k], "to": v} for k, v in changes.items()}})
        log.append({"type": "audit_amendment", "audit_ref": REF, "claim_id": cid, "changed": hist[-1]["changed"], "recorded": NOW, "by": "A0"}); n += 1
    with open(CLM_PATH, "w") as f:
        for c in claims:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    new_ids = []
    existing = read_jsonl(CLM_PATH)
    have_stmt = {c["statement"] for c in existing}
    for rec in NEW_CLAIMS:
        if rec["statement"] in have_stmt:
            continue
        cid, _ = add_claim(dict(rec))
        new_ids.append(cid)
    conf_existing = read_jsonl(CONF)
    have = {(e.get("type"), tuple(e.get("claim_ids") or []), e.get("issue")) for e in conf_existing}
    n_prop = 0
    for p in read_jsonl(PROPOSED):
        key = ("audit_proposal", tuple(p.get("claim_ids") or []), p.get("issue"))
        if key in have:
            continue
        log.append({"type": "audit_proposal", "audit_ref": REF, **p, "director_decision": "accepted", "recorded": NOW, "by": "A0"}); n_prop += 1
    with open(CONF, "a") as f:
        for e in log:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(json.dumps({"claims_amended": n, "new_claims": new_ids, "proposals_recorded": n_prop}))


if __name__ == "__main__":
    main()
