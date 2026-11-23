// Views 1-6: Future, Powerhouses, Differentiators, Pipeline & LOE, Observatory, Ecosystem
import { Fragment, useCallback, useMemo, useState } from "react";
import { Bundle, Claim, COMPANY_COLORS, COMPANY_NAMES, MATURITY_ORDER, fmtMoney, fmtUsdM, uniq, yearFrac, MatrixRow, strat, STRATEGY_ABSENT } from "./data";
import { Absent, Badges, ClaimCard, CoTag, ForceGraph, Gap, Ids, LineChart, MiniBars, Open, Scroll, Swim, SwimItem } from "./components";
import { EMERGING_LEVELS, NARRATIVE, PROVEN_LEVELS, SPINE } from "./narrative";
import { Link } from "react-router-dom";
import { PILLARS } from "./pillars";
import { ReportCard } from "./reader";

const CO3: string[] = ["LLY", "JNJ", "ABBV"];
const CO4: string[] = ["LLY", "JNJ", "ABBV", "TAK"];
const byCo = (b: Bundle, co: string) => b.claims.filter((c) => c.companies.includes(co as any));
const nonXbrl = (cs: Claim[]) => cs.filter((c) => c.run_id !== "RUN-0001-sec-ingest");
const pretty = (s: string) => s.replace(/_/g, " ").toLowerCase();

const DELIV_ORDER = ["executive_summary", "competitor_comparison", "takeda_strategy", "investment_roadmap", "recommendations"];
export function ClaimLine({ c, open }: { c: Claim; open: Open }) {
  return (
    <div className="cline">
      <div className="cline-head">{c.companies.map((co) => <CoTag key={co} co={co} />)}<span className={`tag ${c.kind}`}>{c.kind}</span><Badges c={c} /></div>
      <p className="clamp">{c.statement}</p>
      <Ids ids={[c.claim_id]} open={open} />
    </div>
  );
}

function Chips({ options, value, onChange, label, all = "all" }: { options: string[]; value: string; onChange: (v: string) => void; label: (v: string) => string; all?: string }) {
  return <div className="chips" role="group">{[...(all === "ALL_HIDDEN" ? [] : [all]), ...options].map((o) => <button key={o} className={`chip ${value === o ? "on" : ""}`} aria-pressed={value === o} onClick={() => onChange(o)}>{o === all ? all : label(o)}</button>)}</div>;
}

