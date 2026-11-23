# How to open the MEDICINE 2040 hub

## Option 1: single file (no server)
Double-click `deliverables/MEDICINE_2040_Hub.html`. All data and code are inlined (about 7 MB); routing is hash-based, so it works from `file://`.

## Option 2: served app
```bash
cd ~/Desktop/MEDICINE
./launch.sh     # validate -> data -> build -> single file -> test -> serve
# open http://127.0.0.1:4173/
```
Binds to 127.0.0.1 only. Requires Node >= 18 and Python >= 3.9. Manual: `python3 scripts/build_app_data.py`, then in `executive_application/`: `npm install && npm run build && python3 ../scripts/build_single_file.py && npm test && npm run preview`.

## Layout
Top bar (all eleven pillars visible without scrolling at 1200 px and wider; below that the bar wraps to two rows): Overview, Companies, Commercial, R&D / Pipeline, Data · AI · Robotics, Partnerships, Policy, Takeda Baseline, Future Plan (red forward-looking banner on every page), Evidence & Method, Ask. Every Markdown report in the research tree opens in the reader (`#/read/<path>`); claim and source ID chips open the evidence drawer.

## Ask (grounded Q&A)
Default is retrieval-only: BM25 over claims, report sections and sources, answered with cited bullets, or "No evidence in the corpus". No model, no network.

Optional open-source LLM synthesis (toggle on the Ask page, off by default):
```bash
brew install ollama && ollama pull qwen2.5:3b && ollama serve
```
The page checks `http://127.0.0.1:11434/api/tags`. From the served app this works as is. If you opened the single file from `file://`, start Ollama with `OLLAMA_ORIGINS=* ollama serve`. Alternatively choose "OpenAI-compatible endpoint" and enter a base URL, model and key (stored only in this browser's localStorage). Only the question and the retrieved passages are sent; answers are labelled and their citations audited against the retrieved set.

### Notes on synthesis
- The prompt asks the model to answer part by part: what the passages support (with claim IDs) and `Not stated in the passages.` for parts they do not cover. Temperature is 0 and every cited claim ID is audited against the retrieved passages.
- A compound question whose whole text finds no evidence is split into its sub-questions; supported parts are answered and the rest are listed as not covered.
- From a served app (`http://127.0.0.1:4173`) Ollama needs no extra setting. From the single file (`file://`), the browser origin is `null`: start Ollama with `OLLAMA_ORIGINS=* ollama serve`.
- Command-line check without a browser: `cd executive_application && node tests/llm_probe.mjs "<question>"`.

## Deliverables
`deliverables/*.md` (executive summary, competitor comparison, Takeda strategy, investment roadmap, recommendations) open first in the Overview reading guide, in the Future Plan hub and in Evidence & Method.

Refresh after new research lands: `./launch.sh` (the pipeline fails loudly on any unknown claim, assumption or bet ID).
