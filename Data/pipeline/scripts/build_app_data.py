#!/usr/bin/env python3
"""Data pipeline: encyclopedia (registries + curated markdown) -> validated app datasets -> indexes -> SQLite.

The single path from the research encyclopedia to the application. Reads the claim/source registries, curated
financial models, company timelines, mechanism cards, deal/approval/setback tables, Takeda baseline tables and
(when present) the strategy JSON under strategy/data/. Every claim ID referenced by any generated dataset is checked
against the claims registry; an unknown ID is a build failure (exit 1) so a stale/invalid dataset never reaches the UI.

Writes (data/normalized/ and executive_application/public/data/):
  sources, claims, financials, products, knowledge_graph, research_graph, coverage, maturity, maturity_matrix, project_state,
  timelines, mechanism_cards, deals, approvals, setbacks, takeda_baseline, conflicts, strategy, search_index
Optional inputs that do not exist yet produce {"available": false, "reason": ...} so the UI shows an explicit notice.
"""
import json, os, re, sys, sqlite3, datetime, shutil, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from registry import read_jsonl, SRC_PATH, CLM_PATH, ROOT  # noqa

NORM = os.path.join(ROOT, "data", "normalized"); IDX = os.path.join(ROOT, "data", "indexes"); DB = os.path.join(ROOT, "data", "database")
APP_DATA = os.path.join(ROOT, "executive_application", "public", "data")
NM = os.path.join(ROOT, "New_mediciine")
STRAT = os.path.join(ROOT, "strategy", "data")
COMPANY_META = {
    "LLY": {"name": "Eli Lilly and Company", "short": "Lilly", "hq": "Indianapolis, US", "fiscal_year": "calendar", "currency": "USD", "dir": "eli_lilly"},
    "JNJ": {"name": "Johnson & Johnson", "short": "J&J", "hq": "New Brunswick, US", "fiscal_year": "52/53-week ending ~Dec 31", "currency": "USD", "dir": "johnson_johnson"},
    "ABBV": {"name": "AbbVie Inc.", "short": "AbbVie", "hq": "North Chicago, US", "fiscal_year": "calendar", "currency": "USD", "dir": "abbvie"},
    "TAK": {"name": "Takeda Pharmaceutical Company Limited", "short": "Takeda", "hq": "Tokyo, JP", "fiscal_year": "April–March (FY label = start year)", "currency": "JPY", "dir": "takeda_public_baseline"},
}
CO_ALIAS = {"lilly": "LLY", "eli lilly": "LLY", "eli lilly and company": "LLY", "lly": "LLY", "j&j": "JNJ", "johnson & johnson": "JNJ", "jnj": "JNJ", "abbvie": "ABBV", "abbv": "ABBV",
            "takeda": "TAK", "tak": "TAK", "industry": "INDUSTRY"}
CLASSES = ["EXISTING_BUT_UNDERDEVELOPED", "EXISTING_STRENGTH", "EVIDENCE_GAP", "POTENTIAL_NEW_CAPABILITY"]
STOP = set("the a an and or of to in for on by with from as at is are was were be been its their this that which these those into over under than then also not no yes per vs versus about after before during between within".split())
errors = []


def tokens(text):
    return {t for t in re.findall(r"[a-z0-9][a-z0-9\-\.]{1,}", text.lower()) if t not in STOP and len(t) > 2}


def rel(p):
    return os.path.relpath(p, ROOT)


def co_code(name):
    return CO_ALIAS.get(name.strip().lower().strip("*"))


def read(path):
    return open(path, encoding="utf-8").read() if os.path.exists(path) else None


# ---------------------------------------------------------------- markdown helpers
def strip_md(s):
    return re.sub(r"\s+", " ", s.replace("**", "").replace("`", "")).strip()


def parse_tables(text):
    """Return [{heading, sub, headers, rows}] for every pipe table; rows are lists of raw cell strings."""
    out, h2, h3, lines, i = [], "", "", text.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("## "):
            h2, h3 = ln[3:].strip(), ""
        elif ln.startswith("### "):
            h3 = ln[4:].strip()
        if ln.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            split = lambda l: [c.strip() for c in l.strip().strip("|").replace("\\|", "\u0001").split("|")]
            hdr = [c.replace("\u0001", "|") for c in split(ln)]
            rows, j = [], i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append([c.replace("\u0001", "|") for c in split(lines[j])]); j += 1
            out.append({"heading": h2, "sub": h3, "headers": hdr, "rows": rows}); i = j; continue
        i += 1
    return out


CLM_RE = re.compile(r"CLM-(\d{6})(?:\s*[–\-]\s*(?:CLM-)?(\d{6}))?")


def claim_ids(text, cid, where):
    """Extract CLM ids (expanding written ranges such as CLM-006003–CLM-006007); unknown ids are build errors."""
    ids = []
    for m in CLM_RE.finditer(text or ""):
        a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
        if b < a or b - a > 60:
            errors.append(f"{where}: unusable range {m.group(0)}"); continue
        for n in range(a, b + 1):
            k = f"CLM-{n:06d}"
            if k in cid:
                ids.append(k)
            elif n in (a, b):
                errors.append(f"{where}: unknown claim id {k}")
    return list(dict.fromkeys(ids))


