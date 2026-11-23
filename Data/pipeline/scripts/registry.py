#!/usr/bin/env python3
"""Single-writer registry tool for MEDICINE 2040.

Usage:
  registry.py add-source  <json-file-or-->        # allocates SRC-id, validates, appends
  registry.py add-claim   <json-file-or-->        # allocates CLM-id, validates, appends
  registry.py merge-staging                       # merge New_mediciine/evidence_library/staging/*/*.jsonl
  registry.py next-id source|claim
  registry.py stats

Records may use temporary ids ("TMP-<name>") inside a staged batch; references between
staged claims and staged sources are resolved during merge. Validation is schema-light
(required keys, enums, patterns) and stdlib-only so it runs on Python 3.9 without deps.
All writes are append-only; a lock file guards concurrent appends.
"""
import json, os, re, sys, fcntl, datetime, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EL = os.path.join(ROOT, "New_mediciine", "evidence_library")
SRC_PATH = os.path.join(EL, "source_registry.jsonl")
CLM_PATH = os.path.join(EL, "claims_registry.jsonl")
STAGING = os.path.join(EL, "staging")
SCHEMAS = os.path.join(EL, "schemas")
LOCK = os.path.join(EL, ".registry.lock")


def load_schema(name):
    with open(os.path.join(SCHEMAS, name)) as f:
        return json.load(f)


def read_jsonl(path):
    out = []
    if not os.path.exists(path):
        return out
    with open(path) as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise SystemExit(f"{path}:{i}: bad JSON: {e}")
    return out


def validate(rec, schema, label):
    errs = []
    for k in schema.get("required", []):
        if k not in rec or rec[k] in (None, "", []):
            errs.append(f"missing required '{k}'")
    props = schema.get("properties", {})
    for k, v in rec.items():
        p = props.get(k)
        if not p:
            continue
        if "enum" in p and v is not None and v not in p["enum"]:
            errs.append(f"'{k}'={v!r} not in enum")
        if "pattern" in p and isinstance(v, str) and not re.match(p["pattern"], v):
            errs.append(f"'{k}'={v!r} fails pattern {p['pattern']}")
        if p.get("type") == "array" and v is not None:
            if not isinstance(v, list):
                errs.append(f"'{k}' must be a list")
            else:
                item = p.get("items", {})
                if "enum" in item:
                    for x in v:
                        if x not in item["enum"]:
                            errs.append(f"'{k}' item {x!r} not in enum")
                if "pattern" in item:
                    for x in v:
                        if not isinstance(x, str) or not re.match(item["pattern"], x):
                            errs.append(f"'{k}' item {x!r} fails pattern")
                if item.get("type") == "object" and "required" in item:
                    for x in v:
                        for rk in item["required"]:
                            if not isinstance(x, dict) or rk not in x:
                                errs.append(f"'{k}' item missing '{rk}'")
    if errs:
        raise SystemExit(f"{label} invalid: " + "; ".join(errs) + f"\nrecord={json.dumps(rec)[:300]}")


def next_id(kind, existing=None):
    path = SRC_PATH if kind == "source" else CLM_PATH
    prefix = "SRC" if kind == "source" else "CLM"
    key = "source_id" if kind == "source" else "claim_id"
    recs = existing if existing is not None else read_jsonl(path)
    # Director (A0) allocates only from 000001..000999. Shard records merged from
    # tools/evidence.py keep their own ranges (001000+), so they must not move this counter.
    n = 0
    for r in recs:
        m = re.match(rf"^{prefix}-(\d{{6}})$", r.get(key, ""))
        if m and int(m.group(1)) < 1000:
            n = max(n, int(m.group(1)))
    if n + 1 >= 1000:
        raise SystemExit("director ID range 000001..000999 exhausted; extend ID_RANGES deliberately")
    return f"{prefix}-{n + 1:06d}"


def append(path, rec):
    with open(LOCK, "a+") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        with open(path, "a") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        fcntl.flock(lk, fcntl.LOCK_UN)


