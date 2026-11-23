// Manual probe (not part of npm test): runs the Ask page's retrieval + prompt against a local Ollama, non-streaming, temperature 0, and applies the citation audit.
// Usage: node tests/llm_probe.mjs "<question>" [more questions...]   (needs Ollama on 127.0.0.1:11434 with qwen2.5:3b)
import fs from "node:fs"; import path from "node:path"; import { fileURLToPath } from "node:url"; import { createServer } from "vite";
const app = path.join(path.dirname(fileURLToPath(import.meta.url)), ".."); const data = (n) => JSON.parse(fs.readFileSync(path.join(app, "public", "data", n), "utf8"));
const vite = await createServer({ root: app, server: { middlewareMode: true }, appType: "custom", logLevel: "error" });
const qa = await vite.ssrLoadModule("/src/qa.ts"); const llm = await vite.ssrLoadModule("/src/llm.ts");
const NAMES = { LLY: "Eli Lilly", JNJ: "Johnson & Johnson", ABBV: "AbbVie", TAK: "Takeda" };
const claims = data("claims.json"); const byId = new Map(claims.map((c) => [c.claim_id, c])); const ix = qa.buildIndex(data("qa_index.json").docs);
const model = process.env.MODEL ?? "qwen2.5:3b";
for (const question of process.argv.slice(2)) {
  const whole = qa.retrieve(ix, question); const partial = qa.retrievePartial(ix, question, whole); const res = partial ? partial.view : whole; if (partial) console.log("PARTIAL: supported", partial.supported, "| unsupported", JSON.stringify(partial.unsupported)); console.log("\n=== Q:", question, "\nanswerable:", res.answer.ok, res.answer.ok ? "" : "| " + res.answer.reason);
  if (!res.answer.ok) { console.log("(retrieval-only no-evidence state; the synthesis button is not offered)"); continue; }
  const cl = res.strong.filter((h) => h.doc.k === "claim").slice(0, 10).map((h) => byId.get(h.doc.id)).filter(Boolean);
  const rep = res.strong.filter((h) => h.doc.k === "report").slice(0, 5).map((h) => ({ id: h.doc.id, head: h.doc.h ?? "", text: h.doc.x }));
  const passages = llm.buildPassages(cl, rep, NAMES); const t0 = Date.now();
  const r = await fetch("http://127.0.0.1:11434/api/chat", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ model, messages: llm.buildMessages(question, passages, qa.splitParts(question)), stream: false, options: { temperature: 0 } }) });
  const out = (await r.json()).message?.content ?? ""; const allowed = new Set(passages.map((p) => p.id).concat(cl.map((c) => c.claim_id), passages.flatMap((p) => p.text.match(/CLM-\d{6}/g) ?? [])));
  console.log(`passages: ${passages.length} · ${((Date.now() - t0) / 1000).toFixed(1)}s\n--- answer ---\n${out}\n--- audit ---`, JSON.stringify(llm.auditCitations(out, allowed)));
}
await vite.close();
