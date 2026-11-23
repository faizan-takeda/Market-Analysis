#!/usr/bin/env python3
"""
MEDICINE evidence management CLI (stdlib only; Python >= 3.9).

The filesystem is the system of record. This tool is the ONLY sanctioned way to
write into the canonical registries under New_mediciine/evidence_library/.

Subcommands
  fetch      Retrieve a URL (respecting robots-like politeness), store raw +
             extracted text, compute sha256, return a source record skeleton.
  add-source Append a source record to a shard (validates against schema).
  add-claim  Append a claim record to a shard (validates against schema).
  validate   Validate a shard or registry file; report errors.
  merge      SINGLE-WRITER: validate all shards, de-duplicate by canonical_url /
             claim text, and append new records to the canonical registries.
  stats      Print counts by company / status / source_type / credibility.
  linkcheck  HEAD/GET every canonical_url in the registry; write a report.
  ids        Show the ID range allocated to an agent shard.

ID allocation (prevents parallel-writer collisions; stable forever):
  A1_lilly        SRC-001000..001999  CLM-001000..001999
  A2_jnj          SRC-002000..002999  CLM-002000..002999
  A3_abbvie       SRC-003000..003999  CLM-003000..003999
  A4_financial    SRC-004000..004999  CLM-004000..004999   (EDGAR XBRL, deterministic)
  A5_takeda       SRC-005000..005999  CLM-005000..005999
  A6_ai_robotics  SRC-006000..006999  CLM-006000..006999
  A8_policy       SRC-008000..008999  CLM-008000..008999
  A10_audit       SRC-010000..010999  CLM-010000..010999
  A11_strategy    SRC-011000..011999  CLM-011000..011999
  A0_director     SRC-000001..000999  CLM-000001..000999
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENC = ROOT / "New_mediciine" / "evidence_library"
SCHEMA_DIR = ENC / "schema"
SHARDS = ENC / "shards"
RAW = ENC / "raw_documents"
TXT = ENC / "extracted_text"
REG_SRC = ENC / "source_registry.jsonl"
REG_CLM = ENC / "claims_registry.jsonl"
REG_ALIAS = ENC / "source_aliases.jsonl"
REG_CONF = ENC / "conflicts.jsonl"
REG_REL = ENC / "relationships.jsonl"
UA = "MEDICINE-research-project (academic/strategy research; contact palrahma@amazon.com)"

ID_RANGES = {
    "A0_director": 0, "A1_lilly": 1000, "A2_jnj": 2000, "A3_abbvie": 3000,
    "A4_financial": 4000, "A5_takeda": 5000, "A6_ai_robotics": 6000,
    "A7_commercial": 7000, "A8_policy": 8000, "A9_partnerships": 9000,
    "A10_audit": 10000, "A11_strategy": 11000, "A12_pipeline": 12000, "A14_gapfill": 14000,
}

SOURCE_TYPES = {
    "sec_filing", "annual_report", "earnings_release", "earnings_transcript",
    "investor_presentation", "press_release", "company_web", "regulatory_record",
    "clinical_trial_registry", "peer_reviewed", "preprint", "patent",
    "lobbying_disclosure", "government_record", "news_tier1", "news_trade",
    "industry_report", "academic_report", "interview_transcript", "podcast_video",
    "dataset_api", "other",
}
CREDIBILITY = {"T1_primary_official", "T2_company_technical", "T3_independent_reputable",
               "T4_expert_commentary", "T5_speculative"}
ACCESS = {"retrieved", "metadata_only", "blocked", "unavailable", "paywalled", "api_json"}
CLAIM_STATUS = {"SUPPORTED", "PARTIALLY_SUPPORTED", "CONTRADICTED", "INCONCLUSIVE",
                "NEEDS_MORE_RESEARCH"}
CLAIM_KIND = {"FACT", "INTERPRETATION", "HYPOTHESIS", "SCENARIO", "RECOMMENDATION"}
COMPANIES = {"eli_lilly", "johnson_johnson", "abbvie", "takeda", "industry", "other"}
DOMAINS = {"business", "financials", "pipeline", "scientific_rd", "data_ai",
           "robotics_automation", "commercial_market_access", "patient_care",
           "partnerships_ma", "policy_regulation", "leadership", "successes_failures",
           "competitive_advantage", "methodology", "strategy"}
MATURITY = {"concept", "prototype", "pilot", "operational", "scaled", "demonstrated_outcome",
            "not_applicable", "unknown"}


# ----------------------------------------------------------------------------- helpers
def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    with path.open("r", encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise SystemExit(f"{path}:{i}: invalid JSON ({e})")
    return out


def append_jsonl(path: Path, rec: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")


def canonicalize(url: str) -> str:
    p = urllib.parse.urlsplit(url.strip())
    q = [(k, v) for k, v in urllib.parse.parse_qsl(p.query, keep_blank_values=True)
         if not k.lower().startswith(("utm_", "fbclid", "gclid", "mc_", "ref"))]
    path = re.sub(r"/+$", "", p.path) or "/"
    return urllib.parse.urlunsplit((p.scheme.lower(), p.netloc.lower(), path,
                                    urllib.parse.urlencode(q), ""))


def strip_html(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style|noscript|svg|nav|footer|header).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<br\s*/?>|</p>|</div>|</tr>|</li>|</h[1-6]>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    raw = re.sub(r"[ \t\r\f\v]+", " ", raw)
    raw = re.sub(r"\n\s*\n+", "\n\n", raw)
    return raw.strip()


# ----------------------------------------------------------------------------- validation
def _err(errs: list, msg: str) -> None:
    errs.append(msg)


def validate_source(rec: dict) -> list[str]:
    e: list[str] = []
    for k in ("source_id", "title", "publisher", "company", "domain", "source_type",
              "original_url", "canonical_url", "access_date", "credibility", "access_status"):
        if not rec.get(k):
            _err(e, f"missing {k}")
    if e:
        return e
    if not re.fullmatch(r"SRC-\d{6}", rec["source_id"]):
        _err(e, f"bad source_id {rec['source_id']}")
    if rec["source_type"] not in SOURCE_TYPES:
        _err(e, f"bad source_type {rec['source_type']}")
    if rec["credibility"] not in CREDIBILITY:
        _err(e, f"bad credibility {rec['credibility']}")
    if rec["access_status"] not in ACCESS:
        _err(e, f"bad access_status {rec['access_status']}")
    if rec["company"] not in COMPANIES:
        _err(e, f"bad company {rec['company']}")
    if rec["domain"] not in DOMAINS:
        _err(e, f"bad domain {rec['domain']}")
    if not re.match(r"https?://", rec["original_url"]):
        _err(e, "original_url not http(s)")
    for k in ("publication_date", "access_date"):
        v = rec.get(k)
        if v and v != "unknown" and not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", str(v)[:10]):
            _err(e, f"bad date {k}={v}")
    if rec["access_status"] in ("retrieved", "api_json") and not rec.get("inspected_passage"):
        _err(e, "retrieved source must include inspected_passage (verbatim excerpt <= 600 chars)")
    ip = rec.get("inspected_passage") or ""
    if len(ip) > 1200:
        _err(e, "inspected_passage too long (>1200 chars) — keep lawful excerpt short")
    return e


def validate_claim(rec: dict) -> list[str]:
    e: list[str] = []
    for k in ("claim_id", "statement", "kind", "status", "companies", "domain",
              "supporting_source_ids", "confidence_rationale", "last_verified"):
        if k not in rec or rec[k] in (None, "", []):
            _err(e, f"missing {k}")
    if e:
        return e
    if not re.fullmatch(r"CLM-\d{6}", rec["claim_id"]):
        _err(e, f"bad claim_id {rec['claim_id']}")
    if rec["kind"] not in CLAIM_KIND:
        _err(e, f"bad kind {rec['kind']}")
    if rec["status"] not in CLAIM_STATUS:
        _err(e, f"bad status {rec['status']}")
    if rec["domain"] not in DOMAINS:
        _err(e, f"bad domain {rec['domain']}")
    for c in rec["companies"]:
        if c not in COMPANIES:
            _err(e, f"bad company {c}")
    for s in rec["supporting_source_ids"]:
        if not re.fullmatch(r"SRC-\d{6}", s):
            _err(e, f"bad source ref {s}")
    if rec["kind"] == "FACT" and rec["status"] == "SUPPORTED" and len(rec["supporting_source_ids"]) < 1:
        _err(e, "SUPPORTED FACT needs >=1 source")
    if rec.get("maturity") and rec["maturity"] not in MATURITY:
        _err(e, f"bad maturity {rec['maturity']}")
    if len(rec["statement"]) > 600:
        _err(e, "statement > 600 chars; split it")
    return e


def check_id_range(rec_id: str, shard: str, errs: list[str]) -> None:
    base = ID_RANGES.get(shard)
    if base is None:
        return
    n = int(rec_id.split("-")[1])
    lo, hi = (1, 999) if base == 0 else (base, base + 999)
    if not (lo <= n <= hi):
        errs.append(f"{rec_id} outside range for {shard} ({lo:06d}-{hi:06d})")


# ----------------------------------------------------------------------------- commands
def cmd_fetch(a):
    url = a.url
    cu = canonicalize(url)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    status, body, ctype = "retrieved", b"", ""
    try:
        with urllib.request.urlopen(req, timeout=a.timeout) as r:
            ctype = r.headers.get("Content-Type", "")
            body = r.read(a.max_bytes)
    except urllib.error.HTTPError as ex:
        status = "blocked" if ex.code in (401, 403, 429) else "unavailable"
        print(json.dumps({"url": url, "http_status": ex.code, "access_status": status}))
        return
    except Exception as ex:  # noqa: BLE001
        print(json.dumps({"url": url, "error": str(ex)[:200], "access_status": "unavailable"}))
        return
    sha = hashlib.sha256(body).hexdigest()
    ext = ".pdf" if "pdf" in ctype.lower() or url.lower().endswith(".pdf") else (
        ".json" if "json" in ctype.lower() else ".html")
    RAW.mkdir(parents=True, exist_ok=True)
    TXT.mkdir(parents=True, exist_ok=True)
    raw_path = RAW / f"{sha[:16]}{ext}"
    if a.store_raw:
        raw_path.write_bytes(body)
    txt_path = None
    if ext == ".html":
        text = strip_html(body.decode("utf-8", errors="replace"))
        txt_path = TXT / f"{sha[:16]}.txt"
        txt_path.write_text(text, encoding="utf-8")
    elif ext == ".json":
        txt_path = TXT / f"{sha[:16]}.json"
        txt_path.write_bytes(body)
    out = {
        "original_url": url, "canonical_url": cu, "content_type": ctype, "bytes": len(body),
        "sha256": sha, "access_status": status, "access_date": now_iso()[:10],
        "raw_path": str(raw_path.relative_to(ROOT)) if a.store_raw else None,
        "extracted_text_path": str(txt_path.relative_to(ROOT)) if txt_path else None,
    }
    if txt_path and ext == ".html" and a.grep:
        text = txt_path.read_text(encoding="utf-8")
        hits = []
        for m in re.finditer(re.escape(a.grep), text, flags=re.I):
            s = max(0, m.start() - a.context)
            hits.append(text[s:m.end() + a.context].replace("\n", " "))
            if len(hits) >= a.max_hits:
                break
        out["grep_hits"] = hits
    print(json.dumps(out, ensure_ascii=False, indent=2))
    time.sleep(a.sleep)


def _shard_paths(shard: str) -> tuple[Path, Path]:
    d = SHARDS / shard
    d.mkdir(parents=True, exist_ok=True)
    return d / "sources.jsonl", d / "claims.jsonl"


def cmd_add_source(a):
    rec = json.loads(Path(a.json).read_text(encoding="utf-8")) if a.json else json.load(sys.stdin)
    rec.setdefault("canonical_url", canonicalize(rec.get("original_url", "")))
    rec.setdefault("access_date", now_iso()[:10])
    errs = validate_source(rec)
    check_id_range(rec.get("source_id", "SRC-000000"), a.shard, errs)
    if errs:
        raise SystemExit("INVALID source: " + "; ".join(errs))
    sp, _ = _shard_paths(a.shard)
    existing = {r["source_id"] for r in read_jsonl(sp)}
    if rec["source_id"] in existing:
        raise SystemExit(f"duplicate source_id {rec['source_id']} in shard {a.shard}")
    append_jsonl(sp, rec)
    print(f"OK {rec['source_id']} -> {sp.relative_to(ROOT)}")


def cmd_add_claim(a):
    rec = json.loads(Path(a.json).read_text(encoding="utf-8")) if a.json else json.load(sys.stdin)
    rec.setdefault("last_verified", now_iso()[:10])
    errs = validate_claim(rec)
    check_id_range(rec.get("claim_id", "CLM-000000"), a.shard, errs)
    if errs:
        raise SystemExit("INVALID claim: " + "; ".join(errs))
    _, cp = _shard_paths(a.shard)
    existing = {r["claim_id"] for r in read_jsonl(cp)}
    if rec["claim_id"] in existing:
        raise SystemExit(f"duplicate claim_id {rec['claim_id']} in shard {a.shard}")
    append_jsonl(cp, rec)
    print(f"OK {rec['claim_id']} -> {cp.relative_to(ROOT)}")


def _validate_file(path: Path, kind: str, shard: str | None) -> tuple[int, list[str]]:
    recs = read_jsonl(path)
    errs: list[str] = []
    seen = set()
    for i, r in enumerate(recs, 1):
        e = validate_source(r) if kind == "source" else validate_claim(r)
        rid = r.get("source_id" if kind == "source" else "claim_id", "?")
        if shard:
            check_id_range(rid if re.fullmatch(r"(SRC|CLM)-\d{6}", str(rid)) else "SRC-000000", shard, e)
        if rid in seen:
            e.append("duplicate id within file")
        seen.add(rid)
        errs += [f"{path.name}:{i} {rid}: {m}" for m in e]
    return len(recs), errs


def cmd_validate(a):
    total_err = 0
    targets = []
    if a.path:
        p = Path(a.path)
        if not p.is_absolute():
            p = ROOT / p          # accept repo-relative paths (fixes relative_to ValueError)
        p = p.resolve()
        kind = "claim" if "claim" in p.name else "source"
        targets.append((p, kind, a.shard))
    else:
        for sh in sorted(SHARDS.iterdir()) if SHARDS.exists() else []:
            if sh.is_dir():
                targets.append((sh / "sources.jsonl", "source", sh.name))
                targets.append((sh / "claims.jsonl", "claim", sh.name))
        targets.append((REG_SRC, "source", None))
        targets.append((REG_CLM, "claim", None))
    for p, kind, sh in targets:
        if not p.exists():
            continue
        n, errs = _validate_file(p, kind, sh)
        print(f"{p.relative_to(ROOT)}: {n} records, {len(errs)} errors")
        for e in errs[: a.max_show]:
            print("   ", e)
        total_err += len(errs)
    # cross-ref: every claim's source must exist somewhere (registry or shards)
    all_src = {r["source_id"] for r in read_jsonl(REG_SRC)}
    for sh in sorted(SHARDS.iterdir()) if SHARDS.exists() else []:
        all_src |= {r["source_id"] for r in read_jsonl(sh / "sources.jsonl")}
    dangling = 0
    for sh in [d for d in SHARDS.iterdir() if d.is_dir()] + [ENC]:
        for c in read_jsonl(sh / ("claims.jsonl" if sh != ENC else "claims_registry.jsonl")):
            for s in c.get("supporting_source_ids", []):
                if s not in all_src:
                    dangling += 1
                    if dangling <= a.max_show:
                        print(f"   DANGLING {c['claim_id']} -> {s}")
    print(f"TOTAL errors: {total_err}, dangling source refs: {dangling}")
    sys.exit(1 if (total_err or dangling) and a.strict else 0)


def cmd_merge(a):
    """Single-writer merge of all shards into canonical registries."""
    reg_src = read_jsonl(REG_SRC)
    reg_clm = read_jsonl(REG_CLM)
    have_src = {r["source_id"] for r in reg_src}
    have_clm = {r["claim_id"] for r in reg_clm}
    by_url = {r["canonical_url"]: r["source_id"] for r in reg_src}
    added_s = added_c = aliased = skipped = 0
    problems: list[str] = []
    for sh in sorted(d for d in SHARDS.iterdir() if d.is_dir()):
        n, errs = _validate_file(sh / "sources.jsonl", "source", sh.name)
        n2, errs2 = _validate_file(sh / "claims.jsonl", "claim", sh.name)
        if errs or errs2:
            problems += errs + errs2
            print(f"SKIP shard {sh.name}: {len(errs)+len(errs2)} validation errors")
            skipped += 1
            continue
        for r in read_jsonl(sh / "sources.jsonl"):
            if r["source_id"] in have_src:
                continue
            dup = by_url.get(r["canonical_url"])
            if dup and dup != r["source_id"]:
                # same document registered twice by different agents -> alias, keep both IDs resolvable
                append_jsonl(REG_ALIAS, {"alias_id": r["source_id"], "canonical_id": dup,
                                         "reason": "same canonical_url", "recorded": now_iso()})
                aliased += 1
            r.setdefault("merged_from_shard", sh.name)
            r.setdefault("merged_at", now_iso())
            append_jsonl(REG_SRC, r)
            have_src.add(r["source_id"])
            by_url.setdefault(r["canonical_url"], r["source_id"])
            added_s += 1
        for c in read_jsonl(sh / "claims.jsonl"):
            if c["claim_id"] in have_clm:
                continue
            c.setdefault("merged_from_shard", sh.name)
            c.setdefault("merged_at", now_iso())
            append_jsonl(REG_CLM, c)
            have_clm.add(c["claim_id"])
            added_c += 1
    print(json.dumps({"sources_added": added_s, "claims_added": added_c, "aliases": aliased,
                      "shards_skipped": skipped, "total_sources": len(have_src),
                      "total_claims": len(have_clm), "problems": problems[:30]}, indent=2))


def cmd_stats(a):
    from collections import Counter
    S = read_jsonl(REG_SRC)
    C = read_jsonl(REG_CLM)
    def cnt(recs, key, multi=False):
        c = Counter()
        for r in recs:
            v = r.get(key, "?")
            if multi and isinstance(v, list):
                for x in v:
                    c[x] += 1
            else:
                c[v] += 1
        return dict(sorted(c.items(), key=lambda kv: -kv[1]))
    out = {
        "sources": len(S), "claims": len(C),
        "sources_by_company": cnt(S, "company"), "sources_by_type": cnt(S, "source_type"),
        "sources_by_credibility": cnt(S, "credibility"), "sources_by_access": cnt(S, "access_status"),
        "sources_by_domain": cnt(S, "domain"),
        "claims_by_company": cnt(C, "companies", multi=True), "claims_by_status": cnt(C, "status"),
        "claims_by_kind": cnt(C, "kind"), "claims_by_domain": cnt(C, "domain"),
        "claims_single_interested_source": sum(1 for c in C if c.get("single_interested_source")),
        "claims_with_contrary_evidence": sum(1 for c in C if c.get("contrary_evidence")),
        "generated": now_iso(),
    }
    print(json.dumps(out, indent=2))
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=2), encoding="utf-8")


def cmd_linkcheck(a):
    S = read_jsonl(REG_SRC)
    rows = []
    for i, r in enumerate(S):
        url = r["original_url"]
        code = None
        try:
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=a.timeout) as resp:
                code = resp.status
        except urllib.error.HTTPError as ex:
            code = ex.code
            if code in (405, 403, 400):
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": UA})
                    with urllib.request.urlopen(req, timeout=a.timeout) as resp:
                        code = resp.status
                except urllib.error.HTTPError as ex2:
                    code = ex2.code
                except Exception:  # noqa: BLE001
                    pass
        except Exception as ex:  # noqa: BLE001
            code = f"ERR {type(ex).__name__}"
        rows.append({"source_id": r["source_id"], "url": url, "http": code,
                     "recorded_access_status": r["access_status"]})
        if a.verbose:
            print(r["source_id"], code, url[:100])
        time.sleep(a.sleep)
    ok = sum(1 for x in rows if x["http"] == 200)
    rep = {"checked": len(rows), "http_200": ok, "generated": now_iso(), "rows": rows}
    out = Path(a.out) if a.out else ROOT / "quality" / "citation_audits" / f"linkcheck_{now_iso()[:10]}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rep, indent=2), encoding="utf-8")
    print(f"checked {len(rows)} urls, 200={ok}, report -> {out.relative_to(ROOT)}")


def cmd_ids(a):
    base = ID_RANGES[a.shard]
    lo, hi = (1, 999) if base == 0 else (base, base + 999)
    sp, cp = _shard_paths(a.shard)
    used_s = sorted(int(r["source_id"][4:]) for r in read_jsonl(sp))
    used_c = sorted(int(r["claim_id"][4:]) for r in read_jsonl(cp))
    print(json.dumps({"shard": a.shard, "source_range": f"SRC-{lo:06d}..SRC-{hi:06d}",
                      "claim_range": f"CLM-{lo:06d}..CLM-{hi:06d}",
                      "next_source_id": f"SRC-{(used_s[-1]+1 if used_s else lo):06d}",
                      "next_claim_id": f"CLM-{(used_c[-1]+1 if used_c else lo):06d}",
                      "sources_in_shard": len(used_s), "claims_in_shard": len(used_c)}, indent=2))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("fetch"); p.add_argument("url"); p.add_argument("--grep"); p.add_argument("--context", type=int, default=300)
    p.add_argument("--max-hits", type=int, default=5); p.add_argument("--timeout", type=int, default=30)
    p.add_argument("--max-bytes", type=int, default=15_000_000); p.add_argument("--store-raw", action="store_true")
    p.add_argument("--sleep", type=float, default=1.0); p.set_defaults(fn=cmd_fetch)
    p = sp.add_parser("add-source"); p.add_argument("--shard", required=True); p.add_argument("--json"); p.set_defaults(fn=cmd_add_source)
    p = sp.add_parser("add-claim"); p.add_argument("--shard", required=True); p.add_argument("--json"); p.set_defaults(fn=cmd_add_claim)
    p = sp.add_parser("validate"); p.add_argument("--path"); p.add_argument("--shard"); p.add_argument("--strict", action="store_true")
    p.add_argument("--max-show", type=int, default=25); p.set_defaults(fn=cmd_validate)
    p = sp.add_parser("merge"); p.set_defaults(fn=cmd_merge)
    p = sp.add_parser("stats"); p.add_argument("--out"); p.set_defaults(fn=cmd_stats)
    p = sp.add_parser("linkcheck"); p.add_argument("--out"); p.add_argument("--timeout", type=int, default=20)
    p.add_argument("--sleep", type=float, default=0.5); p.add_argument("--verbose", action="store_true"); p.set_defaults(fn=cmd_linkcheck)
    p = sp.add_parser("ids"); p.add_argument("shard"); p.set_defaults(fn=cmd_ids)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
