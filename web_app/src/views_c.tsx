// Views 9-11: Strategy Lab, Portfolio Simulator, Execution Roadmap. All content comes from strategy/data/*.json via the pipeline
// (contract: strategy/DATA_CONTRACT.md). When a file is absent each view shows an explicit notice; nothing is invented here.
import { useMemo, useState } from "react";
import { Bundle, COMPANY_COLORS, fmtUsdM, strat, uniq, yearFrac } from "./data";
import { Absent, Assumption, ClaimCard, CoTag, Dag, Gap, Ids, Open, Scroll, Simulated, Swim, useWidth } from "./components";

const pretty = (s: string) => String(s ?? "").replace(/_/g, " ").toLowerCase();
const arr = <T,>(x: T[] | undefined | null): T[] => (Array.isArray(x) ? x : []);
const DECISION_TONE: Record<string, string> = { BUILD: "ok", PARTNER: "ok", INVEST: "ok", ACQUIRE: "ok", EXPERIMENT: "mid", DEFER: "oth", REJECT: "bad" };

function useAssumptions(b: Bundle) {
  const list = arr(strat<{ assumptions: any[] }>(b, "assumptions")?.assumptions);
  return useMemo(() => new Map(list.map((a) => [a.id, a])), [list]);
}
function AssumptionList({ ids, map }: { ids: string[]; map: Map<string, any> }) {
  if (!ids.length) return null;
  return <ul className="alist">{ids.map((id) => { const a = map.get(id); return <li key={id}><Assumption id={id} /> {a ? <>{a.text}{a.value != null ? <> — <b>{String(a.value)} {a.unit ?? ""}</b></> : null} <span className="meta">sensitivity {a.sensitivity ?? "n/a"}{a.needs_internal_validation ? ` · needs internal validation${a.ivb_ref ? ` (${a.ivb_ref})` : ""}` : ""}</span><div className="meta">{a.rationale}</div></> : <span className="meta">not defined in assumptions file</span>}</li>; })}</ul>;
}

