#!/usr/bin/env python3
"""Check relative markdown links across the repo (maps, reports, strategy docs).
Ignores http(s)/mailto links. Exit 1 if any relative link target is missing.
Writes quality/coverage_reports/link_check_<date>.json
"""
import os, re, sys, json, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"node_modules", ".git", "dist", "raw_documents"}
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def main():
    broken, total = [], 0
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dp, fn)
            with open(p, encoding="utf-8", errors="replace") as f:
                text = f.read()
            for m in LINK_RE.finditer(text):
                target = m.group(2)
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                total += 1
                t = target.split("#")[0]
                if not t:
                    continue
                tp = os.path.normpath(os.path.join(dp, t))
                if not os.path.exists(tp):
                    broken.append({"file": os.path.relpath(p, ROOT), "link": target})
    rep = {"run_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "relative_links_checked": total, "broken": broken, "result": "PASS" if not broken else "FAIL"}
    out = os.path.join(ROOT, "quality", "coverage_reports"); os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, f"link_check_{datetime.date.today().isoformat()}.json"), "w") as f:
        json.dump(rep, f, indent=2)
    print(json.dumps(rep, indent=2))
    return 0 if not broken else 1


if __name__ == "__main__":
    sys.exit(main())
