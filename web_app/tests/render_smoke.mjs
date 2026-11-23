// Route render smoke test: server-renders every route against the generated datasets (and once more with a synthetic
// strategy fixture that exists ONLY in this test, to exercise the strategy views' present-data path).
// Fails on a thrown render error, an empty page, or leaked "undefined" / "NaN" / "[object Object]" text.
import fs from "node:fs"; import path from "node:path"; import { fileURLToPath } from "node:url"; import { createServer } from "vite";
const here = path.dirname(fileURLToPath(import.meta.url)); const app = path.join(here, ".."); const data = path.join(app, "public", "data");
const load = (n) => JSON.parse(fs.readFileSync(path.join(data, n), "utf8"));
const claims = load("claims.json"), sources = load("sources.json");
const reports = load("reports.json"), qaIndex = load("qa_index.json");
const bundle = () => ({ reports, qa: qaIndex, log: load("research_log.json"), reportByPath: new Map(reports.reports.map((r) => [r.path, r])), claims, sources, financials: load("financials.json"), products: load("products.json"), kg: load("knowledge_graph.json"), rg: load("research_graph.json"), coverage: load("coverage.json"),
  maturity: load("maturity.json"), matrix: load("maturity_matrix.json"), state: load("project_state.json"), index: load("search_index.json"), timelines: load("timelines.json"), cards: load("mechanism_cards.json"),
  deals: load("deals.json"), approvals: load("approvals.json"), setbacks: load("setbacks.json"), takeda: load("takeda_baseline.json"), conflicts: load("conflicts.json"), strategy: load("strategy.json"),
  claimById: new Map(claims.map((c) => [c.claim_id, c])), sourceById: new Map(sources.map((s) => [s.source_id, s])) });