def src_ids(text, sid, where):
    ids = []
    for m in re.finditer(r"SRC-(\d{6})(?:\s*[–\-]\s*(?:SRC-)?(\d{6}))?|(?<=[,;]\s)(\d{6})(?=[,;\s]|$)", text or ""):
        if m.group(1):
            a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
            for n in range(a, b + 1):
                k = f"SRC-{n:06d}"
                if k in sid:
                    ids.append(k)
                elif n in (a, b):
                    errors.append(f"{where}: unknown source id {k}")
    return list(dict.fromkeys(ids))


def year_of(s):
    m = re.search(r"(20\d\d)", s or "")
    return int(m.group(1)) if m else None


def col(headers, *names):
    low = [h.lower() for h in headers]
    for n in names:
        for i, h in enumerate(low):
            if h.startswith(n.lower()):
                return i
    return None


# ---------------------------------------------------------------- generators
def gen_timelines(cid):
    out = {}
    for co, m in COMPANY_META.items():
        p = os.path.join(NM, "companies", m["dir"], "timeline.md"); t = read(p)
        if t is None:
            out[co] = {"available": False, "events": []}; continue
        ev = []
        for tb in parse_tables(t):
            ci, ei, ki = col(tb["headers"], "date"), col(tb["headers"], "event"), col(tb["headers"], "claim", "evidence")
            if None in (ci, ei, ki):
                continue
            for r in tb["rows"]:
                if len(r) <= max(ci, ei, ki):
                    continue
                ids = claim_ids(r[ki], cid, f"{rel(p)} row '{r[ci]}'")
                ev.append({"date": strip_md(r[ci]), "year": year_of(r[ci]), "event": strip_md(r[ei]), "claim_ids": ids})
        out[co] = {"available": True, "path": rel(p), "events": ev}
    return out


STAGE_MAP = [("problem", ["initial problem"]), ("investment", ["starting investment"]), ("capability", ["capability"]), ("execution", ["execution"]),
             ("outcome", ["evidence of value"]), ("moat", ["durability"]), ("response", ["competitive response"]), ("takeda", ["takeda relevance"]), ("maturity", ["maturity"])]


def gen_cards(cid, sid):
    cards = []
    p = os.path.join(NM, "industry_transformation", "ai_data_robotics", "capability_mechanism_cards.md"); t = read(p)
    if t:
        parts = re.split(r"^## (Card \d+\..*)$", t, flags=re.M)
        for k in range(1, len(parts), 2):
            head, body = parts[k].strip(), parts[k + 1]
            m = re.match(r"Card (\d+)\.\s*(.*?)(?:\s+—\s+(.*))?$", head)
            num, title, cos = m.group(1), m.group(2).strip(), (m.group(3) or "")
            codes = []
            for piece in re.split(r",|\bplus\b", re.sub(r"\(.*?\)", "", cos)):
                c = co_code(piece)
                if c and c not in codes:
                    codes.append(c)
            fields, tb = [], parse_tables(body)
            for tbl in tb:
                for r in tbl["rows"]:
                    if len(r) >= 2:
                        fields.append({"label": strip_md(r[0]), "text": strip_md(r[1]), "claim_ids": claim_ids(r[1], cid, f"{rel(p)} {head}")})
            stages = {}
            for key, names in STAGE_MAP + [("assets", ["enabling assets"])]:
                for f in fields:
                    if any(f["label"].lower().startswith(n) for n in names) and key not in stages:
                        stages[key] = {"text": f["text"], "claim_ids": f["claim_ids"]}
            ev = next((f for f in fields if f["label"].lower() == "evidence ids"), None)
            allids = claim_ids(body, cid, f"{rel(p)} {head}")
            cards.append({"id": f"CARD-{int(num):02d}", "kind": "mechanism_card", "title": title, "companies": codes or ["INDUSTRY"], "company_label": cos.strip(), "fields": fields, "stages": stages,
                          "claim_ids": allids, "source_ids": src_ids(ev["text"] if ev else "", sid, f"{rel(p)} {head}"), "contrary": [f["text"] for f in fields if f["label"].lower().startswith("contrary")], "source_file": rel(p)})
    for co, m in COMPANY_META.items():
        p = os.path.join(NM, "companies", m["dir"], "competitive_advantage", "moats.md"); t = read(p)
        if not t:
            continue
        body = "\n".join(l for l in t.split("\n") if not l.startswith("#")).strip()
        pos, n, marks = 0, 1, []
        while True:
            mm = re.compile(rf"(?:^|\s)({n})\.\s+(?=[A-Z*])").search(body, pos)
            if not mm:
                break
            marks.append((n, mm.start(1))); pos = mm.end(); n += 1
        for idx, (n, st) in enumerate(marks):
            seg = body[st:(marks[idx + 1][1] if idx + 1 < len(marks) else len(body))]
            seg = re.sub(r"^\d+\.\s+", "", seg).strip()
            txt = strip_md(seg)
            title = re.split(r"\.\s|:\s| \[CLM", txt, 1)[0][:110]
            ids = claim_ids(seg, cid, f"{rel(p)} moat {n}")
            cards.append({"id": f"MOAT-{co}-{n}", "kind": "moat", "title": title, "companies": [co], "company_label": m["short"], "fields": [{"label": "Moat analysis", "text": txt, "claim_ids": ids}],
                          "stages": {"moat": {"text": txt, "claim_ids": ids}}, "claim_ids": ids, "source_ids": [], "contrary": [], "source_file": rel(p),
                          "gap": bool(re.search(r"not evidenced|\(gap\)|gap\)", txt))})
    return cards if cards else {"available": False, "reason": "capability_mechanism_cards.md not found"}


