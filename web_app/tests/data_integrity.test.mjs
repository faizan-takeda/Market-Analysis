// Application gate tests (machine-checked, no framework needed): run with `npm test` after `npm run data && npm run build`.
// 1 datasets exist and parse · 2 registry cross-refs (sources, claims) · 3 every claim ID referenced by any generated dataset exists
// 4 strategy files validated when present / flagged absent when not · 5 no research literals in src/ · 6 every route is wired and in the built bundle
// 7 dataset counts in project_state match the files · 8 public/data == data/normalized == dist/data · 9 search index resolves.
import fs from "node:fs"; import path from "node:path"; import { fileURLToPath } from "node:url";
const here = path.dirname(fileURLToPath(import.meta.url)); const app = path.join(here, ".."); const root = path.join(app, ".."); const data = path.join(app, "public", "data");
const results = []; const ok = (name, cond, detail = "") => results.push({ name, pass: !!cond, detail: cond ? "" : String(detail).slice(0, 400) });
const load = (n) => JSON.parse(fs.readFileSync(path.join(data, n), "utf8"));
const need = ["claims", "sources", "financials", "products", "knowledge_graph", "research_graph", "coverage", "maturity", "maturity_matrix", "project_state", "search_index", "timelines", "mechanism_cards", "deals", "approvals", "setbacks", "takeda_baseline", "conflicts", "strategy", "reports", "qa_index", "research_log"].map((n) => n + ".json");
for (const n of need) ok(`dataset ${n} present and parses`, fs.existsSync(path.join(data, n)) && (() => { try { load(n); return true; } catch { return false; } })());
const claims = load("claims.json"), sources = load("sources.json"), products = load("products.json"), kg = load("knowledge_graph.json"), fin = load("financials.json");
const state = load("project_state.json"), timelines = load("timelines.json"), cards = load("mechanism_cards.json"), deals = load("deals.json"), approvals = load("approvals.json"), setbacks = load("setbacks.json");
const takeda = load("takeda_baseline.json"), conflicts = load("conflicts.json"), strategy = load("strategy.json"), matrix = load("maturity_matrix.json"), maturity = load("maturity.json"), index = load("search_index.json");
const reports = load("reports.json"), qa = load("qa_index.json");
const sid = new Set(sources.map((s) => s.source_id)); const cid = new Set(claims.map((c) => c.claim_id));

// --- registry integrity
ok("claims non-empty", claims.length > 0, claims.length);
ok("all claim sources resolve", claims.every((c) => c.supporting_sources.every((s) => sid.has(s.source_id))));
ok("all claims have locators", claims.every((c) => c.supporting_sources.every((s) => (s.locator || "").length >= 3)));
const tier = Object.fromEntries(sources.map((s) => [s.source_id, s.credibility_tier]));
ok("no SUPPORTED FACT on T4/T5 only", claims.filter((c) => c.kind === "FACT" && c.status === "SUPPORTED").every((c) => c.supporting_sources.some((s) => !["T4_expert_opinion", "T5_speculative"].includes(tier[s.source_id]))));
ok("claims carry enrichment fields", claims.every((c) => "status" in c && "kind" in c && "maturity" in c && "event_date" in c && "single_interested_source" in c && "contrary_evidence" in c));
ok("merged claims carry merged_from_shard", claims.filter((c) => c.merged_from_shard).length > 0);
ok("financials have 3 competitors with revenue", ["LLY", "JNJ", "ABBV"].every((co) => fin[co] && fin[co].concepts.revenue && Object.keys(fin[co].concepts.revenue).length >= 5));
ok("every financial cell carries a claim id", Object.values(fin).every((co) => Object.values(co.concepts).every((c) => Object.values(c).every((v) => cid.has(v.claim_id)))));

