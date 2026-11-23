// Pillar pages: companies, commercial, R&D, data/AI, partnerships, policy, Takeda baseline, future plan, evidence & method.
// Content is rendered from reports.json and the generated datasets; this file holds navigation labels and layout only.
import { useMemo, useState } from "react";
import { Link, useParams, useSearchParams } from "react-router-dom";
import { Bundle, COMPANY_COLORS, COMPANY_NAMES, Report, fmtMoney, strat, uniq, yearFrac } from "./data";
import { Absent, CoTag, Ids, MiniBars, Open, Scroll, Swim, SwimItem } from "./components";
import { GroupedReports, MdView, Notice, ReportCard, ReportEmbed, ReportGrid, ReportMeta, readPath } from "./reader";
import { PILLARS, sectionLabel } from "./pillars";

const pretty = (s: string) => s.replace(/_/g, " ");
const SLUG: Record<string, string> = { lly: "LLY", jnj: "JNJ", abbvie: "ABBV" };
const isRef = (r: Report) => /(xbrl|edgar)_annual_facts|ctgov_inventory/.test(r.path);

export function Hero({ eyebrow, title, lede, children }: { eyebrow: string; title: string; lede?: string; children?: React.ReactNode }) {
  return <header className="hero"><div className="eyebrow">{eyebrow}</div><h1>{title}</h1>{lede ? <p className="lede">{lede}</p> : null}{children}</header>;
}
const inPillar = (b: Bundle, id: string) => b.reports.reports.filter((r) => r.pillar === id || r.also.includes(id));
const words = (rs: Report[]) => rs.reduce((a, r) => a + r.word_count, 0);

function Stat({ k, v }: { k: string; v: React.ReactNode }) { return <div><dt>{k}</dt><dd>{v}</dd></div>; }

// ------------------------------------------------------------------ company pages
interface Tab { key: string; label: string; sections: string[] }
const BASE_TABS: Tab[] = [
  { key: "dossier", label: "Dossier", sections: ["dossier"] }, { key: "timeline", label: "Timeline", sections: ["timeline"] },
  { key: "business", label: "Business & Financials", sections: ["business"] }, { key: "pipeline", label: "Pipeline", sections: ["pipeline"] },
  { key: "commercial", label: "Commercial", sections: ["commercial"] }, { key: "successes", label: "Successes & Failures", sections: ["successes"] },
  { key: "moats", label: "Moats", sections: ["moats"] }, { key: "leadership", label: "Leadership", sections: ["leadership"] }, { key: "dataai", label: "Data & Robotics", sections: ["dataai"] },
];
const TAK_TABS: Tab[] = [
  { key: "dossier", label: "Dossier", sections: ["dossier"] }, { key: "capability", label: "Capability baseline", sections: ["capability"] }, { key: "loe", label: "Exclusivity exposure", sections: ["loe"] },
  { key: "dataai", label: "Data & AI baseline", sections: ["dataai"] }, { key: "pipeline", label: "Pipeline", sections: ["pipeline"] }, { key: "business", label: "Financials", sections: ["business"] },
  { key: "timeline", label: "Timeline", sections: ["timeline"] }, { key: "backlog", label: "Validation backlog", sections: ["backlog"] }, { key: "successes", label: "Successes & Failures", sections: ["successes"] },
];
const GAP_TAB: Tab = { key: "gaps", label: "Evidence gaps", sections: ["gaps", "evidence_notes", "map"] };

function FinMultiples({ b, co, open }: { b: Bundle; co: string; open: Open }) {
  const f = b.financials[co]; if (!f) return null;
  const items: [string, string][] = [["revenue", "Revenue"], ["rnd_expense", "R&D expense"], ["net_income", "Net income"], ["capex", "Capital expenditure"], ["op_cash_flow", "Operating cash flow"], ["sga_expense", "SG&A"]];
  const shown = items.filter(([k]) => f.concepts[k] && Object.keys(f.concepts[k]).length);
  if (!shown.length) return <Absent what="No structured financial series for this company." />;
  return (
    <div className="multiples" style={{ gridTemplateColumns: "repeat(auto-fit, minmax(230px, 1fr))" }}>
      {shown.map(([k, label]) => {
        const cells = Object.entries(f.concepts[k]).sort((a, c) => a[0].localeCompare(c[0]));
        const unit = cells[0][1].unit;
        return <div key={k} className="mcell"><div className="mlabel">{label}</div><MiniBars data={cells.map(([fy, v]) => ({ label: `FY${fy}`, value: v.value, claim_id: v.claim_id }))} color={COMPANY_COLORS[co]} fmt={(v) => fmtMoney(v, unit)} open={open} /></div>;
      })}
    </div>
  );
}

function TimelineBlock({ b, co, open }: { b: Bundle; co: string; open: Open }) {
  const tl = b.timelines[co];
  if (!tl || !tl.available) return <Absent what="Timeline file not found for this company." />;
  const items: SwimItem[] = tl.events.map((e) => ({ lane: co, t: yearFrac(e.date) ?? 0, label: `${e.date}: ${e.event}`, claim_ids: e.claim_ids })).filter((i) => i.t > 0);
  return (
    <>
      <div className="panel" style={{ padding: 10 }}><Swim lanes={[{ key: co, label: COMPANY_NAMES[co] ?? co, color: COMPANY_COLORS[co] }]} items={items} open={open} laneH={80} /></div>
      <Scroll><table><thead><tr><th>Date</th><th>Event</th><th>Evidence</th></tr></thead><tbody>
        {tl.events.map((e, i) => <tr key={i}><td className="num" style={{ whiteSpace: "nowrap" }}>{e.date}</td><td>{e.event}</td><td><Ids ids={e.claim_ids} open={open} /></td></tr>)}
      </tbody></table></Scroll>
    </>
  );
}