export function StrategyLab({ b, open }: { b: Bundle; open: Open }) {
  const bets: any[] = arr(strat<{ bets: any[] }>(b, "strategy_bets")?.bets);
  const asm = useAssumptions(b);
  const [sel, setSel] = useState<string | null>(null); const [hz, setHz] = useState("all"); const [dec, setDec] = useState("all"); const [bc, setBc] = useState("all");
  const list = bets.filter((x) => (hz === "all" || x.horizon === hz) && (dec === "all" || x.decision === dec) && (bc === "all" || x.baseline_class === bc));
  const cur = bets.find((x) => x.id === sel) ?? list[0];
  return (
    <>
      <div className="eyebrow">View 9 · Takeda 2040 Strategy Lab</div>
      <h1>Candidate platform bets, their evidence and their prerequisites</h1>
      {!bets.length ? <Absent kind="strategy" what="The bets explorer, prerequisite graph and per-bet evidence appear when the strategy files are produced." file="strategy/data/strategy_bets.json" /> : <>
        <p className="lede">Each bet carries a decision, its evidence IDs and the assumptions it depends on. Investment figures are scenario assumptions, not forecasts. “Hypothesis” confidence means the bet rests on reasoning more than on inspected evidence.</p>
        <div className="toolbar filters">
          <label className="sel">horizon<select value={hz} onChange={(e) => setHz(e.target.value)}><option value="all">all</option>{uniq(bets.map((x) => x.horizon)).sort().map((v) => <option key={v}>{v}</option>)}</select></label>
          <label className="sel">decision<select value={dec} onChange={(e) => setDec(e.target.value)}><option value="all">all</option>{uniq(bets.map((x) => x.decision)).sort().map((v) => <option key={v}>{v}</option>)}</select></label>
          <label className="sel">baseline<select value={bc} onChange={(e) => setBc(e.target.value)}><option value="all">all</option>{uniq(bets.map((x) => x.baseline_class)).sort().map((v) => <option key={v} value={v}>{pretty(v)}</option>)}</select></label>
        </div>
        <Scroll><table className="matrix"><thead><tr><th>Bet</th><th>Horizon</th><th>Decision</th><th>Takeda baseline</th><th>Confidence</th><th>Evidence</th></tr></thead><tbody>
          {list.map((x) => <tr key={x.id} className={cur?.id === x.id ? "hl" : ""}><td><button className="linkbtn" onClick={() => setSel(x.id)} aria-pressed={cur?.id === x.id}><b>{x.id}</b> {x.name}</button></td><td>{x.horizon}</td><td><span className={`cell ${DECISION_TONE[x.decision] ?? "oth"}`}>{x.decision}</span></td><td>{pretty(x.baseline_class)}</td><td>{pretty(x.confidence)}</td><td><Ids ids={arr(x.claim_ids)} open={open} /></td></tr>)}</tbody></table></Scroll>
        {!list.length ? <Gap>No bet matches the filters.</Gap> : null}
        <h2 style={{ marginTop: 28 }}>Prerequisite graph</h2>
        <div className="panel" style={{ padding: 8 }}><Dag nodes={bets.map((x) => ({ id: x.id, label: x.name, sub: `${x.horizon} · ${x.decision}`, color: x.decision === "REJECT" ? "#b3261e" : x.decision === "DEFER" ? "#9aa3b2" : "#C5000F" }))}
          edges={bets.flatMap((x) => arr<string>(x.prerequisites).map((p) => ({ source: p, target: x.id, label: `${p} must precede ${x.id}` })))} selected={cur?.id} onSelect={setSel} /></div>
        {cur ? <article className="bet" aria-live="polite">
          <h2>{cur.id} · {cur.name}</h2>
          <div><span className="tag">{cur.horizon}</span><span className={`cell ${DECISION_TONE[cur.decision] ?? "oth"}`}>{cur.decision}</span><span className="tag">{pretty(cur.baseline_class)}</span><span className={`tag ${cur.confidence === "hypothesis" ? "HYPOTHESIS" : "FACT"}`}>{pretty(cur.confidence)}</span>{arr<string>(cur.moat_mechanism).map((m) => <span key={m} className="tag">{pretty(m)}</span>)}</div>
          <div className="grid g2" style={{ marginTop: 12 }}>
            <div><h4>Thesis</h4><p>{cur.thesis}</p><h4>Market change</h4><p>{cur.market_change}</p><h4>Problem</h4><p>{cur.problem}</p></div>
            <div><h4>Architecture</h4>{(["build", "buy", "license", "partner"] as const).map((k) => arr<string>(cur.architecture?.[k]).length ? <p key={k}><b>{k}:</b> {arr<string>(cur.architecture[k]).join("; ")}</p> : null)}
              <h4>Time to value</h4><p><b>near term:</b> {cur.time_to_value?.near_term ?? "n/a"}<br /><b>long horizon:</b> {cur.time_to_value?.long_horizon ?? "n/a"}</p>
              <h4>Options</h4><p>{arr<string>(cur.options).map(pretty).join(" · ")}</p></div>
          </div>
          <h4>Investment envelope <Assumption /></h4>
          {cur.investment_usd_m ? <Scroll><table><thead><tr><th>Scenario</th><th style={{ textAlign: "right" }}>Initial</th><th style={{ textAlign: "right" }}>Follow-on</th><th style={{ textAlign: "right" }}>Scaled</th></tr></thead><tbody>
            {Object.entries(cur.investment_usd_m).filter(([, v]) => v && typeof v === "object" && !Array.isArray(v)).map(([k, v]: [string, any]) => <tr key={k}><td>{pretty(k)}</td>{["initial", "follow_on", "scaled"].map((f) => <td key={f} className="num">{typeof v[f] === "number" ? fmtUsdM(v[f]) : "—"}</td>)}</tr>)}</tbody></table></Scroll> : <Gap>No investment envelope in the file.</Gap>}
          <AssumptionList ids={uniq([...arr<string>(cur.investment_usd_m?.assumption_ids), ...arr<string>(cur.assumption_ids)])} map={asm} />
          <div className="grid g2"><div><h4>Outcomes</h4><ul>{arr<string>(cur.outcomes).map((o, i) => <li key={i}>{o}</li>)}</ul></div>
            <div><h4>Risks</h4><ul>{arr<any>(cur.risks).map((r, i) => <li key={i}><span className="tag">{pretty(r.type)}</span> {r.text}</li>)}</ul></div></div>
          {arr<any>(cur.competitor_analogues).length ? <><h4>Competitor analogues</h4>{arr<any>(cur.competitor_analogues).map((a, i) => <div key={i}><CoTag co={a.company} /> <Ids ids={arr(a.claim_ids)} open={open} /></div>)}</> : null}
          <h4>Evidence</h4>{arr<string>(cur.claim_ids).length ? arr<string>(cur.claim_ids).map((id) => { const c = b.claimById.get(id); return c ? <ClaimCard key={id} c={c} b={b} onOpen={open} /> : null; }) : <Gap>No registry claim is cited for this bet; treat the thesis as hypothesis.</Gap>}
        </article> : null}
      </>}
    </>
  );
}