// --- every claim ID referenced by any generated dataset exists
const ids = (o, acc = []) => { if (typeof o === "string") { for (const m of o.matchAll(/CLM-\d{6}/g)) acc.push(m[0]); } else if (Array.isArray(o)) o.forEach((x) => ids(x, acc)); else if (o && typeof o === "object") Object.values(o).forEach((x) => ids(x, acc)); return acc; };
const refSets = { products, knowledge_graph: kg, timelines, mechanism_cards: cards, deals, approvals, setbacks, takeda_baseline: takeda, conflicts, strategy, maturity_matrix: matrix, maturity };
for (const [n, o] of Object.entries(refSets)) { const bad = ids(o).filter((k) => !cid.has(k)); ok(`all claim IDs referenced in ${n} exist`, bad.length === 0, bad.slice(0, 5).join(",")); }
const cardSrc = (cards.cards ?? []).flatMap((c) => c.source_ids); ok("mechanism-card source IDs exist", cardSrc.every((s) => sid.has(s)), cardSrc.filter((s) => !sid.has(s)).join(","));
ok("product series claim ids resolve", [...products.series, ...products.loe_events].every((s) => s.claims.every((k) => cid.has(k))));

// --- dataset presence and live counts
ok("timelines present for all four companies", ["LLY", "JNJ", "ABBV", "TAK"].every((c) => timelines[c]?.available && timelines[c].events.length > 0));
ok("every timeline event is dated and evidenced", Object.values(timelines).every((t) => t.events.every((e) => e.date && e.claim_ids.length > 0)));
ok("mechanism cards parsed (cards and moats)", cards.available && cards.cards.some((c) => c.kind === "mechanism_card") && cards.cards.some((c) => c.kind === "moat"));
ok("every mechanism entry cites claims", cards.cards.every((c) => c.claim_ids.length > 0 || c.gap));
ok("deals: edges and inventory present", deals.available && deals.edges.length > 0 && deals.inventory.length > 0);
ok("deal edges evidenced", deals.edges.every((e) => e.claim_ids.length > 0));
ok("takeda baseline present with classes and backlog", takeda.available && takeda.capabilities.length > 0 && takeda.backlog.length > 0);
ok("approvals/setbacks datasets declare availability", typeof approvals.available === "boolean" && typeof setbacks.available === "boolean");
if (approvals.available) ok("approval rows evidenced", approvals.rows.length > 0 && approvals.rows.every((r) => r.claim_ids.length > 0));
if (setbacks.available) ok("setback rows evidenced", setbacks.rows.length > 0 && setbacks.rows.every((r) => r.claim_ids.length > 0));
const d = state.datasets;
ok("project_state counts match dataset files", d.timeline_events === Object.values(timelines).reduce((a, t) => a + t.events.length, 0) && d.deal_edges === deals.edges.length && d.approvals === approvals.rows.length && d.setbacks === setbacks.rows.length
  && d.takeda_capabilities === takeda.capabilities.length && d.conflicts === conflicts.items.length && state.claims === claims.length && state.sources === sources.length, JSON.stringify(d));

// --- strategy contract: validated when present, explicitly absent otherwise
const sf = strategy.files; const names = ["strategy_bets", "assumptions", "portfolios", "stage_gates", "roadmap", "scenarios", "council_reviews", "counterarguments", "takeda_lessons"];
ok("strategy.json lists every contract file", names.every((n) => n in sf));
ok("strategy availability flags match project_state", names.every((n) => sf[n].available === state.strategy_files[n]));
ok("absent strategy files carry no data", names.every((n) => sf[n].available || sf[n].data === null));
const asm = new Set((sf.assumptions.data?.assumptions ?? []).map((a) => a.id)); const bets = new Set((sf.strategy_bets.data?.bets ?? []).map((b) => b.id));
if (sf.assumptions.available) { const used = []; const walk = (o, k = "") => { if (Array.isArray(o)) o.forEach((x) => walk(x, k)); else if (o && typeof o === "object") Object.entries(o).forEach(([kk, v]) => walk(v, kk)); else if (typeof o === "string" && k === "assumption_ids") used.push(o); }; walk(sf); ok("strategy assumption IDs defined", used.every((a) => asm.has(a)), used.filter((a) => !asm.has(a)).join(",")); }
if (sf.strategy_bets.available) { const refs = [...(sf.portfolios.data?.portfolios ?? []).flatMap((p) => p.bets.map((b) => b.bet_id)), ...(sf.roadmap.data?.milestones ?? []).map((m) => m.bet_id), ...(sf.stage_gates.data?.gates ?? []).map((g) => g.bet_id), ...[...bets].flatMap((id) => sf.strategy_bets.data.bets.find((b) => b.id === id).prerequisites ?? [])]; ok("strategy bet references resolve", refs.every((r) => bets.has(r)), refs.filter((r) => !bets.has(r)).join(",")); }
if (sf.roadmap.available) { const m = new Set(sf.roadmap.data.milestones.map((x) => x.id)); ok("roadmap dependencies resolve", sf.roadmap.data.milestones.every((x) => (x.depends_on ?? []).every((d) => m.has(d)))); }
if (sf.portfolios.available) ok("every simulated portfolio value is labelled ASSUMPTION", sf.portfolios.data.portfolios.every((p) => p.basis === "ASSUMPTION"));