export function Future({ b, open }: { b: Bundle; open: Open }) {
  const st = b.state;
  const [lens, setLens] = useState<"all" | "proven" | "emerging">("all");
  const mat = (lv: string[]) => b.maturity.filter((m) => lv.includes(m.maturity));
  const total = Math.max(1, b.maturity.length);
  const stratOn = Object.values(st.strategy_files).filter(Boolean).length; const stratAll = Object.keys(st.strategy_files).length;
  return (
    <>
      <div className="eyebrow">View 1 · The Future of Medicine</div>
      <h1>What is changing, who is winning, and what Takeda must prepare for</h1>
      <p className="lede">An executive reading of a research encyclopedia of {st.sources} inspected sources and {st.claims} traceable claims. Each passage below is bound to registry claim IDs; the statements shown are the registry's own wording. Where the research has not reached a question, the page says so.</p>
      <dl className="kpis">
        <div><dt>sources inspected</dt><dd>{st.sources}</dd></div>
        <div><dt>claims ({st.claims_by_status.SUPPORTED ?? 0} supported)</dt><dd>{st.claims}</dd></div>
        <div><dt>tier-1 primary sources</dt><dd>{st.sources_by_tier.T1_primary_official ?? 0}</dd></div>
        <div><dt>claims with contrary evidence</dt><dd>{st.claims_contrary}</dd></div>
        <div><dt>strategy files produced</dt><dd>{stratOn}/{stratAll}</dd></div>
      </dl>
      <nav className="spine" aria-label="The story in ten steps"><ol>
        {SPINE.map((st, i) => <li key={st.id}>{st.block ? <a href={`#n-${st.block}`} onClick={(e) => { e.preventDefault(); document.getElementById(`n-${st.block}`)?.scrollIntoView({ block: "start" }); }}><span>{String(i + 1).padStart(2, "0")}</span>{st.label}</a> : <a href={`#stage-${st.id}`} onClick={(e) => { e.preventDefault(); document.getElementById(`stage-${st.id}`)?.scrollIntoView({ block: "start" }); }}><span>{String(i + 1).padStart(2, "0")}</span>{st.label}<small className="fwd-tag">forward-looking</small></a>}</li>)}
      </ol></nav>
      <div className="narr-list">
        {NARRATIVE.map((n) => {
          const cl = n.claimIds.map((id) => b.claimById.get(id)).filter(Boolean) as Claim[];
          return (
            <section key={n.id} className="narr" aria-labelledby={`n-${n.id}`}>
              <div className="narr-text">
                <div className="stage-no">{SPINE.findIndex((x) => x.block === n.id) >= 0 ? String(SPINE.findIndex((x) => x.block === n.id) + 1).padStart(2, "0") : "+"}<span>{n.stage}</span></div>
                <h2 id={`n-${n.id}`}>{n.heading}</h2>
                <p>{n.lead}</p>
              </div>
              <div className="narr-evidence">{cl.length ? cl.map((c) => <ClaimLine key={c.claim_id} c={c} open={open} />) : <Gap>None of the bound claims is in the registry yet.</Gap>}</div>
            </section>
          );
        })}
      </div>
      <h2 style={{ marginTop: 36 }}>AI, data and robotics: operating versus announced</h2>
      <p className="lede">Maturity is assigned from the evidence, not from the announcement. “Operating” means a platform or product is live; it does not mean value has been shown. Outcome evidence is tracked separately in View 5.</p>
      <div className="ladder" role="img" aria-label="maturity distribution">
        {MATURITY_ORDER.map((l) => { const n = b.maturity.filter((m) => m.maturity === l).length; return <div key={l} style={{ flex: Math.max(n, 0.4) }} className={`rung r-${l}`} title={`${pretty(l)}: ${n}`}><b>{n}</b><span>{pretty(l)}</span></div>; })}
      </div>
      <div className="toolbar"><Chips options={["proven", "emerging"]} value={lens} onChange={(v) => setLens(v as any)} label={(v) => (v === "proven" ? "operating / scaled / outcome" : "concept / prototype / pilot")} all="all" /></div>
      <div className="grid g2">
        {(lens === "all" || lens === "proven") && <div className="ledger"><h3>Operating, scaled or with an observed outcome <small>({mat(PROVEN_LEVELS).length} of {total})</small></h3>{mat(PROVEN_LEVELS).map((m) => <div key={m.claim_id} className="lrow"><CoTag co={m.company} /><span className="tag">{pretty(m.maturity)}</span><p className="clamp">{m.statement}</p><Ids ids={[m.claim_id]} open={open} /></div>)}</div>}
        {(lens === "all" || lens === "emerging") && <div className="ledger"><h3>Announced, prototyped or piloting <small>({mat(EMERGING_LEVELS).length} of {total})</small></h3>{mat(EMERGING_LEVELS).map((m) => <div key={m.claim_id} className="lrow"><CoTag co={m.company} /><span className="tag">{pretty(m.maturity)}</span><p className="clamp">{m.statement}</p><Ids ids={[m.claim_id]} open={open} /></div>)}</div>}
      </div>
      <ForwardStages b={b} open={open} />
      <h2 style={{ marginTop: 40 }}>Reading guide</h2>
      {DELIV_ORDER.some((n) => b.reportByPath.has(`deliverables/${n}.md`)) ? <><h3>Start here: the deliverables</h3><div className="rgrid">{DELIV_ORDER.map((n) => b.reportByPath.get(`deliverables/${n}.md`)).filter((r): r is NonNullable<typeof r> => !!r).map((r) => <ReportCard key={r.path} r={r} />)}</div></> : null}
      <div className="grid g3">{PILLARS.filter((p) => p.id !== "overview").map((p) => <Link key={p.id} to={p.path} className={`rcard ${p.forward ? "fwdcard" : ""}`}><b>{p.label}</b><span className="rcard-ex">{p.blurb}</span>{p.forward ? <span className="fwd-tag">forward-looking</span> : null}</Link>)}</div>
      <div className="panel integrity"><h3>Research integrity</h3>
        <p>{st.sources} sources inspected and {st.claims} claims recorded, of which {st.claims_by_status.SUPPORTED ?? 0} are fully supported. {st.claims_contrary} claims carry contrary evidence and {st.claims_single_source} rest on a single interested source. {st.datasets.conflicts} status changes, contradictions and audit amendments are logged. Latest claim verification in the registry: {b.claims.map((c) => c.last_verified).sort().pop()}.</p>
        <p><Link to="/conflicts">Read the audit and conflict log</Link> · <Link to="/coverage">See what was never read</Link> · <Link to="/evidence">Evidence & method</Link></p></div>
    </>
  );
}

function ForwardStages({ b, open }: { b: Bundle; open: Open }) {
  const gaps = b.takeda.available ? b.takeda.capabilities.filter((c) => ["EVIDENCE_GAP", "EXISTING_BUT_UNDERDEVELOPED", "POTENTIAL_NEW_CAPABILITY"].includes(c.class)) : [];
  const bets = strat<any>(b, "strategy_bets")?.bets as any[] | undefined; const pf = strat<any>(b, "portfolios")?.portfolios as any[] | undefined;
  const rm = strat<any>(b, "roadmap")?.milestones as any[] | undefined; const sg = strat<any>(b, "stage_gates")?.gates as any[] | undefined; const ca = strat<any>(b, "counterarguments")?.items as any[] | undefined;
  const body = (id: string) => {
    if (id === "opportunity") return gaps.length ? <ul className="alist">{gaps.slice(0, 8).map((c, i) => <li key={i}><span className="tag">{c.class.replace(/_/g, " ").toLowerCase()}</span> {c.area} <Ids ids={c.claim_ids} open={open} /></li>)}</ul> : <Absent what="Takeda capability baseline not available." />;
    const data: Record<string, any[] | undefined> = { build: bets, invest: pf, execute: rm, measure: sg ?? ca };
    const d = data[id];
    if (!d || !d.length) return <Absent kind="strategy" what="This step fills in when the strategy files exist." />;
    return <ul className="alist">{d.slice(0, 6).map((x, i) => <li key={i}><span className="tag SCENARIO">scenario</span> {x.name ?? x.milestone ?? x.text ?? x.bet_id ?? x.id}</li>)}</ul>;
  };
  return (
    <section className="stages-fwd" aria-label="Forward-looking steps">
      {SPINE.slice(5).map((st, i) => (
        <div key={st.id} id={`stage-${st.id}`} className="narr fwd">
          <div className="narr-text"><div className="stage-no">{String(i + 6).padStart(2, "0")}<span>{st.label}</span></div><p>{st.lead}</p>{st.to ? <p><Link to={st.to}>Open this step in detail →</Link></p> : null}</div>
          <div className="narr-evidence">{body(st.id)}</div>
        </div>
      ))}
      {Object.values(b.state.strategy_files).every((v) => !v) ? <p className="meta">{STRATEGY_ABSENT}</p> : null}
    </section>
  );
}

