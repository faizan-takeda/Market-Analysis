import React, { useCallback, useState } from "react";
import ReactDOM from "react-dom/client";
import { HashRouter, Link, NavLink, useLocation, useNavigate } from "react-router-dom";
import "./styles.css";
import { useBundle } from "./data";
import { EvidenceDrawer } from "./components";
import { Body } from "./routes";
import { PILLARS, pillarOf } from "./pillars";

function Shell({ b, open }: { b: NonNullable<ReturnType<typeof useBundle>["bundle"]>; open: (id: string) => void }) {
  const loc = useLocation(); const nav = useNavigate(); const pl = pillarOf(loc.pathname);
  const [q, setQ] = useState("");
  const items = pl.items.length > 1 ? pl.items : [];
  return (
    <>
      <a className="skip" href="#main" onClick={(e) => { e.preventDefault(); document.getElementById("main")?.focus(); }}>Skip to content</a>
      <header className="topbar">
        <div className="topbar-in">
          <Link to="/" className="brand"><span className="mark" aria-hidden="true" />MEDICINE<small>2040 · Pharma intelligence for Takeda</small></Link>
          <nav className="pillars" aria-label="Sections">
            {PILLARS.map((p) => <NavLink key={p.id} to={p.path} className={() => `pillar ${pl.id === p.id ? "active" : ""} ${p.forward ? "fwd" : ""}`} aria-current={pl.id === p.id ? "page" : undefined}>{p.label}</NavLink>)}
          </nav>
          <form className="gsearch" role="search" onSubmit={(e) => { e.preventDefault(); if (q.trim()) { nav(`/encyclopedia?q=${encodeURIComponent(q.trim())}`); setQ(""); } }}>
            <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search claims and sources" aria-label="Search the encyclopedia" />
          </form>
        </div>
      </header>
      <div className={`shell ${items.length ? "with-sub" : ""}`}>
        {items.length ? (
          <aside className="subnav" aria-label={`${pl.label} pages`}>
            <div className="subnav-h">{pl.label}</div>
            <ul>{items.map((i) => <li key={i.path}><NavLink to={i.path} end className={({ isActive }) => (isActive ? "active" : "")}>{i.label}{i.note ? <small>{i.note}</small> : null}</NavLink></li>)}</ul>
            <div className="state">{b.state.sources} sources · {b.state.claims} claims<br />{b.reports.count} reports<br />built {b.state.built_at.slice(0, 16).replace("T", " ")} UTC</div>
          </aside>
        ) : null}
        <Body b={b} open={open} />
      </div>
    </>
  );
}

function App() {
  const { bundle: b, error } = useBundle();
  const [openId, setOpen] = useState<string | null>(null);
  const close = useCallback(() => setOpen(null), []);
  if (error) return <main><h1>Data not available</h1><p className="notice">{error}</p><p>Run <code>python3 scripts/build_app_data.py</code> from the MEDICINE root, then rebuild.</p></main>;
  if (!b) return <main><p className="meta">Loading the encyclopedia…</p></main>;
  return (
    <>
      <Shell b={b} open={setOpen} />
      <EvidenceDrawer id={openId} b={b} onClose={close} onOpen={setOpen} />
    </>
  );
}

ReactDOM.createRoot(document.getElementById("root")!).render(<React.StrictMode><HashRouter><App /></HashRouter></React.StrictMode>);
