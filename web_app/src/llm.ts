// Optional open-source LLM synthesis. Off by default. Only the question and the retrieved passages are ever sent.
// Provider "ollama": local Ollama (/api/chat, NDJSON stream). Provider "openai": any OpenAI-compatible endpoint (/chat/completions, SSE stream).
export type Provider = "ollama" | "openai";
export interface LlmSettings { enabled: boolean; provider: Provider; ollamaUrl: string; ollamaModel: string; openaiUrl: string; openaiModel: string; openaiKey: string }
export const DEFAULT_SETTINGS: LlmSettings = {
  enabled: false, provider: "ollama", ollamaUrl: "http://127.0.0.1:11434", ollamaModel: "qwen2.5:3b", openaiUrl: "https://api.groq.com/openai/v1", openaiModel: "", openaiKey: "",
};
const KEY = "medicine-llm-settings";
export function loadSettings(): LlmSettings {
  try { const raw = typeof localStorage !== "undefined" ? localStorage.getItem(KEY) : null; return raw ? { ...DEFAULT_SETTINGS, ...JSON.parse(raw) } : { ...DEFAULT_SETTINGS }; } catch { return { ...DEFAULT_SETTINGS }; }
}
export function saveSettings(s: LlmSettings) { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch { /* storage unavailable: settings last for this page view only */ } }

export const SETUP_HINT = "brew install ollama && ollama pull qwen2.5:3b && ollama serve";
export const NO_ANSWER = "The supplied evidence does not answer this question.";
export const SYSTEM_PROMPT = "You answer questions about the pharmaceutical industry using ONLY the numbered evidence passages supplied by the user. Use no outside knowledge and do not guess.\n" +
  "Step 1: decide how many separate things the question asks for. Only a question that asks for two or more different things (for example 'what is X and what is Y') has several parts. A question about one topic, such as 'how did X respond', is exactly ONE part: write only 'Part 1' and put the whole answer in it.\n" +
  "Step 2: write one line per part, in this exact form:\n" +
  "Part 1 (<the part, in a few words>): <answer using only what the passages state> [CLM-NNNNNN]\n" +
  "Every statement must end with the claim ID in square brackets of the passage that states it, copied exactly from the start of that passage (written [CLM-NNNNNN]). A statement without a claim ID is not allowed.\n" +
  "If the passages do not state the answer to a part, write: Part N (<the part>): Not stated in the passages.\n" +
  "Always answer the parts the passages support, even when another part is unsupported. Never discard a supported part because a different part is missing.\n" +
  "Cite only claim IDs that appear in the passages. Quote numbers exactly as written. Reply only with the sentence '" + NO_ANSWER + "' when no part of the question is supported. Keep the whole answer under 200 words.";

export interface Passage { n: number; id: string; label: string; text: string }
export function buildMessages(question: string, passages: Passage[], parts: string[] = []) {
  const ev = passages.map((p) => `${/^CLM-\d{6}$/.test(p.id) ? `[${p.id}]` : `(report passage ${p.n})`} ${p.label}: ${p.text}`).join("\n\n");
  return [{ role: "system", content: SYSTEM_PROMPT }, { role: "user", content: `Evidence passages:\n\n${ev}\n\nQuestion: ${question}\n\n${parts.length > 1 ? `The question has ${parts.length} parts, answer each one on its own line:\n${parts.map((x, i) => `Part ${i + 1}: ${x}`).join("\n")}\n\n` : ""}Answer part by part, using only the passages above, and cite claim IDs.` }];
}

/** Assemble the passages sent to the model: up to 8 claims, then up to 3 report sections. Shared by the Ask page and tests/llm_probe.mjs. */
export function buildPassages(claims: { claim_id: string; kind: string; companies: string[]; statement: string }[], reportHits: { id: string; head: string; text: string }[], names: Record<string, string>): Passage[] {
  const cs = claims.slice(0, 8);
  return [
    ...cs.map((c, i) => ({ n: i + 1, id: c.claim_id, label: `${c.kind} about ${c.companies.map((x) => names[x] ?? x).join(", ")}`, text: c.statement })),
    ...reportHits.slice(0, 3).map((h, i) => ({ n: cs.length + i + 1, id: h.id, label: `report section "${h.head}"`, text: h.text.slice(0, 700) })),
  ];
}

const trim = (u: string) => u.replace(/\/+$/, "");
export interface Status { state: "up" | "down" | "unconfigured"; detail: string; models?: string[] }