const CONCEPTS: [string, string][] = [["revenue", "Revenue"], ["rnd_expense", "R&D expense"], ["net_income", "Net income"], ["op_cash_flow", "Operating cash flow"], ["capex", "Capital expenditure"], ["acquisitions_cash", "Cash for acquisitions"], ["acquired_iprd_payments", "Acquired IPR&D (cash)"], ["sga_expense", "SG&A"], ["total_assets", "Total assets"], ["long_term_debt", "Long-term debt"]];
const MULTIPLES = ["revenue", "rnd_expense", "net_income", "capex"];

export function Powerhouses({ b, open }: { b: Bundle; open: Open }) {
  const [concept, setConcept] = useState("revenue");
  const [cos, setCos] = useState<string[]>([...CO3]);
  const [domain, setDomain] = useState("all");
  const [tl, setTl] = useState<string[]>([...CO4]);
  const fyOf = (co: string, k: string) => Object.keys(b.financials[co]?.concepts[k] ?? {}).sort();
  const years = uniq(cos.flatMap((co) => fyOf(co, concept))).sort().map((y) => parseInt(y, 10));
  const series = cos.map((co) => ({ key: COMPANY_NAMES[co], color: COMPANY_COLORS[co], points: years.map((y) => { const v = b.financials[co]?.concepts[concept]?.[String(y)]; return v ? ([y, v.value] as [number, number]) : null; }).filter(Boolean) as [number, number][] })).filter((s) => s.points.length);
  const domains = uniq(b.claims.flatMap((c) => c.domains ?? [])).sort();
  const items: SwimItem[] = [];
  for (const co of tl) for (const e of b.timelines[co]?.events ?? []) {
    const t = yearFrac(e.date); if (t == null) continue;
    if (domain !== "all" && !e.claim_ids.some((id) => (b.claimById.get(id)?.domains ?? []).includes(domain))) continue;
    items.push({ lane: co, t, label: `${COMPANY_NAMES[co]} · ${e.date} · ${e.event}`, claim_ids: e.claim_ids, color: COMPANY_COLORS[co] });
  }
  const events = tl.flatMap((co) => (b.timelines[co]?.events ?? []).map((e) => ({ co, ...e }))).filter((e) => domain === "all" || e.claim_ids.some((id) => (b.claimById.get(id)?.domains ?? []).includes(domain))).sort((a, c) => (yearFrac(a.date) ?? 0) - (yearFrac(c.date) ?? 0));
  const [showAll, setShowAll] = useState(false);
  const toggle = (arr: string[], set: (v: string[]) => void, co: string) => set(arr.includes(co) ? arr.filter((x) => x !== co) : [...arr, co]);
  return (
    <>
      <div className="eyebrow">View 2 · The Three Pharmaceutical Powerhouses</div>
      <h1>Lilly, J&J and AbbVie as filed, with Takeda alongside</h1>
      <p className="lede">Audited annual values from each company's SEC XBRL submissions, in the unit each cell states. Fiscal-year conventions: {CO4.map((c) => `${COMPANY_NAMES[c]} (${b.financials[c]?.meta.fiscal_year})`).join("; ")}.</p>
      <div className="notice" role="note"><b>Comparability caveats.</b> J&J's perimeter changed during the period (the Consumer Health separation); earlier years are as originally reported, so a year-on-year step can be partly perimeter rather than performance. Takeda reports in yen on an April–March year labelled by its start year and is shown in the timeline only.</div>
      <div className="toolbar"><div className="chips" role="group" aria-label="companies">{CO3.map((co) => <button key={co} className={`chip ${cos.includes(co) ? "on" : ""}`} aria-pressed={cos.includes(co)} onClick={() => toggle(cos, setCos, co)}>{COMPANY_NAMES[co]}</button>)}</div>
        <label className="sel">metric <select value={concept} onChange={(e) => setConcept(e.target.value)}>{CONCEPTS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}</select></label></div>
      <div className="panel"><LineChart series={series} yLabel="as filed (unit per table)" xTicks={years} /></div>
      <Scroll><table style={{ marginTop: 14 }}>
        <thead><tr><th>Company</th>{years.map((y) => <th key={y} style={{ textAlign: "right" }}>FY{y}</th>)}<th>Evidence</th></tr></thead>
        <tbody>{cos.map((co) => <tr key={co}><td><CoTag co={co} /></td>{years.map((y) => { const v = b.financials[co]?.concepts[concept]?.[String(y)]; return <td key={y} className="num">{v ? fmtMoney(v.value, v.unit) : "—"}</td>; })}<td>{years.map((y) => { const v = b.financials[co]?.concepts[concept]?.[String(y)]; return v ? <button key={y} className="chip id" onClick={() => open(v.claim_id)} title={`FY${y} evidence`}>{y}</button> : null; })}</td></tr>)}</tbody>
      </table></Scroll>
      <h2 style={{ marginTop: 32 }}>Financial small multiples</h2>
      <p className="meta">One bar series per company and metric; bars are focusable and open their filing claim. Scales are independent per cell.</p>
      <div className="multiples" style={{ gridTemplateColumns: `repeat(${Math.max(1, cos.length)}, minmax(0,1fr))` }}>
        {cos.map((co) => <div key={co} className="mcol"><h3><CoTag co={co} /></h3>
          {MULTIPLES.map((k) => { const ys = fyOf(co, k); const data = ys.map((y) => ({ label: `FY${y}`, value: b.financials[co].concepts[k][y].value, claim_id: b.financials[co].concepts[k][y].claim_id })); const unit = ys.length ? b.financials[co].concepts[k][ys[0]].unit : undefined;
            return <div key={k} className="mcell"><div className="mlabel">{CONCEPTS.find((c) => c[0] === k)?.[1]}</div><MiniBars data={data} color={COMPANY_COLORS[co]} fmt={(v) => fmtMoney(v, unit)} open={open} /></div>; })}
        </div>)}
      </div>
      <h2 style={{ marginTop: 32 }}>Products as disclosed</h2>
      <div className="multiples" style={{ gridTemplateColumns: "repeat(auto-fit,minmax(220px,1fr))" }}>
        {b.products.series.filter((s) => cos.includes(s.company)).map((s) => { const data = Object.entries(s.values).filter(([, v]) => v != null).map(([k, v]) => ({ label: k, value: v as number, claim_id: s.claims[0] }));
          return <div key={s.company + s.product} className="mcell"><div className="mlabel"><CoTag co={s.company} /> <b>{s.product}</b> <span className="tag">{pretty(s.role)}</span></div><MiniBars data={data} color={COMPANY_COLORS[s.company]} fmt={(v) => fmtMoney(v, s.unit)} open={open} />{s.loe_note ? <div className="meta">{s.loe_note}</div> : null}</div>; })}
      </div>
      <h2 style={{ marginTop: 32 }}>Dated strategic events</h2>
      <div className="toolbar"><div className="chips" role="group" aria-label="timeline companies">{CO4.map((co) => <button key={co} className={`chip ${tl.includes(co) ? "on" : ""}`} aria-pressed={tl.includes(co)} onClick={() => toggle(tl, setTl, co)}>{COMPANY_NAMES[co]}</button>)}</div>
        <label className="sel">domain <select value={domain} onChange={(e) => setDomain(e.target.value)}><option value="all">all domains</option>{domains.map((d) => <option key={d} value={d}>{pretty(d)}</option>)}</select></label></div>
      {items.length ? <div className="panel"><Swim lanes={tl.map((co) => ({ key: co, label: COMPANY_NAMES[co], color: COMPANY_COLORS[co] }))} items={items} open={open} /></div> : <Gap>No dated events match this filter.</Gap>}
      <Scroll><table style={{ marginTop: 12 }}><thead><tr><th>Date</th><th>Company</th><th>Event</th><th>Evidence</th></tr></thead><tbody>
        {(showAll ? events : events.slice(0, 15)).map((e, i) => <tr key={i}><td className="num">{e.date}</td><td><CoTag co={e.co} /></td><td>{e.event}</td><td><Ids ids={e.claim_ids} open={open} /></td></tr>)}
      </tbody></table></Scroll>
      {events.length > 15 ? <button className="chip" onClick={() => setShowAll(!showAll)}>{showAll ? "show fewer" : `show all ${events.length} events`}</button> : null}
      <h2 style={{ marginTop: 32 }}>Strategic record by company</h2>
      <div className="grid g3">
        {CO3.map((co) => { const cl = nonXbrl(byCo(b, co)).filter((c) => domain === "all" || (c.domains ?? []).includes(domain)); return (
          <div key={co}><h3><CoTag co={co} /> {cl.length} claims</h3>{cl.length ? cl.slice(0, 12).map((c) => <ClaimLine key={c.claim_id} c={c} open={open} />) : <Gap>No claims in this domain yet for {COMPANY_NAMES[co]}.</Gap>}{cl.length > 12 ? <p className="meta">First 12 shown; use the Encyclopedia for the rest.</p> : null}</div>
        ); })}
      </div>
    </>
  );
}

