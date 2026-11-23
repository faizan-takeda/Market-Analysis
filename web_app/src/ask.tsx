// Ask: grounded Q&A. Retrieval-only by default (BM25 over claims, report sections and sources). Optional open-source LLM synthesis.
import { useEffect, useMemo, useRef, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { Bundle, Claim, COMPANY_NAMES } from "./data";
import { Badges, CoTag, Ids, Open, SourceLink } from "./components";
import { buildIndex, retrieve, retrievePartial, Retrieval, splitParts } from "./qa";
import { auditCitations, buildPassages, checkStatus, DEFAULT_SETTINGS, loadSettings, LlmSettings, Passage, saveSettings, SETUP_HINT, Status, synthesize } from "./llm";
import { readPath } from "./reader";
import { slugify } from "./markdown";
import { Hero } from "./pages";

function CiteText({ text, open }: { text: string; open: Open }) {
  const parts = text.split(/(CLM-\d{6})/g);
  return <>{parts.map((p, i) => (/^CLM-\d{6}$/.test(p) ? <button key={i} className="idchip" onClick={() => open(p)}>{p.slice(4)}</button> : <span key={i}>{p}</span>))}</>;
}

function ClaimBullet({ c, b, open }: { c: Claim; b: Bundle; open: Open }) {
  const s = c.supporting_sources[0];
  return (
    <li className="abullet">
      <div className="cline-head">{c.companies.map((co) => <CoTag key={co} co={co} />)}<span className={`tag ${c.kind}`}>{c.kind}</span><span className={`tag ${c.status}`}>{c.status.replace(/_/g, " ").toLowerCase()}</span><Badges c={c} /></div>
      <p>{c.statement}</p>
      <div className="meta"><Ids ids={[c.claim_id]} open={open} />{s ? <SourceLink s={b.sourceById.get(s.source_id)} locator={s.locator} /> : null}</div>
    </li>
  );
}

export function Ask({ b, open }: { b: Bundle; open: Open }) {
  const [sp, setSp] = useSearchParams();
  const ix = useMemo(() => buildIndex(b.qa.docs), [b]);
  const [q, setQ] = useState(sp.get("q") ?? ""); const [asked, setAsked] = useState(sp.get("q") ?? "");
  const whole: Retrieval | null = useMemo(() => (asked.trim() ? retrieve(ix, asked) : null), [ix, asked]);
  const partial = useMemo(() => (whole ? retrievePartial(ix, asked, whole) : null), [ix, asked, whole]);
  const res: Retrieval | null = partial ? partial.view : whole;
  const [cfg, setCfg] = useState<LlmSettings>(() => loadSettings()); const [status, setStatus] = useState<Status | null>(null);
  const [out, setOut] = useState(""); const [busy, setBusy] = useState(false); const [err, setErr] = useState(""); const ctl = useRef<AbortController | null>(null);
  const golden = useMemo(() => {
    const r = b.reportByPath.get("quality/evaluation_results/golden_questions_wave1.md");
    return r ? Array.from(r.markdown.matchAll(/^##\s+Q\d+\.\s+(.+)$/gm)).map((m) => m[1].trim()) : [];
  }, [b]);
  useEffect(() => { const v = sp.get("q"); if (v && v !== asked) { setQ(v); setAsked(v); } }, [sp]); // eslint-disable-line
  useEffect(() => { saveSettings(cfg); }, [cfg]);
  useEffect(() => { if (!cfg.enabled) { setStatus(null); return; } let live = true; checkStatus(cfg).then((s) => { if (live) setStatus(s); }); return () => { live = false; }; }, [cfg.enabled, cfg.provider, cfg.ollamaUrl, cfg.openaiUrl, cfg.openaiModel, cfg.ollamaModel]);

  const ask = (text: string) => { setAsked(text); setQ(text); setOut(""); setErr(""); setSp(text ? { q: text } : {}); };
  const claimHits = res ? res.strong.filter((h) => h.doc.k === "claim").slice(0, 10) : [];
  const reportHits = res ? res.strong.filter((h) => h.doc.k === "report").slice(0, 5) : [];
  const claims = claimHits.map((h) => b.claimById.get(h.doc.id)).filter(Boolean) as Claim[];
  const byCo = new Map<string, Claim[]>(); claims.forEach((c) => { const k = c.companies[0]; byCo.set(k, [...(byCo.get(k) ?? []), c]); });
  const sourceHits = res ? res.hits.filter((h) => h.doc.k === "source" && h.coverage >= 0.5).slice(0, 3) : [];
  const contrary = claims.filter((c) => c.contrary_evidence && c.contrary_evidence.length).length; const nonFact = claims.filter((c) => c.kind !== "FACT").length;

  const passages: Passage[] = buildPassages(claims, reportHits.map((h) => ({ id: h.doc.id, head: h.doc.h ?? "", text: h.doc.x })), COMPANY_NAMES);
  const run = async () => {
    if (!res?.answer.ok || !passages.length) return;
    ctl.current?.abort(); const c = new AbortController(); ctl.current = c; setBusy(true); setOut(""); setErr("");
    try { await synthesize(cfg, asked, passages, (t) => setOut((o) => o + t), c.signal, splitParts(asked)); } catch (e: any) { if (!c.signal.aborted) setErr(`${e?.message ?? e}. Showing the retrieval-only answer above.`); } finally { setBusy(false); }
  };
  const allowed = new Set(passages.map((p) => p.id).concat(claims.map((c) => c.claim_id), passages.flatMap((p) => p.text.match(/CLM-\d{6}/g) ?? [])));
  const audit = out ? auditCitations(out, allowed) : null;
  const upd = (p: Partial<LlmSettings>) => setCfg({ ...cfg, ...p });

  return (
    <>
      <Hero eyebrow="Ask" title="Ask the evidence base" lede="Answers are composed only from claims, report sections and sources in this encyclopedia, each with its citation. If the evidence does not cover the question, the answer says so." />
      <form className="askbar" onSubmit={(e) => { e.preventDefault(); ask(q); }} role="search">
        <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="e.g. How did AbbVie respond to the loss of Humira exclusivity?" aria-label="question" />
        <button className="btn primary" type="submit">Ask</button>
      </form>
      {golden.length ? <div className="suggest"><span className="meta">Try:</span>{golden.filter((g) => !/^NEGATIVE/i.test(g)).slice(0, 6).map((g) => <button key={g} className="chip" onClick={() => ask(g)}>{g.length > 90 ? g.slice(0, 88) + "…" : g}</button>)}</div> : null}

      <details className="llm" open={cfg.enabled}>
        <summary><label><input type="checkbox" checked={cfg.enabled} onChange={(e) => upd({ enabled: e.target.checked })} /> Synthesize with an open-source LLM <span className="meta">(optional, off by default)</span></label>
          {cfg.enabled && status ? <span className={`pill ${status.state}`}>{status.state === "up" ? "ready" : status.state === "down" ? "unreachable" : "not configured"}</span> : null}</summary>
        <div className="llm-body">
          <div className="toolbar">
            <label className="sel">provider<select value={cfg.provider} onChange={(e) => upd({ provider: e.target.value as any })}><option value="ollama">Local Ollama</option><option value="openai">OpenAI-compatible endpoint</option></select></label>
            {cfg.provider === "ollama" ? <>
              <label className="sel">Ollama URL<input value={cfg.ollamaUrl} onChange={(e) => upd({ ollamaUrl: e.target.value })} /></label>
              <label className="sel">model<input value={cfg.ollamaModel} onChange={(e) => upd({ ollamaModel: e.target.value })} /></label></> : <>
              <label className="sel">base URL<input value={cfg.openaiUrl} onChange={(e) => upd({ openaiUrl: e.target.value })} /></label>
              <label className="sel">model<input value={cfg.openaiModel} onChange={(e) => upd({ openaiModel: e.target.value })} /></label>
              <label className="sel">API key (kept in this browser only)<input type="password" value={cfg.openaiKey} onChange={(e) => upd({ openaiKey: e.target.value })} autoComplete="off" /></label></>}
          </div>
          {status ? <p className="meta">{status.detail}</p> : null}
          {cfg.provider === "ollama" && status?.state !== "up" ? <p className="meta">Set up once: <code>{SETUP_HINT}</code>. Without it, the retrieval-only answer below is used.</p> : null}
          <p className="meta">Only your question and the retrieved passages are sent. Nothing else leaves this page. <button className="linkbtn" onClick={() => setCfg({ ...DEFAULT_SETTINGS })}>Reset settings</button></p>
        </div>
      </details>

      {res && !res.answer.ok ? (
        <section className="noevidence" role="status">
          <h2>No evidence in the corpus</h2>
          <p>{res.answer.reason}</p>
          <p>The question may be about something the research has not reached. Try fewer or different terms, or <Link to="/encyclopedia">browse the encyclopedia</Link>. The coverage ledger lists known gaps: <Link to="/coverage">coverage</Link>.</p>
          {res.hits.length ? <details><summary>Closest records (context only, they do not answer the question)</summary><ul>{res.hits.slice(0, 5).map((h) => <li key={h.doc.id}><span className="tag">{h.doc.k}</span> {h.doc.k === "report" ? <Link to={`${readPath(h.doc.path ?? "")}?h=${slugify(h.doc.h ?? "")}`}>{h.doc.h}</Link> : <button className="linkbtn" onClick={() => open(h.doc.id)}>{h.doc.id}</button>} <span className="meta">{h.doc.x.slice(0, 160)}</span></li>)}</ul></details> : null}
        </section>
      ) : null}

      {res?.answer.ok ? (
        <section className="answer" aria-live="polite">
          {partial ? <div className="notice gap" role="note"><b>Partly covered.</b> The evidence base answers {partial.supported.length} of {partial.supported.length + partial.unsupported.length} parts of this question. Not covered: {partial.unsupported.map((u) => <span key={u.part}>“{u.part}” ({u.reason}) </span>)}</div> : null}
          <div className="answer-head"><h2>Grounded answer</h2><span className="tag">retrieval only · no model</span></div>
          <p className="meta">{claims.length} supporting claim{claims.length === 1 ? "" : "s"}, {reportHits.length} report section{reportHits.length === 1 ? "" : "s"} matched. Statements below are the registry's own wording.</p>
          {Array.from(byCo.entries()).map(([co, cs]) => <div key={co}><h3>{COMPANY_NAMES[co] ?? co}</h3><ul className="alist2">{cs.map((c) => <ClaimBullet key={c.claim_id} c={c} b={b} open={open} />)}</ul></div>)}
          {reportHits.length ? <><h3>From the reports</h3><ul className="alist2">{reportHits.map((h) => <li key={h.doc.id} className="abullet"><Link to={`${readPath(h.doc.path ?? "")}?h=${slugify(h.doc.h ?? "")}`}><b>{h.doc.h}</b></Link> <span className="meta">{h.doc.path}</span><p className="clamp">{h.doc.x.slice(0, 420)}</p><Ids ids={h.doc.ids ?? []} open={open} /></li>)}</ul></> : null}
          {sourceHits.length ? <><h3>Sources</h3><p>{sourceHits.map((h) => <button key={h.doc.id} className="idchip" onClick={() => open(h.doc.id)} title={h.doc.t}>{h.doc.id}</button>)}</p></> : null}
          <div className="notice gap"><b>What the evidence base does not say.</b>{" "}
            {claims.length < 3 ? "Fewer than three claims match strongly, so this answer is thin. " : ""}
            {nonFact ? `${nonFact} of the claims shown are interpretations, hypotheses or scenarios rather than facts. ` : ""}
            {contrary ? `${contrary} carry recorded contrary evidence; open the chip to read it. ` : ""}
            Absence from this list is not evidence of absence: see the <Link to="/coverage">coverage ledger</Link> for what was never read.</div>
          {cfg.enabled ? (
            <div className="synth">
              <button className="btn primary" onClick={run} disabled={busy || status?.state === "down" || status?.state === "unconfigured"}>{busy ? "Synthesizing…" : "Synthesize from these passages"}</button>
              {busy ? <button className="btn" onClick={() => ctl.current?.abort()}>Stop</button> : null}
              {status?.state === "down" ? <span className="meta"> The model is not reachable; the retrieval-only answer above stands.</span> : null}
              {err ? <p className="notice">{err}</p> : null}
              {out ? <div className="llmout"><span className="tag SCENARIO">LLM synthesis · {cfg.provider === "ollama" ? cfg.ollamaModel : cfg.openaiModel} · verify against the cited claims</span>
                <p><CiteText text={out} open={open} /></p>
                {audit && audit.unknown.length ? <p className="notice">The model cited ids that were not in the retrieved evidence: {audit.unknown.join(", ")}. Disregard those citations.</p> : null}
                {audit && !audit.cited.length && !busy ? <p className="notice">The answer cites no claim ids. Treat it as unverified.</p> : null}
                <details><summary>Passages sent to the model</summary><ol>{passages.map((p) => <li key={p.id}><b>{p.id}</b> {p.text.slice(0, 220)}</li>)}</ol></details></div> : null}
            </div>
          ) : null}
        </section>
      ) : null}
    </>
  );
}
