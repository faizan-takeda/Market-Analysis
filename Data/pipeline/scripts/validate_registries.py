#!/usr/bin/env python3
"""Validate source/claim registries: schema, id uniqueness, referential integrity,
period discipline, locator presence. Exit 1 on any error. Writes a JSON report to
quality/citation_audits/registry_validation_<date>.json.
"""
import json, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from registry import read_jsonl, load_schema, SRC_PATH, CLM_PATH, ROOT  # noqa

PERIOD_RE = re.compile(r"^(FY\d{4}|Q[1-4]-\d{4}|CY\d{4}|TAK-FY\d{4}|9M-\d{4}|6M-\d{4}|H[12]-\d{4}|\d{4}-\d{2}-\d{2}|\d{4})$")


def check(rec, schema):
    errs = []
    for k in schema["required"]:
        if k not in rec or rec[k] in (None, "", []):
            errs.append(f"missing {k}")
    for k, p in schema["properties"].items():
        if k in rec and rec[k] is not None and "enum" in p and rec[k] not in p["enum"]:
            errs.append(f"{k} not in enum")
        if k in rec and isinstance(rec[k], str) and "pattern" in p and not re.match(p["pattern"], rec[k]):
            errs.append(f"{k} bad pattern")
    return errs


def main():
    s_schema = load_schema("source.schema.json"); c_schema = load_schema("claim.schema.json")
    sources = read_jsonl(SRC_PATH); claims = read_jsonl(CLM_PATH)
    errors, warnings = [], []
    sids = {}
    for s in sources:
        for e in check(s, s_schema):
            errors.append(f"{s.get('source_id')}: {e}")
        if s.get("source_id") in sids:
            errors.append(f"duplicate source id {s['source_id']}")
        sids[s.get("source_id")] = s
        if s.get("reporting_period") and not PERIOD_RE.match(s["reporting_period"]):
            warnings.append(f"{s['source_id']}: unusual reporting_period {s['reporting_period']!r}")
        if s.get("access_status") == "retrieved" and not (s.get("local_document_path") or s.get("local_extracted_text_path") or s.get("content_sha256")):
            warnings.append(f"{s['source_id']}: retrieved but no local artifact/hash recorded")
        lp = s.get("local_document_path")
        if lp and not os.path.exists(os.path.join(ROOT, lp)):
            errors.append(f"{s['source_id']}: local_document_path missing on disk: {lp}")
    cids = set()
    for c in claims:
        for e in check(c, c_schema):
            errors.append(f"{c.get('claim_id')}: {e}")
        if c.get("claim_id") in cids:
            errors.append(f"duplicate claim id {c['claim_id']}")
        cids.add(c.get("claim_id"))
        for ss in c.get("supporting_sources", []):
            if ss.get("source_id") not in sids:
                errors.append(f"{c['claim_id']}: unknown source {ss.get('source_id')}")
            if len(ss.get("locator", "")) < 3:
                errors.append(f"{c['claim_id']}: locator missing")
        for x in c.get("independent_corroboration", []) or []:
            if x not in sids:
                errors.append(f"{c['claim_id']}: unknown corroboration source {x}")
        if c.get("value") is not None and not c.get("reporting_period") and not c.get("event_date"):
            warnings.append(f"{c['claim_id']}: numeric claim without reporting_period/event_date")
        if c.get("kind") == "FACT" and c.get("status") == "SUPPORTED":
            tiers = {sids[ss["source_id"]].get("credibility_tier") for ss in c["supporting_sources"] if ss["source_id"] in sids}
            if tiers and tiers <= {"T4_expert_opinion", "T5_speculative"}:
                errors.append(f"{c['claim_id']}: SUPPORTED FACT rests only on T4/T5 sources")
            if tiers == {"T2_company_published"} and not c.get("single_interested_source") and not c.get("independent_corroboration"):
                warnings.append(f"{c['claim_id']}: company-only support not flagged single_interested_source")
    report = {
        "run_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "sources": len(sources), "claims": len(claims),
        "errors": errors, "warnings": warnings,
        "result": "PASS" if not errors else "FAIL",
    }
    outdir = os.path.join(ROOT, "quality", "citation_audits"); os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"registry_validation_{datetime.date.today().isoformat()}.json")
    with open(out, "w") as f:
        json.dump(report, f, indent=2)
    print(json.dumps({k: v for k, v in report.items() if k != "warnings"}, indent=2))
    if warnings:
        print(f"{len(warnings)} warning(s); see {out}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