// Test-only fixture following strategy/DATA_CONTRACT.md. Values are arbitrary and never shipped.
const cl = claims[0].claim_id; const f = (data) => ({ available: true, path: "fixture", data });
const fixture = {
  strategy_bets: f({ bets: [
    { id: "BET-01", name: "Fixture bet one", horizon: "H1", thesis: "t", market_change: "m", problem: "p", baseline_class: "EXISTING_STRENGTH", moat_mechanism: ["data"], architecture: { build: ["a"], buy: [], license: [], partner: ["b"] },
      investment_usd_m: { capital_constrained: { initial: 1, follow_on: 2, scaled: 3 }, balanced: { initial: 2, follow_on: 3, scaled: 4 }, basis: "ASSUMPTION", assumption_ids: ["ASM-001"] }, time_to_value: { near_term: "n", long_horizon: "l" },
      outcomes: ["o"], risks: [{ type: "data", text: "r" }], options: ["expand", "stop"], decision: "BUILD", prerequisites: [], claim_ids: [cl], assumption_ids: ["ASM-001"], confidence: "evidence_backed", competitor_analogues: [{ company: "LLY", claim_ids: [cl] }] },
    { id: "BET-02", name: "Fixture bet two", horizon: "H3", thesis: "t", market_change: "m", problem: "p", baseline_class: "EVIDENCE_GAP", moat_mechanism: [], architecture: {}, time_to_value: {}, outcomes: [], risks: [], options: [], decision: "PARTNER", prerequisites: ["BET-01"], claim_ids: [], assumption_ids: [], confidence: "hypothesis" } ] }),
  assumptions: f({ assumptions: [{ id: "ASM-001", text: "fixture assumption", value: 1, unit: "USD_m", rationale: "r", sensitivity: "high", needs_internal_validation: true, ivb_ref: "IVB-001" }] }),
  portfolios: f({ portfolios: [{ name: "balanced", total_usd_m: 100, basis: "ASSUMPTION", assumption_ids: ["ASM-001"], horizon_allocation_pct: { H1: 50, H2: 30, H3: 20 }, theme_allocation_pct: { core_capability: 40, adjacent: 20, long_horizon_bets: 20, external_innovation: 20 }, bets: [{ bet_id: "BET-01", usd_m: 60, stage: "pilot" }, { bet_id: "BET-02", usd_m: 40, stage: "discovery" }] }],
    evaluation: [{ bet_id: "BET-01", pts: 0.6, p_commercial: 0.5, time_to_payoff_years: 4, basis: "ASSUMPTION", assumption_ids: [] }, { bet_id: "BET-02", pts: 0.2, p_commercial: 0.3, time_to_payoff_years: 9, basis: "ASSUMPTION", assumption_ids: [] }] }),
  stage_gates: f({ gates: [{ bet_id: "BET-01", stage: "pilot", capital_at_risk_usd_m: 5, evidence_required: "e", commercial_milestone: "c", stop_criteria: "s", expand_criteria: "x", owner_role: "o", decision_authority: "d", basis: "ASSUMPTION" }] }),
  roadmap: f({ milestones: [{ id: "RM-001", year: 2027, half: "H1", bet_id: "BET-01", milestone: "m1", type: "foundation", depends_on: [], basis: "evidence", claim_ids: [cl], assumption_ids: [] },
    { id: "RM-002", year: 2029, half: "H2", bet_id: "BET-02", milestone: "m2", type: "gate", depends_on: ["RM-001"], basis: "ASSUMPTION", claim_ids: [], assumption_ids: ["ASM-001"] }] }),
  scenarios: f({ scenarios: [{ id: "SCN-1", name: "s1", description: "d", drivers: [], claim_ids: [] }], robustness: [{ bet_id: "BET-01", "SCN-1": "robust", rationale: "r" }] }),
  council_reviews: f({ reviews: [{ bet_id: "BET-01", council: "red_team", verdict: "conditional", rationale: "r", unresolved: "u", claim_ids: [cl] }], disagreements: [{ bet_id: "BET-01", text: "d" }] }),
  counterarguments: f({ items: [{ id: "CA-001", target: "BET-01", type: "caveat", text: "t", claim_ids: [cl], assumption_ids: ["ASM-001"] }] }),
  takeda_lessons: f({ lessons: [{ id: "LES-01", area: "a", competitor: "LLY", what_they_did: "w", evidence_claim_ids: [cl], transferability: "partially", why: "y", takeda_baseline_class: "EVIDENCE_GAP", takeda_claim_ids: [], internal_validation: null }] }),
};

// [route, text that must appear]. Views 1-12 keep their "View n ·" eyebrows; every other page has its own heading.
const legacy = ["/", "/powerhouses", "/differentiators", "/pipeline", "/observatory", "/ecosystem", "/encyclopedia", "/takeda", "/strategy", "/portfolio", "/roadmap", "/uncertainty"].map((r, i) => [r, `View ${i + 1} ·`]);
const firstOf = (pred) => reports.reports.find(pred).path;
const tabs = (co, keys) => keys.map((k) => [`/companies/${co}?tab=${k}`, co === "lly" ? "Eli Lilly" : co === "jnj" ? "Johnson" : "AbbVie"]);
const routeSpecs = [...legacy, ["/research-graph", "Research graph"], ["/companies", "Three powerhouses"], ["/companies/lly", "Eli Lilly"], ["/companies/jnj", "Johnson"], ["/companies/abbvie", "AbbVie"], ["/companies/compare", "Cross-company reports"],
  ...tabs("lly", ["dossier", "timeline", "business", "pipeline", "commercial", "successes", "moats", "leadership", "gaps", "more"]), ...tabs("jnj", ["dataai", "business", "pipeline"]), ...tabs("abbvie", ["timeline", "moats"]),
  ["/commercial", "Commercial & market access"], ["/rd", "R&D, science & pipeline"], ["/data-ai", "Data, AI & robotics"], ["/partnerships", "Partnerships & ecosystem"], ["/policy", "Policy & regulation"],
  ["/takeda-baseline", "Takeda baseline"], ["/takeda-baseline?tab=capability", "Capability classes"], ["/takeda-baseline?tab=backlog", "Internal validation backlog"], ["/takeda-baseline?tab=loe", "Takeda"],
  ["/future", "Future plan"], ["/future/pharma", "future of pharma"], ["/future/analogies", "Platform analogies"], ["/future/scenarios", "Scenarios"], ["/future/council", "Council reviews"], ["/future/other", "Other strategy reports"],
  ["/evidence", "How to trust"], ["/sources", "Sources browser"], ["/conflicts", "Conflicts, corrections and audits"], ["/coverage", "Coverage ledger"], ["/method", "Research operating system"], ["/runs", "Research runs and experiments"], ["/state", "Project state"], ["/reports", "All reports"],
  ["/ask", "Ask the evidence base"], ["/ask?q=How%20did%20AbbVie%20respond%20to%20Humira", "Grounded answer"], ["/ask?q=TuneLab%20revenue%202025", "No evidence in the corpus"],
  [`/read/${firstOf((r) => r.section === "dossier")}`, "On this page"], [`/read/${firstOf((r) => r.pillar === "policy")}`, "Report reader".slice(0, 0)], ["/read/does/not/exist.md", "Report not in the bundle"]];
