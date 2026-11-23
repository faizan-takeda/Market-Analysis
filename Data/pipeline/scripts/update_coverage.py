#!/usr/bin/env python3
"""Recompute the source-family coverage ledger from the canonical registries.

Keeps the Director's hand-written rows (notes/gaps) and adds/refreshes a machine-computed block:
for every company x source family (mapped from source_type) -> discovered (all records),
reviewed (retrieved|api_json), unavailable (blocked|paywalled|unavailable), metadata_only.
Also writes research_coverage/coverage_summary.md for humans and the app.
"""
import collections, datetime, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from registry import read_jsonl, SRC_PATH, CLM_PATH, ROOT  # noqa

LEDGER = os.path.join(ROOT, "New_mediciine", "research_coverage", "coverage_ledger.json")
SUMMARY = os.path.join(ROOT, "New_mediciine", "research_coverage", "coverage_summary.md")
FAMILY = {
    "sec_filing": "SEC filings (10-K/20-F/8-K/6-K)", "xbrl_companyfacts": "XBRL financial facts", "annual_report": "Annual / integrated reports",
    "earnings_release": "Earnings releases", "earnings_transcript": "Earnings transcripts", "investor_presentation": "Investor / R&D day decks",
    "press_release": "Company press releases", "company_webpage": "Company web pages", "company_web": "Company web pages",
    "regulatory_decision": "Regulator records (FDA/EMA)", "regulatory_record": "Regulator records (FDA/EMA)",
    "clinical_trial_record": "Clinical trial registry", "clinical_trial_registry": "Clinical trial registry",
    "peer_reviewed": "Peer-reviewed publications", "preprint": "Preprints", "patent": "Patents",
    "lobbying_disclosure": "Lobbying / political disclosures", "government_data": "Government data & records", "government_record": "Government data & records",
    "news_report": "Independent reporting", "news_tier1": "Independent reporting", "news_trade": "Trade press",
    "analyst_report": "Industry / analyst reports", "industry_report": "Industry / analyst reports", "academic_report": "Academic reports",
    "interview": "Leadership interviews / transcripts", "interview_transcript": "Leadership interviews / transcripts", "podcast_video": "Leadership interviews / transcripts",
    "dataset_api": "Public dataset APIs", "methodology_doc": "Methodology references", "other": "Other",
}
EXPECTED = ["SEC filings (10-K/20-F/8-K/6-K)", "XBRL financial facts", "Earnings releases", "Earnings transcripts", "Investor / R&D day decks",
            "Company press releases", "Regulator records (FDA/EMA)", "Clinical trial registry", "Peer-reviewed publications", "Patents",
            "Lobbying / political disclosures", "Government data & records", "Independent reporting", "Trade press", "Leadership interviews / transcripts"]


def main():
    sources = read_jsonl(SRC_PATH); claims = read_jsonl(CLM_PATH)
    led = json.load(open(LEDGER)) if os.path.exists(LEDGER) else {"rows": []}
    manual = [r for r in led.get("rows", []) if not r.get("computed")]
    cnt = collections.defaultdict(lambda: {"discovered": 0, "reviewed": 0, "metadata_only": 0, "unavailable": 0})
    for s in sources:
        fam = FAMILY.get(s.get("source_type"), "Other"); co = s.get("company", "INDUSTRY")
        c = cnt[(co, fam)]; c["discovered"] += 1
        st = s.get("access_status")
        if st in ("retrieved", "api_json"): c["reviewed"] += 1
        elif st == "metadata_only": c["metadata_only"] += 1
        else: c["unavailable"] += 1
    claims_by_co = collections.Counter(co for c in claims for co in c.get("companies", []))
    claims_by_co_dom = collections.Counter((co, d) for c in claims for co in c.get("companies", []) for d in c.get("domains", []))
    rows = []
    for co in ["LLY", "JNJ", "ABBV", "TAK", "INDUSTRY", "MULTI", "METHODOLOGY"]:
        fams = set(EXPECTED) | {f for (c, f) in cnt if c == co}
        for fam in sorted(fams):
            c = cnt.get((co, fam), {"discovered": 0, "reviewed": 0, "metadata_only": 0, "unavailable": 0})
            if co in ("INDUSTRY", "MULTI", "METHODOLOGY") and c["discovered"] == 0:
                continue
            status = "not_started" if c["discovered"] == 0 else "reviewed" if c["reviewed"] == c["discovered"] else "partially_reviewed" if c["reviewed"] else "discovered"
            rows.append({"company": co, "family": fam, "status": status, "computed": True, **c})
    led = {"_about": led.get("_about", "Coverage ledger"), "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "totals": {"sources": len(sources), "claims": len(claims), "claims_by_company": dict(claims_by_co)},
           "rows": manual + rows}
    json.dump(led, open(LEDGER, "w"), indent=1)
    with open(SUMMARY, "w") as f:
        f.write(f"# Research coverage summary (computed {led['updated_at']})\n\nSources {len(sources)}, claims {len(claims)}. Claims by company: "
                + ", ".join(f"{k} {v}" for k, v in sorted(claims_by_co.items())) + ".\n\n")
        f.write("| Company | Source family | Status | Discovered | Reviewed | Metadata-only | Unavailable |\n|---|---|---|---|---|---|---|\n")
        for r in rows:
            f.write(f"| {r['company']} | {r['family']} | {r['status']} | {r['discovered']} | {r['reviewed']} | {r['metadata_only']} | {r['unavailable']} |\n")
        f.write("\n## Claims by company x domain\n\n| Company | Domain | Claims |\n|---|---|---|\n")
        for (co, d), n in sorted(claims_by_co_dom.items()):
            f.write(f"| {co} | {d} | {n} |\n")
        f.write("\n## Manual rows (Director notes and gaps)\n\n| Company | Family | Status | Notes | Gap |\n|---|---|---|---|---|\n")
        for r in manual:
            f.write(f"| {r.get('company')} | {r.get('family')} | {r.get('status')} | {(r.get('notes') or '')[:160]} | {(r.get('gap') or '')[:120]} |\n")
    print(json.dumps({"rows_computed": len(rows), "manual_rows": len(manual), "sources": len(sources), "claims": len(claims)}))


if __name__ == "__main__":
    main()
