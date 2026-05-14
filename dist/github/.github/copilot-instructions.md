# CLAUDE.md

**Disruption Cascade** — Agentic research engine for JTBD-based investment thesis development.

## What This Is

A standalone prototyping workspace for running the Disruption Cascade v4 workflow. Each run takes a C-suite role + industry + segment and produces a defensible investment thesis through 6 sequential moves: territory mapping, disruption screening, temporal filtering, build level determination, demand-side validation, and opportunity analysis.

This workspace is intentionally isolated from any other project context. The workflow's value comes from producing valid results from scratch — external project knowledge would contaminate the validation.

## How It Works

Each run uses a **coordinator + sub-agent** pattern:
- The coordinator (main conversation) plans, delegates, checks gates, and requests user approval
- Sub-agents execute each move independently with fresh context windows
- A context firewall prevents external knowledge from leaking into results
- JSON handoff files pass structured data between moves
- Each sub-agent runs recursive self-validation before producing output
- A consolidated audit trail tracks sources, ratings, and decisions across all moves

Use `/run` to start a new run.

## Key Constraints

- **Context firewall** — Sub-agents must not reference external project artifacts, memory files, or project-specific conclusions. All claims must trace to fresh web research.
- **ODI methodology** — `.claude/rules/odi-*.md` files are authoritative. Outcomes use "Minimize time..." / "Minimize likelihood..." format only.
- **Framework separation** — Three axes (ODI/JTBD, APQC PCF, subject matter classification) must never be conflated into a single hierarchy.
- **Evidence at every step** — No unsourced assertions. H/M/L ratings cite evidence. Scores cite data points.
- **Confidence scoring** — Every H/M/L rating and 1-10 score includes a confidence level (High/Medium/Low).
- **JSON handoff** — Structured JSON files are the authoritative data transfer between moves, not markdown.
- **Self-validation** — Each sub-agent runs a recursive validation loop against applicable rules before producing output.

## Available Commands

| Command | Purpose |
|---------|---------|
| `/run` | Start a new Disruption Cascade v4 run |

## Key Rules

| Rule File | Scope |
|-----------|-------|
| `odi-job-validation.md` | 4-test job validation (universality, mutual exclusivity, data support, ends-vs-means) |
| `odi-core-job-statements.md` | Job statement format, boundary rules, goal framing |
| `odi-ends-vs-means.md` | Ends-vs-means test for candidate job sets |
| `odi-abstraction-level.md` | Client-level mapping |
| `odi-job-map-structure.md` | 8-step map structure, cross-cutting capabilities |
| `odi-outcome-statements.md` | Outcome format and MECE rules |
| `odi-executor-discipline.md` | One executor per map, emotional/social jobs |
| `odi-scoring.md` | 1-10 scale, hypothesis labeling, variance checks |
| `odi-checklist.md` | Full pre-submission checklist |

## File Structure

```
disruption-cascade-plugin/
├── CLAUDE.md                      # This file
├── README.md                      # Quick start and workflow overview
├── .claude/
│   ├── commands/
│   │   └── run.md                 # /run command — initializes new runs
│   ├── rules/
│   │   └── odi-*.md               # ODI/JTBD methodology rules (authoritative)
│   └── agents/
│       ├── cascade-researcher.md  # Web research agent
│       ├── cascade-writer.md      # Document synthesis agent
│       ├── cascade-validator.md   # Rule compliance validator
│       └── cascade-synthesizer.md # Executive summary assembler
└── prototype/
    └── _template/                 # Run template (copied for each new run)
        ├── README.md
        ├── workflow-plan.md
        ├── executive_summary.md
        ├── audit_trail.md
        ├── move1-6_*.md
        └── rules/
            ├── agent-architecture.md
            ├── context-firewall.md
            ├── disruption-cascade-rules.md
            ├── json-handoff-schema.md
            └── recursive-validation.md
```

## Out of Scope

- Client-specific discovery research (SME interviews, primary data collection)
- Solution design or implementation planning
- Sharing confidential client details in outputs