function RegTable({ b, co, kind, open }: { b: Bundle; co: string; kind: "approvals" | "setbacks"; open: Open }) {
  if (kind === "approvals") {
    if (!b.approvals.available) return <Absent what={b.approvals.reason ?? "Approvals table not yet produced."} />;
    const rows = b.approvals.rows.filter((r) => r.company === co);
    return <><h3>Regulatory approvals recorded</h3>{rows.length ? <Scroll><table><thead><tr><th>Date</th><th>Product</th><th>Type</th><th>Detail</th><th>Evidence</th></tr></thead><tbody>{rows.map((r, i) => <tr key={i}><td className="num">{r.date}</td><td>{r.product}</td><td>{pretty(r.kind)}</td><td>{r.detail}</td><td><Ids ids={r.claim_ids} open={open} /></td></tr>)}</tbody></table></Scroll> : <p className="meta">No approvals for this company in the table.</p>}</>;
  }
  if (!b.setbacks.available) return <Absent what={b.setbacks.reason ?? "Setbacks table not yet produced."} />;
  const rows = b.setbacks.rows.filter((r) => r.company === co);
  return <><h3>Setbacks, refusals and withdrawals recorded</h3>{rows.length ? <Scroll><table><thead><tr><th>When</th><th>Asset</th><th>What happened</th><th>Evidence</th></tr></thead><tbody>{rows.map((r, i) => <tr key={i}><td className="num">{r.when}</td><td>{r.asset}</td><td>{r.what}</td><td><Ids ids={r.claim_ids} open={open} /></td></tr>)}</tbody></table></Scroll> : <p className="meta">No setbacks for this company in the table.</p>}</>;
}

function MoatList({ b, co, open }: { b: Bundle; co: string; open: Open }) {
  const cards = (b.cards.cards ?? []).filter((c) => c.kind === "moat" && c.companies.includes(co as any));
  if (!cards.length) return null;
  return <><h3>Moat entries from the analysis</h3>{cards.map((c) => <div key={c.id} className="lrow"><b>{c.title}</b>{c.gap ? <span className="tag warnb">gap</span> : null}<p className="clamp">{c.fields[0]?.text}</p><Ids ids={c.claim_ids} open={open} /></div>)}</>;
}

function Capabilities({ b, open }: { b: Bundle; open: Open }) {
  if (!b.takeda.available) return <Absent what={b.takeda.reason ?? "Takeda baseline not found."} />;
  return <><h3>Capability classes</h3><Scroll><table><thead><tr><th>Capability</th><th>Class</th><th>Evidence</th><th>Needs internal validation</th></tr></thead><tbody>
    {b.takeda.capabilities.map((c, i) => <tr key={i}><td>{c.area}</td><td><span className="tag">{pretty(c.class)}</span></td><td><Ids ids={c.claim_ids} open={open} /></td><td>{c.validation}</td></tr>)}
  </tbody></table></Scroll><p><Link to="/takeda">Open the interactive capability view (View 8) →</Link></p></>;
}
function Backlog({ b, open }: { b: Bundle; open: Open }) {
  if (!b.takeda.available) return null;
  return <><h3>Internal validation backlog (only Takeda can answer these)</h3><Scroll><table><thead><tr><th>ID</th><th>Question</th><th>Why it matters</th><th>Evidence</th></tr></thead><tbody>
    {b.takeda.backlog.map((x) => <tr key={x.id}><td className="src">{x.id}</td><td>{x.question}</td><td>{x.why}</td><td><Ids ids={x.claim_ids} open={open} /></td></tr>)}
  </tbody></table></Scroll></>;
}

function TabBody({ b, open, co, tab, rs }: { b: Bundle; open: Open; co: string; tab: Tab; rs: Report[] }) {
  const embeds = rs.filter((r) => !isRef(r)); const refs = rs.filter(isRef);
  return (
    <div className="tabbody">
      {tab.key === "timeline" ? <TimelineBlock b={b} co={co} open={open} /> : null}
      {tab.key === "business" ? <><h3>Financial series from the filings</h3><FinMultiples b={b} co={co} open={open} /></> : null}
      {tab.key === "capability" ? <Capabilities b={b} open={open} /> : null}
      {embeds.map((r, i) => <ReportEmbed key={r.path} b={b} r={r} open={open} startOpen={i === 0 && tab.key !== "timeline"} />)}
      {refs.length ? <><h3>Reference tables</h3><ReportGrid reports={refs} /></> : null}
      {tab.key === "pipeline" ? <RegTable b={b} co={co} kind="approvals" open={open} /> : null}
      {tab.key === "successes" ? <RegTable b={b} co={co} kind="setbacks" open={open} /> : null}
      {tab.key === "moats" ? <MoatList b={b} co={co} open={open} /> : null}
      {tab.key === "backlog" ? <Backlog b={b} open={open} /> : null}
    </div>
  );
}

