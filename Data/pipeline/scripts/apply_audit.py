#!/usr/bin/env python3
"""Director (A0) application of the A10 wave-1 audit.

Rules applied (see RESEARCH_OPERATING_SYSTEM.md §4 'status amendment rule'):
- `statement` text is never edited. Corrections live in a `correction` field and in conflicts.jsonl.
- `status`, `maturity`, `basis`, `single_interested_source`, `implications`, `correction` may be amended by the
  Director; every amendment appends an entry to the record's `audit_history` and a line to conflicts.jsonl.
- Every A10 proposal is appended to conflicts.jsonl with the Director's decision (accepted / accepted_with_change / deferred).
Idempotent: amendments carry an `audit_ref`; re-running skips ones already applied.
"""
import datetime, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from registry import read_jsonl, CLM_PATH, EL  # noqa

CONF = os.path.join(EL, "conflicts.jsonl")
PROPOSED = os.path.join(EL, "conflicts_proposed_A10.jsonl")
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
REF = "A10-wave1-2026-11-21"

DEBT_IDS = [f"CLM-0000{n}" for n in range(66, 71)] + [f"CLM-0001{n}" for n in range(28, 33)] + ["CLM-003042"]
DEBT_NOTE = ("Label correction (A10): the value is total long-term debt INCLUDING the current portion (XBRL tag us-gaap:LongTermDebt), "
             "not the balance-sheet non-current amount. Non-current FY2025: AbbVie 58,941; J&J 39,438 (USD m). Number itself is correct.")
JNJ_T2_ONLY = ["CLM-002037", "CLM-002039", "CLM-002040", "CLM-002041", "CLM-002044", "CLM-002060", "CLM-002061", "CLM-002064"]
MATURITY_RETAG = {  # proposal 12 + table 3 of audit_wave1_status_discipline.md
    "CLM-006022": None, "CLM-006026": "OPERATIONAL", "CLM-006047": None, "CLM-006049": None, "CLM-006051": None, "CLM-006020": "PILOT",
    "CLM-000246": None, "CLM-000252": None, "CLM-000278": "CONCEPT", "CLM-000279": None, "CLM-000286": "OPERATIONAL",
    "CLM-006015": None, "CLM-006025": None, "CLM-006036": None, "CLM-006045": "CONCEPT", "CLM-006046": None, "CLM-006050": "PILOT",
    "CLM-006053": None, "CLM-006054": "OPERATIONAL", "CLM-006057": None, "CLM-006058": None, "CLM-006059": None,
    "CLM-005049": "PROTOTYPE", "CLM-005054": "CONCEPT", "CLM-005062": None, "CLM-005063": None, "CLM-005065": None,
    "CLM-005066": None, "CLM-005067": None, "CLM-005068": None,
}
MATURITY_NOTE = {"CLM-006022": "workforce-training metric, not a deployment", "CLM-006047": "describes Recursion, not one of the four companies",
                 "CLM-006049": "describes Exscientia/BenevolentAI, not one of the four companies", "CLM-006051": "describes Zymergen, not one of the four companies",
                 "CLM-006020": "single CIO interview sentence, no baseline: self-reported pilot-level evidence"}