def gen_matrix(cid, claims_by_id):
    p = os.path.join(NM, "industry_transformation", "ai_data_robotics", "maturity_matrix.md"); t = read(p)
    if not t:
        return {"available": False, "reason": "maturity_matrix.md not found", "rows": []}
    rows = []
    for tb in parse_tables(t):
        ci, ii, mi, ei, oi, ni = (col(tb["headers"], *n) for n in (("company",), ("initiative",), ("maturity",), ("evidence",), ("outcome",), ("note",)))
        if None in (ci, ii, mi, ei):
            continue
        for r in tb["rows"]:
            ids = claim_ids(r[ei] + " " + (r[ni] if ni is not None and ni < len(r) else ""), cid, f"{rel(p)} {r[ii]}")
            cos = [co_code(x) for x in re.split(r",|\bplus\b", r[ci])]; cos = [c for c in cos if c] or ["INDUSTRY"]
            lvl = strip_md(r[mi]); base = re.match(r"[a-z_]+", lvl.lower())
            rows.append({"companies": cos, "initiative": strip_md(r[ii]), "maturity_raw": lvl, "maturity": (base.group(0) if base else "unknown").upper(),
                         "claim_ids": ids, "outcome_evidence": strip_md(r[oi]) if oi is not None else "", "note": strip_md(r[ni]) if ni is not None else "",
                         "domains": sorted({d for k in ids for d in claims_by_id[k].get("domains", [])}),
                         "years": sorted({year_of(claims_by_id[k].get("event_date") or "") for k in ids if year_of(claims_by_id[k].get("event_date") or "")})})
    return {"available": True, "path": rel(p), "rows": rows}


def gen_deals(cid):
    ep = os.path.join(NM, "industry_transformation", "partnerships_ecosystem", "ecosystem_graph_edges.jsonl")
    ip = os.path.join(NM, "industry_transformation", "partnerships_ecosystem", "deal_inventory.md")
    edges, inv = [], []
    if os.path.exists(ep):
        for n, l in enumerate(open(ep, encoding="utf-8"), 1):
            if not l.strip():
                continue
            e = json.loads(l)
            for k in e.get("claim_ids", []):
                if k not in cid:
                    errors.append(f"{rel(ep)}:{n} unknown claim id {k}")
            e["year"] = year_of(e.get("date")); e["from_code"] = co_code(e["from"]); edges.append(e)
    t = read(ip)
    if t:
        for tb in parse_tables(t):
            co = co_code(tb["heading"])
            if not co:
                continue
            h = tb["headers"]
            ix = {k: col(h, *v) for k, v in {"date": ("announced",), "counterparty": ("counterparty",), "type": ("type",), "area": ("area",), "upfront": ("upfront",), "contingent": ("contingent",), "accounting": ("accounting",), "status": ("status",), "claims": ("claims",)}.items()}
            if ix["claims"] is None or ix["counterparty"] is None:
                continue
            for r in tb["rows"]:
                g = lambda k: strip_md(r[ix[k]]) if ix[k] is not None and ix[k] < len(r) else ""
                inv.append({"company": co, "date": g("date"), "year": year_of(g("date")), "counterparty": g("counterparty"), "type": g("type"), "area": g("area"), "upfront": g("upfront"),
                            "contingent": g("contingent"), "accounting": g("accounting"), "status": g("status"), "claim_ids": claim_ids(r[ix["claims"]], cid, f"{rel(ip)} {g('counterparty')}")})
    if not edges and not inv:
        return {"available": False, "reason": "ecosystem_graph_edges.jsonl / deal_inventory.md not found", "edges": [], "inventory": []}
    return {"available": True, "edges_path": rel(ep), "inventory_path": rel(ip), "edges": edges, "inventory": inv}


def gen_approvals(cid):
    p = os.path.join(NM, "industry_transformation", "pipeline_regulatory", "fda_approvals_2022_2026.md"); t = read(p)
    if not t:
        return {"available": False, "reason": "fda_approvals_2022_2026.md not yet produced", "rows": []}
    rows = []
    for tb in parse_tables(t):
        h = tb["headers"]; di, ki = col(h, "date"), col(h, "claim")
        if di is None or ki is None:
            continue
        sect = tb["heading"][:1]
        pi, ci, ai, ii, si, di2 = col(h, "product"), col(h, "company"), col(h, "active"), col(h, "indication"), col(h, "sponsor"), col(h, "description", "supplement")
        for r in tb["rows"]:
            g = lambda i: strip_md(r[i]) if i is not None and i < len(r) else ""
            co = co_code(g(ci)) if ci is not None else co_code(re.sub(r"\(.*?\)", "", tb["sub"]))
            rows.append({"section": tb["heading"], "kind": {"A": "novel", "B": "other_application", "C": "supplemental"}.get(sect, "other"), "company": co, "date": g(di), "year": year_of(g(di)),
                         "product": g(pi), "ingredient": g(ai), "detail": g(ii) or g(di2), "sponsor": g(si), "claim_ids": claim_ids(r[ki], cid, f"{rel(p)} {g(pi)}")})
    return {"available": True, "path": rel(p), "rows": rows}