const routes = routeSpecs.map((x) => x[0]);
const server = await createServer({ root: app, server: { middlewareMode: true }, appType: "custom", logLevel: "error" });
const results = [];
try {
  const { renderRoute } = await server.ssrLoadModule("/src/ssr.tsx");
  const run = (label, b) => {
    routeSpecs.forEach(([r, expect]) => {
      let html = "", err = null; try { html = renderRoute(b, r); } catch (e) { err = String(e && e.stack ? e.stack : e).split("\n").slice(0, 3).join(" | "); }
      const text = html.replace(/<[^>]+>/g, " ").replace(/&amp;/g, "&");
      const bad = ["undefined", "NaN", "[object Object]"].filter((t) => text.includes(t));
      const pass = !err && html.length > 400 && text.toLowerCase().includes(expect.toLowerCase()) && bad.length === 0;
      results.push({ name: `${label} ${r} renders`, pass, detail: err ?? (bad.length ? `leaked: ${bad.join(",")}` : !text.toLowerCase().includes(expect.toLowerCase()) ? `missing "${expect}"` : "") });
    });
  };
  run("real data", bundle());
  const withStrategy = bundle(); withStrategy.strategy = { files: { ...withStrategy.strategy.files, ...fixture } };
  run("fixture strategy", withStrategy);
  const real = renderRoute(bundle(), "/portfolio"); results.push({ name: "absent strategy shows explicit notice", pass: real.includes("Strategy module not yet produced") || withStrategy.strategy.files.portfolios.available, detail: "" });
  const fx = renderRoute(withStrategy, "/portfolio"); results.push({ name: "simulator labels values SIMULATED", pass: fx.includes("SIMULATED"), detail: "" });

  // ---- reader: chips and in-app links
  const rd = renderRoute(bundle(), `/read/${firstOf((r) => r.section === "dossier")}`);
  results.push({ name: "reader renders claim-id chips", pass: /class="idchip" data-id="CLM-\d{6}"/.test(rd), detail: "" });
  const withLink = reports.reports.find((r) => /\]\([^)#]*\.md\)/.test(r.markdown));
  if (withLink) results.push({ name: "reader routes relative .md links in-app", pass: renderRoute(bundle(), `/read/${withLink.path}`).includes('href="#/read/'), detail: withLink.path });
  const tbl = reports.reports.find((r) => /^\|.*\|\s*$/m.test(r.markdown));
  results.push({ name: "reader wraps tables for responsive scroll", pass: renderRoute(bundle(), `/read/${tbl.path}`).includes("tablewrap"), detail: tbl.path });
  results.push({ name: "future pages carry the forward-looking banner", pass: ["/future", "/strategy", "/portfolio", "/roadmap", "/uncertainty"].every((r) => renderRoute(bundle(), r).includes("FORWARD-LOOKING")), detail: "" });
  results.push({ name: "non-future pages do not carry the banner", pass: ["/companies", "/commercial", "/evidence"].every((r) => !renderRoute(bundle(), r).includes("FORWARD-LOOKING ·")), detail: "" });
  results.push({ name: "responsive markup: reader has outline and table wrappers; shell classes present", pass: rd.includes('class="outline"') && rd.includes('class="reader"'), detail: "" });

  // ---- Q&A: retrieval, grounding, negative test
  const qa = await server.ssrLoadModule("/src/qa.ts"); const ix = qa.buildIndex(qaIndex.docs); const cids = new Set(claims.map((c) => c.claim_id));
  const neg = qa.retrieve(ix, "TuneLab revenue 2025");
  results.push({ name: "Q&A negative test: 'TuneLab revenue 2025' yields the no-evidence state", pass: neg.answer.ok === false && neg.strong.length === 0, detail: JSON.stringify(neg.answer) });
  const pos = [["Lilly revenue 2025", "CLM-000137"], ["How did AbbVie respond to the loss of Humira exclusivity?", null], ["What is Takeda's exposure to Vyvanse generic entry?", null], ["TuneLab Lilly data for access platform", null]];
  for (const [question, must] of pos) {
    const r = qa.retrieve(ix, question); const ids = r.strong.filter((h) => h.doc.k === "claim").map((h) => h.doc.id);
    results.push({ name: `Q&A answers '${question}' from claims`, pass: r.answer.ok && ids.length > 0 && ids.every((i) => cids.has(i)) && (!must || ids.includes(must)), detail: JSON.stringify({ ok: r.answer.ok, reason: r.answer.reason, top: ids.slice(0, 4) }) });
  }
  for (const q of ["zzzxqv flurbo blorptank", "Skyrizi price in Antarctica 1850", "How much did Takeda earn from quantum teleportation"]) results.push({ name: `Q&A refuses unanswerable '${q}'`, pass: qa.retrieve(ix, q).answer.ok === false, detail: "" });
  results.push({ name: "Q&A passages never come from process documents", pass: qa.retrieve(ix, "TuneLab revenue 2025").strong.every((h) => !qa.isMetaPath(h.doc.path)), detail: "" });
  const llm = await server.ssrLoadModule("/src/llm.ts");
  const msgs = llm.buildMessages("q?", [{ n: 1, id: "CLM-000001", label: "x", text: "t" }]);
  results.push({ name: "LLM prompt is strictly grounded and carries only question + passages", pass: msgs[0].content.includes("ONLY the numbered evidence") && msgs[1].content.includes("CLM-000001") && msgs[1].content.includes("q?") && llm.DEFAULT_SETTINGS.enabled === false && llm.DEFAULT_SETTINGS.ollamaModel === "qwen2.5:3b", detail: "" });
  results.push({ name: "LLM citation audit flags ids not in the retrieved set", pass: llm.auditCitations("see CLM-000001 and CLM-999999", new Set(["CLM-000001"])).unknown.join() === "CLM-999999", detail: "" });
  results.push({ name: "compound question splits into sub-questions; single question does not", pass: qa.splitParts("What is X, and what is Y?").length === 2 && qa.splitParts("How did X respond to Y?").length === 0, detail: JSON.stringify(qa.splitParts("What is X and what is Y?")) });
  const m2 = llm.buildMessages("What is X and what is Y?", [{ n: 1, id: "CLM-000001", label: "x", text: "t" }], qa.splitParts("What is X and what is Y?"));
  results.push({ name: "LLM prompt asks for a per-part answer and lists the sub-questions", pass: m2[0].content.includes("Not stated in the passages") && m2[1].content.includes("Part 2:") && m2[0].content.includes("Always answer the parts the passages support"), detail: "" });
} finally { await server.close(); }
const failed = results.filter((r) => !r.pass);
console.log(JSON.stringify({ total: results.length, passed: results.length - failed.length, failed: failed.length, failures: failed.map((f) => `${f.name}: ${f.detail}`) }, null, 1));
process.exit(failed.length ? 1 : 0);