AMEND = {  # claim_id -> dict of field amendments (+ correction text)
    "CLM-006017": {"status": "NEEDS_MORE_RESEARCH", "correction": "A10: neither cited BiopharmaTrend page mentions Strateos or a ~2020 launch; they date the Life Sciences Studio to 2017 (USD 90m). The Strateos link and 2020 date are unsupported until the Fierce article (403) is opened."},
    "CLM-009022": {"status": "SUPPORTED", "correction": "A10 resolved: 874.9 (FY2021 10-K) vs 970.1 (FY2022 10-K comparative) is a line-item definition change (FY2022 widened the line to include development milestones, +95.2); both figures are correct on their own basis."},
    "CLM-000284": {"status": "PARTIALLY_SUPPORTED", "correction": "A10: the J&J release says Memorial Hermann 'will be the first hospital to install' OTTAVA; completion of the installation is not shown. Treat as announced installation site, not a completed install; do not derive 'IDE-to-install' durations from it."},
    "CLM-000286": {"status": "PARTIALLY_SUPPORTED", "correction": "A10: 'regulator-verified' rests on J&J releases for OTTAVA/VELYS/MONARCH. openFDA 510(k) records exist for MONARCH (K260382, K243219) and VELYS (K260480, K240211); the OTTAVA De Novo (DEN250068, per A14 CLM-014022) is from a J&J release, not yet opened in an FDA database."},
    "CLM-006054": {"status": "PARTIALLY_SUPPORTED", "correction": "A10: wording stronger than the sources support (see audit_wave1_reinspection.md)."},
    "CLM-005078": {"status": "PARTIALLY_SUPPORTED", "correction": "A10: the restructuring-cost series is ~JPY 150bn (25 Mar 2026 estimate) -> JPY 170.0bn (original FY2026 forecast, May 2026) -> JPY 160.0bn (revised, Oct 2026); 170bn is Takeda's own figure, not a press figure."},
    "CLM-005025": {"correction": "A10: JPY 58.0bn was the October 2025 announced expectation; the recognised impairment in the FY2025 20-F is JPY 58.2bn (CLM-009100). The '137 Massachusetts roles' element could not be re-verified (Fierce 403)."},
    "CLM-000280": {"implications": "An ecosystem/platform move: Lilly offers proprietary models to biotechs in exchange for data contributions (data-for-access), analogous in intent to developer-platform strategies. The corpus shows no revenue or asset outcome from TuneLab; whether it yields assets is unproven."},
    "CLM-001014": {"basis": "acquired IPR&D EXPENSE as reported in the income statement (not cash paid)"},
    "CLM-000247": {"basis": "cash paid for acquired IPR&D (cash-flow statement); differs from the expensed IPR&D line (2.91 / 3.28 / 3.8 bn for 2025 / 2024 / 2023)"},
    "CLM-009000": {"basis": "acquired IPR&D expense (income statement); cash-paid basis differs (see CLM-000247)"},
    "CLM-009002": {"correction": "A10: USD 3.2bn is the announced deal value; the audited IPR&D charge was USD 2.55bn and cash paid USD 3.35bn — different measures, not a contradiction."},
    "CLM-009001": {"correction": "A10: headline deal values and expensed IPR&D charges are different measures (see CLM-009002)."},
    "CLM-003086": {"correction": "A10: USD 18.5bn = consideration transferred for ImmunoGen+Cerevel; USD 17.5bn net of cash acquired. ImmunoGen alone: 10.1bn announced total value, 9.8bn consideration, 9.2bn net of cash."},
    "CLM-009074": {"status": "INCONCLUSIVE", "correction": "A10: AbbVie Ventures founding 2009 ('investing since 2009') vs ~2015 ('ten years ago') unresolved; impact-report PDF not readable (403 / no extractable text)."},
    "CLM-009101": {"status": "INCONCLUSIVE", "correction": "See CLM-009074 (founding-date conflict unresolved)."},
}
for cid in [f"CLM-0000{n}" for n in range(26, 31)]:
    AMEND.setdefault(cid, {})["basis"] = "consolidated net earnings (us-gaap:ProfitLoss / NetIncomeLoss as tagged); A4 shard uses net earnings attributable to AbbVie (differs by noncontrolling interest, e.g. 11,549 vs 11,542)"
for cid in ["CLM-004108", "CLM-004119", "CLM-004130", "CLM-004141", "CLM-004152"]:
    AMEND.setdefault(cid, {})["basis"] = "net earnings attributable to AbbVie; RUN-0001 claims use consolidated net earnings (definitional difference)"
for cid in DEBT_IDS:
    AMEND.setdefault(cid, {})["correction"] = DEBT_NOTE
    AMEND[cid]["basis"] = "total long-term debt including current portion (us-gaap:LongTermDebt)"
for cid in JNJ_T2_ONLY:
    AMEND.setdefault(cid, {})["single_interested_source"] = True
for cid, m in MATURITY_RETAG.items():
    AMEND.setdefault(cid, {})["maturity"] = m
    if cid in MATURITY_NOTE:
        AMEND[cid]["correction"] = (AMEND[cid].get("correction", "") + " A10 maturity retag: " + MATURITY_NOTE[cid]).strip()


def main():
    claims = read_jsonl(CLM_PATH)
    idx = {c["claim_id"]: c for c in claims}
    missing = [k for k in AMEND if k not in idx]
    if missing:
        print("WARNING unknown claim ids:", missing)
    log = []
    n_changed = 0
    for cid, changes in AMEND.items():
        c = idx.get(cid)
        if not c:
            continue
        hist = c.setdefault("audit_history", [])
        if any(h.get("audit_ref") == REF for h in hist):
            continue
        before = {k: c.get(k) for k in changes}
        if all(c.get(k) == v for k, v in changes.items()):
            continue
        c.update(changes)
        c["last_verified"] = NOW[:10]
        hist.append({"audit_ref": REF, "at": NOW, "by": "A0", "changed": {k: {"from": before[k], "to": v} for k, v in changes.items()}})
        log.append({"type": "audit_amendment", "audit_ref": REF, "claim_id": cid, "changed": hist[-1]["changed"], "recorded": NOW, "by": "A0"})
        n_changed += 1
    with open(CLM_PATH, "w") as f:
        for c in claims:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    # accept proposals into conflicts.jsonl
    existing = read_jsonl(CONF)
    have = {(e.get("type"), tuple(e.get("claim_ids") or []), e.get("issue")) for e in existing}
    n_prop = 0
    for p in read_jsonl(PROPOSED):
        key = ("audit_proposal", tuple(p.get("claim_ids") or []), p.get("issue"))
        if key in have:
            continue
        decision = "accepted"
        if "AbbVie Ventures" in (p.get("issue") or ""):
            decision = "accepted (left INCONCLUSIVE; source unreadable)"
        log.append({"type": "audit_proposal", "audit_ref": REF, **p, "director_decision": decision, "recorded": NOW, "by": "A0"})
        n_prop += 1
    with open(CONF, "a") as f:
        for e in log:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(json.dumps({"claims_amended": n_changed, "proposals_recorded": n_prop, "conflict_records_total": len(existing) + len(log)}))


if __name__ == "__main__":
    main()
