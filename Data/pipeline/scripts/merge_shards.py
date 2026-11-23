#!/usr/bin/env python3
"""Single-writer merge: agent shards (tools/evidence.py schema, lowercase company enums)
-> canonical registries (scripts/registry.py schema, ticker company enums).

  python3 scripts/merge_shards.py                 # merge every shard under evidence_library/shards/
  python3 scripts/merge_shards.py A6_ai_robotics  # merge one shard
  python3 scripts/merge_shards.py --dry-run

Idempotent: records whose IDs already exist in the canonical registries are skipped. Shard IDs are
preserved (they live in disjoint ranges >= 001000; the Director's own counter stays < 001000).
Duplicate documents (same canonical_url as an existing source) are kept under their own ID and an
alias is appended to source_aliases.jsonl so either ID resolves. The original shard record is kept
verbatim under `shard_record` for auditability. Writes a merge report to quality/citation_audits/.
"""
import datetime, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from registry import read_jsonl, load_schema, validate, append, SRC_PATH, CLM_PATH, ROOT, EL  # noqa

SHARDS = os.path.join(EL, "shards")
ALIAS_PATH = os.path.join(EL, "source_aliases.jsonl")
COMPANY = {"eli_lilly": "LLY", "johnson_johnson": "JNJ", "abbvie": "ABBV", "takeda": "TAK",
           "industry": "INDUSTRY", "other": "INDUSTRY"}
CRED = {"T1_primary_official": "T1_primary_official", "T2_company_technical": "T2_company_published",
        "T3_independent_reputable": "T3_independent_reporting", "T4_expert_commentary": "T4_expert_opinion",
        "T5_speculative": "T5_speculative"}
# canonical maturity enum is upper-case; shard enum is lower-case
MATURITY = {"concept": "CONCEPT", "prototype": "PROTOTYPE", "pilot": "PILOT", "operational": "OPERATIONAL",
            "scaled": "SCALED", "demonstrated_outcome": "DEMONSTRATED_OUTCOME", "not_applicable": None, "unknown": None}


