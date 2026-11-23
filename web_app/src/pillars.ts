// Information architecture: eleven pillars, each with a sub-navigation. Labels only; all content comes from the generated datasets.
export interface NavItem { path: string; label: string; note?: string }
export interface Pillar { id: string; label: string; path: string; blurb: string; forward?: boolean; items: NavItem[]; paths: string[] }

export const PILLARS: Pillar[] = [
  { id: "overview", label: "Overview", path: "/", blurb: "The story in ten steps, with the evidence behind each step.", items: [{ path: "/", label: "The story spine" }], paths: ["/"] },
  { id: "companies", label: "Companies", path: "/companies", blurb: "Eli Lilly, Johnson & Johnson and AbbVie: dossiers, timelines, financials, pipeline, moats and gaps.",
    items: [{ path: "/companies", label: "Companies hub" }, { path: "/companies/lly", label: "Eli Lilly" }, { path: "/companies/jnj", label: "Johnson & Johnson" }, { path: "/companies/abbvie", label: "AbbVie" },
      { path: "/powerhouses", label: "Compare", note: "View 2" }, { path: "/differentiators", label: "Differentiators", note: "View 3" }, { path: "/companies/compare", label: "Cross-company reports" }],
    paths: ["/companies", "/powerhouses", "/differentiators"] },
  { id: "commercial", label: "Commercial", path: "/commercial", blurb: "Launch execution, pricing and access, patient programmes and what transfers to Takeda.", items: [{ path: "/commercial", label: "Commercial & market access" }], paths: ["/commercial"] },
  { id: "rd", label: "R&D / Pipeline", path: "/rd", blurb: "Approvals, setbacks, late-stage pipeline, scientific platforms and R&D productivity.", items: [{ path: "/rd", label: "R&D, science & pipeline" }, { path: "/pipeline", label: "Pipeline & LOE timelines", note: "View 4" }], paths: ["/rd", "/pipeline"] },
  { id: "dataai", label: "Data · AI · Robotics", path: "/data-ai", blurb: "What is operating, what is announced, and what outcome evidence exists.", items: [{ path: "/data-ai", label: "Data, AI & robotics" }, { path: "/observatory", label: "Observatory", note: "View 5" }], paths: ["/data-ai", "/observatory"] },
  { id: "partnerships", label: "Partnerships", path: "/partnerships", blurb: "Deals, platforms versus assets, and how each company buys innovation.", items: [{ path: "/partnerships", label: "Partnerships & ecosystem" }, { path: "/ecosystem", label: "Ecosystem graph", note: "View 6" }], paths: ["/partnerships", "/ecosystem"] },
  { id: "policy", label: "Policy", path: "/policy", blurb: "Price negotiation exposure, tariffs and pledges, 340B, litigation and lobbying.", items: [{ path: "/policy", label: "Policy & regulation" }], paths: ["/policy"] },
  { id: "takeda", label: "Takeda Baseline", path: "/takeda-baseline", blurb: "What Takeda publicly has today: dossier, capabilities, exclusivity exposure, and what only Takeda can validate.",
    items: [{ path: "/takeda-baseline", label: "Takeda dossier & baseline" }, { path: "/takeda", label: "What Takeda can learn", note: "View 8" }], paths: ["/takeda-baseline", "/takeda"] },
  { id: "future", label: "Future Plan", path: "/future", forward: true, blurb: "Forward-looking: domains of change, analogies, bets, capital, roadmap, scenarios and challenge.",
    items: [{ path: "/future", label: "Future plan hub" }, { path: "/future/pharma", label: "Future of pharma" }, { path: "/future/analogies", label: "Platform analogies" }, { path: "/strategy", label: "Strategic bets", note: "View 9" },
      { path: "/portfolio", label: "Capital allocation", note: "View 10" }, { path: "/roadmap", label: "Roadmap", note: "View 11" }, { path: "/future/scenarios", label: "Scenarios" }, { path: "/future/council", label: "Council & red team" },
      { path: "/uncertainty", label: "Counterarguments & uncertainty", note: "View 12" }, { path: "/future/other", label: "Other strategy reports" }],
    paths: ["/future", "/strategy", "/portfolio", "/roadmap", "/uncertainty"] },
  { id: "evidence", label: "Evidence & Method", path: "/evidence", blurb: "The encyclopedia, sources, conflicts and audit, coverage, method and project state.",
    items: [{ path: "/evidence", label: "Evidence hub" }, { path: "/encyclopedia", label: "Encyclopedia", note: "View 7" }, { path: "/sources", label: "Sources browser" }, { path: "/conflicts", label: "Conflicts & audit" }, { path: "/coverage", label: "Coverage" },
      { path: "/method", label: "Research operating system" }, { path: "/research-graph", label: "Research graph" }, { path: "/runs", label: "Runs & experiments" }, { path: "/state", label: "Project state" }, { path: "/reports", label: "All reports" }],
    paths: ["/evidence", "/encyclopedia", "/sources", "/conflicts", "/coverage", "/method", "/research-graph", "/runs", "/state", "/reports", "/read"] },
  { id: "ask", label: "Ask", path: "/ask", blurb: "Grounded questions answered only from the evidence base.", items: [{ path: "/ask", label: "Ask the evidence" }], paths: ["/ask"] },
];

export function pillarOf(pathname: string): Pillar {
  const p = pathname === "" ? "/" : pathname;
  if (p === "/") return PILLARS[0];
  for (const pl of PILLARS.slice(1)) if (pl.paths.some((x) => p === x || p.startsWith(x + "/"))) return pl;
  return PILLARS[0];
}

export const SECTION_LABELS: Record<string, string> = {
  dossier: "Dossier", timeline: "Timeline", business: "Business & financials", pipeline: "Pipeline", commercial: "Commercial & market access", successes: "Successes & failures", moats: "Competitive advantage",
  leadership: "Leadership", gaps: "Evidence gaps", map: "Folder map", dataai: "Data, AI & robotics", compare: "Cross-company analysis", capability: "Capability baseline", backlog: "Internal validation backlog",
  loe: "Exclusivity exposure", method: "Method", briefs: "Agent briefs", runs: "Research runs", citation_audits: "Citation audits", evaluation_results: "Evaluation results", research_coverage: "Coverage",
  deliverables: "Deliverables", unanswered_questions: "Open questions", state: "Project state", validation: "Validation", framework: "Framework", evidence_notes: "Evidence notes",
};
export const sectionLabel = (s: string) => SECTION_LABELS[s] ?? s.replace(/_/g, " ").replace(/^./, (c) => c.toUpperCase());
