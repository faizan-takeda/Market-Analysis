import { Link, Route, Routes, useLocation } from "react-router-dom";
import type { Bundle } from "./data";
import { Differentiators, Ecosystem, Future, Observatory, PipelineLOE, Powerhouses } from "./views_a";
import { Encyclopedia, ResearchGraph, TakedaLearn, Uncertainty } from "./views_b";
import { Portfolio, Roadmap, StrategyLab } from "./views_c";
import { Reader } from "./reader";
import { Ask } from "./ask";
import { PILLARS, pillarOf } from "./pillars";
import { AllReports, Analogies, CompaniesHub, CompanyRoute, Commercial, ConflictsPage, Council, CoveragePage, DataAi, EvidenceHub, FutureHub, FuturePharma, MethodPage, OtherStrategy, Partnerships, Policy, RnD, RunsPage, Scenarios, SourcesBrowser, StatePage, TakedaBaselinePage } from "./pages";

/** Flat list kept for tests and for anything that needs every view route. */
export const VIEWS: [string, string][] = [
  ["/", "The Future of Medicine"], ["/powerhouses", "Three Powerhouses"], ["/differentiators", "What Makes Them Different"], ["/pipeline", "Pipeline & LOE"],
  ["/observatory", "AI, Data & Robotics"], ["/ecosystem", "Innovation Ecosystem"], ["/encyclopedia", "Research Encyclopedia"], ["/takeda", "What Takeda Can Learn"],
  ["/strategy", "Takeda Strategy Lab"], ["/portfolio", "Portfolio Simulator"], ["/roadmap", "Execution Roadmap"], ["/uncertainty", "Evidence & Uncertainty"],
];

export const FORWARD_NOTE = "FORWARD-LOOKING · SCENARIO — hypotheses, scenarios and recommendations. Not reported facts.";

function Crumbs() {
  const loc = useLocation(); const pl = pillarOf(loc.pathname);
  const here = pl.items.find((i) => i.path === loc.pathname);
  if (pl.id === "overview") return null;
  return <nav className="crumbs" aria-label="Breadcrumb"><Link to="/">Home</Link> › <Link to={pl.path}>{pl.label}</Link>{here && here.path !== pl.path ? <> › <span>{here.label}</span></> : null}</nav>;
}

export function Body({ b, open }: { b: Bundle; open: (id: string) => void }) {
  const loc = useLocation(); const pl = pillarOf(loc.pathname);
  return (
    <main id="main" tabIndex={-1} key={loc.pathname} data-pillar={pl.id}>
      {pl.forward ? <div className="forward" role="note"><b>{FORWARD_NOTE}</b></div> : null}
      <Crumbs />
      <Routes>
        <Route path="/" element={<Future b={b} open={open} />} />
        <Route path="/companies" element={<CompaniesHub b={b} open={open} />} />
        <Route path="/companies/:slug" element={<CompanyRoute b={b} open={open} />} />
        <Route path="/powerhouses" element={<Powerhouses b={b} open={open} />} />
        <Route path="/differentiators" element={<Differentiators b={b} open={open} />} />
        <Route path="/commercial" element={<Commercial b={b} open={open} />} />
        <Route path="/rd" element={<RnD b={b} open={open} />} />
        <Route path="/pipeline" element={<PipelineLOE b={b} open={open} />} />
        <Route path="/data-ai" element={<DataAi b={b} open={open} />} />
        <Route path="/observatory" element={<Observatory b={b} open={open} />} />
        <Route path="/partnerships" element={<Partnerships b={b} open={open} />} />
        <Route path="/ecosystem" element={<Ecosystem b={b} open={open} />} />
        <Route path="/policy" element={<Policy b={b} open={open} />} />
        <Route path="/takeda-baseline" element={<TakedaBaselinePage b={b} open={open} />} />
        <Route path="/takeda" element={<TakedaLearn b={b} open={open} />} />
        <Route path="/future" element={<FutureHub b={b} open={open} />} />
        <Route path="/future/pharma" element={<FuturePharma b={b} open={open} />} />
        <Route path="/future/analogies" element={<Analogies b={b} open={open} />} />
        <Route path="/future/scenarios" element={<Scenarios b={b} open={open} />} />
        <Route path="/future/council" element={<Council b={b} open={open} />} />
        <Route path="/future/other" element={<OtherStrategy b={b} open={open} />} />
        <Route path="/strategy" element={<StrategyLab b={b} open={open} />} />
        <Route path="/portfolio" element={<Portfolio b={b} open={open} />} />
        <Route path="/roadmap" element={<Roadmap b={b} open={open} />} />
        <Route path="/uncertainty" element={<Uncertainty b={b} open={open} />} />
        <Route path="/evidence" element={<EvidenceHub b={b} open={open} />} />
        <Route path="/encyclopedia" element={<Encyclopedia b={b} open={open} />} />
        <Route path="/sources" element={<SourcesBrowser b={b} open={open} />} />
        <Route path="/conflicts" element={<ConflictsPage b={b} open={open} />} />
        <Route path="/coverage" element={<CoveragePage b={b} open={open} />} />
        <Route path="/method" element={<MethodPage b={b} open={open} />} />
        <Route path="/research-graph" element={<ResearchGraph b={b} />} />
        <Route path="/runs" element={<RunsPage b={b} open={open} />} />
        <Route path="/state" element={<StatePage b={b} open={open} />} />
        <Route path="/reports" element={<AllReports b={b} open={open} />} />
        <Route path="/read/*" element={<Reader b={b} open={open} />} />
        <Route path="/ask" element={<Ask b={b} open={open} />} />
        <Route path="*" element={<><h1>Unknown page</h1><p>Choose a section from the navigation, or <Link to="/ask">ask a question</Link>.</p></>} />
      </Routes>
      <footer className="fine">
        Every figure links to a source record (SRC) through a claim record (CLM). <span className="legend-k"><b>FACT</b> ≠ <b>INTERPRETATION</b> ≠ <b>HYPOTHESIS</b> ≠ <b>SCENARIO</b> ≠ <b>RECOMMENDATION</b>.</span>{" "}
        {b.state.sources} sources · {b.state.claims} claims · {b.reports.count} reports · data built {b.state.built_at.slice(0, 10)} · latest claim verification {b.claims.map((c) => c.last_verified).sort().pop()}. The application stores no research of its own; data is generated by <code>scripts/build_app_data.py</code>.
        {" "}<span className="print-only">Sources are listed with URLs in each claim's evidence trail.</span>
      </footer>
    </main>
  );
}
export const PILLAR_LIST = PILLARS;