const STAGES: [string, string][] = [["problem", "Problem"], ["investment", "Investment"], ["capability", "Capability"], ["execution", "Execution"], ["outcome", "Outcome"], ["moat", "Moat"]];

export function Differentiators({ b, open }: { b: Bundle; open: Open }) {
  const cards = b.cards.cards;
  const [co, setCo] = useState("all"); const [kind, setKind] = useState("all");
  const list = cards.filter((c) => (co === "all" || c.companies.includes(co as any)) && (kind === "all" || c.kind === kind));
  const [sel, setSel] = useState<string | null>(null);
  const cur = cards.find((c) => c.id === sel) ?? list[0];
  if (!b.cards.available) return <><div className="eyebrow">View 3 · What Makes Them Different?</div><h1>Differentiators</h1><Absent what="Capability mechanism cards and moat tables could not be parsed." file="New_mediciine/industry_transformation/ai_data_robotics/capability_mechanism_cards.md" /></>;
  const cos = uniq(cards.flatMap((c) => c.companies));
  return (
    <>
      <div className="eyebrow">View 3 · What Makes Them Different?</div>
      <h1>Each differentiator as a mechanism, not a slogan</h1>
      <p className="lede">Capability cards trace Problem → Investment → Capability → Execution → Outcome → Moat → Evidence. Moat analyses are interpretations by the research team and are shown with the facts they rest on. A stage the source does not cover is marked as not covered rather than inferred.</p>
      <div className="toolbar"><Chips options={cos} value={co} onChange={setCo} label={(c) => COMPANY_NAMES[c] ?? c} all="all companies" /><Chips options={["mechanism_card", "moat"]} value={kind} onChange={setKind} label={(k) => (k === "moat" ? "moat analyses" : "capability cards")} all="all types" /></div>
      <div className="explorer">
        <nav aria-label="Differentiators" className="xlist">
          {list.map((c) => <button key={c.id} className={`xitem ${cur?.id === c.id ? "on" : ""}`} aria-current={cur?.id === c.id} onClick={() => setSel(c.id)}>
            <span className="xco" style={{ background: COMPANY_COLORS[c.companies[0]] }} /><span><b>{c.title}</b><small>{c.kind === "moat" ? "moat analysis" : "capability card"} · {c.claim_ids.length} claims</small></span></button>)}
          {!list.length ? <Gap>No differentiator matches the filters.</Gap> : null}
        </nav>
        {cur ? <section className="xdetail" aria-live="polite">
          <div>{cur.companies.map((x) => <CoTag key={x} co={x} />)}<span className="tag">{cur.kind === "moat" ? "moat analysis (interpretation)" : "capability mechanism card"}</span>{cur.gap ? <span className="tag warnb">gap noted</span> : null}</div>
          <h2 style={{ marginTop: 8 }}>{cur.title}</h2>
          <ol className="chain">
            {STAGES.map(([k, l]) => { const s = cur.stages[k]; return <li key={k} className={s ? "" : "na"}><h4>{l}</h4>{s ? <><p>{s.text}</p><Ids ids={s.claim_ids} open={open} /></> : <p className="meta">Not covered by this source.</p>}</li>; })}
            <li className="ev"><h4>Evidence</h4><Ids ids={cur.claim_ids} open={open} /><div style={{ marginTop: 6 }}><Ids ids={cur.source_ids} open={open} label="sources" /></div>{!cur.claim_ids.length ? <p className="meta">No claim IDs cited.</p> : null}</li>
          </ol>
          {cur.stages.assets ? <p><b>Enabling assets.</b> {cur.stages.assets.text}</p> : null}
          {cur.stages.response ? <p><b>Competitive response.</b> {cur.stages.response.text}</p> : null}
          {cur.stages.maturity ? <p><b>Maturity.</b> {cur.stages.maturity.text}</p> : null}
          {cur.stages.takeda ? <p className="impl"><b>Takeda relevance (analyst view).</b> {cur.stages.takeda.text}</p> : null}
          {cur.contrary.length ? <p className="contrary"><b>Contrary evidence:</b> {cur.contrary.join(" ")}</p> : null}
          <p className="src">source file: {cur.source_file}</p>
        </section> : null}
      </div>
    </>
  );
}