// --- report bundle (the reader's backbone) and the Q&A index
const mdFiles = []; const walk = (d) => { for (const e of fs.readdirSync(d, { withFileTypes: true })) { if (e.name.startsWith(".") || ["node_modules", "raw_documents", "extracted_text"].includes(e.name)) continue; const p = path.join(d, e.name); if (e.isDirectory()) walk(p); else if (e.name.toLowerCase().endsWith(".md")) mdFiles.push(path.relative(root, p).split(path.sep).join("/")); } };
// Layout: the MEDICINE repository (../New_mediciine, ../data, ../deliverables) or the packaged Final_Medicine folder
// (../Data/{normalized,database}, ../index.html). Repo-only checks are skipped in the package.
const repoLayout = fs.existsSync(path.join(root, "New_mediciine"));
const firstExisting = (...cands) => cands.find((p) => fs.existsSync(p));
if (repoLayout) {
  for (const r of ["New_mediciine", "strategy", "research_methodology", "quality"]) walk(path.join(root, r));
  for (const f of ["map.md", "PROJECT_STATE.md", "CONTINUE.md", "COORDINATION.md", "README.md"]) if (fs.existsSync(path.join(root, f))) mdFiles.push(f);
}
const rpaths = new Set(reports.reports.map((r) => r.path));
ok("reports.json covers at least 95 Markdown files", reports.reports.length >= 95, reports.reports.length);
if (repoLayout) ok("reports.json covers every Markdown file in the research tree", mdFiles.every((f) => rpaths.has(f)), mdFiles.filter((f) => !rpaths.has(f)).slice(0, 5).join(","));
ok("every report has title, pillar, section, markdown and word count", reports.reports.every((r) => r.title && r.pillar && r.section && r.markdown.length > 0 && r.word_count > 0 && r.updated));
ok("every claim-id chip in a report resolves to a claim", reports.reports.every((r) => r.claim_ids.every((k) => cid.has(k))));
ok("every pillar with a reports page has reports", ["companies", "commercial", "rd", "dataai", "partnerships", "policy", "takeda", "future", "evidence"].every((p) => reports.reports.some((r) => r.pillar === p)));
ok("Q&A index has claim, report and source passages", ["claim", "report", "source"].every((k) => qa.docs.some((d) => d.k === k)) && qa.count === qa.docs.length);
ok("Q&A claim passages cover every claim", claims.every((c) => qa.docs.some((d) => d.k === "claim" && d.id === c.claim_id)) || claims.length === qa.docs.filter((d) => d.k === "claim").length);
ok("research log datasets parse", Array.isArray(load("research_log.json").experiments) && Array.isArray(load("research_log.json").backlog));