export function CompanyPage({ b, open, code }: { b: Bundle; open: Open; code: string }) {
  const [sp, setSp] = useSearchParams();
  const tak = code === "TAK"; const color = COMPANY_COLORS[code];
  const mine = b.reports.reports.filter((r) => r.company === code);
  const tabs0 = (tak ? TAK_TABS : BASE_TABS);
  const covered = new Set([...tabs0.flatMap((t) => t.sections), ...GAP_TAB.sections]);
  const tabs: Tab[] = [...tabs0, GAP_TAB, { key: "more", label: "Other reports", sections: uniq(mine.filter((r) => !covered.has(r.section)).map((r) => r.section)) }];
  const hasExtra = (t: Tab) => (t.key === "timeline" && b.timelines[code]?.available) || (t.key === "business" && !!b.financials[code]) || (t.key === "capability" && b.takeda.available) || (t.key === "backlog" && b.takeda.available)
    || (t.key === "pipeline" && b.approvals.available) || (t.key === "successes" && b.setbacks.available) || (t.key === "moats" && (b.cards.cards ?? []).some((c) => c.kind === "moat" && c.companies.includes(code as any)));
  const visible = tabs.filter((t) => mine.some((r) => t.sections.includes(r.section)) || hasExtra(t));
  const cur = visible.find((t) => t.key === sp.get("tab")) ?? visible[0];
  const rs = cur ? mine.filter((r) => cur.sections.includes(r.section)) : [];
  const fin = b.financials[code]; const lastFy = fin ? Object.keys(fin.concepts.revenue ?? {}).sort().pop() : undefined;
  const rev = lastFy ? fin.concepts.revenue[lastFy] : undefined; const rnd = lastFy ? fin.concepts.rnd_expense?.[lastFy] : undefined;
  const nClaims = b.claims.filter((c) => c.companies.includes(code as any)).length;
  return (
    <>
      <Hero eyebrow={tak ? "Takeda baseline" : "Companies"} title={COMPANY_NAMES[code] ?? code} lede={tak ? "What Takeda's public record shows today. Everything the public record cannot show is listed as an internal validation question." : "Dossier, timeline, financials, pipeline, commercial model, successes and failures, moats, leadership and the gaps the research could not close."}>
        <div className="coband" style={{ background: color }} />
        <dl className="kpis">
          {rev ? <Stat k={`revenue FY${lastFy}`} v={<button className="linkbtn" onClick={() => open(rev.claim_id)}>{fmtMoney(rev.value, rev.unit)}</button>} /> : null}
          {rnd ? <Stat k={`R&D expense FY${lastFy}`} v={<button className="linkbtn" onClick={() => open(rnd.claim_id)}>{fmtMoney(rnd.value, rnd.unit)}</button>} /> : null}
          <Stat k="claims in registry" v={nClaims} /><Stat k="dated timeline events" v={b.timelines[code]?.events.length ?? 0} /><Stat k="reports" v={mine.length} /><Stat k="words in reports" v={words(mine).toLocaleString()} />
        </dl>
      </Hero>
      <div className="tabs" role="tablist" aria-label="Company sections">
        {visible.map((t) => <button key={t.key} role="tab" aria-selected={cur?.key === t.key} className={`tab ${cur?.key === t.key ? "on" : ""}`} onClick={() => setSp({ tab: t.key })}>{t.label}</button>)}
      </div>
      {cur ? <TabBody b={b} open={open} co={code} tab={cur} rs={rs} /> : <Notice title="Not yet produced.">No reports for this company were found in the bundle.</Notice>}
    </>
  );
}

export function CompanyRoute({ b, open }: { b: Bundle; open: Open }) {
  const { slug } = useParams();
  if (slug === "compare") return <CrossCompany b={b} open={open} />;
  const code = SLUG[slug ?? ""];
  if (!code) return <><h1>Unknown company</h1><p><Link to="/companies">Back to the companies hub</Link></p></>;
  return <CompanyPage b={b} open={open} code={code} />;
}

function CrossCompany({ b }: { b: Bundle; open: Open }) {
  const rs = b.reports.reports.filter((r) => r.section === "compare");
  return <><Hero eyebrow="Companies · cross-company analysis" title="Cross-company reports" lede="Side-by-side analyses written across Lilly, J&J, AbbVie and Takeda. Where a comparison file does not exist yet, it is not listed." />
    <GroupedReports reports={rs} empty={<Notice title="Not yet produced.">No cross-company reports found.</Notice>} /></>;
}

export function CompaniesHub({ b }: { b: Bundle; open: Open }) {
  return (
    <>
      <Hero eyebrow="Companies" title="Three powerhouses, studied one by one" lede="Each company page opens on its dossier and carries its own timeline, financial series, pipeline, commercial model, successes and failures, moats, leadership and evidence gaps." />
      <div className="grid g3">
        {Object.entries(SLUG).map(([slug, code]) => {
          const mine = b.reports.reports.filter((r) => r.company === code); const fin = b.financials[code]; const fy = Object.keys(fin?.concepts.revenue ?? {}).sort().pop(); const rev = fy ? fin.concepts.revenue[fy] : null;
          return (
            <Link key={slug} to={`/companies/${slug}`} className="cocard" style={{ borderTopColor: COMPANY_COLORS[code] }}>
              <span className="cocard-name" style={{ color: COMPANY_COLORS[code] }}>{COMPANY_NAMES[code]}</span>
              {rev ? <span className="cocard-fig">{fmtMoney(rev.value, rev.unit)}<small>revenue FY{fy}</small></span> : null}
              <span className="meta">{mine.length} reports · {words(mine).toLocaleString()} words · {b.claims.filter((c) => c.companies.includes(code as any)).length} claims</span>
            </Link>
          );
        })}
      </div>
      <h2 style={{ marginTop: 32 }}>Compare and differentiate</h2>
      <div className="grid g3">
        <Link className="rcard" to="/powerhouses"><b>Compare the three</b><span className="rcard-ex">Financial series, mix and growth side by side, each point linked to its claim.</span></Link>
        <Link className="rcard" to="/differentiators"><b>What makes them different</b><span className="rcard-ex">Mechanism cards and moats, with the evidence for each.</span></Link>
        <Link className="rcard" to="/companies/compare"><b>Cross-company reports</b><span className="rcard-ex">Written comparisons across the four companies.</span></Link>
      </div>
    </>
  );
}

export function TakedaBaselinePage({ b, open }: { b: Bundle; open: Open }) { return <CompanyPage b={b} open={open} code="TAK" />; }

// ------------------------------------------------------------------ thematic pillars
function ProductConcentration({ b, open }: { b: Bundle; open: Open }) {
  const rows: { co: string; product: string; fy: string; share: number; claim: string }[] = [];
  for (const s of b.products.series) {
    const fy = Object.keys(s.values).filter((k) => s.values[k] != null).sort().pop(); const rev = fy ? b.financials[s.company]?.concepts.revenue?.[fy] : undefined;
    if (!fy || !rev || rev.unit !== s.unit || !rev.value) continue;
    rows.push({ co: s.company, product: s.product, fy, share: ((s.values[fy] as number) / rev.value) * 100, claim: s.claims[0] });
  }
  if (!rows.length) return <Absent what="No product series could be matched to reported revenue." />;
  rows.sort((a, c) => c.share - a.share);
  return <div className="hbars">{rows.slice(0, 14).map((r) => <div key={r.co + r.product} className="hbar"><span><CoTag co={r.co} />{r.product}</span><div className="bar"><i style={{ width: `${Math.min(100, r.share)}%`, background: COMPANY_COLORS[r.co] }} /></div><b><button className="linkbtn" onClick={() => open(r.claim)}>{r.share.toFixed(1)}%</button></b></div>)}</div>;
}

