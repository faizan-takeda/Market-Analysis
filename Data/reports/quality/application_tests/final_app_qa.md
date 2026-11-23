# Final application QA (A13, wave 5)

Date: 2026-11-21. Build order: data pipeline -> `npm run build` -> `build_single_file.py` -> `npm test`.

## Automated
- `npm run build` (tsc + vite): clean. `npm test`: data integrity 109/109, route render smoke 145/145 (includes a strategy fixture, sub-question split and per-part prompt checks). A harmless esbuild "all goroutines are asleep" message can print at process exit; exit code is 0.
- Single file `deliverables/MEDICINE_2040_Hub.html` is rebuilt after the bundle; test "single file data equals public/data" passes.

## Navigation (screenshots, headless Chrome)
| Width | Result | File |
|---|---|---|
| 1024 | pillars wrap to two rows, no horizontal scroll, search kept | `screenshots/nav_1024.png` |
| 1280 | all eleven pillars in one row, search kept | `screenshots/nav_1280.png` |
| 1440 | all eleven pillars in one row | `screenshots/nav_1440.png` |

## file:// load of the single file (1440 px)
`screenshots/file_strategy.png`, `file_portfolio.png`, `file_roadmap.png` (Gantt 2027-2040, dependency arrows, evidence/assumption outlines), `file_uncertainty.png`, `file_future.png`.

## Strategy views on real files
Bets explorer (17 bets, decision badges, prerequisite graph), portfolio simulator (3 portfolios, 33 assumptions, SIMULATED/ASSUMPTION labels, 67 gates), roadmap (50 milestones), scenario x bet matrix (5 scenarios, 17 bets). `council_reviews.json` and `counterarguments.json` did not exist during this run: the council matrix and counterarguments show the explicit notice (rendering verified only against the test fixture).

## Ask / Ollama (qwen2.5:3b, temperature 0)
Log: `llm_probe_output.txt`. Golden Q6 (Takeda LOE and replacement plan) answered per part with audited citations; ecosystem question answered with audited citations; negative question (TuneLab revenue) returns "Not stated in the passages"; compound question with one unsupported part returns Part 1 supported with a claim ID and Part 2 "Not stated".
Fixes: per-part prompt; sub-question retrieval fallback; generic words (evidence, support, number) no longer block retrieval; audit counts claim IDs inside supplied passage text.

## Not tested
Browser-side streaming from `file://` against Ollama (needs `OLLAMA_ORIGINS=*`); the probe uses the same prompt non-streamed. Screenshots of the 3-model-free Ask page UI.