// --- UI source: no research literals; routes wired
const srcDir = path.join(app, "src"); const srcFiles = fs.readdirSync(srcDir).filter((f) => /\.(tsx?|css)$/.test(f)); const read = (f) => fs.readFileSync(path.join(srcDir, f), "utf8");
const code = srcFiles.filter((f) => /\.tsx?$/.test(f) && f !== "narrative.ts").map((f) => [f, read(f).replace(/\/\*[\s\S]*?\*\/|(^|[^:])\/\/.*$/gm, "$1")]);
const hit = (re) => code.filter(([, t]) => re.test(t)).map(([f]) => f);
ok("no claim/source ID literals in UI source (IDs live in narrative.ts only)", hit(/\b(CLM|SRC)-\d{3,}/).length === 0, hit(/\b(CLM|SRC)-\d{3,}/).join(","));
ok("no hardcoded revenue literals", hit(/\b(65,?179|94,?193|61,?160|4,?505\.7)\b/).length === 0);
ok("no comma-grouped or money/percent number literals", hit(/\b\d{1,3}(,\d{3})+\b|\b\d+(\.\d+)?\s?(bn|billion|percent)\b|USD\s?\d|\$\d|¥\d/).length === 0, hit(/\b\d{1,3}(,\d{3})+\b|\b\d+(\.\d+)?\s?(bn|billion|percent)\b|USD\s?\d|\$\d|¥\d/).join(","));
ok("no year literals in UI source", hit(/\b(19|20)(?!40\b)\d\d\b/).length === 0, hit(/\b(19|20)(?!40\b)\d\d\b/).join(","));
ok("no sample / lorem text", hit(/lorem ipsum|sample data|placeholder number/i).length === 0);
const narr = read("narrative.ts"); const nIds = [...narr.matchAll(/CLM-\d{6}/g)].map((m) => m[0]);
ok("narrative.ts has claim IDs and all exist", nIds.length > 0 && nIds.every((k) => cid.has(k)), nIds.filter((k) => !cid.has(k)).join(","));
ok("narrative.ts prose contains no digits", !/\d/.test(narr.replace(/\/\/.*$/gm, "").replace(/CLM-\d{6}/g, "").replace(/H1|H2|H3/g, "")), "digits found in narrative prose");
const main = read("routes.tsx"); const routes = [...main.matchAll(/<Route path="([^"]+)"/g)].map((m) => m[1]);
const expected = ["/", "/powerhouses", "/differentiators", "/pipeline", "/observatory", "/ecosystem", "/encyclopedia", "/takeda", "/strategy", "/portfolio", "/roadmap", "/uncertainty", "/research-graph",
  "/companies", "/companies/:slug", "/commercial", "/rd", "/data-ai", "/partnerships", "/policy", "/takeda-baseline", "/future", "/future/pharma", "/future/analogies", "/future/scenarios", "/future/council", "/future/other",
  "/evidence", "/sources", "/conflicts", "/coverage", "/method", "/runs", "/state", "/reports", "/read/*", "/ask"];