export function PipelineLOE({ b, open }: { b: Bundle; open: Open }) {
  const [co, setCo] = useState<string>("ABBV");
  const ser = b.products.series.filter((s) => s.company === co);
  const unit = ser[0]?.unit;
  const xs = uniq(ser.flatMap((s) => Object.keys(s.values))).map((k) => parseInt(k.replace("FY", ""), 10)).sort();
  const series = ser.map((s, i) => ({ key: s.product, color: PALETTE[i % PALETTE.length], points: Object.entries(s.values).filter(([, v]) => v != null).map(([k, v]) => [parseInt(k.replace("FY", ""), 10), v as number] as [number, number]) }));
  const ev = b.products.loe_events.filter((e) => e.company === co);
  const [show, setShow] = useState({ novel: true, other_application: false, supplemental: false, setbacks: true });
  const [cof, setCof] = useState<string>("all");
  const lanes = CO4.filter((c) => cof === "all" || c === cof).map((c) => ({ key: c, label: COMPANY_NAMES[c], color: COMPANY_COLORS[c] }));
  const items: SwimItem[] = [];
  for (const a of b.approvals.rows) { if (!a.company || !(show as any)[a.kind]) continue; const t = yearFrac(a.date); if (t == null) continue; items.push({ lane: a.company, t, label: `Approval · ${a.date} · ${a.product} · ${a.detail}`, claim_ids: a.claim_ids, color: "#0f6b3d", shape: a.kind === "novel" ? "dot" : "diamond" }); }
  if (show.setbacks) for (const s of b.setbacks.rows) { if (!s.company) continue; const t = yearFrac(s.when); if (t == null) continue; items.push({ lane: s.company, t, label: `Setback · ${s.when} · ${s.asset} · ${s.what}`, claim_ids: s.claim_ids, color: "#b3261e", shape: "cross" }); }
  const laneKeys = new Set(lanes.map((l) => l.key)); const shown = items.filter((i) => laneKeys.has(i.lane));
  return (
    <>
      <div className="eyebrow">View 4 · Pipeline and LOE Intelligence</div>
      <h1>Product dependence, exclusivity cliffs, approvals and setbacks</h1>
      <p className="lede">Product revenue as disclosed in each company's latest annual report; years without a cited value are left blank and no forecasts are drawn. Approval dates come from the regulator's record; setbacks are only those the company or registry disclosed.</p>
      <div className="toolbar"><Chips options={[...CO4]} value={co} onChange={setCo} label={(c) => COMPANY_NAMES[c]} all="ALL_HIDDEN" /></div>
      <div className="panel"><LineChart series={series} yLabel={unit === "JPY_billions" ? "JPY billions (FY = April–March)" : "USD millions"} xTicks={xs} /></div>
      <Scroll><table style={{ marginTop: 14 }}><thead><tr><th>Product</th><th>Molecule</th><th>Role</th>{xs.map((x) => <th key={x} style={{ textAlign: "right" }}>{unit === "JPY_billions" ? "FY" : ""}{x}</th>)}<th>LOE note</th><th>Evidence</th></tr></thead>
        <tbody>{ser.map((s) => <tr key={s.product}><td><b>{s.product}</b></td><td>{s.molecule}</td><td><span className="tag">{pretty(s.role)}</span></td>{xs.map((x) => { const v = s.values[String(x)] ?? s.values[`FY${x}`]; return <td key={x} className="num">{v != null ? fmtMoney(v, s.unit) : "—"}</td>; })}<td style={{ fontSize: "0.82rem" }}>{s.loe_note ?? ""}</td><td><Ids ids={s.claims} open={open} /></td></tr>)}</tbody></table></Scroll>
      <h2 style={{ marginTop: 30 }}>Exclusivity events (occurred and company-disclosed expected)</h2>
      <div className="timeline">{[...ev].sort((a, c) => a.date.localeCompare(c.date)).map((e, i) => <div key={i} className={`ev ${e.status}`}><b>{e.date}</b> · <b>{e.product}</b> — {e.event} <span className="tag">{e.status}</span> <Ids ids={e.claims} open={open} /></div>)}</div>
      {ev.length === 0 ? <Gap>No LOE events recorded for this company yet.</Gap> : null}
      <h2 style={{ marginTop: 30 }}>Approvals and setbacks, all four companies</h2>
      {!b.approvals.available && !b.setbacks.available ? <Absent what={`${b.approvals.reason ?? "approvals"}; ${b.setbacks.reason ?? "setbacks"}.`} file="New_mediciine/industry_transformation/pipeline_regulatory/" /> : <>
        <div className="toolbar">
          <div className="chips" role="group" aria-label="layers">
            <button className={`chip ${show.novel ? "on" : ""}`} aria-pressed={show.novel} onClick={() => setShow({ ...show, novel: !show.novel })}>● novel approvals</button>
            <button className={`chip ${show.other_application ? "on" : ""}`} aria-pressed={show.other_application} onClick={() => setShow({ ...show, other_application: !show.other_application })}>◆ other applications</button>
            <button className={`chip ${show.supplemental ? "on" : ""}`} aria-pressed={show.supplemental} onClick={() => setShow({ ...show, supplemental: !show.supplemental })}>◆ supplemental approvals</button>
            <button className={`chip ${show.setbacks ? "on" : ""}`} aria-pressed={show.setbacks} onClick={() => setShow({ ...show, setbacks: !show.setbacks })}>✕ setbacks</button>
          </div>
          <label className="sel">company <select value={cof} onChange={(e) => setCof(e.target.value)}><option value="all">all</option>{CO4.map((c) => <option key={c} value={c}>{COMPANY_NAMES[c]}</option>)}</select></label>
        </div>
        <div className="panel"><Swim lanes={lanes} items={shown} open={open} laneH={64} /></div>
        <div className="grid g2" style={{ marginTop: 14 }}>
          <div><h3>Approvals ({b.approvals.rows.filter((a) => cof === "all" || a.company === cof).length})</h3><Scroll><table><thead><tr><th>Date</th><th>Co.</th><th>Product</th><th>Detail</th><th>Evidence</th></tr></thead><tbody>
            {b.approvals.rows.filter((a) => (cof === "all" || a.company === cof) && (show as any)[a.kind]).map((a, i) => <tr key={i}><td className="num">{a.date}</td><td>{a.company ? <CoTag co={a.company} /> : null}</td><td><b>{a.product}</b></td><td>{a.detail}</td><td><Ids ids={a.claim_ids} open={open} /></td></tr>)}</tbody></table></Scroll></div>
          <div><h3>Setbacks ({b.setbacks.rows.filter((a) => cof === "all" || a.company === cof).length})</h3><Scroll><table><thead><tr><th>When</th><th>Co.</th><th>Asset</th><th>Disclosed</th><th>Evidence</th></tr></thead><tbody>
            {b.setbacks.rows.filter((a) => cof === "all" || a.company === cof).map((a, i) => <tr key={i}><td className="num">{a.when}</td><td>{a.company ? <CoTag co={a.company} /> : null}</td><td><b>{a.asset}</b></td><td>{a.what}</td><td><Ids ids={a.claim_ids} open={open} /></td></tr>)}</tbody></table></Scroll></div>
        </div></>}
      <Gap>Asset-level late-stage pipeline status (trial read-outs by programme) is not a generated dataset in this build.</Gap>
    </>
  );
}
const PALETTE = ["#C5000F", "#0F766E", "#0f6b3d", "#7a4b00", "#5b4ba0", "#0b5e6f", "#8a1538"];

