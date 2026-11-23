#!/usr/bin/env python3
"""Single-file export: inline the built app (JS, CSS) and every dataset.

Run after `npm run build` in web_app/ (or executive_application/ in the original repository). The result opens from file:// with no server:
data is read from <script type="application/json" id="medicine-data"> (see src/data.ts), routing is hash-based, and no
external font, script or stylesheet is referenced. Exit 1 on any missing input.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.join(ROOT, "executive_application")
DIST = os.path.join(APP, "dist")
OUT = os.path.join(ROOT, "deliverables", "MEDICINE_2040_Hub.html")
PACKAGE_ROOT = os.path.dirname(os.path.dirname(ROOT))
if os.path.isdir(os.path.join(PACKAGE_ROOT, "web_app")):
    ROOT = PACKAGE_ROOT
    APP = os.path.join(ROOT, "web_app")
    DIST = os.path.join(APP, "dist")
    OUT = os.path.join(ROOT, "index.html")
DATASETS = ["claims", "sources", "financials", "products", "knowledge_graph", "research_graph", "coverage", "maturity", "maturity_matrix", "project_state", "search_index", "timelines",
            "mechanism_cards", "deals", "approvals", "setbacks", "takeda_baseline", "conflicts", "strategy", "reports", "qa_index", "research_log"]


def fail(msg):
    print("SINGLE-FILE BUILD FAILED: " + msg); sys.exit(1)


def js_safe(s):
    return s.replace("</script", "<\\/script").replace("<!--", "<\\!--")


def main():
    idx = os.path.join(DIST, "index.html")
    if not os.path.exists(idx):
        fail("dist/index.html missing; run `npm run build` in the app directory first")
    html = open(idx, encoding="utf-8").read()
    blob = {}
    for n in DATASETS:
        p = os.path.join(DIST, "data", n + ".json")
        if not os.path.exists(p):
            fail("dist/data/%s.json missing; run scripts/build_app_data.py then npm run build" % n)
        blob[n + ".json"] = json.load(open(p, encoding="utf-8"))
    data = json.dumps(blob, ensure_ascii=False, separators=(",", ":"))
    data = data.replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")

    css_m = re.search(r'<link[^>]+rel="stylesheet"[^>]*href="([^"]+\.css)"[^>]*>', html)
    js_m = re.search(r'<script[^>]+type="module"[^>]*src="([^"]+\.js)"[^>]*></script>', html)
    if not css_m or not js_m:
        fail("could not find the built CSS/JS tags in dist/index.html")
    css = open(os.path.join(DIST, css_m.group(1).lstrip("./")), encoding="utf-8").read()
    js = open(os.path.join(DIST, js_m.group(1).lstrip("./")), encoding="utf-8").read()
    # Function replacements: the bundle contains backslashes and dollar signs that a string template would interpret.
    html = html.replace(css_m.group(0), lambda_str("<style>" + css.replace("</style", "<\\/style") + "</style>"))
    html = html.replace(js_m.group(0), "")
    body_script = '<script type="application/json" id="medicine-data">' + data + "</script>\n<script type=\"module\">" + js_safe(js) + "</script>"
    html = html.replace("</body>", body_script + "\n</body>", 1)
    if "medicine-data" not in html or "src=\"./assets" in html or "href=\"./assets" in html:
        fail("output still references external assets or lacks the data blob")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(json.dumps({"written": os.path.relpath(OUT, ROOT), "bytes": os.path.getsize(OUT), "mb": round(os.path.getsize(OUT) / 1048576, 2), "datasets": len(blob)}))
    return 0


def lambda_str(s):
    return s


if __name__ == "__main__":
    sys.exit(main())
