# Disruption Cascade

A Claude Code plugin that takes a C-suite role and industry segment and produces a defensible investment thesis — Go, Conditional Go, or No-Go — in a single command.

```bash
/run CFO Manufacturing "Mid-Market ($100M–$1B revenue)"
```

---

## The Problem It Solves

Strategy and investment decisions get made on incomplete research. Opportunity assessments are assembled from disconnected sources, the methodology isn't rigorous enough to defend, and the conclusions don't connect back to what the target buyer actually needs to accomplish. The result is a thesis that sounds plausible but won't hold up in a room.

This plugin runs a structured 6-move research workflow — territory mapping, disruption scoring, timing analysis, build/buy assessment, demand validation, and opportunity scoring — as an agentic chain with evidence gates at each step. Every claim traces to a source. The output is a recommendation you can defend.

---

## How It Works

Six moves run in sequence as a **coordinator + sub-agent** pattern. Each move is executed by an independent agent with a fresh context window — no contamination between moves.

| Move | What It Does | Key Output |
|------|-------------|-----------|
| **1. Territory Map** | ODI-validated job × domain matrix | Jobs × Domains grid + executor definition |
| **2. Disruption Screen** | Scores each territory for disruption potential | Hot territories (2+ High ratings) |
| **3. Temporal Filter** | Identifies timing windows | In-progress zones (30–70% adoption) |
| **4. Build Level** | Platform vs. point solution decision | Build recommendation with rationale |
| **5. Demand Validation** | ODI job maps with scored outcomes | Job map + outcome scores (1–10) |
| **6. Opportunity Analysis** | Full thesis synthesis | Thesis score + Go/Conditional Go/No-Go |

**Gates:** You approve at Move 1 (job/domain map) and Move 4 (build level) before the workflow continues. All other moves have automatic evidence-quality gates.

---

## Installation

**Requirements:** [Claude Code](https://claude.ai/code)

1. **[Download ZIP](https://github.com/willmcdermott-crowe/disruption-cascade-plugin/archive/refs/heads/main.zip)**
2. Unzip the downloaded file
3. Open Claude Code in the `disruption-cascade-plugin-main/` folder
4. Type `/run` to start

No configuration required. Run outputs save into `prototype/` inside the folder.

---

### Other CLIs

For CLI-specific installs, copy from the `dist/` folder after downloading and unzipping:

### OpenCode

```bash
cp -r dist/opencode/. your-project/
```

### GitHub Copilot

```bash
cp -r dist/github/.github your-project/
```

### Gemini CLI

```bash
cp -r dist/gemini/.gemini your-project/
```

### Codex CLI

```bash
cp -r dist/codex/.agents your-project/
mkdir -p your-project/.codex
cp -r dist/codex/.codex/agents your-project/.codex/
```

### Trae

```bash
cp -r dist/trae/.trae/skills/* ~/.trae/skills/
```

### Rovo Dev

```bash
# Project-specific
cp -r dist/rovo-dev/.rovodev your-project/

# Or global
cp -r dist/rovo-dev/.rovodev/skills/* ~/.rovodev/skills/
```

### Qoder

```bash
# Project-specific
cp -r dist/qoder/.qoder your-project/

# Or global
cp -r dist/qoder/.qoder/skills/* ~/.qoder/skills/
```

### Pi

```bash
cp -r dist/pi/.pi your-project/
```

---

## Usage

```
/run [role] [industry] [segment]
```

**Examples:**
```
/run CFO Manufacturing "Mid-Market ($100M–$1B revenue)"
/run CRO Banking "Enterprise ($1B+ assets)"
/run CHRO Healthcare "Mid-Market health systems"
```

A new run folder is created under `prototype/` with all move outputs, the executive summary, and an audit trail.

---

## What One Run Produces

| Artifact | What It Contains |
|----------|-----------------|
| `executive_summary.md` | Thesis score, recommendation, top risks, investment thesis |
| `move1_territory_map.md` | Validated job-domain matrix |
| `move2_disruption_screen.md` | Scored territories with evidence |
| `move3_temporal_filter.md` | Disruption stage and timing window |
| `move4_build_level.md` | Platform vs. point solution recommendation |
| `move5_demand_validation.md` | ODI job map + scored outcome statements |
| `move6_opportunity_analysis.md` | Full investment thesis |
| `audit_trail.md` | Consolidated sources, ratings, validation log |
| `move{N}_output.json` | Structured handoff files between moves |

---

## Methodology

Built on **Outcome-Driven Innovation (ODI)** as developed by Tony Ulwick / Strategyn:

- Jobs are stable end-states, not activities — they don't change with technology
- Outcome statements measure what executors want to be true, not what they do
- Opportunity scoring: Importance + max(Importance − Satisfaction, 0)
- Scores are hypothesized from web evidence; in production, replace with client survey data from 8+ executor interviews

The 9 ODI rule files in `.claude/rules/` are the authoritative methodology reference and take precedence over any other guidance.

---

## Guardrails

- **Context firewall** — each sub-agent starts fresh. Project-specific knowledge cannot contaminate results. Every run is independently defensible.
- **Evidence gates** — Move 5 requires external citations for outcome scores. Citations are logged in `audit_trail.md`.
- **ODI compliance** — outcome statements are validated against strict format rules (Minimize/Maximize + measurable metric + context). Violations fail before proceeding.
- **Gate review** — Move 1 and Move 4 block on your approval. Don't skim them. Everything downstream inherits the territory map and build framing.

---

## License

MIT