function Landing({ b, open, id, eyebrow, title, lede, extra, links }: { b: Bundle; open: Open; id: string; eyebrow: string; title: string; lede: string; extra?: React.ReactNode; links?: [string, string, string][] }) {
  const rs = inPillar(b, id);
  return (
    <>
      <Hero eyebrow={eyebrow} title={title} lede={lede}><p className="meta">{rs.length} reports · {words(rs).toLocaleString()} words in this pillar.</p></Hero>
      {links?.length ? <div className="grid g3">{links.map(([to, t, d]) => <Link key={to} className="rcard" to={to}><b>{t}</b><span className="rcard-ex">{d}</span></Link>)}</div> : null}
      {extra}
      <h2 style={{ marginTop: 28 }}>Reports</h2>
      <GroupedReports reports={rs} empty={<Notice title="Not yet produced.">No reports for this pillar were found in the bundle.</Notice>} />
    </>
  );
}

export function Commercial({ b, open }: { b: Bundle; open: Open }) {
  return <Landing b={b} open={open} id="commercial" eyebrow="Commercial & market access" title="How the leaders launch, price, win access and serve patients" lede="Launch execution, pricing and payer dynamics, patient programmes and care delivery, the cross-company commercial comparison, and what transfers to Takeda."
    extra={<><h2>Dependence on single products</h2><p className="meta">Each bar is a product's latest-year revenue as a share of that company's reported revenue, computed from the product series and the filings. Click a figure to open its claim.</p><ProductConcentration b={b} open={open} /></>}
    links={[["/pipeline", "Pipeline & exclusivity timelines", "Product series and loss-of-exclusivity events (View 4)."], ["/companies/compare", "Cross-company reports", "Commercial comparison and related analyses."]]} />;
}

function Regulatory({ b, open }: { b: Bundle; open: Open }) {
  const [co, setCo] = useState("all");
  const ap = b.approvals.rows.filter((r) => co === "all" || r.company === co); const sb = b.setbacks.rows.filter((r) => co === "all" || r.company === co);
  return (
    <>
      <div className="chips" role="group" aria-label="company filter">{["all", "LLY", "JNJ", "ABBV", "TAK"].map((c) => <button key={c} className={`chip ${co === c ? "on" : ""}`} aria-pressed={co === c} onClick={() => setCo(c)}>{c === "all" ? "all companies" : COMPANY_NAMES[c]}</button>)}</div>
      <h3>Approvals recorded</h3>
      {b.approvals.available ? <Scroll><table><thead><tr><th>Date</th><th>Company</th><th>Product</th><th>Type</th><th>Detail</th><th>Evidence</th></tr></thead><tbody>{ap.map((r, i) => <tr key={i}><td className="num">{r.date}</td><td>{r.company ? <CoTag co={r.company} /> : null}</td><td>{r.product}</td><td>{pretty(r.kind)}</td><td>{r.detail}</td><td><Ids ids={r.claim_ids} open={open} /></td></tr>)}</tbody></table></Scroll> : <Absent what={b.approvals.reason ?? ""} />}
      <h3>Setbacks, refusals and withdrawals</h3>
      {b.setbacks.available ? <Scroll><table><thead><tr><th>When</th><th>Company</th><th>Asset</th><th>What happened</th><th>Evidence</th></tr></thead><tbody>{sb.map((r, i) => <tr key={i}><td className="num">{r.when}</td><td>{r.company ? <CoTag co={r.company} /> : null}</td><td>{r.asset}</td><td>{r.what}</td><td><Ids ids={r.claim_ids} open={open} /></td></tr>)}</tbody></table></Scroll> : <Absent what={b.setbacks.reason ?? ""} />}
    </>
  );
}
export function RnD({ b, open }: { b: Bundle; open: Open }) {
  return <Landing b={b} open={open} id="rd" eyebrow="R&D, science & pipeline" title="What was approved, what failed, and what is in late-stage development" lede="Approvals and supplemental approvals, regulatory setbacks, the late-stage snapshot, scientific platforms and an assessment of pipeline quality."
    extra={<Regulatory b={b} open={open} />} links={[["/pipeline", "Pipeline & exclusivity timelines", "Interactive timelines of approvals, setbacks and exclusivity events (View 4)."]]} />;
}

function MaturityBars({ b, open }: { b: Bundle; open: Open }) {
  const order = ["CONCEPT", "PROTOTYPE", "PILOT", "OPERATIONAL", "SCALED", "DEMONSTRATED_OUTCOME"]; const n = Math.max(1, b.maturity.length);
  return <div className="hbars">{order.map((l) => { const k = b.maturity.filter((m) => m.maturity === l); return <div key={l} className="hbar"><span>{pretty(l).toLowerCase()}</span><div className="bar"><i style={{ width: `${(k.length / n) * 100}%` }} /></div><b>{k.length}</b></div>; })}<p className="meta">Maturity is assigned from the evidence, not the announcement. <button className="linkbtn" onClick={() => open(b.maturity[0]?.claim_id ?? "")}>See an example claim</button></p></div>;
}
export function DataAi({ b, open }: { b: Bundle; open: Open }) {
  return <Landing b={b} open={open} id="dataai" eyebrow="Data, AI & robotics" title="Operating, announced, or demonstrated: what the evidence supports" lede="The landscape, fourteen-plus mechanism cards, the maturity matrix and a reality check on autonomous laboratories."
    extra={<><h2>Maturity of recorded initiatives</h2><MaturityBars b={b} open={open} /></>} links={[["/observatory", "Observatory", "Maturity landscape and outcome evidence by company and domain (View 5)."], ["/differentiators", "Mechanism cards", "How each capability was built and whether it created a moat."]]} />;
}
export function Partnerships({ b, open }: { b: Bundle; open: Open }) {
  const inv = b.deals.inventory; const byCo = (c: string) => inv.filter((d) => d.company === c).length;
  return <Landing b={b} open={open} id="partnerships" eyebrow="Partnerships & ecosystem" title="How each company buys, licenses and builds innovation" lede="The deal inventory, scorecard of outcomes, external-innovation machinery and the split between platform bets and asset purchases."
    extra={<>{b.deals.available ? <dl className="kpis">{["LLY", "JNJ", "ABBV", "TAK"].map((c) => <Stat key={c} k={`${COMPANY_NAMES[c]} deals recorded`} v={byCo(c)} />)}</dl> : <Absent what={b.deals.reason ?? ""} />}</>} links={[["/ecosystem", "Ecosystem graph", "Interactive deal graph with evidence on each link (View 6)."]]} />;
}
export function Policy({ b, open }: { b: Bundle; open: Open }) {
  const pc = b.claims.filter((c) => (c.domains ?? []).includes("policy_regulation"));
  return <Landing b={b} open={open} id="policy" eyebrow="Policy & regulation" title="Price negotiation, tariffs, pledges, litigation and lobbying" lede="Exposure to government price setting, manufacturing pledges tied to tariffs, 340B and litigation with a policy dimension."
    extra={<p className="meta">{pc.length} claims in the registry carry the policy and regulation domain. Open the <Link to="/encyclopedia">encyclopedia</Link> to filter them.</p>} />;
}