const THEMES = ["core_capability", "adjacent", "long_horizon_bets", "external_innovation"];
const themeOf = (bet: any) => (["PARTNER", "INVEST", "ACQUIRE"].includes(bet?.decision) ? "external_innovation" : bet?.horizon === "H3" ? "long_horizon_bets"
  : ["EXISTING_STRENGTH", "EXISTING_BUT_UNDERDEVELOPED"].includes(bet?.baseline_class) ? "core_capability" : "adjacent");

export function Portfolio({ b, open }: { b: Bundle; open: Open }) {
  const pf = strat<any>(b, "portfolios"); const bets: any[] = arr(strat<{ bets: any[] }>(b, "strategy_bets")?.bets); const gates: any[] = arr(strat<{ gates: any[] }>(b, "stage_gates")?.gates);
  const asm = useAssumptions(b);
  const ports: any[] = arr(pf?.portfolios); const evals = new Map<string, any>(arr<any>(pf?.evaluation).map((e) => [e.bet_id, e]));
  const [name, setName] = useState<string | null>(null);
  const base = ports.find((p) => p.name === name) ?? ports[0];
  const [budget, setBudget] = useState<number | null>(null); const [hw, setHw] = useState<Record<string, number>>({ H1: 100, H2: 100, H3: 100 });
  const [tw, setTw] = useState<Record<string, number>>({ core_capability: 100, adjacent: 100, long_horizon_bets: 100, external_innovation: 100 });
  const [minPts, setMinPts] = useState(0); const [cut, setCut] = useState<number | null>(null);
  const totals = ports.map((p) => p.total_usd_m).filter((v) => typeof v === "number" && v > 0);
  const rows = useMemo(() => {
    if (!base) return [];
    const betMap = new Map(bets.map((x) => [x.id, x]));
    const raw = arr<any>(base.bets).map((x) => { const bet = betMap.get(x.bet_id); const ev = evals.get(x.bet_id); const th = themeOf(bet); const pts = typeof ev?.pts === "number" ? ev.pts : null;
      const on = pts == null || pts >= minPts; const w = ((hw[bet?.horizon] ?? 100) / 100) * ((tw[th] ?? 100) / 100);
      return { id: x.bet_id, name: bet?.name ?? x.bet_id, horizon: bet?.horizon ?? "n/a", theme: th, stage: x.stage, base: x.usd_m as number, raw: on ? (x.usd_m as number) * w : 0, on, pts, pc: ev?.p_commercial, ttp: ev?.time_to_payoff_years }; });
    const sum = raw.reduce((a, r) => a + r.raw, 0); const tot = budget ?? base.total_usd_m ?? 0;
    return raw.map((r) => ({ ...r, usd: sum > 0 ? (r.raw / sum) * tot : 0 }));
  }, [base, bets, hw, tw, minPts, budget, pf]);
  if (!ports.length) return <><div className="eyebrow">View 10 · Investment Portfolio Simulator</div><h1>Portfolio simulator</h1><Absent kind="strategy" what="The simulator recomputes allocations from the portfolios and assumptions files; it has no numbers of its own." file="strategy/data/portfolios.json, assumptions.json" /></>;
  const bMin = totals.length ? Math.floor(Math.min(...totals) * 0.25) : 0; const bMax = totals.length ? Math.ceil(Math.max(...totals) * 1.5) : 0; const step = Math.max(1, Math.round((bMax - bMin) / 200));
  const B = budget ?? base.total_usd_m ?? 0; const ptsAll = rows.map((r) => r.pts).filter((v): v is number => typeof v === "number");
  const pMin = ptsAll.length ? Math.min(...ptsAll) : 0; const pMax = ptsAll.length ? Math.max(...ptsAll) : 1;
  const ttps = rows.map((r) => r.ttp).filter((v): v is number => typeof v === "number"); const cutMax = ttps.length ? Math.max(...ttps) : 0; const C = cut ?? cutMax;
  const sumBy = (key: "horizon" | "theme") => { const m: Record<string, number> = {}; rows.forEach((r) => { m[r[key]] = (m[r[key]] ?? 0) + r.usd; }); return m; };
  const rw = rows.reduce((a, r) => a + (r.pts != null ? r.usd * r.pts : 0), 0); const atRisk = rows.reduce((a, r) => a + (r.pts != null ? r.usd * (1 - r.pts) : 0), 0);
  const inH = rows.filter((r) => r.ttp == null || r.ttp <= C).reduce((a, r) => a + r.usd, 0);
  const maxUsd = Math.max(1, ...rows.map((r) => r.usd));
  const Slider = ({ label, v, set, min, max, unit }: { label: string; v: number; set: (n: number) => void; min: number; max: number; unit?: string }) => <label className="slider"><span>{label}</span><input type="range" min={min} max={max} step={max - min > 100 ? 1 : 0.01} value={v} onChange={(e) => set(+e.target.value)} /><b>{v}{unit}</b></label>;
  return (
    <>
      <div className="eyebrow">View 10 · Investment Portfolio Simulator</div>
      <h1>Capital allocation exploration</h1>
      <div className="notice sim" role="note"><b>Every number on this page is <Simulated />.</b> Budgets, allocations and probabilities come from the strategy team's explicit assumptions ({pf.portfolios.length} portfolios in <code>portfolios.json</code>). Takeda's actual budget is unknown. Sliders rescale those assumptions; they do not forecast.</div>
      <div className="toolbar"><div className="chips" role="group" aria-label="base portfolio">{ports.map((p) => <button key={p.name} className={`chip ${base.name === p.name ? "on" : ""}`} aria-pressed={base.name === p.name} onClick={() => { setName(p.name); setBudget(null); }}>{pretty(p.name)}</button>)}</div></div>
      <div className="sliders">
        <Slider label="Total budget (USD m)" v={B} set={setBudget} min={bMin} max={bMax} />
        <Slider label="H1 emphasis %" v={hw.H1} set={(n) => setHw({ ...hw, H1: n })} min={0} max={200} /><Slider label="H2 emphasis %" v={hw.H2} set={(n) => setHw({ ...hw, H2: n })} min={0} max={200} /><Slider label="H3 emphasis %" v={hw.H3} set={(n) => setHw({ ...hw, H3: n })} min={0} max={200} />
        {THEMES.map((t) => <Slider key={t} label={`${pretty(t)} %`} v={tw[t]} set={(n) => setTw({ ...tw, [t]: n })} min={0} max={200} />)}
        {ptsAll.length ? <Slider label="Min. probability of technical success" v={minPts} set={setMinPts} min={Math.floor(pMin * 100) / 100} max={pMax} /> : null}
        {ttps.length ? <Slider label="Payoff within (years)" v={C} set={setCut} min={0} max={cutMax} /> : null}
      </div>
      <p className="meta">Theme mapping is a display heuristic: external = partner/invest/acquire decisions; long-horizon = H3 bets; core = existing strength or underdeveloped baseline; adjacent = everything else. Allocations are renormalised to the chosen budget.</p>
      <dl className="kpis"><div><dt>total allocated <Simulated /></dt><dd>{fmtUsdM(rows.reduce((a, r) => a + r.usd, 0))}</dd></div><div><dt>probability-weighted capital <Simulated /></dt><dd>{ptsAll.length ? fmtUsdM(rw) : "n/a"}</dd></div><div><dt>capital at risk <Simulated /></dt><dd>{ptsAll.length ? fmtUsdM(atRisk) : "n/a"}</dd></div><div><dt>capital paying off within horizon <Simulated /></dt><dd>{ttps.length ? fmtUsdM(inH) : "n/a"}</dd></div></dl>
      <div className="grid g2">
        {(["horizon", "theme"] as const).map((k) => { const m = sumBy(k); return <div key={k} className="panel"><h3>By {k} <Simulated /></h3>{Object.entries(m).map(([n, v]) => <div key={n} className="hbar"><span>{pretty(n)}</span><div className="bar"><i style={{ width: `${(v / Math.max(1, B)) * 100}%` }} /></div><b>{fmtUsdM(v)}</b></div>)}
          {k === "horizon" && base.horizon_allocation_pct ? <p className="meta"><Assumption /> declared split: {Object.entries(base.horizon_allocation_pct).map(([h, p]) => `${h} ${p}%`).join(" · ")}</p> : null}
          {k === "theme" && base.theme_allocation_pct ? <p className="meta"><Assumption /> declared split: {Object.entries(base.theme_allocation_pct).map(([h, p]) => `${pretty(h)} ${p}%`).join(" · ")}</p> : null}</div>; })}
      </div>
      <h2 style={{ marginTop: 24 }}>Allocation by bet</h2>
      <Scroll><table><thead><tr><th>Bet</th><th>Horizon</th><th>Stage</th><th>Allocation <Simulated /></th><th style={{ textAlign: "right" }}>USD</th><th style={{ textAlign: "right" }}>P(technical) <Assumption /></th><th style={{ textAlign: "right" }}>P(commercial) <Assumption /></th><th style={{ textAlign: "right" }}>Years to payoff <Assumption /></th></tr></thead><tbody>
        {rows.map((r) => <tr key={r.id} className={r.on ? "" : "off"}><td><b>{r.id}</b> {r.name}{r.on ? "" : <span className="tag"> excluded by risk filter</span>}</td><td>{r.horizon}</td><td>{pretty(r.stage)}</td><td><div className="bar"><i style={{ width: `${(r.usd / maxUsd) * 100}%` }} /></div></td><td className="num">{fmtUsdM(r.usd)}</td><td className="num">{r.pts != null ? r.pts : "—"}</td><td className="num">{r.pc ?? "—"}</td><td className="num">{r.ttp ?? "—"}</td></tr>)}</tbody></table></Scroll>
      <AssumptionList ids={arr<string>(base.assumption_ids)} map={asm} />
      <h2 style={{ marginTop: 24 }}>Stage gates and capital at risk</h2>
      {!gates.length ? <Absent kind="strategy" what="Stage-gate criteria, capital at risk per stage, and stop/expand rules." file="strategy/data/stage_gates.json" /> : <Scroll><table><thead><tr><th>Bet</th><th>Stage</th><th style={{ textAlign: "right" }}>Capital at risk <Assumption /></th><th>Evidence required</th><th>Stop if</th><th>Expand if</th><th>Owner / authority</th></tr></thead><tbody>
        {gates.filter((g) => rows.some((r) => r.id === g.bet_id)).map((g, i) => <tr key={i}><td><b>{g.bet_id}</b></td><td>{pretty(g.stage)}</td><td className="num">{typeof g.capital_at_risk_usd_m === "number" ? fmtUsdM(g.capital_at_risk_usd_m) : "—"}</td><td>{g.evidence_required}</td><td>{g.stop_criteria}</td><td>{g.expand_criteria}</td><td>{g.owner_role} / {g.decision_authority}</td></tr>)}</tbody></table></Scroll>}
      {arr<any>(pf.evaluation).some((e) => e.strategic_differentiation) ? <p className="meta">Per-bet differentiation and execution-complexity notes are in the Strategy Lab and in <code>portfolios.json</code>.</p> : null}
      <p className="meta">Evidence behind any bet opens from <Ids ids={uniq(bets.flatMap((x) => arr<string>(x.claim_ids))).slice(0, 12)} open={open} label="sample claims" /></p>
    </>
  );
}