def adapt_source(r, shard):
    out = {
        "source_id": r["source_id"], "title": r["title"], "author_or_org": r.get("publisher"),
        "publisher": r["publisher"], "company": COMPANY.get(r["company"], "INDUSTRY"),
        "subject_category": [r["domain"]] if r.get("domain") else [],
        "source_type": r["source_type"], "credibility_tier": CRED.get(r["credibility"], r["credibility"]),
        "original_url": r.get("original_url"), "canonical_url": r["canonical_url"],
        "published_at": r.get("publication_date"), "reporting_period": r.get("reporting_period"),
        "retrieved_at": r.get("access_date"), "identifiers": {},
        "local_document_path": r.get("raw_path"), "local_extracted_text_path": r.get("extracted_text_path"),
        "content_sha256": r.get("sha256"), "access_status": r["access_status"],
        "rights": r.get("licensing"), "limitations": r.get("notes"),
        "inspected_passage": r.get("inspected_passage"), "locator": r.get("locator"),
        "added_by": shard, "run_id": f"WAVE1-{shard}", "merged_from_shard": shard,
        "merged_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    }
    if r.get("document_identifier"):
        out["identifiers"]["document_identifier"] = r["document_identifier"]
    for k in ("api_url", "doi", "nct_id", "accession"):
        if r.get(k):
            out["identifiers"][k] = r[k]
    # local paths must exist on disk or the canonical validator fails; drop stale ones but keep in shard_record
    for k in ("local_document_path", "local_extracted_text_path"):
        if out[k] and not os.path.exists(os.path.join(ROOT, out[k])):
            out[k] = None
    out["shard_record"] = r
    return out


def flatten_entities(e):
    if isinstance(e, dict):
        vals = []
        for v in e.values():
            vals += v if isinstance(v, list) else [v]
        return [str(x) for x in vals if x]
    if isinstance(e, list):
        return [str(x) for x in e if x]
    return []


def adapt_claim(c, shard):
    dates = c.get("dates") or {}
    rp = dates.get("period") or dates.get("reporting_period")
    if not rp and dates.get("fiscal_year"):
        rp = f"FY{dates['fiscal_year']}"
    contrary = c.get("contrary_evidence")
    if isinstance(contrary, str):
        contrary = [contrary] if contrary else []
    out = {
        "claim_id": c["claim_id"], "statement": c["statement"], "kind": c["kind"],
        "companies": sorted({COMPANY.get(x, "INDUSTRY") for x in c["companies"]}) or ["INDUSTRY"],
        "domains": [c["domain"]] if c.get("domain") else [],
        "entities": flatten_entities(c.get("entities")),
        "supporting_sources": [{"source_id": s, "locator": c.get("locator") or "see source record"} for s in c["supporting_source_ids"]],
        "independent_corroboration": [], "single_interested_source": bool(c.get("single_interested_source")),
        "contrary_evidence": contrary or [], "contrary_source_ids": c.get("contrary_source_ids") or [],
        "value": c.get("value"), "unit": c.get("unit"), "reporting_period": rp,
        "event_date": dates.get("event") or dates.get("period_end") or dates.get("event_date"),
        "basis": c.get("metric"), "status": c["status"], "confidence_rationale": c.get("confidence_rationale"),
        "maturity": MATURITY.get(c.get("maturity")) if c.get("maturity") else None,
        "last_verified": c.get("last_verified"), "related_reports": c.get("related_reports") or [],
        "implications": c.get("implication"), "tags": c.get("tags") or [], "locator": c.get("locator"),
        "added_by": shard, "run_id": f"WAVE1-{shard}", "merged_from_shard": shard,
        "merged_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    }
    out["shard_record"] = c
    return out


def downgrade_weakly_sourced(a, src_index):
    """Canonical rule: a SUPPORTED FACT may not rest only on T4/T5 sources. Downgrade at merge time
    (recorded in confidence_rationale) rather than rejecting the evidence."""
    tiers = {src_index[s["source_id"]].get("credibility_tier") for s in a["supporting_sources"] if s["source_id"] in src_index}
    if a["kind"] == "FACT" and a["status"] == "SUPPORTED" and tiers and tiers <= {"T4_expert_opinion", "T5_speculative"}:
        a["status"] = "PARTIALLY_SUPPORTED"
        a["confidence_rationale"] = (a.get("confidence_rationale") or "") + " [merge rule: only T4/T5 support -> PARTIALLY_SUPPORTED]"
    return a


def main(argv):
    dry = "--dry-run" in argv
    wanted = [a for a in argv if not a.startswith("--")]
    s_schema, c_schema = load_schema("source.schema.json"), load_schema("claim.schema.json")
    sources, claims = read_jsonl(SRC_PATH), read_jsonl(CLM_PATH)
    have_s = {s["source_id"] for s in sources}; have_c = {c["claim_id"] for c in claims}
    by_url = {s.get("canonical_url"): s["source_id"] for s in sources if s.get("canonical_url")}
    report = {"run_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "shards": {}, "errors": []}
    for shard in sorted(os.listdir(SHARDS)):
        if wanted and shard not in wanted:
            continue
        sdir = os.path.join(SHARDS, shard)
        if not os.path.isdir(sdir):
            continue
        srcs = read_jsonl(os.path.join(sdir, "sources.jsonl")); clms = read_jsonl(os.path.join(sdir, "claims.jsonl"))
        rep = {"sources_in_shard": len(srcs), "claims_in_shard": len(clms), "sources_added": 0, "claims_added": 0, "aliases": 0, "skipped_invalid": 0}
        new_s = []
        for r in srcs:
            if r["source_id"] in have_s:
                continue
            a = adapt_source(r, shard)
            try:
                validate(a, s_schema, a["source_id"])
            except SystemExit as e:
                rep["skipped_invalid"] += 1; report["errors"].append(f"{shard} {r['source_id']}: {e}"); continue
            new_s.append(a)
        for a in new_s:
            dup = by_url.get(a["canonical_url"])
            if not dry:
                append(SRC_PATH, a)
                if dup and dup != a["source_id"]:
                    append(ALIAS_PATH, {"alias_id": a["source_id"], "canonical_id": dup, "reason": "same canonical_url", "recorded": report["run_at"]})
            if dup and dup != a["source_id"]:
                rep["aliases"] += 1
            have_s.add(a["source_id"]); by_url.setdefault(a["canonical_url"], a["source_id"]); rep["sources_added"] += 1
        src_index = {s["source_id"]: s for s in read_jsonl(SRC_PATH)} if not dry else {**{s["source_id"]: s for s in sources}, **{a["source_id"]: a for a in new_s}}
        for c in clms:
            if c["claim_id"] in have_c:
                continue
            a = adapt_claim(c, shard)
            a = downgrade_weakly_sourced(a, src_index)
            missing = [s["source_id"] for s in a["supporting_sources"] if s["source_id"] not in have_s]
            if missing:
                rep["skipped_invalid"] += 1; report["errors"].append(f"{shard} {c['claim_id']}: unknown sources {missing}"); continue
            try:
                validate(a, c_schema, a["claim_id"])
            except SystemExit as e:
                rep["skipped_invalid"] += 1; report["errors"].append(f"{shard} {c['claim_id']}: {e}"); continue
            if not dry:
                append(CLM_PATH, a)
            have_c.add(a["claim_id"]); rep["claims_added"] += 1
        report["shards"][shard] = rep
        if not dry and (rep["sources_added"] or rep["claims_added"]):
            with open(os.path.join(sdir, ".merged_log"), "a") as f:
                f.write(json.dumps({"at": report["run_at"], **rep}) + "\n")
    report["totals"] = {"sources": len(have_s), "claims": len(have_c)}
    out = os.path.join(ROOT, "quality", "citation_audits", f"shard_merge_{datetime.date.today().isoformat()}.json")
    if not dry:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w") as f:
            json.dump(report, f, indent=2)
    print(json.dumps(report, indent=2)[:6000])
    return 0 if not report["errors"] else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