def add_source(rec, existing_sources=None):
    schema = load_schema("source.schema.json")
    # de-dup on canonical_url
    existing = existing_sources if existing_sources is not None else read_jsonl(SRC_PATH)
    for e in existing:
        if e.get("canonical_url") == rec.get("canonical_url"):
            return e["source_id"], False
    rec["source_id"] = next_id("source", existing)
    rec.setdefault("retrieved_at", datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"))
    validate(rec, schema, rec["source_id"])
    append(SRC_PATH, rec)
    existing.append(rec)
    return rec["source_id"], True


def add_claim(rec, existing_claims=None, known_sources=None):
    schema = load_schema("claim.schema.json")
    existing = existing_claims if existing_claims is not None else read_jsonl(CLM_PATH)
    known = known_sources if known_sources is not None else {s["source_id"] for s in read_jsonl(SRC_PATH)}
    for s in rec.get("supporting_sources", []):
        if s.get("source_id") not in known:
            raise SystemExit(f"claim references unknown source {s.get('source_id')}")
    for s in rec.get("independent_corroboration", []) or []:
        if s not in known:
            raise SystemExit(f"claim corroboration references unknown source {s}")
    rec["claim_id"] = next_id("claim", existing)
    rec.setdefault("last_verified", datetime.date.today().isoformat())
    validate(rec, schema, rec["claim_id"])
    append(CLM_PATH, rec)
    existing.append(rec)
    return rec["claim_id"], True


def merge_staging():
    """Merge staged batches. Each staging file holds mixed records with a 'record_type'
    of 'source' or 'claim'. Temporary ids 'TMP-*' used in supporting_sources are remapped."""
    if not os.path.isdir(STAGING):
        print("no staging dir"); return
    sources = read_jsonl(SRC_PATH)
    claims = read_jsonl(CLM_PATH)
    known = {s["source_id"] for s in sources}
    n_s = n_c = 0
    for agent in sorted(os.listdir(STAGING)):
        adir = os.path.join(STAGING, agent)
        if not os.path.isdir(adir):
            continue
        for fn in sorted(os.listdir(adir)):
            if not fn.endswith(".jsonl"):
                continue
            path = os.path.join(adir, fn)
            tmpmap = {}
            recs = read_jsonl(path)
            for r in recs:
                if r.get("record_type") == "source":
                    tmp = r.pop("tmp_id", None)
                    r.pop("record_type", None)
                    r.setdefault("added_by", agent)
                    sid, created = add_source(r, sources)
                    known.add(sid)
                    if tmp:
                        tmpmap[tmp] = sid
                    n_s += int(created)
            for r in recs:
                if r.get("record_type") == "claim":
                    r.pop("record_type", None)
                    r.setdefault("added_by", agent)
                    for s in r.get("supporting_sources", []):
                        s["source_id"] = tmpmap.get(s["source_id"], s["source_id"])
                    r["independent_corroboration"] = [tmpmap.get(x, x) for x in r.get("independent_corroboration", []) or []]
                    add_claim(r, claims, known)
                    n_c += 1
            done = path + ".merged"
            os.rename(path, done)
            print(f"merged {path} -> {done}")
    print(f"sources added: {n_s}; claims added: {n_c}")


def stats():
    s = read_jsonl(SRC_PATH); c = read_jsonl(CLM_PATH)
    by_co = {}
    for r in s:
        by_co[r.get("company")] = by_co.get(r.get("company"), 0) + 1
    st = {}
    for r in c:
        st[r.get("status")] = st.get(r.get("status"), 0) + 1
    print(json.dumps({"sources": len(s), "sources_by_company": by_co, "claims": len(c), "claims_by_status": st}, indent=2))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 1
    cmd = argv[1]
    if cmd == "next-id":
        print(next_id(argv[2])); return 0
    if cmd == "stats":
        stats(); return 0
    if cmd == "merge-staging":
        merge_staging(); return 0
    if cmd in ("add-source", "add-claim"):
        src = sys.stdin if argv[2] == "-" else open(argv[2])
        data = json.load(src)
        recs = data if isinstance(data, list) else [data]
        for rec in recs:
            if cmd == "add-source":
                sid, created = add_source(rec)
                print(sid, "created" if created else "exists")
            else:
                cid, _ = add_claim(rec)
                print(cid)
        return 0
    if cmd == "sha256":
        print(sha256_file(argv[2])); return 0
    print(__doc__); return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