export function Roadmap({ b, open }: { b: Bundle; open: Open }) {
  const ms: any[] = arr(strat<{ milestones: any[] }>(b, "roadmap")?.milestones); const bets: any[] = arr(strat<{ bets: any[] }>(b, "strategy_bets")?.bets); const gates: any[] = arr(strat<{ gates: any[] }>(b, "stage_gates")?.gates);
  const asm = useAssumptions(b); const [sel, setSel] = useState<string | null>(null); const [wrap, w] = useWidth(900);
  const betName = (id: string) => bets.find((x) => x.id === id)?.name ?? id;
  const years = ms.map((m) => m.year).filter((y) => typeof y === "number") as number[];
  const y0 = years.length ? Math.min(...years) : 0; const y1 = years.length ? Math.max(Math.min(...years) + 13, ...years) : 0; const nY = y1 - y0 + 1;
  const lanesIds = uniq(ms.map((m) => m.bet_id)); const laneH = 44; const ml = 170; const iw = Math.max(560, w - ml - 20); const colW = iw / Math.max(1, nY);
  const px = (m: any) => ml + (m.year - y0 + (m.half === "H2" ? 0.75 : 0.25)) * colW; const py = (m: any) => 30 + lanesIds.indexOf(m.bet_id) * laneH + laneH / 2;
  const byId = new Map(ms.map((m) => [m.id, m])); const cur = ms.find((m) => m.id === sel);
  const TYPE_SHAPE: Record<string, string> = { gate: "◆", scale_decision: "◆", outcome: "★", foundation: "●", validation: "●", pilot: "●", partnership: "●" };
  const anchors = b.products.loe_events.filter((e) => e.company === "TAK");
  const items = anchors.map((e) => ({ lane: "TAK", t: yearFrac(e.date) ?? NaN, label: `${e.product}: ${e.event} (${e.date}, ${e.status})`, claim_ids: e.claims, color: COMPANY_COLORS.TAK, shape: e.status === "expected" ? ("diamond" as const) : ("dot" as const) })).filter((i) => !Number.isNaN(i.t));
  return (
    <>
      <div className="eyebrow">View 11 · Strategy Execution Roadmap</div>
      <h1>Milestones, gates and dependencies</h1>
      {!ms.length ? <Absent kind="strategy" what="The milestone Gantt, dependency arrows and stage gates appear when the roadmap file is produced." file="strategy/data/roadmap.json" /> : <>
        <p className="lede">One row per bet. Markers are placed by half-year; arrows point from a prerequisite milestone to the milestone that depends on it. Evidence-based milestones and assumption-based ones are marked differently.</p>
        <div className="legend" style={{ marginBottom: 8 }}><span>● foundation / validation / pilot / partnership</span><span>◆ gate or scale decision</span><span>★ outcome</span><span style={{ color: "#b3261e" }}>red outline = assumption-based</span><span style={{ color: "#0f6b3d" }}>green outline = evidence-based</span></div>
        <div ref={wrap} className="panel scroll" style={{ padding: 8 }}>
          <svg width={ml + iw + 20} height={lanesIds.length * laneH + 40} role="group" aria-label="roadmap">
            <defs><marker id="arr2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="#6b7384" /></marker></defs>
            {Array.from({ length: nY }, (_, i) => <g key={i}><line x1={ml + i * colW} x2={ml + i * colW} y1={20} y2={lanesIds.length * laneH + 34} stroke="#e4e7ee" /><text x={ml + i * colW + colW / 2} y={14} textAnchor="middle" fontSize={10} fill="#6b7384">{y0 + i}</text></g>)}
            {lanesIds.map((id) => { const mine = ms.filter((m) => m.bet_id === id); if (mine.length < 2) return null; const xs = mine.map(px); return <rect key={"bar" + id} className="gantt-bar" x={Math.min(...xs)} width={Math.max(...xs) - Math.min(...xs)} y={30 + lanesIds.indexOf(id) * laneH + laneH / 2 - 9} height={18} rx={9} />; })}
            {lanesIds.map((id, i) => <g key={id}><text x={0} y={30 + i * laneH + laneH / 2 + 4} fontSize={11} fontWeight={600} fill="#141a24">{id}</text><text x={0} y={30 + i * laneH + laneH / 2 + 17} fontSize={9} fill="#6b7384">{betName(id).slice(0, 26)}</text><line x1={ml} x2={ml + iw} y1={30 + i * laneH + laneH / 2} y2={30 + i * laneH + laneH / 2} stroke="#eceff4" /></g>)}
            {ms.flatMap((m) => arr<string>(m.depends_on).map((d) => { const a = byId.get(d); if (!a) return null; const x1 = px(a) + 7, y1 = py(a), x2 = px(m) - 8, y2 = py(m); const mx = (x1 + x2) / 2;
              return <path key={d + m.id} d={`M${x1},${y1} C${mx},${y1} ${mx},${y2} ${x2},${y2}`} fill="none" stroke="#8a93a5" strokeWidth={1.2} markerEnd="url(#arr2)"><title>{`${d} → ${m.id}`}</title></path>; }))}
            {ms.map((m) => <g key={m.id} tabIndex={0} role="button" aria-label={`${m.id} ${m.milestone}`} style={{ cursor: "pointer" }} onClick={() => setSel(m.id)} onKeyDown={(e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); setSel(m.id); } }}>
              <title>{`${m.id}: ${m.milestone} (${m.year} ${m.half})`}</title>
              <circle cx={px(m)} cy={py(m)} r={8} fill={sel === m.id ? "#C5000F" : "#fff"} stroke={m.basis === "evidence" ? "#0f6b3d" : "#b3261e"} strokeWidth={2} />
              <text x={px(m)} y={py(m) + 4} textAnchor="middle" fontSize={10} fill={sel === m.id ? "#fff" : "#141a24"}>{TYPE_SHAPE[m.type] ?? "●"}</text>
            </g>)}
          </svg>
        </div>
        {cur ? <div className="panel" aria-live="polite"><h3>{cur.id} · {betName(cur.bet_id)}</h3><p>{cur.milestone}</p><div><span className="tag">{cur.year} {cur.half}</span><span className="tag">{pretty(cur.type)}</span><span className={`tag ${cur.basis === "evidence" ? "FACT" : "HYPOTHESIS"}`}>{cur.basis}</span></div>
          {arr<string>(cur.depends_on).length ? <p className="meta">depends on: {arr<string>(cur.depends_on).map((d) => <button key={d} className="chip id" onClick={() => setSel(d)}>{d}</button>)}</p> : null}<Ids ids={arr(cur.claim_ids)} open={open} label="claims" /><AssumptionList ids={arr(cur.assumption_ids)} map={asm} />{gates.filter((g) => g.bet_id === cur.bet_id).length ? <><h4>Stage gates for {cur.bet_id}</h4><ul className="alist">{gates.filter((g) => g.bet_id === cur.bet_id).map((g, i) => <li key={i}><b>{pretty(g.stage)}</b> <Assumption /> capital at risk {typeof g.capital_at_risk_usd_m === "number" ? fmtUsdM(g.capital_at_risk_usd_m) : "n/a"}<div className="meta">stop if: {g.stop_criteria} · expand if: {g.expand_criteria}</div></li>)}</ul></> : null}</div> : <p className="meta">Select a milestone for its dependencies, claims and assumptions.</p>}
        <h2 style={{ marginTop: 24 }}>Gates</h2>
        {!gates.length ? <Absent kind="strategy" what="Gate definitions per stage." file="strategy/data/stage_gates.json" /> : <Scroll><table><thead><tr><th>Bet</th><th>Stage</th><th>Evidence required</th><th>Commercial milestone</th><th>Stop</th><th>Expand</th></tr></thead><tbody>{gates.map((g, i) => <tr key={i}><td><b>{g.bet_id}</b></td><td>{pretty(g.stage)}</td><td>{g.evidence_required}</td><td>{g.commercial_milestone}</td><td>{g.stop_criteria}</td><td>{g.expand_criteria}</td></tr>)}</tbody></table></Scroll>}
      </>}
      <h2 style={{ marginTop: 24 }}>Disclosed Takeda exclusivity anchors</h2>
      <p className="meta">Company-disclosed events from the registry (facts), shown independently of the strategy milestones.</p>
      {items.length ? <div className="panel"><Swim lanes={[{ key: "TAK", label: "Takeda", color: COMPANY_COLORS.TAK }]} items={items} open={open} /></div> : <Gap>No dated Takeda exclusivity events in the product dataset.</Gap>}
    </>
  );
}