async function timed(url: string, init: RequestInit, ms: number): Promise<Response> {
  const ctl = new AbortController(); const t = setTimeout(() => ctl.abort(), ms);
  try { return await fetch(url, { ...init, signal: ctl.signal }); } finally { clearTimeout(t); }
}

export async function checkStatus(s: LlmSettings): Promise<Status> {
  try {
    if (s.provider === "ollama") {
      const r = await timed(`${trim(s.ollamaUrl)}/api/tags`, {}, 2500);
      if (!r.ok) return { state: "down", detail: `Ollama answered ${r.status}` };
      const j = await r.json(); const models: string[] = (j.models ?? []).map((m: any) => m.name);
      const has = models.some((m) => m === s.ollamaModel || (s.ollamaModel.indexOf(":") < 0 && m.startsWith(s.ollamaModel + ":")));
      return { state: "up", models, detail: has ? `Ollama running, model ${s.ollamaModel} available` : `Ollama running, but model ${s.ollamaModel} is not pulled (ollama pull ${s.ollamaModel})` };
    }
    if (!s.openaiUrl || !s.openaiModel) return { state: "unconfigured", detail: "Enter a base URL and a model name." };
    const r = await timed(`${trim(s.openaiUrl)}/models`, { headers: s.openaiKey ? { Authorization: `Bearer ${s.openaiKey}` } : {} }, 4000);
    return r.ok ? { state: "up", detail: "Endpoint reachable" } : { state: "down", detail: `Endpoint answered ${r.status}` };
  } catch (e) {
    return { state: "down", detail: s.provider === "ollama" ? "Ollama is not reachable. If the app is opened from a file, start it with OLLAMA_ORIGINS=* ollama serve." : "Endpoint not reachable (network or CORS)." };
  }
}

/** Streams tokens to onToken. Throws on transport errors so the caller can fall back to the retrieval-only answer. */
export async function synthesize(s: LlmSettings, question: string, passages: Passage[], onToken: (t: string) => void, signal: AbortSignal, parts: string[] = []): Promise<void> {
  const messages = buildMessages(question, passages, parts);
  if (s.provider === "ollama") {
    const r = await fetch(`${trim(s.ollamaUrl)}/api/chat`, { method: "POST", signal, headers: { "Content-Type": "application/json" }, body: JSON.stringify({ model: s.ollamaModel, messages, stream: true, options: { temperature: 0 } }) });
    if (!r.ok || !r.body) throw new Error(`Ollama answered ${r.status}`);
    await readLines(r.body, signal, (line) => { const j = JSON.parse(line); if (j.error) throw new Error(j.error); const t = j.message?.content; if (t) onToken(t); });
    return;
  }
  const r = await fetch(`${trim(s.openaiUrl)}/chat/completions`, { method: "POST", signal, headers: { "Content-Type": "application/json", ...(s.openaiKey ? { Authorization: `Bearer ${s.openaiKey}` } : {}) }, body: JSON.stringify({ model: s.openaiModel, messages, stream: true, temperature: 0 }) });
  if (!r.ok || !r.body) throw new Error(`Endpoint answered ${r.status}`);
  await readLines(r.body, signal, (line) => {
    if (!line.startsWith("data:")) return; const d = line.slice(5).trim(); if (!d || d === "[DONE]") return;
    const t = JSON.parse(d).choices?.[0]?.delta?.content; if (t) onToken(t);
  });
}

async function readLines(body: ReadableStream<Uint8Array>, signal: AbortSignal, onLine: (l: string) => void) {
  const reader = body.getReader(); const dec = new TextDecoder(); let buf = "";
  for (;;) {
    if (signal.aborted) { reader.cancel().catch(() => {}); return; }
    const { done, value } = await reader.read(); if (done) break;
    buf += dec.decode(value, { stream: true });
    let i: number; while ((i = buf.indexOf("\n")) >= 0) { const line = buf.slice(0, i).trim(); buf = buf.slice(i + 1); if (line) onLine(line); }
  }
  if (buf.trim()) onLine(buf.trim());
}

/** Keep only claim IDs that really were retrieved; anything else the model cites is flagged. */
export function auditCitations(answer: string, allowed: Set<string>): { cited: string[]; unknown: string[] } {
  const cited = Array.from(new Set(answer.match(/CLM-\d{6}/g) ?? [])); return { cited, unknown: cited.filter((c) => !allowed.has(c)) };
}