def gen_setbacks(cid):
    p = os.path.join(NM, "industry_transformation", "pipeline_regulatory", "setbacks_crls_withdrawals.md"); t = read(p)
    if not t:
        return {"available": False, "reason": "setbacks_crls_withdrawals.md not yet produced", "rows": []}
    rows = []
    for tb in parse_tables(t):
        h = tb["headers"]; wi, ci, ai, xi, ki = col(h, "when"), col(h, "company"), col(h, "asset"), col(h, "what"), col(h, "claim")
        if None in (wi, ci, ai, xi, ki):
            continue
        for r in tb["rows"]:
            g = lambda i: strip_md(r[i]) if i < len(r) else ""
            rows.append({"when": g(wi), "year": year_of(g(wi)), "company": co_code(g(ci)), "asset": g(ai), "what": g(xi), "claim_ids": claim_ids(r[ki], cid, f"{rel(p)} {g(ai)}")})
    return {"available": True, "path": rel(p), "rows": rows}


def gen_takeda(cid):
    base = os.path.join(NM, "companies", "takeda_public_baseline")
    cp, bp = os.path.join(base, "capability_baseline", "capability_baseline.md"), os.path.join(base, "internal_validation_backlog", "backlog.md")
    caps, backlog = [], []
    t = read(cp)
    for tb in parse_tables(t or ""):
        h = tb["headers"]; ai, ci, ei, vi = col(h, "capability"), col(h, "class"), col(h, "evidence"), col(h, "internal")
        if None in (ai, ci, ei):
            continue
        for r in tb["rows"]:
            raw = strip_md(r[ci]); cls = next((c for c in CLASSES if c in raw), "OTHER")
            caps.append({"area": strip_md(r[ai]), "class": cls, "class_raw": raw, "claim_ids": claim_ids(r[ei], cid, f"{rel(cp)} {r[ai]}"),
                         "validation": strip_md(r[vi]) if vi is not None and vi < len(r) else "", "ivb_refs": sorted(set(re.findall(r"IVB-\d+", r[vi] if vi is not None and vi < len(r) else "")))})
    t = read(bp)
    for tb in parse_tables(t or ""):
        h = tb["headers"]; ii, qi, wi, li, oi = col(h, "id"), col(h, "question"), col(h, "why"), col(h, "linked"), col(h, "owner")
        if None in (ii, qi, li):
            continue
        for r in tb["rows"]:
            g = lambda i: strip_md(r[i]) if i is not None and i < len(r) else ""
            backlog.append({"id": g(ii), "question": g(qi), "why": g(wi), "linked": g(li), "owner": g(oi), "claim_ids": claim_ids(r[li], cid, f"{rel(bp)} {g(ii)}")})
    if not caps and not backlog:
        return {"available": False, "reason": "Takeda baseline files not found", "capabilities": [], "backlog": []}
    return {"available": True, "capability_path": rel(cp), "backlog_path": rel(bp), "capabilities": caps, "backlog": backlog}


def gen_conflicts(cid):
    p = os.path.join(NM, "evidence_library", "conflicts.jsonl"); out = []
    if os.path.exists(p):
        for n, l in enumerate(open(p, encoding="utf-8"), 1):
            if not l.strip():
                continue
            e = json.loads(l)
            for k in ([e["claim_id"]] if e.get("claim_id") else []) + list(e.get("claim_ids", [])):
                if k not in cid:
                    errors.append(f"{rel(p)}:{n} unknown claim id {k}")
            out.append(e)
    return {"available": os.path.exists(p), "path": rel(p), "items": out}


STRATEGY_FILES = ["strategy_bets", "assumptions", "portfolios", "stage_gates", "roadmap", "scenarios", "council_reviews", "counterarguments", "takeda_lessons"]


def gen_strategy(cid):
    files = {}
    for name in STRATEGY_FILES:
        p = os.path.join(STRAT, name + ".json")
        files[name] = {"available": os.path.exists(p), "path": rel(p), "data": json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None}
    asm = {a["id"] for a in (files["assumptions"]["data"] or {}).get("assumptions", [])} if files["assumptions"]["available"] else None
    bets = {b["id"] for b in (files["strategy_bets"]["data"] or {}).get("bets", [])} if files["strategy_bets"]["available"] else None

    def walk(o, where, key=""):
        if isinstance(o, dict):
            for k, v in o.items():
                walk(v, where, k)
        elif isinstance(o, list):
            for v in o:
                walk(v, where, key)
        elif isinstance(o, str):
            if re.fullmatch(r"CLM-\d{6}", o) and o not in cid:
                errors.append(f"{where}: unknown claim id {o} (key {key})")
            if re.fullmatch(r"ASM-\w+", o) and asm is not None and key in ("assumption_ids", "ivb_ref") and o not in asm:
                errors.append(f"{where}: unknown assumption id {o}")
            if re.fullmatch(r"BET-\w+", o) and bets is not None and key in ("bet_id", "prerequisites") and o not in bets:
                errors.append(f"{where}: unknown bet id {o}")
    for name, f in files.items():
        if f["available"]:
            walk(f["data"], f["path"])
    return files