export function Observatory({ b, open }: { b: Bundle; open: Open }) {
  const cols = [...MATURITY_ORDER, "OTHER"];
  const [lvl, setLvl] = useState("all"); const [co, setCo] = useState("all"); const [dom, setDom] = useState("all"); const [yr, setYr] = useState("all");
  const [sel, setSel] = useState<MatrixRow | null>(null);
  const rows = b.matrix.rows;
  const lvlOf = (r: MatrixRow) => (MATURITY_ORDER.includes(r.maturity) ? r.maturity : "OTHER");
  const fil = rows.filter((r) => (lvl === "all" || lvlOf(r) === lvl) && (co === "all" || r.companies.includes(co as any)) && (dom === "all" || r.domains.includes(dom)) && (yr === "all" || r.years.includes(+yr)));
  const lanes = ["LLY", "JNJ", "ABBV", "TAK", "INDUSTRY"];
  const domains = uniq(rows.flatMap((r) => r.domains)).sort(); const yrs = uniq(rows.flatMap((r) => r.years)).sort();
  const claimsF = b.maturity.filter((m) => (lvl === "all" || m.maturity === lvl) && (co === "all" || m.companies.includes(co as any)) && (dom === "all" || m.domains.includes(dom)) && (yr === "all" || (m.event_date ?? "").includes(yr)));
  const outcomeY = (r: MatrixRow) => /^y/i.test(r.outcome_evidence);
  return (
    <>
      <div className="eyebrow">View 5 · AI, Data and Robotics Observatory</div>
      <h1>Initiatives placed on a maturity ladder, not a hype curve</h1>
      <p className="lede">A press release moves an initiative to “concept”; a regulator's record or an audited result is needed for stronger placement. Filled dots have independent outcome evidence; hollow dots do not. Each dot opens its claims.</p>
      <div className="toolbar">
        <Chips options={cols} value={lvl} onChange={setLvl} label={pretty} all="all levels" />
      </div>
      <div className="toolbar">
        <Chips options={lanes} value={co} onChange={setCo} label={(c) => COMPANY_NAMES[c]} all="all companies" />
        <label className="sel">domain <select value={dom} onChange={(e) => setDom(e.target.value)}><option value="all">all</option>{domains.map((d) => <option key={d} value={d}>{pretty(d)}</option>)}</select></label>
        <label className="sel">year <select value={yr} onChange={(e) => setYr(e.target.value)}><option value="all">all</option>{yrs.map((y) => <option key={y}>{y}</option>)}</select></label>
      </div>
      {!b.matrix.available ? <Absent what={b.matrix.reason ?? "maturity matrix"} file="New_mediciine/industry_transformation/ai_data_robotics/maturity_matrix.md" /> :
        <Scroll><div className="landscape" style={{ gridTemplateColumns: `110px repeat(${cols.length}, minmax(120px,1fr))` }}>
          <div />{cols.map((c) => <div key={c} className="lh">{pretty(c)}</div>)}
          {lanes.map((l) => <Fragment key={l}><div className="ll" style={{ color: COMPANY_COLORS[l] }}>{COMPANY_NAMES[l]}</div>{cols.map((c) => { const cell = fil.filter((r) => r.companies.includes(l as any) && lvlOf(r) === c);
            return <div key={l + c} className="lc">{cell.map((r, i) => <button key={i} className={`dot ${outcomeY(r) ? "full" : ""} ${sel === r ? "sel" : ""}`} style={{ borderColor: COMPANY_COLORS[l], background: outcomeY(r) ? COMPANY_COLORS[l] : "#fff" }} title={`${r.initiative} (${r.maturity_raw})`} aria-label={r.initiative} onClick={() => setSel(r)} />)}</div>; })}</Fragment>)}
        </div></Scroll>}
      {sel ? <div className="panel" style={{ marginTop: 14 }} aria-live="polite"><h3>{sel.initiative}</h3><div>{sel.companies.map((c) => <CoTag key={c} co={c} />)}<span className="tag">{sel.maturity_raw}</span>{sel.domains.map((d) => <span key={d} className="tag">{pretty(d)}</span>)}</div>
        <p><b>Outcome evidence:</b> {sel.outcome_evidence || "not stated"}</p><p className="meta">{sel.note}</p><Ids ids={sel.claim_ids} open={open} label="claims" /></div> : <p className="meta">Select a dot for the initiative's note and claims. {fil.length} of {rows.length} initiatives match.</p>}
      <h2 style={{ marginTop: 28 }}>Claim-level maturity records ({claimsF.length})</h2>
      <Scroll><table><thead><tr><th>Company</th><th>Maturity</th><th>Initiative (as evidenced)</th><th>Date</th><th>Independent?</th><th>Evidence</th></tr></thead>
        <tbody>{claimsF.map((m) => <tr key={m.claim_id}><td>{m.companies.map((c) => <CoTag key={c} co={c} />)}</td><td><span className="tag">{pretty(m.maturity)}</span></td><td>{m.statement}</td><td className="num">{m.event_date ?? ""}</td><td>{m.single_interested_source ? "company only" : "yes"}</td><td><Ids ids={[m.claim_id]} open={open} /></td></tr>)}</tbody></table></Scroll>
      {claimsF.length === 0 ? <Gap>No claim-level maturity records match.</Gap> : null}
    </>
  );
}

export function Ecosystem({ b, open }: { b: Bundle; open: Open }) {
  const [edge, setEdge] = useState<any>(null);
  const [co, setCo] = useState("all"); const [mode, setMode] = useState<"deals" | "evidence" | "both">("deals"); const [type, setType] = useState("all"); const [minYear, setMinYear] = useState(0);
  const onEdge = useCallback((e: any) => setEdge(e), []);
  const dealYears = b.deals.edges.map((e) => e.year).filter(Boolean) as number[]; const yMin = dealYears.length ? Math.min(...dealYears) : 0; const yMax = dealYears.length ? Math.max(...dealYears) : 0;
  const types = uniq(b.deals.edges.map((e) => e.type)).sort();
  const g = useMemo(() => {
    const nodes = new Map<string, { id: string; type: string; label: string }>(); const edges: any[] = [];
    for (const c of ["LLY", "JNJ", "ABBV", "TAK"]) nodes.set(c, { id: c, type: "company", label: COMPANY_NAMES[c] });
    if (mode !== "evidence") for (const e of b.deals.edges) {
      if (!e.from_code || (co !== "all" && e.from_code !== co) || (type !== "all" && e.type !== type) || (minYear && (e.year ?? 0) < minYear)) continue;
      const id = "D:" + e.to; if (!nodes.has(id)) nodes.set(id, { id, type: "deal", label: e.to });
      edges.push({ source: e.from_code, target: id, claims: e.claim_ids, weight: e.value_usd_m, dashed: /terminat|dissol|divest/.test(e.type + " " + (e.status ?? "")), deal: e });
    }
    if (mode !== "deals") for (const e of b.kg.edges) {
      if (co !== "all" && e.source !== co) continue; if (!["LLY", "JNJ", "ABBV", "TAK"].includes(e.source)) continue;
      const n = b.kg.nodes.find((x) => x.id === e.target); if (!n) continue; if (!nodes.has(n.id)) nodes.set(n.id, n);
      edges.push({ source: e.source, target: e.target, claims: e.claims });
    }
    const used = new Set(edges.flatMap((e) => [e.source, e.target]));
    return { nodes: Array.from(nodes.values()).filter((n) => n.type === "company" || used.has(n.id)), edges };
  }, [b, co, mode, type, minYear]);
  const inv = b.deals.inventory.filter((r) => co === "all" || r.company === co);
  if (!b.deals.available && !b.kg.edges.length) return <><div className="eyebrow">View 6 · The Innovation Ecosystem Graph</div><h1>Ecosystem</h1><Absent what="No deal or evidence-link data." file="New_mediciine/industry_transformation/partnerships_ecosystem/" /></>;
  return (
    <>
      <div className="eyebrow">View 6 · The Innovation Ecosystem Graph</div>
      <h1>Companies, partners, deals and technologies, linked by evidence</h1>
      <p className="lede">{b.kg.note} Deal edges come from the partnership inventory; edge width is the disclosed deal value (USD millions) where one exists, otherwise a thin line. Dashed edges are terminated or divested. Click or focus a link for its claims.</p>
      <div className="toolbar"><Chips options={["deals", "evidence", "both"]} value={mode} onChange={(v) => setMode(v as any)} label={(m) => (m === "deals" ? "deals" : m === "evidence" ? "evidence links" : "both")} all="ALL_HIDDEN" />
        <Chips options={[...CO4]} value={co} onChange={setCo} label={(c) => COMPANY_NAMES[c]} all="all" />
        <label className="sel">type <select value={type} onChange={(e) => setType(e.target.value)}><option value="all">all</option>{types.map((t) => <option key={t} value={t}>{pretty(t)}</option>)}</select></label>
        {yMin ? <label className="sel">from year <input type="range" min={yMin} max={yMax} value={minYear || yMin} onChange={(e) => setMinYear(+e.target.value === yMin ? 0 : +e.target.value)} /> {minYear || yMin}</label> : null}
      </div>
      <div className="legend" style={{ marginBottom: 8 }}><span><i style={{ background: "#7a4b00" }} />deal counterparty</span><span><i style={{ background: "#C5000F" }} />technology</span><span><i style={{ background: "#0f6b3d" }} />product</span><span><i style={{ background: "#8a8f9c" }} />other entity</span></div>
      <div className="panel" style={{ padding: 0 }}><ForceGraph nodes={g.nodes} edges={g.edges} onEdge={onEdge} /></div>
      {edge ? <div className="panel" style={{ marginTop: 14 }} aria-live="polite"><h3>{COMPANY_NAMES[edge.source?.id ?? edge.source] ?? edge.source?.id} ↔ {String(edge.target?.label ?? edge.target?.id ?? edge.target).replace(/^E:/, "")}</h3>
        {edge.deal ? <p className="meta">{pretty(edge.deal.type)} · {edge.deal.date ?? ""} · {edge.deal.status ?? ""}{edge.deal.value_usd_m != null ? ` · ${fmtUsdM(edge.deal.value_usd_m)} (as listed in the deal edge file)` : " · value not disclosed in edge file"}</p> : null}
        {edge.claims.map((id: string) => { const c = b.claimById.get(id); return c ? <ClaimCard key={id} c={c} b={b} onOpen={open} /> : null; })}</div> : null}
      <h2 style={{ marginTop: 28 }}>Deal list (keyboard-accessible alternative to the graph)</h2>
      <Scroll><table><thead><tr><th>Date</th><th>Company</th><th>Counterparty</th><th>Type</th><th>Area</th><th>Upfront / consideration</th><th>Status at cutoff</th><th>Evidence</th></tr></thead><tbody>
        {inv.map((r, i) => <tr key={i}><td className="num">{r.date}</td><td><CoTag co={r.company} /></td><td><b>{r.counterparty}</b></td><td>{r.type}</td><td>{r.area}</td><td>{r.upfront}{r.contingent && r.contingent !== "n/a" ? <div className="meta">contingent: {r.contingent}</div> : null}</td><td>{r.status}</td><td><Ids ids={r.claim_ids} open={open} /></td></tr>)}</tbody></table></Scroll>
    </>
  );
}
