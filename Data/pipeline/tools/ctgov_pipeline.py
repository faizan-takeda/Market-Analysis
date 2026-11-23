#!/usr/bin/env python3
"""
ClinicalTrials.gov v2 API pipeline inventory (deterministic; A4 shard, IDs continue after EDGAR).

For each sponsor, pulls interventional Phase 2 / Phase 3 / Phase 2-3 studies with start date
2021-01-01..2026-11-21, where the company is lead sponsor. Writes:
  data/normalized/ctgov_pipeline.json                  per-company counts by phase x start-year x status x condition
  New_mediciine/companies/<co>/pipeline/ctgov_inventory.md   human table + top conditions + list of Phase 3 starts
  New_mediciine/financial_models/ctgov_<co>.jsonl          one JSON per study (NCT, title, phase, status, start, conditions, interventions)
  shard A4_financial: one dataset_api source per company query + summary claims

Limits (recorded, not hidden): lead-sponsor filter misses collaborator-only studies; phase labels are
registrant-entered; counts are of registrations, not of distinct molecules.
"""
from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from evidence import append_jsonl, now_iso, read_jsonl  # noqa: E402

SPONSORS = {
    "eli_lilly": ("Eli Lilly and Company", "eli_lilly"),
    "johnson_johnson": ("Janssen Research & Development, LLC", "johnson_johnson"),
    "abbvie": ("AbbVie", "abbvie"),
    "takeda": ("Takeda", "takeda_public_baseline"),
}
BASE = "https://clinicaltrials.gov/api/v2/studies"
FIELDS = ",".join([
    "protocolSection.identificationModule.nctId", "protocolSection.identificationModule.briefTitle",
    "protocolSection.statusModule.overallStatus", "protocolSection.statusModule.startDateStruct",
    "protocolSection.statusModule.primaryCompletionDateStruct", "protocolSection.designModule.phases",
    "protocolSection.designModule.enrollmentInfo", "protocolSection.conditionsModule.conditions",
    "protocolSection.armsInterventionsModule.interventions", "protocolSection.sponsorCollaboratorsModule.leadSponsor",
])


def fetch_all(sponsor: str) -> list[dict]:
    out, token = [], None
    while True:
        q = {"query.lead": sponsor, "filter.advanced": "AREA[StartDate]RANGE[2021-01-01,2026-11-21] AND AREA[StudyType]INTERVENTIONAL AND (AREA[Phase]PHASE2 OR AREA[Phase]PHASE3)",
             "fields": FIELDS, "pageSize": 1000, "countTotal": "true"}
        if token:
            q["pageToken"] = token
        url = BASE + "?" + urllib.parse.urlencode(q)
        req = urllib.request.Request(url, headers={"User-Agent": "MEDICINE-research palrahma@amazon.com"})
        with urllib.request.urlopen(req, timeout=90) as r:
            d = json.loads(r.read())
        out += d.get("studies", [])
        token = d.get("nextPageToken")
        time.sleep(0.6)
        if not token:
            return out


def flat(s: dict) -> dict:
    p = s["protocolSection"]
    idm, st, de = p.get("identificationModule", {}), p.get("statusModule", {}), p.get("designModule", {})
    return {
        "nct": idm.get("nctId"), "title": idm.get("briefTitle"), "status": st.get("overallStatus"),
        "start": (st.get("startDateStruct") or {}).get("date"), "primary_completion": (st.get("primaryCompletionDateStruct") or {}).get("date"),
        "phases": de.get("phases", []), "enrollment": (de.get("enrollmentInfo") or {}).get("count"),
        "conditions": p.get("conditionsModule", {}).get("conditions", [])[:6],
        "interventions": [i.get("name") for i in p.get("armsInterventionsModule", {}).get("interventions", [])][:6],
        "lead_sponsor": (p.get("sponsorCollaboratorsModule", {}).get("leadSponsor") or {}).get("name"),
        "url": f"https://clinicaltrials.gov/study/{idm.get('nctId')}",
    }