# ---------------------------------------------------------------- reports (Markdown bundle) and Q&A index
REPORT_ROOTS = ["deliverables", "New_mediciine", "strategy", "research_methodology", "quality"]
ROOT_MD = ["map.md", "PROJECT_STATE.md", "CONTINUE.md", "COORDINATION.md", "README.md"]
COMPANY_DIRS = {m["dir"]: code for code, m in COMPANY_META.items()}
CO_SECTION = {"business": "business", "financials": "business", "pipeline": "pipeline", "commercial_market_access": "commercial", "competitive_advantage": "moats",
              "successes_failures": "successes", "leadership": "leadership", "robotics_automation": "dataai", "data_ai": "dataai", "capability_baseline": "capability",
              "internal_validation_backlog": "backlog", "loe_risk": "loe"}
CO_SECTION_ALSO = {"commercial": "commercial", "pipeline": "rd", "dataai": "dataai", "successes": "rd", "loe": "rd"}
CC_FILES = {"commercial_capabilities_comparison": ("commercial", "compare"), "rd_investment_and_productivity": ("rd", "compare"), "pipeline_and_revenue_dependence": ("rd", "compare"),
            "loe_resilience_comparison": ("rd", "compare"), "data_ai_maturity_matrix": ("dataai", "compare"), "robotics_deployment_comparison": ("dataai", "compare"),
            "partner_ecosystem_comparison": ("partnerships", "compare")}
IT_PILLAR = {"commercial_patient": "commercial", "pipeline_regulatory": "rd", "ai_data_robotics": "dataai", "partnerships_ecosystem": "partnerships", "policy": "policy"}


def classify_report(p):
    """-> (pillar, company, section, also[]). Pillars: companies, commercial, rd, dataai, partnerships, policy, takeda, future, evidence."""
    parts = p.split("/"); stem = os.path.splitext(parts[-1])[0]
    if parts[0] == "deliverables":
        return "evidence", "MULTI", "deliverables", []
    if parts[0] == "New_mediciine":
        if len(parts) > 2 and parts[1] == "companies":
            co = COMPANY_DIRS.get(parts[2], "MULTI")
            sec = {"master_report": "dossier", "timeline": "timeline", "evidence_gaps": "gaps", "map": "map"}.get(stem, stem) if len(parts) == 4 else CO_SECTION.get(parts[3], parts[3])
            also = [CO_SECTION_ALSO[sec]] if sec in CO_SECTION_ALSO else []
            return ("takeda" if co == "TAK" else "companies"), co, sec, also
        if len(parts) > 2 and parts[1] == "cross_company_analysis":
            pil, sec = CC_FILES.get(stem, ("companies", "compare"))
            return ("companies" if pil != "companies" else pil), "MULTI", sec, ([pil] if pil != "companies" else [])
        if len(parts) > 2 and parts[1] == "industry_transformation":
            pil = IT_PILLAR.get(parts[2], "evidence")
            return pil, "INDUSTRY", {"evidence_gaps": "gaps", "map": "map"}.get(stem, stem), []
        return "evidence", "METHODOLOGY", parts[1] if len(parts) > 2 else "map", []
    if parts[0] == "strategy":
        return "future", "MULTI", (parts[1] if len(parts) > 2 else "framework"), []
    if parts[0] == "research_methodology":
        return "evidence", "METHODOLOGY", ("runs" if "research_runs" in parts else "briefs" if "briefs" in parts else "method"), []
    if parts[0] == "quality":
        return "evidence", "METHODOLOGY", (parts[1] if len(parts) > 2 else "validation"), []
    return "evidence", "METHODOLOGY", "state" if stem in ("PROJECT_STATE", "CONTINUE", "COORDINATION") else "map", []


