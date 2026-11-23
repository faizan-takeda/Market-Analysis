# Research dependency graph

Rendered interactively in the application (View: Methodology). Persisted here as Mermaid.

```mermaid
flowchart TD
    A["Research Mission"] --> B["Research Protocol & Architecture (Gate 0)"]
    B --> C["Build Encyclopedia & Evidence Schema"]
    C --> D["Research Question Decomposition"]
    D --> E1["Eli Lilly Research (A1)"]
    D --> E2["J&J Research (A2)"]
    D --> E3["AbbVie Research (A3)"]
    D --> E4["Cross-Company AI/Data/Robotics (A6)"]
    D --> E5["Policy (A8) & Financial (A4 EDGAR)"]
    D --> E6["Takeda Public Baseline (A5)"]
    E1 --> F["Source & Claims Registry (single-writer merge)"]
    E2 --> F
    E3 --> F
    E4 --> F
    E5 --> F
    E6 --> F
    F --> G["Independent Evidence Audit (A10)"]
    G --> H{"Evidence sufficient?"}
    H -->|No| I["Gap Analysis & Revised Queries"]
    I --> D
    H -->|Yes| J["Company Dossiers & Knowledge Graph (Gate 1)"]
    J --> K["Cross-Company Comparative Analysis"]
    K --> L["Takeda Baseline accepted (Gate 2)"]
    L --> M["Strategic Futures & Investment Council (A11)"]
    M --> N["Independent Challenge, Red Team & Scenario Tests"]
    N --> O{"Decision-grade?"}
    O -->|No| P["Targeted Research & Model Revision"]
    P --> M
    O -->|Yes| Q["Interactive Executive Application (A13) (Gate 3 inputs only)"]
    Q --> R["Automated & Manual QA"]
    R --> S{"All acceptance gates pass?"}
    S -->|No| T["Correct Defects & Revalidate"]
    T --> R
    S -->|Yes| U["Final Encyclopedia & Strategic Deliverables"]
```

Node status is tracked in `PROJECT_STATE.md` and `.kiro/specs/medicine-2040/tasks.md`.