// ------------------------------------------------------------------ future plan
interface FlowStep { title: string; text: string; folders: string[]; data: string[]; to: [string, string][] }
const FLOW: FlowStep[] = [
  { title: "Module 1 · Seven domains of change", text: "Where the industry is changing, domain by domain, and which platform analogies from other industries help or mislead. Each domain separates what the evidence shows from what is projected.", folders: ["future_of_pharma", "platform_moats"], data: [], to: [["/future/pharma", "Future of pharma"], ["/future/analogies", "Platform analogies"]] },
  { title: "Module 2 · Strategic bets", text: "Candidate platform bets for Takeda, each with a decision (build, partner, invest, defer, reject), prerequisites, evidence IDs and assumptions. Framing of the central question, investment theses, pipeline resilience and ecosystem rules sit here.", folders: ["takeda_future_2030_2040", "investment_theses", "pipeline_resilience", "ecosystem_partnerships"], data: ["strategy_bets", "assumptions"], to: [["/strategy", "Bets explorer (View 9)"], ["/future/other", "Strategy reports"]] },
  { title: "Capital allocation", text: "Three assumption-based portfolios, per-bet probabilities and stage gates with capital at risk. Every number is simulated from stated assumptions; Takeda's real budget is unknown.", folders: ["financial_cases"], data: ["portfolios", "stage_gates"], to: [["/portfolio", "Portfolio simulator (View 10)"]] },
  { title: "Scenarios", text: "Five alternative futures and how robust each bet is under each. A bet that only works in one scenario is labelled fragile.", folders: ["scenarios"], data: ["scenarios"], to: [["/future/scenarios", "Scenario definitions"], ["/uncertainty", "Robustness matrix (View 12)"]] },
  { title: "Roadmap", text: "Milestones and dependencies across the full horizon to 2040, with gates that stop or expand each bet.", folders: ["strategic_roadmap"], data: ["roadmap"], to: [["/roadmap", "Roadmap Gantt (View 11)"]] },
  { title: "Council and red team", text: "Independent councils challenge every bet. Disagreements are recorded, not smoothed over.", folders: ["critical_challenges"], data: ["council_reviews"], to: [["/future/council", "Council verdicts"]] },
  { title: "Counterarguments", text: "Unsupported assumptions, unresolved questions, conflicting sources and public-knowledge gaps that could make the plan wrong.", folders: [], data: ["counterarguments"], to: [["/uncertainty", "Why we could be wrong (View 12)"]] },
];
const DATA_LABEL: Record<string, string> = { strategy_bets: "bets", assumptions: "assumptions", portfolios: "portfolios", stage_gates: "gates", scenarios: "scenarios", roadmap: "milestones", council_reviews: "reviews", counterarguments: "counterarguments" };
const DATA_KEY: Record<string, string> = { strategy_bets: "bets", assumptions: "assumptions", portfolios: "portfolios", stage_gates: "gates", scenarios: "scenarios", roadmap: "milestones", council_reviews: "reviews", counterarguments: "items" };

export function FutureHub({ b }: { b: Bundle; open: Open }) {
  const fr = b.reports.reports.filter((r) => r.pillar === "future");
  const dl = b.reports.reports.filter((r) => r.section === "deliverables");
  return (
    <>
      <Hero eyebrow="Future plan" title="From evidence to options: what Takeda could build next" lede="Everything in this pillar is forward-looking: hypotheses, scenarios and recommendations built on the evidence base. Read the modules in order; each one builds on the one before." />
      {dl.length ? <><h2>Start with the deliverables</h2><ReportGrid reports={dl.filter((r) => r.path !== "deliverables/OPEN_APPLICATION.md")} /></> : null}
      <h2>How the plan is built</h2>
      <ol className="flow">{FLOW.map((st) => {
        const rs = fr.filter((r) => st.folders.includes(r.section)); const words = rs.reduce((a, r) => a + r.word_count, 0);
        const dataCounts = st.data.map((k) => { const f = b.state.strategy_files[k]; const d = strat<any>(b, k); const n = d && Array.isArray(d[DATA_KEY[k]]) ? d[DATA_KEY[k]].length : 0; return { k, on: !!f && n > 0, n }; });
        const ready = rs.length > 0 || dataCounts.some((d) => d.on);
        return <li key={st.title} className={ready ? "ready" : "pending"}>
          <div><h3>{st.title}</h3><p>{st.text}</p></div>
          <div className="flow-meta">{rs.length ? <div><b>{rs.length}</b> report{rs.length > 1 ? "s" : ""} · <b>{words.toLocaleString()}</b> words</div> : st.folders.length ? <div>no report yet</div> : null}
            {dataCounts.map((d) => <div key={d.k}>{d.on ? <><b>{d.n}</b> {DATA_LABEL[d.k]}</> : `${DATA_LABEL[d.k]}: not yet produced`}</div>)}</div>
          <div className="flow-links">{st.to.map(([to, label]) => <Link key={to + label} to={to}>{label} →</Link>)}{rs.map((r) => <Link key={r.path} to={readPath(r.path)}>{r.title}</Link>)}</div>
        </li>;
      })}</ol>
      <p className="meta">All reports in this pillar: {fr.length} files, {fr.reduce((a, r) => a + r.word_count, 0).toLocaleString()} words. Every number in the simulator and roadmap is labelled SIMULATED or ASSUMPTION; every evidence ID opens its source.</p>
    </>
  );
}

