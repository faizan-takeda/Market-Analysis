#!/usr/bin/env python3
"""Download annual-report primary documents (10-K / 20-F HTML, public domain) listed in the
SEC inventories, convert to plain text, store under raw_documents/sec and extracted_text/sec,
and upgrade the matching source records (access_status -> retrieved, local paths, sha256).

Usage: python3 scripts/sec_fetch_filings.py LLY:2025,2024 JNJ:2025,2024 ABBV:2025,2024 TAK:2026
(the number is the period-end YEAR of the filing's report_period)
"""
import json, os, re, sys, html, hashlib, time
from html.parser import HTMLParser
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sec_ingest import fetch, META, RAW, ROOT  # noqa
from registry import read_jsonl, SRC_PATH, LOCK  # noqa
import fcntl

EXT = os.path.join(ROOT, "New_mediciine", "evidence_library", "extracted_text", "sec")


class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.out = []; self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "head"):
            self.skip += 1
        if tag in ("p", "div", "br", "tr", "li", "h1", "h2", "h3", "h4", "table"):
            self.out.append("\n")
        if tag in ("td", "th"):
            self.out.append(" | ")
    def handle_endtag(self, tag):
        if tag in ("script", "style", "head") and self.skip:
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def to_text(raw_html):
    p = Text(); p.feed(raw_html)
    t = html.unescape("".join(p.out))
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip()


def update_sources(mutator):
    with open(LOCK, "a+") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        recs = read_jsonl(SRC_PATH)
        changed = 0
        for r in recs:
            if mutator(r):
                changed += 1
        tmp = SRC_PATH + ".tmp"
        with open(tmp, "w") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        os.replace(tmp, SRC_PATH)
        fcntl.flock(lk, fcntl.LOCK_UN)
    return changed


def main(argv):
    os.makedirs(RAW, exist_ok=True); os.makedirs(EXT, exist_ok=True)
    done = []
    for spec in argv[1:]:
        ticker, years = spec.split(":"); years = years.split(",")
        inv = json.load(open(os.path.join(META, f"{ticker}_sec_filings_inventory.json")))
        for r in inv["filings"]:
            if r["form"] in ("10-K", "20-F") and r["report_period"][:4] in years:
                url = r["primary_document_url"]; accn = r["accession_number"]
                fn = f"{ticker}_{r['form'].replace('/', '')}_{r['report_period']}_{accn}.htm"
                raw_path = os.path.join(RAW, fn); txt_path = os.path.join(EXT, fn.replace(".htm", ".txt"))
                if not os.path.exists(raw_path):
                    print("fetching", url)
                    data = fetch(url, binary=True)
                    with open(raw_path, "wb") as f:
                        f.write(data)
                else:
                    data = open(raw_path, "rb").read()
                sha = hashlib.sha256(data).hexdigest()
                text = to_text(data.decode("utf-8", errors="replace"))
                with open(txt_path, "w") as f:
                    f.write(text)
                rel_raw = os.path.relpath(raw_path, ROOT); rel_txt = os.path.relpath(txt_path, ROOT)
                def mut(s, accn=accn, rel_raw=rel_raw, rel_txt=rel_txt, sha=sha):
                    if (s.get("identifiers") or {}).get("accession_number") == accn:
                        s["access_status"] = "retrieved"; s["local_document_path"] = rel_raw
                        s["local_extracted_text_path"] = rel_txt; s["content_sha256"] = sha
                        s["limitations"] = "Full primary document retrieved and converted to text; tables flattened with ' | ' separators."
                        return True
                    return False
                n = update_sources(mut)
                done.append({"ticker": ticker, "accn": accn, "bytes": len(data), "text_chars": len(text), "sources_updated": n, "text": rel_txt})
                print(f"  {ticker} {accn}: {len(data):,} bytes -> {len(text):,} chars; updated {n} source record(s)")
    print(json.dumps(done, indent=1))


if __name__ == "__main__":
    main(sys.argv)
