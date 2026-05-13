# Disruption Cascade

An agentic research engine that takes a C-suite role and industry segment and produces a defensible investment thesis in ~120 minutes of agent execution.

**Methodology:** JTBD/ODI (Outcome-Driven Innovation) + 6-move workflow with evidence gates  
**What you get:** Go/Conditional Go/No-Go recommendation backed by job maps, scored outcomes, and cited sources

---

## Quick Start

**Requirements:** Claude Code (claude.ai/code or VS Code extension) with API access

1. Clone the repo and open Claude Code in the project folder:
   ```
   git clone <repo-url>
   cd disruption-cascade-plugin
   ```
2. Type `/run` in Claude Code
3. Answer 3 questions: role, industry, segment
4. The workflow runs automatically. You approve at Move 1 and Move 4.

That's it. A new run folder is created under `prototype/` with all outputs.

---

## How It Works

The workflow runs as a **coordinator + sub-agents** pattern. Claude Code orchestrates 6 sequential research moves, each executed by an independent agent with a fresh context window.

```
Move 1: Map Territory       → Jobs × Domains matrix, ODI-validated          (~25 min)
Move 2: Disruption Screen   → Hot territories (2+ High disruption ratings)   (~15 min)
Move 3: Temporal Filter     → In Progress windows (30-70% adoption)          (~10 min)
Move 4: Build Level         → Platform vs. point solution decision            (~25 min)
Move 5: Demand Validation   → ODI job maps, scored outcomes (1-10 scale)     (~30 min)
Move 6: Opportunity Analysis→ Investment thesis, GO/CONDITIONAL/NO-GO        (~20 min)
```

**Total:** ~120 minutes of agent execution = 3-6 weeks of human research equivalent

**Gates:** You approve Move 1 (job/domain map) and Move 4 (build level decision) before the workflow continues. Other moves have automatic evidence-quality gates.

---

## Inputs

- **C-suite role** — CFO, CRO, CTO, CHRO, CAE, CEO, etc.
- **Industry** — Manufacturing, Banking, Insurance, Healthcare, Financial Services, etc.
- **Segment** — e.g., "Mid-Market ($100M–$1B revenue)", "Enterprise ($1B+)", "Upper Mid-Market ($1B–$10B assets)"

The workflow is blank-slate — it starts from fresh web research every time. No prior knowledge leaks in.

---

## Outputs

Each run produces a folder under `prototype/` containing:

| File | What it is |
|------|-----------|
| `executive_summary.md` | 1-page key findings + thesis score + recommendation |
| `move1_territory_map.md` | Validated job-domain matrix |
| `move2_disruption_screen.md` | Hot territories with evidence |
| `move3_temporal_filter.md` | Disruption stage assessments |
| `move4_build_level.md` | Build level recommendation |
| `move5_demand_validation.md` | ODI job maps + scored outcomes |
| `move6_opportunity_analysis.md` | Full investment thesis |
| `audit_trail.md` | Consolidated sources, ratings, validation log |
| `move{N}_output.json` | Structured handoff files between moves |

---

## File Structure

```
disruption-cascade-plugin/
├── README.md                   ← This file
├── CLAUDE.md                   ← System context for Claude Code
├── .claude/
│   ├── commands/
│   │   └── run.md              ← /run command (entry point)
│   ├── rules/
│   │   └── odi-*.md (9 files)  ← ODI/JTBD methodology (authoritative, don't modify)
│   └── agents/
│       ├── cascade-researcher.md
│       ├── cascade-writer.md
│       ├── cascade-validator.md
│       └── cascade-synthesizer.md
└── prototype/
    └── _template/              ← Blueprint for each run (do not edit directly)
        ├── workflow-plan.md
        ├── move1–6_*.md
        ├── executive_summary.md
        ├── audit_trail.md
        └── rules/              ← Per-run workflow rules
```

---

## Methodology

The workflow is built on **Outcome-Driven Innovation (ODI)** as developed by Tony Ulwick / Strategyn. Key principles:

- Jobs are stable end-states, not activities (they don't change with technology)
- Outcome statements measure what executors want to be true, not what they do
- Scores are hypothesized from web evidence (in production, replace with client survey data)
- All scores use a 1-10 scale; opportunity = Importance + max(Importance − Satisfaction, 0)

The 9 ODI rule files in `.claude/rules/` are the authoritative methodology reference. They take precedence over any other guidance in the workflow.

---

## Tips

- **Run it fresh.** The context firewall prevents project-specific knowledge from contaminating results. This is a feature — it means every run is independently defensible.
- **Trust the gates.** When you approve Move 1 and Move 4, you're making strategic decisions. Review the job map carefully at Move 1 — everything downstream follows from it.
- **Prototype vs. production.** Move 5 uses web evidence as a proxy for client interviews. In production use, replace web evidence with ODI survey data from 8+ interviews with each executor type.
- **Model selection matters.** The researcher and validator agents run on Sonnet; writer and synthesizer run on Opus. This is intentional — Opus produces better structured documents.
