# MEDICINE 2040

MEDICINE 2040 is a pharmaceutical market-intelligence and research package for exploring competitors, industry change and strategic options for Takeda. It combines an evidence-linked research library, an interactive web application, a standalone offline page and a narrated film.

The research covers Eli Lilly, Johnson & Johnson, AbbVie and Takeda's public baseline. The package describes a research cutoff of 21 November 2026; it is a snapshot, not a live source of market information. Forward-looking scenarios and investment envelopes are planning assumptions, not approved forecasts or budgets.

## What the system provides

- **Interactive intelligence hub:** company comparisons, commercial and market access, R&D and pipeline, data/AI/robotics, partnerships, policy, and Takeda's baseline.
- **Strategy views:** strategic bets, portfolios, scenarios, roadmaps, council reviews and counterarguments.
- **Evidence and reports:** searchable claims, source records, conflicts, coverage, research methodology and linked reports. Claim and source identifiers connect findings to supporting evidence.
- **Ask:** browser-based retrieval over the evidence base, with citations and a no-evidence response. Optional model-assisted synthesis is disabled by default.
- **Film:** a narrated TAKEDA 2040 presentation with subtitles, transcript and references.

## Quick start

### Standalone page

Open [index.html](index.html) directly in a modern browser. It contains the app and its data, so it does not require a server or an internet connection for normal offline use.

### Web application

Install Node.js 18 or newer and npm. On Windows, double-click [run_webapp.bat](web_app/run_webapp.bat); on macOS or Linux, run `./run_webapp.sh` from the `web_app` directory. The launcher installs dependencies if needed, builds the app if there is no build, and opens `http://127.0.0.1:4173/`.

Alternatively, from a terminal:

```sh
cd web_app
npm ci
npm run build
npm run preview
```

For development, run `npm run dev` from `web_app` and open the URL printed by Vite. The app reads the included JSON datasets in `web_app/public/data`; a data-generation step is not needed to run the packaged snapshot.

The generated `web_app/dist` directory and installed dependencies are excluded from Git. Rebuild with `npm run build` after changing the source or packaged datasets.

## Package layout

| Path | Contents |
| --- | --- |
| [index.html](index.html) | Standalone, self-contained intelligence hub. |
| [web_app/](web_app/) | React, TypeScript, Vite and D3 application, its packaged datasets and tests. |
| [Data/registries/](Data/registries/) | Source and claim registries, conflicts and schemas; the evidence system of record. |
| [Data/normalized/](Data/normalized/) | App-ready JSON views; copies are provided in `web_app/public/data`. |
| [Data/database/medicine.sqlite](Data/database/medicine.sqlite) | SQLite mirror for ad-hoc queries. |
| [Data/reports/](Data/reports/) | Research, competitor analyses, methodology, strategy and executive deliverables. |
| [Data/strategy/](Data/strategy/) | Strategy data and its data contract. |
| [Data/source_text/](Data/source_text/) | Extracted source text used for research verification. |
| [Data/pipeline/](Data/pipeline/) | Original Python data and evidence tools, retained for reference. |
| [Data/film/](Data/film/) | Film script, scenes, storyboard and evidence ledger. |
| [Final_video.mp4](Final_video.mp4) | Narrated film; see the accompanying [transcript](Final_video_transcript.md), [subtitles](Final_video_subtitles.srt) and [references](Final_video_references.md). |
| [quality/](quality/) | Packaged application test results. |

See the [data catalog](Data/README.md) for dataset details and identifiers.

## Data flow and limitations

The evidence registries and research reports are the source material for normalized JSON views and the SQLite mirror. The web app loads the packaged JSON files; the standalone page embeds its data. Claims distinguish facts from interpretations, hypotheses, scenarios and recommendations, and carry evidence status and source references.

The pipeline scripts under `Data/pipeline` were written for the original MEDICINE repository layout. The `data` and `launch` npm scripts also reference that original layout, so they are not turnkey regeneration commands for this packaged folder. Use the included data to run the application; rebuilding research datasets requires restoring or adapting the original pipeline inputs and paths.

## Testing

From `web_app`, run `npm run build` followed by `npm test`. The suite checks dataset integrity and references, built assets, routes and server-side rendering. **Package limitation:** the integrity test expects the standalone export to be named `MEDICINE_2040_Hub.html` in the original locations, while this package calls it `index.html`; that check reports a missing export unless the test or layout is adapted. Tests also write results to `quality/application_tests`.

## Optional model-assisted answers

Ask works in retrieval-only mode by default. Its settings can enable local Ollama or an OpenAI-compatible endpoint. Enabling synthesis sends the question and retrieved passages to the configured endpoint; an external endpoint therefore receives that content. Settings, including any API key entered, are stored in browser local storage when available. Use only endpoints and credentials approved for the data, and verify generated answers against the cited evidence.

## Provenance

The package records 524 sources and 1,401 claims at the research cutoff. Use the evidence status, source locators, limitations and contrary evidence when interpreting results. Consult [Data/README.md](Data/README.md), [PROJECT_STATE.md](Data/reports/PROJECT_STATE.md) and [PROJECT_MAP.md](Data/reports/PROJECT_MAP.md) for further context.