def gen_reports(cid, sid):
    paths = []
    for r in REPORT_ROOTS:
        for dp, dn, fn in os.walk(os.path.join(ROOT, r)):
            dn[:] = sorted(d for d in dn if not d.startswith(".") and d not in ("node_modules", "raw_documents", "extracted_text"))
            paths += [os.path.join(dp, f) for f in sorted(fn) if f.lower().endswith(".md")]
    paths += [os.path.join(ROOT, f) for f in ROOT_MD if os.path.exists(os.path.join(ROOT, f))]
    out = []
    for fp in paths:
        rp = rel(fp).replace(os.sep, "/"); text = open(fp, encoding="utf-8", errors="replace").read()
        h1 = re.search(r"^#\s+(.+?)\s*$", text, flags=re.M)
        pillar, co, sec, also = classify_report(rp)
        known = []
        for m in CLM_RE.finditer(text):
            a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
            for n in range(a, min(b, a + 60) + 1):
                k = "CLM-%06d" % n
                if k in cid:
                    known.append(k)
        out.append({"path": rp, "title": strip_md(h1.group(1)) if h1 else os.path.splitext(os.path.basename(rp))[0].replace("_", " "), "pillar": pillar, "company": co, "section": sec, "also": also,
                    "markdown": text, "word_count": len(text.split()), "claim_ids": list(dict.fromkeys(known)),
                    "source_ids": sorted(set(re.findall(r"SRC-\d{6}", text)) & set(sid)),
                    "updated": datetime.datetime.fromtimestamp(os.path.getmtime(fp)).strftime("%Y-%m-%d")})
    return {"generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "count": len(out), "reports": out}


def plain(s):
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[|`*_>#]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def gen_research_log():
    out = {}
    for key, fn in (("experiments", "research_experiments.jsonl"), ("backlog", "task_backlog.jsonl")):
        path = os.path.join(ROOT, "research_methodology", fn); rows = []
        if os.path.exists(path):
            for l in open(path, encoding="utf-8"):
                if l.strip():
                    rows.append(json.loads(l))
        out[key] = rows
    return out


def gen_qa(claims, sources, reports):
    """Passages for in-browser BM25: claims, report sections (~300 words) and sources. Field boosts are applied client-side (t = title, x = text)."""
    docs = []
    for c in claims:
        txt = " ".join(x for x in [c["statement"], c.get("implications") or ""] if x)
        docs.append({"k": "claim", "id": c["claim_id"], "t": " ".join([c["claim_id"]] + c.get("entities", []) + c.get("domains", [])), "x": txt, "co": c["companies"], "kind": c["kind"], "sr": [s["source_id"] for s in c["supporting_sources"]][:3]})
    for s in sources:
        docs.append({"k": "source", "id": s["source_id"], "t": s["title"], "x": " ".join([s["publisher"], s.get("reporting_period") or "", s.get("limitations") or ""]), "co": [s["company"]]})
    for r in reports["reports"]:
        sections, cur, buf = [], r["title"], []
        for ln in r["markdown"].split("\n"):
            m = re.match(r"^(#{1,4})\s+(.*)$", ln)
            if m:
                if buf:
                    sections.append((cur, buf))
                cur, buf = plain(m.group(2)), []
            else:
                buf.append(ln)
        sections.append((cur, buf))
        n = 0
        for head, lines in sections:
            words = plain(" ".join(lines)).split(" ")
            words = [w for w in words if w]
            for i in range(0, max(1, len(words)), 300):
                chunk = " ".join(words[i:i + 300])
                if len(chunk) < 40:
                    continue
                n += 1
                docs.append({"k": "report", "id": "%s#%d" % (r["path"], n), "t": head + " " + r["title"], "x": chunk, "co": [r["company"]], "path": r["path"], "h": head, "pillar": r["pillar"],
                             "ids": list(dict.fromkeys(re.findall(r"CLM-\d{6}", chunk)))[:6]})
    return {"count": len(docs), "docs": docs}


# ---------------------------------------------------------------- main
def main():
    sources = read_jsonl(SRC_PATH); claims = read_jsonl(CLM_PATH)
    sid = {s["source_id"]: s for s in sources}; cid = {c["claim_id"]: c for c in claims}
    for c in claims:
        for ss in c["supporting_sources"]:
            if ss["source_id"] not in sid:
                errors.append(f"{c['claim_id']} -> missing {ss['source_id']}")
    fin = collections.defaultdict(lambda: collections.defaultdict(dict))
    for c in claims:
        if c.get("run_id") == "RUN-0001-sec-ingest" and c.get("_concept_key"):
            fin[c["companies"][0]][c["_concept_key"]][str(c["_fy"])] = {"value": c["value"], "unit": c["unit"], "claim_id": c["claim_id"], "period": c["reporting_period"]}
    financials = {co: {"meta": COMPANY_META[co], "concepts": fin[co]} for co in COMPANY_META}
    products = json.load(open(os.path.join(NM, "financial_models", "product_revenue_series.json")))
    for s in products["series"] + products["loe_events"]:
        for k in s["claims"]:
            if k not in cid:
                errors.append(f"product_revenue_series references unknown {k}")
    maturity = [{"claim_id": c["claim_id"], "company": c["companies"][0], "companies": c["companies"], "maturity": c["maturity"], "statement": c["statement"], "event_date": c.get("event_date"),
                 "entities": c.get("entities", []), "domains": c.get("domains", []), "sources": [s["source_id"] for s in c["supporting_sources"]],
                 "single_interested_source": c.get("single_interested_source", False), "status": c["status"], "shard": c.get("merged_from_shard")}
                for c in claims if c.get("maturity")]
    # knowledge graph (claim-evidenced company<->entity links), then merged with deal edges client-side
    nodes, edges = {}, {}
    for co, m in COMPANY_META.items():
        nodes[co] = {"id": co, "type": "company", "label": m["short"]}
    for c in claims:
        if c.get("run_id") == "RUN-0001-sec-ingest":
            continue
        for co in c["companies"]:
            if co not in nodes:
                nodes[co] = {"id": co, "type": "company_group", "label": co}
            for e in c.get("entities", []):
                if e == COMPANY_META.get(co, {}).get("name"):
                    continue
                eid = "E:" + e
                etype = "technology" if any(d in ("data_ai", "robotics_automation") for d in c.get("domains", [])) else "product" if "financials" in c.get("domains", []) and c.get("value") else "entity"
                nodes.setdefault(eid, {"id": eid, "type": etype, "label": e})
                ed = edges.setdefault((co, eid), {"source": co, "target": eid, "claims": [], "domains": set(), "kinds": set()})
                ed["claims"].append(c["claim_id"]); ed["domains"].update(c.get("domains", [])); ed["kinds"].add(c["kind"])
    kg = {"nodes": list(nodes.values()), "edges": [{**e, "domains": sorted(e["domains"]), "kinds": sorted(e["kinds"])} for e in edges.values()],
          "note": "Edges are evidence links (company ↔ entity mentioned in a claim), not causal assertions."}
    mm = open(os.path.join(ROOT, "research_methodology", "research_graph.md")).read()
    rg_nodes, rg_edges = {}, []
    for m in re.finditer(r'(\w+)\[\"([^\"]+)\"\]|(\w+)\{\"([^\"]+)\"\}', mm):
        if m.group(1):
            rg_nodes[m.group(1)] = {"id": m.group(1), "label": m.group(2), "shape": "box"}
        else:
            rg_nodes[m.group(3)] = {"id": m.group(3), "label": m.group(4), "shape": "diamond"}
    for m in re.finditer(r'(\w+)(?:\[[^\]]*\]|\{[^}]*\})?\s*-->\s*(?:\|([^|]*)\|)?\s*(\w+)', mm):
        rg_edges.append({"source": m.group(1), "target": m.group(3), "label": (m.group(2) or "").strip()})
    status_path = os.path.join(ROOT, "research_methodology", "research_graph_status.json")
    status = json.load(open(status_path)) if os.path.exists(status_path) else {}
    for n in rg_nodes.values():
        n["status"] = status.get(n["id"], "pending")
    research_graph = {"nodes": list(rg_nodes.values()), "edges": rg_edges}
    cov_path = os.path.join(NM, "research_coverage", "coverage_ledger.json")
    coverage = json.load(open(cov_path)) if os.path.exists(cov_path) else {"rows": []}

    timelines = gen_timelines(cid); cards = gen_cards(cid, sid); matrix = gen_matrix(cid, cid); deals = gen_deals(cid)
    approvals = gen_approvals(cid); setbacks = gen_setbacks(cid); takeda = gen_takeda(cid); conflicts = gen_conflicts(cid); strategy = gen_strategy(cid)
    for co, tl in timelines.items():
        if tl["available"] and not tl["events"]:
            errors.append(f"timeline for {co} parsed 0 events")
    if isinstance(cards, list) and not cards:
        errors.append("mechanism cards parsed 0 cards")
    reports = gen_reports(cid, sid); qa_index = gen_qa(claims, sources, reports)
    if errors:
        print("PIPELINE FAILED — broken references:"); print("\n".join(sorted(set(errors)))); return 1

    ps_text = open(os.path.join(ROOT, "PROJECT_STATE.md")).read() if os.path.exists(os.path.join(ROOT, "PROJECT_STATE.md")) else ""
    phase = re.search(r"\*\*Current phase:\*\*\s*(.+)", ps_text)
    cards_list = cards if isinstance(cards, list) else []
    project_state = {"built_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "phase": phase.group(1).strip() if phase else "unknown",
                     "sources": len(sources), "claims": len(claims),
                     "claims_by_status": dict(collections.Counter(c["status"] for c in claims)), "claims_by_kind": dict(collections.Counter(c["kind"] for c in claims)),
                     "claims_by_maturity": dict(collections.Counter(c["maturity"] for c in claims if c.get("maturity"))),
                     "claims_by_shard": dict(collections.Counter(c.get("merged_from_shard") or "canonical" for c in claims)),
                     "claims_contrary": sum(1 for c in claims if c.get("contrary_evidence")), "claims_single_source": sum(1 for c in claims if c.get("single_interested_source")),
                     "sources_by_tier": dict(collections.Counter(s["credibility_tier"] for s in sources)), "sources_by_company": dict(collections.Counter(s["company"] for s in sources)),
                     "datasets": {"timeline_events": sum(len(t["events"]) for t in timelines.values()), "mechanism_cards": sum(1 for c in cards_list if c["kind"] == "mechanism_card"),
                                  "moat_entries": sum(1 for c in cards_list if c["kind"] == "moat"), "deal_edges": len(deals["edges"]), "deal_inventory_rows": len(deals["inventory"]),
                                  "approvals": len(approvals["rows"]), "setbacks": len(setbacks["rows"]), "takeda_capabilities": len(takeda["capabilities"]), "takeda_backlog": len(takeda["backlog"]),
                                  "conflicts": len(conflicts["items"]), "maturity_matrix_rows": len(matrix["rows"]),
                                  "reports": reports["count"], "qa_passages": qa_index["count"]},
                     "strategy_files": {k: v["available"] for k, v in strategy.items()},
                     "lead_model": "Claude Fable 5.1", "harness": "Kiro Crew 0.13.1.1 / kiro-cli 3.5.0"}

    inv = collections.defaultdict(set)
    for c in claims:
        txt = " ".join([c["statement"], " ".join(c.get("entities", [])), " ".join(c.get("domains", [])), " ".join(c.get("related_reports", []) or []), c.get("event_date") or "", c.get("reporting_period") or "", c["claim_id"]])
        for t in tokens(txt):
            inv[t].add(c["claim_id"])
    for s in sources:
        for t in tokens(s["title"] + " " + s["publisher"] + " " + s["source_id"]):
            inv[t].add(s["source_id"])
    search_index = {t: sorted(v) for t, v in inv.items()}

    for d in (NORM, IDX, DB, APP_DATA):
        os.makedirs(d, exist_ok=True)
    pub_claims = [{k: v for k, v in c.items() if not k.startswith("_") and k not in ("shard_record", "added_by", "merged_at")} for c in claims]
    out = {"sources.json": sources, "claims.json": pub_claims, "financials.json": financials, "products.json": products, "knowledge_graph.json": kg, "research_graph.json": research_graph,
           "coverage.json": coverage, "maturity.json": maturity, "maturity_matrix.json": matrix, "project_state.json": project_state, "timelines.json": timelines,
           "mechanism_cards.json": {"available": bool(cards_list), "reason": None if cards_list else cards.get("reason"), "cards": cards_list}, "deals.json": deals, "approvals.json": approvals, "setbacks.json": setbacks,
           "takeda_baseline.json": takeda, "conflicts.json": conflicts, "strategy.json": {"files": strategy}, "reports.json": reports, "qa_index.json": qa_index, "research_log.json": gen_research_log()}
    for fn, obj in out.items():
        with open(os.path.join(NORM, fn), "w") as f:
            json.dump(obj, f, ensure_ascii=False, indent=0)
        shutil.copy(os.path.join(NORM, fn), os.path.join(APP_DATA, fn))
    with open(os.path.join(IDX, "search_index.json"), "w") as f:
        json.dump(search_index, f)
    shutil.copy(os.path.join(IDX, "search_index.json"), os.path.join(APP_DATA, "search_index.json"))

    dbp = os.path.join(DB, "medicine.sqlite")
    if os.path.exists(dbp):
        os.remove(dbp)
    con = sqlite3.connect(dbp); cur = con.cursor()
    cur.execute("create table sources(source_id text primary key, company text, title text, publisher text, source_type text, credibility_tier text, canonical_url text, published_at text, reporting_period text, access_status text, json text)")
    cur.execute("create table claims(claim_id text primary key, kind text, status text, maturity text, value real, unit text, reporting_period text, event_date text, statement text, merged_from_shard text, single_interested_source integer, has_contrary_evidence integer, json text)")
    cur.execute("create table claim_companies(claim_id text, company text)")
    cur.execute("create table claim_sources(claim_id text, source_id text, locator text)")
    cur.execute("create table claim_entities(claim_id text, entity text)")
    cur.execute("create table timeline_events(company text, date text, year integer, event text, claim_ids text)")
    cur.execute("create table deal_edges(from_company text, to_party text, type text, date text, status text, value_usd_m real, claim_ids text)")
    cur.execute("create table approvals(kind text, company text, date text, product text, detail text, claim_ids text)")
    cur.execute("create table setbacks(company text, when_text text, asset text, what text, claim_ids text)")
    for s in sources:
        cur.execute("insert into sources values(?,?,?,?,?,?,?,?,?,?,?)", (s["source_id"], s["company"], s["title"], s["publisher"], s["source_type"], s["credibility_tier"], s["canonical_url"], s.get("published_at"), s.get("reporting_period"), s["access_status"], json.dumps(s)))
    for c in pub_claims:
        v = c.get("value"); v = v if isinstance(v, (int, float)) else None
        cur.execute("insert into claims values(?,?,?,?,?,?,?,?,?,?,?,?,?)", (c["claim_id"], c["kind"], c["status"], c.get("maturity"), v, c.get("unit"), c.get("reporting_period"), c.get("event_date"), c["statement"],
                                                                         c.get("merged_from_shard"), 1 if c.get("single_interested_source") else 0, 1 if c.get("contrary_evidence") else 0, json.dumps(c)))
        for co in c["companies"]:
            cur.execute("insert into claim_companies values(?,?)", (c["claim_id"], co))
        for ss in c["supporting_sources"]:
            cur.execute("insert into claim_sources values(?,?,?)", (c["claim_id"], ss["source_id"], ss["locator"]))
        for e in c.get("entities", []):
            cur.execute("insert into claim_entities values(?,?)", (c["claim_id"], e))
    for co, tl in timelines.items():
        for e in tl["events"]:
            cur.execute("insert into timeline_events values(?,?,?,?,?)", (co, e["date"], e["year"], e["event"], ",".join(e["claim_ids"])))
    for e in deals["edges"]:
        cur.execute("insert into deal_edges values(?,?,?,?,?,?,?)", (e["from"], e["to"], e["type"], e.get("date"), e.get("status"), e.get("value_usd_m"), ",".join(e["claim_ids"])))
    for a in approvals["rows"]:
        cur.execute("insert into approvals values(?,?,?,?,?,?)", (a["kind"], a["company"], a["date"], a["product"], a["detail"], ",".join(a["claim_ids"])))
    for s in setbacks["rows"]:
        cur.execute("insert into setbacks values(?,?,?,?,?)", (s["company"], s["when"], s["asset"], s["what"], ",".join(s["claim_ids"])))
    con.commit(); con.close()
    print(json.dumps({"sources": len(sources), "claims": len(claims), "kg_nodes": len(kg["nodes"]), "kg_edges": len(kg["edges"]), "maturity_rows": len(maturity), "index_terms": len(search_index),
                      "datasets": project_state["datasets"], "strategy_files_present": [k for k, v in strategy.items() if v["available"]], "app_data": APP_DATA}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