function FolderPage({ b, open, folders, eyebrow, title, lede, children }: { b: Bundle; open: Open; folders: string[]; eyebrow: string; title: string; lede: string; children?: React.ReactNode }) {
  const rs = b.reports.reports.filter((r) => r.pillar === "future" && folders.includes(r.section));
  return (
    <>
      <Hero eyebrow={eyebrow} title={title} lede={lede} />
      {folders.filter((f) => !rs.some((r) => r.section === f)).map((f) => <Notice key={f} title="Not yet produced.">Expected: <code>strategy/{f}/*.md</code></Notice>)}
      {rs.map((r, i) => <ReportEmbed key={r.path} b={b} r={r} open={open} startOpen={i === 0} />)}
      {children}
    </>
  );
}
export const FuturePharma = (p: { b: Bundle; open: Open }) => <FolderPage {...p} folders={["future_of_pharma"]} eyebrow="Future plan · forward-looking" title="The future of pharma, domain by domain" lede="Seven areas where the industry is changing, each separating what the evidence shows from what is projected." />;
export const Analogies = (p: { b: Bundle; open: Open }) => <FolderPage {...p} folders={["platform_moats"]} eyebrow="Future plan · analogies" title="Platform analogies: what other industries teach, and where they break" lede="Analogies are hypotheses. Each states the mechanism, then where the comparison fails for a pharmaceutical company." />;
export function Scenarios({ b, open }: { b: Bundle; open: Open }) {
  const sc = strat<any>(b, "scenarios");
  return <FolderPage b={b} open={open} folders={["scenarios"]} eyebrow="Future plan · scenarios" title="Scenarios" lede="Alternative futures and a combined downside, against which each bet is tested.">
    {sc?.scenarios?.length ? <><h3>Scenario definitions</h3>{sc.scenarios.map((s: any) => <div key={s.id} className="lrow"><b>{s.name}</b> <span className="tag SCENARIO">scenario</span><p>{s.description}</p><Ids ids={s.claim_ids ?? []} open={open} /></div>)}</> : <Absent kind="strategy" what="Scenario definitions will appear here." file="strategy/data/scenarios.json" />}
  </FolderPage>;
}
const COUNCILS = ["scientific", "technology", "commercial", "capital", "regulatory_ethics", "red_team", "takeda_execution"];
const VCLS: Record<string, string> = { support: "sup", conditional: "cond", oppose: "opp" };
export function Council({ b, open }: { b: Bundle; open: Open }) {
  const cr = strat<any>(b, "council_reviews"); const reviews: any[] = Array.isArray(cr?.reviews) ? cr.reviews : [];
  const bets = uniq(reviews.map((r) => r.bet_id)).sort(); const councils = [...COUNCILS.filter((c) => reviews.some((r) => r.council === c)), ...uniq(reviews.map((r) => r.council)).filter((c) => !COUNCILS.includes(c))];
  const [sel, setSel] = useState<string | null>(null); const chosen = reviews.filter((r) => r.bet_id === (sel ?? bets[0]));
  return <FolderPage b={b} open={open} folders={["critical_challenges"]} eyebrow="Future plan · challenge" title="Council reviews and red team" lede="Each bet is challenged by independent councils; disagreements are recorded, not smoothed over.">
    {reviews.length ? <>
      <h3>Verdict matrix</h3>
      <Scroll><table className="vmatrix"><thead><tr><th>Bet</th>{councils.map((c) => <th key={c}>{pretty(c)}</th>)}</tr></thead><tbody>
        {bets.map((id) => <tr key={id} className={(sel ?? bets[0]) === id ? "hl" : ""}><td><button className="linkbtn" onClick={() => setSel(id)}><b>{id}</b></button></td>{councils.map((c) => { const r = reviews.find((x) => x.bet_id === id && x.council === c); return <td key={c}>{r ? <span className={`cell ${VCLS[r.verdict] ?? ""}`}>{r.verdict}</span> : "—"}</td>; })}</tr>)}</tbody></table></Scroll>
      <h3 style={{ marginTop: 18 }}>{sel ?? bets[0]}: rationale and unresolved points</h3>
      <Scroll><table><thead><tr><th>Council</th><th>Verdict</th><th>Rationale</th><th>Unresolved</th><th>Evidence</th></tr></thead><tbody>{chosen.map((r, i) => <tr key={i}><td>{pretty(r.council ?? "")}</td><td><span className={`cell ${VCLS[r.verdict] ?? ""}`}>{r.verdict}</span></td><td>{r.rationale}</td><td>{r.unresolved}</td><td><Ids ids={r.claim_ids ?? []} open={open} /></td></tr>)}</tbody></table></Scroll>
      {(cr.disagreements ?? []).length ? <><h3>Recorded disagreements</h3>{cr.disagreements.map((d: any, i: number) => <p key={i} className="contrary"><b>{d.bet_id}:</b> {d.text}</p>)}</> : null}
    </> : <Absent kind="strategy" what="Council verdicts per bet, with a council by bet matrix, appear here when the council has reviewed the bets." file="strategy/data/council_reviews.json" />}
  </FolderPage>;
}
export const OtherStrategy = (p: { b: Bundle; open: Open }) => <FolderPage {...p} folders={["takeda_future_2030_2040", "investment_theses", "pipeline_resilience", "ecosystem_partnerships", "financial_cases", "strategic_roadmap", "framework"]} eyebrow="Future plan · reports" title="Other strategy reports" lede="Framing of the central question, investment theses, pipeline resilience, ecosystem rules, financial cases and the roadmap narrative." />;

// ------------------------------------------------------------------ evidence & method
export function EvidenceHub({ b }: { b: Bundle; open: Open }) {
  const st = b.state; const verified = b.claims.map((c) => c.last_verified).sort().pop();
  const bars = (o: Record<string, number>) => { const m = Math.max(1, ...Object.values(o)); return <div className="hbars">{Object.entries(o).sort((a, c) => c[1] - a[1]).map(([k, v]) => <div key={k} className="hbar"><span>{pretty(k)}</span><div className="bar"><i style={{ width: `${(v / m) * 100}%` }} /></div><b>{v}</b></div>)}</div>; };
  return (
    <>
      <Hero eyebrow="Evidence & method" title="How to trust what you read here" lede="Every figure traces through a claim record to a source record and an original locator. Facts, interpretations, hypotheses, scenarios and recommendations are never mixed." />
      <dl className="kpis">
        <Stat k="sources inspected" v={st.sources} /><Stat k="claims" v={st.claims} /><Stat k="reports in the reader" v={st.datasets.reports} /><Stat k="recorded conflicts and corrections" v={st.datasets.conflicts} />
        <Stat k="claims with contrary evidence" v={st.claims_contrary} /><Stat k="claims resting on one interested source" v={st.claims_single_source} />
      </dl>
      <p className="meta">Latest claim verification date in the registry: {verified}. Data built {st.built_at.slice(0, 16).replace("T", " ")} UTC.</p>
      <div className="grid g3">
        <div className="panel"><h3>Claims by status</h3>{bars(st.claims_by_status)}</div>
        <div className="panel"><h3>Claims by kind</h3>{bars(st.claims_by_kind)}</div>
        <div className="panel"><h3>Sources by credibility tier</h3>{bars(st.sources_by_tier)}</div>
      </div>
      {b.reports.reports.some((r) => r.section === "deliverables") ? <><h2 style={{ marginTop: 28 }}>Deliverables</h2><ReportGrid reports={b.reports.reports.filter((r) => r.section === "deliverables")} /></> : null}
      <h2 style={{ marginTop: 28 }}>Where to go</h2>
      <div className="grid g3">{PILLARS.find((p) => p.id === "evidence")!.items.filter((i) => i.path !== "/evidence").map((i) => <Link key={i.path} to={i.path} className="rcard"><b>{i.label}</b>{i.note ? <span className="meta">{i.note}</span> : null}</Link>)}</div>
    </>
  );
}

export function SourcesBrowser({ b, open }: { b: Bundle; open: Open }) {
  const [q, setQ] = useState(""); const [co, setCo] = useState("all"); const [tier, setTier] = useState("all"); const [type, setType] = useState("all"); const [lim, setLim] = useState(80);
  const rows = useMemo(() => { const t = q.toLowerCase(); return b.sources.filter((s) => (co === "all" || s.company === co) && (tier === "all" || s.credibility_tier === tier) && (type === "all" || s.source_type === type) && (!t || (s.title + " " + s.publisher + " " + s.source_id).toLowerCase().includes(t))); }, [b, q, co, tier, type]);
  const sel = (label: string, v: string, set: (x: string) => void, opts: string[], fmt?: (x: string) => string) => <label className="sel">{label}<select value={v} onChange={(e) => { set(e.target.value); setLim(80); }}><option value="all">all</option>{opts.map((o) => <option key={o} value={o}>{fmt ? fmt(o) : pretty(o)}</option>)}</select></label>;
  return (
    <>
      <Hero eyebrow="Evidence & method" title="Sources browser" lede="Every inspected source with its credibility tier, access status and the number of claims resting on it. Click an ID for the evidence trail." />
      <div className="toolbar"><input placeholder="filter by title, publisher or SRC id" value={q} onChange={(e) => { setQ(e.target.value); setLim(80); }} aria-label="filter sources" style={{ flex: "1 1 260px" }} /></div>
      <div className="toolbar filters">{sel("company", co, setCo, uniq(b.sources.map((s) => s.company)).sort(), (x) => COMPANY_NAMES[x] ?? x)}{sel("credibility tier", tier, setTier, uniq(b.sources.map((s) => s.credibility_tier)).sort())}{sel("type", type, setType, uniq(b.sources.map((s) => s.source_type)).sort())}</div>
      <p className="meta">{rows.length} of {b.sources.length} sources</p>
      <Scroll><table><thead><tr><th>ID</th><th>Title</th><th>Publisher</th><th>Tier</th><th>Type</th><th>Published</th><th>Access</th></tr></thead><tbody>
        {rows.slice(0, lim).map((s) => <tr key={s.source_id}><td><Ids ids={[s.source_id]} open={open} /></td><td><a href={s.canonical_url} target="_blank" rel="noreferrer">{s.title}</a></td><td>{s.publisher}</td><td>{pretty(s.credibility_tier)}</td><td>{pretty(s.source_type)}</td><td className="num">{s.published_at ?? ""}</td><td>{s.access_status}</td></tr>)}
      </tbody></table></Scroll>
      {rows.length > lim ? <p><button className="chip" onClick={() => setLim(lim + 120)}>Show more</button></p> : null}
    </>
  );
}

const cell = (v: any) => (v == null ? "" : typeof v === "object" ? JSON.stringify(v) : String(v));
function RowsTable({ rows, open }: { rows: Record<string, any>[]; open: Open }) {
  if (!rows.length) return <p className="meta">No rows.</p>;
  const keys = uniq(rows.flatMap((r) => Object.keys(r)));
  return <Scroll><table><thead><tr>{keys.map((k) => <th key={k}>{pretty(k)}</th>)}</tr></thead><tbody>{rows.map((r, i) => <tr key={i}>{keys.map((k) => { const v = cell(r[k]); return <td key={k}>{/^CLM-\d{6}$/.test(v) ? <Ids ids={[v]} open={open} /> : v.length > 220 ? v.slice(0, 220) + "…" : v}</td>; })}</tr>)}</tbody></table></Scroll>;
}

export function ConflictsPage({ b, open }: { b: Bundle; open: Open }) {
  const items = b.conflicts.items; const types = items.reduce<Record<string, number>>((a, c) => { const t = c.type ?? "other"; a[t] = (a[t] ?? 0) + 1; return a; }, {});
  const audits = b.reports.reports.filter((r) => ["citation_audits", "evaluation_results", "validation"].includes(r.section));
  return (
    <>
      <Hero eyebrow="Evidence & method" title="Conflicts, corrections and audits" lede="Every status downgrade, contradiction and audit amendment is recorded. The audit reports below are the reviewers' own words." />
      <div className="chips">{Object.entries(types).map(([t, n]) => <span key={t} className="tag">{pretty(t)} · {n}</span>)}</div>
      <h2>Recorded conflicts and amendments</h2>
      {b.conflicts.available ? <RowsTable rows={items.map((c) => ({ type: c.type, claim_id: c.claim_id, from: c.from ?? c.changed?.status?.from, to: c.to ?? c.changed?.status?.to, reason: c.reason ?? c.audit_ref ?? "", recorded: c.recorded }))} open={open} /> : <Absent what="conflicts.jsonl not found." />}
      <h2 style={{ marginTop: 28 }}>Audit and evaluation reports</h2>
      {audits.map((r, i) => <ReportEmbed key={r.path} b={b} r={r} open={open} startOpen={i === 0} />)}
      {!audits.length ? <Notice title="Not yet produced.">No audit reports found.</Notice> : null}
    </>
  );
}

export function CoveragePage({ b, open }: { b: Bundle; open: Open }) {
  const sum = b.reports.reports.filter((r) => r.path.endsWith("coverage_summary.md")); const rows = b.coverage.rows;
  return (
    <>
      <Hero eyebrow="Evidence & method" title="Coverage" lede="What was discovered, what was reviewed and what remains, by company and source family." />
      {sum.map((r) => <ReportEmbed key={r.path} b={b} r={r} open={open} />)}
      <h2>Coverage ledger</h2>
      <Scroll><table><thead><tr><th>Company</th><th>Source family</th><th>Status</th><th>Discovered</th><th>Reviewed</th><th>Notes</th><th>Gap</th></tr></thead><tbody>
        {rows.map((r, i) => <tr key={i}><td><CoTag co={r.company} /></td><td>{r.family}</td><td><span className="tag">{pretty(r.status)}</span></td><td className="num">{r.discovered}</td><td className="num">{r.reviewed}</td><td>{r.notes ?? ""}</td><td>{r.gap ?? ""}</td></tr>)}
      </tbody></table></Scroll>
    </>
  );
}

export function MethodPage({ b, open }: { b: Bundle; open: Open }) {
  const rs = b.reports.reports.filter((r) => r.section === "method");
  return <><Hero eyebrow="Evidence & method" title="Research operating system" lede="Protocols, source-quality rules, the evaluation rubric and the research graph that structure how evidence was gathered and judged." />
    <p><Link to="/research-graph">Open the interactive research graph →</Link></p>{rs.map((r, i) => <ReportEmbed key={r.path} b={b} r={r} open={open} startOpen={i === 0} />)}</>;
}
export function RunsPage({ b, open }: { b: Bundle; open: Open }) {
  const rs = b.reports.reports.filter((r) => r.section === "runs"); const briefs = b.reports.reports.filter((r) => r.section === "briefs");
  return <><Hero eyebrow="Evidence & method" title="Research runs and experiments" lede="Each run records its question, hypothesis, evidence gained and whether the approach was kept." />
    <h2>Experiment log</h2><RowsTable rows={b.log.experiments} open={open} /><h2 style={{ marginTop: 28 }}>Task backlog</h2><RowsTable rows={b.log.backlog} open={open} />
    <h2 style={{ marginTop: 28 }}>Run reports</h2>{rs.map((r, i) => <ReportEmbed key={r.path} b={b} r={r} open={open} startOpen={i === 0} />)}
    <h2 style={{ marginTop: 28 }}>Agent briefs</h2><ReportGrid reports={briefs} /></>;
}
export function StatePage({ b, open }: { b: Bundle; open: Open }) {
  const rs = b.reports.reports.filter((r) => r.section === "state");
  return <><Hero eyebrow="Evidence & method" title="Project state and how to continue" lede="Where the project stands, what is next and who owns what." />
    <h2>Dataset counts</h2><dl className="kpis">{Object.entries(b.state.datasets).map(([k, v]) => <Stat key={k} k={pretty(k)} v={v} />)}</dl>
    {rs.map((r, i) => <ReportEmbed key={r.path} b={b} r={r} open={open} startOpen={i === 0} />)}</>;
}

export function AllReports({ b }: { b: Bundle; open: Open }) {
  const [q, setQ] = useState(""); const [pil, setPil] = useState("all");
  const rows = b.reports.reports.filter((r) => (pil === "all" || r.pillar === pil) && (!q || (r.title + " " + r.path).toLowerCase().includes(q.toLowerCase())));
  return (
    <>
      <Hero eyebrow="Evidence & method" title="All reports" lede={`Every Markdown file in the research tree, ${b.reports.count} in total.`} />
      <div className="toolbar"><input placeholder="filter by title or path" value={q} onChange={(e) => setQ(e.target.value)} aria-label="filter reports" style={{ flex: "1 1 260px" }} /></div>
      <div className="chips" role="group" aria-label="pillar filter">{["all", ...PILLARS.filter((p) => !["overview", "ask"].includes(p.id)).map((p) => p.id)].map((id) => <button key={id} className={`chip ${pil === id ? "on" : ""}`} aria-pressed={pil === id} onClick={() => setPil(id)}>{id === "all" ? "all" : PILLARS.find((p) => p.id === id)!.label}</button>)}</div>
      <Scroll><table><thead><tr><th>Report</th><th>Pillar</th><th>Section</th><th>Words</th><th>Updated</th><th>File</th></tr></thead><tbody>
        {rows.map((r) => <tr key={r.path}><td><Link to={readPath(r.path)}>{r.title}</Link></td><td>{PILLARS.find((p) => p.id === r.pillar)?.label}</td><td>{sectionLabel(r.section)}</td><td className="num">{r.word_count.toLocaleString()}</td><td className="num">{r.updated}</td><td className="src">{r.path}</td></tr>)}
      </tbody></table></Scroll>
    </>
  );
}
export { ReportCard, ReportMeta, MdView };