def main():
    shard = ROOT / "New_mediciine" / "evidence_library" / "shards" / "A4_financial"
    src_path, clm_path = shard / "sources.jsonl", shard / "claims.jsonl"
    used_s = [int(r["source_id"][4:]) for r in read_jsonl(src_path)]
    used_c = [int(r["claim_id"][4:]) for r in read_jsonl(clm_path)]
    sid = max(used_s) if used_s else 4000
    cid = max(used_c) if used_c else 4000
    existing_titles = {r["title"] for r in read_jsonl(src_path)}
    summary = {"generated": now_iso(), "query": "lead sponsor; interventional; Phase 2/3; start 2021-01-01..2026-11-21",
               "limits": ["lead-sponsor only (collaborator studies excluded)", "registrant-entered phase labels", "registrations != molecules",
                          "J&J queried as Janssen Research & Development, LLC (main pharma registrant); other J&J entities not included"],
               "companies": {}}
    for co, (sponsor, folder) in SPONSORS.items():
        print(f"CT.gov {co} ({sponsor}) ...", file=sys.stderr)
        try:
            studies = [flat(s) for s in fetch_all(sponsor)]
        except Exception as ex:  # noqa: BLE001
            print("  FAILED", ex, file=sys.stderr)
            summary["companies"][co] = {"error": str(ex)[:200]}
            continue
        by_phase_year = defaultdict(Counter)
        by_status = Counter()
        cond = Counter()
        for s in studies:
            yr = (s["start"] or "????")[:4]
            ph = "/".join(s["phases"]) or "NA"
            by_phase_year[ph][yr] += 1
            by_status[s["status"]] += 1
            for c in s["conditions"]:
                cond[c] += 1
        p3_starts = sorted([s for s in studies if "PHASE3" in s["phases"]], key=lambda x: x["start"] or "")
        summary["companies"][co] = {"sponsor_query": sponsor, "total": len(studies),
                                    "by_phase_year": {k: dict(sorted(v.items())) for k, v in by_phase_year.items()},
                                    "by_status": dict(by_status.most_common()), "top_conditions": cond.most_common(25),
                                    "phase3_count": len(p3_starts)}
        fm = ROOT / "New_mediciine" / "financial_models"
        fm.mkdir(parents=True, exist_ok=True)
        with (fm / f"ctgov_{co}.jsonl").open("w", encoding="utf-8") as fh:
            for s in studies:
                fh.write(json.dumps(s, ensure_ascii=False) + "\n")
        # source record (dataset API query)
        title = f"ClinicalTrials.gov v2 API query: lead sponsor '{sponsor}', interventional Phase 2/3, start 2021-2026"
        qurl = BASE + "?" + urllib.parse.urlencode({"query.lead": sponsor, "filter.advanced": "AREA[StartDate]RANGE[2021-01-01,2026-11-21] AND AREA[StudyType]INTERVENTIONAL AND (AREA[Phase]PHASE2 OR AREA[Phase]PHASE3)"})
        if title not in existing_titles:
            sid += 1
            src_id = f"SRC-{sid:06d}"
            append_jsonl(src_path, {"source_id": src_id, "title": title, "publisher": "U.S. National Library of Medicine, ClinicalTrials.gov",
                                    "company": co, "domain": "pipeline", "source_type": "clinical_trial_registry", "original_url": qurl, "canonical_url": qurl,
                                    "publication_date": now_iso()[:10], "reporting_period": "2021-2026 start dates", "access_date": now_iso()[:10],
                                    "credibility": "T1_primary_official", "access_status": "api_json",
                                    "inspected_passage": f"API returned {len(studies)} studies; status counts {dict(by_status.most_common(6))}; Phase 3 = {len(p3_starts)}",
                                    "licensing": "US government public record", "notes": "Lead-sponsor filter; registrant-entered phases."})
        else:
            src_id = next(r["source_id"] for r in read_jsonl(src_path) if r["title"] == title)
        cid += 1
        append_jsonl(clm_path, {"claim_id": f"CLM-{cid:06d}", "statement": f"ClinicalTrials.gov lists {len(studies)} interventional Phase 2/3 studies with lead sponsor '{sponsor}' starting between 2021-01-01 and 2026-11-21, of which {len(p3_starts)} include Phase 3 (query run {now_iso()[:10]}).",
                                "kind": "FACT", "status": "SUPPORTED", "companies": [co], "domain": "pipeline", "supporting_source_ids": [src_id],
                                "locator": "API totalCount + phases field", "dates": {"period": "2021-2026"}, "confidence_rationale": "Machine count from the public registry; subject to lead-sponsor and phase-label limits stated in the source notes.",
                                "last_verified": now_iso()[:10], "single_interested_source": False, "value": len(studies), "unit": "registrations", "metric": "ctgov_p2p3_starts_2021_2026",
                                "tags": ["ctgov", "pipeline_breadth"], "implication": "Registration counts indicate development breadth, not pipeline quality or probability of success."})
        # human table
        d = ROOT / "New_mediciine" / "companies" / folder / "pipeline"
        d.mkdir(parents=True, exist_ok=True)
        L = [f"# {co} — ClinicalTrials.gov Phase 2/3 inventory (lead sponsor '{sponsor}')", "",
             f"Generated {now_iso()}. Source claim: see A4 shard (dataset_api). Full per-study list: `New_mediciine/financial_models/ctgov_{co}.jsonl`.", "",
             f"Total registrations: **{len(studies)}** (Phase 3-containing: {len(p3_starts)}). Limits: lead-sponsor only; registrant-entered phase; registrations are not molecules.", "",
             "## Starts by phase and year", "", "| Phase | " + " | ".join(str(y) for y in range(2021, 2027)) + " |", "|---|" + "---|" * 6]
        for ph, yrs in sorted(by_phase_year.items()):
            L.append(f"| {ph} | " + " | ".join(str(yrs.get(str(y), 0)) for y in range(2021, 2027)) + " |")
        L += ["", "## Status", "", "| Status | n |", "|---|---|"] + [f"| {k} | {v} |" for k, v in by_status.most_common()]
        L += ["", "## Top conditions (registrant terms)", "", "| Condition | n |", "|---|---|"] + [f"| {k} | {v} |" for k, v in cond.most_common(20)]
        L += ["", "## Phase 3 studies started 2021-2026 (first 60 by start date)", "", "| NCT | Start | Status | Title | Conditions |", "|---|---|---|---|---|"]
        for s in p3_starts[:60]:
            L.append(f"| [{s['nct']}]({s['url']}) | {s['start']} | {s['status']} | {(s['title'] or '')[:90]} | {', '.join(s['conditions'][:3])} |")
        (d / "ctgov_inventory.md").write_text("\n".join(L) + "\n", encoding="utf-8")
        print(f"  {co}: {len(studies)} studies, P3={len(p3_starts)}", file=sys.stderr)
    (ROOT / "data" / "normalized").mkdir(parents=True, exist_ok=True)
    (ROOT / "data" / "normalized" / "ctgov_pipeline.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(json.dumps({k: v.get("total") for k, v in summary["companies"].items()}))


if __name__ == "__main__":
    main()