ok("all 12 view routes, the research graph and every pillar route are wired", expected.every((r) => routes.includes(r)), expected.filter((r) => !routes.includes(r)).join(","));
const navPaths = [...read("pillars.ts").matchAll(/path: "(\/[^"]*)"/g)].map((m) => m[1]);
const matches = (p) => routes.some((r) => r === p || (r.includes(":slug") && p.startsWith(r.split(":")[0]) && p.split("/").length === r.split("/").length));
ok("every navigation entry has a route", navPaths.every(matches), navPaths.filter((p) => !matches(p)).join(","));
ok("eleven pillars are defined", (read("pillars.ts").match(/^  \{ id: "/gm) ?? []).length === 11);
ok("strategy views show the explicit absent notice", /Absent kind="strategy"/.test(read("views_c.tsx")) && /Strategy module not yet produced — see PROJECT_STATE\.md/.test(read("data.ts")));

// --- built output smoke test (routes render from the bundle)
const dist = path.join(app, "dist"); const distIdx = path.join(dist, "index.html");
ok("dist/index.html built", fs.existsSync(distIdx));
if (fs.existsSync(distIdx)) {
  const html = fs.readFileSync(distIdx, "utf8"); const js = [...html.matchAll(/src="\.?\/?(assets\/[^"]+\.js)"/g)].map((m) => path.join(dist, m[1]));
  ok("index.html references an existing bundle with a root element", js.length > 0 && js.every((f) => fs.existsSync(f)) && /id="root"/.test(html));
  const bundle = js.map((f) => fs.readFileSync(f, "utf8")).join("\n");
  for (let n = 1; n <= 12; n++) ok(`view ${n} is in the built bundle`, bundle.includes(`View ${n} · `), `View ${n}`);
  ok("every route path is in the built bundle", expected.every((r) => bundle.includes(`path:"${r}"`) || bundle.includes(`path: "${r}"`)));
  ok("Ask and reader code is in the built bundle", bundle.includes("No evidence in the corpus") && bundle.includes("data-id") && bundle.includes("medicine-data"));
  ok("bundle was built after the latest source edit", srcFiles.every((f) => fs.statSync(path.join(srcDir, f)).mtimeMs <= fs.statSync(distIdx).mtimeMs + 1000), "run npm run build");
  const stale = need.filter((n) => !fs.existsSync(path.join(dist, "data", n)) || fs.statSync(path.join(dist, "data", n)).size !== fs.statSync(path.join(data, n)).size);
  ok("dist/data matches public/data (no stale build)", stale.length === 0, stale.join(","));
}
// --- single-file export
const single = firstExisting(path.join(root, "deliverables", "MEDICINE_2040_Hub.html"), path.join(root, "MEDICINE_2040_Hub.html"), path.join(root, "index.html")) ?? path.join(root, "deliverables", "MEDICINE_2040_Hub.html");
ok("single-file export exists (run scripts/build_single_file.py)", fs.existsSync(single));
if (fs.existsSync(single)) {
  const h = fs.readFileSync(single, "utf8"); const mb = fs.statSync(single).size / 1048576;
  ok("single file contains the data blob and the app", h.includes('id="medicine-data"') && h.includes("No evidence in the corpus") && h.includes('<div id="root">'));
  const shell = h.replace(/<script[^>]*>[\s\S]*?<\/script>/g, (m) => (/\ssrc=/.test(m.slice(0, m.indexOf(">"))) ? m : "<script></script>")).replace(/<style>[\s\S]*?<\/style>/g, "<style></style>");
  ok("single file references no external script, stylesheet or font", !/<script[^>]+src=/.test(shell) && !/<link[^>]+(rel="stylesheet"|href=)/.test(shell) && !/fonts\.googleapis|cdn\./.test(shell));
  ok("single file is under 15 MB", mb < 15, mb.toFixed(1));
  const m = h.match(/<script type="application\/json" id="medicine-data">([\s\S]*?)<\/script>/); let blob = null; try { blob = JSON.parse(m[1]); } catch { /* reported below */ }
  ok("single file data blob parses and holds every dataset", blob && need.every((n) => n in blob), blob ? need.filter((n) => !(n in blob)).join(",") : "unparseable");
  ok("single file data equals public/data (not stale)", blob && blob["claims.json"].length === claims.length && blob["reports.json"].count === reports.count, "rebuild with scripts/build_single_file.py");
}
const dataRoot = firstExisting(path.join(root, "data", "normalized"), path.join(root, "Data", "normalized"));
if (dataRoot) {
  const drift = need.filter((n) => n !== "search_index.json" && (!fs.existsSync(path.join(dataRoot, n)) || !fs.readFileSync(path.join(dataRoot, n)).equals(fs.readFileSync(path.join(data, n)))));
  ok("public/data equals the normalized data folder", drift.length === 0, drift.join(","));
  ok("sqlite database exists", fs.existsSync(path.join(path.dirname(dataRoot), "database", "medicine.sqlite")));
}

// --- search index
const all = new Set([...cid, ...sid]); let bad = 0; for (const v of Object.values(index)) for (const x of v) if (!all.has(x)) bad++;
ok("search index resolves to claims/sources", bad === 0, `${bad} dangling`);
ok("search index covers entities, domains and source titles", Object.keys(index).length > 1000 && "skyrizi" in index);

const failed = results.filter((r) => !r.pass);
const report = { run_at: new Date().toISOString(), total: results.length, passed: results.length - failed.length, failed: failed.length, results };
const out = path.join(root, "quality", "application_tests"); fs.mkdirSync(out, { recursive: true });
fs.writeFileSync(path.join(out, `app_tests_${report.run_at.slice(0, 10)}.json`), JSON.stringify(report, null, 2));
console.log(JSON.stringify({ total: report.total, passed: report.passed, failed: report.failed, failures: failed.map((f) => `${f.name}: ${f.detail}`) }, null, 1));
process.exit(failed.length ? 1 : 0);
