# Sub-Agent Architecture

Design principle: Each move runs as an independent sub-agent with a fresh context window. The main conversation acts as coordinator. This prevents context exhaustion (moves filling up a shared window) and reinforces context isolation (each agent starts clean).

---

## Architecture

```
Main Agent (Coordinator)
├── Reads: README.md (run config), workflow-plan.md, rules/
├── Does NOT do research or write move content
├── For each move:
│   ├── Launches Task sub-agent (general-purpose) with:
│   │   ├── Move template (the template file for this move)
│   │   ├── Relevant ODI rules (only the ones needed for this move)
│   │   ├── Context firewall rule
│   │   ├── Disruption cascade rules + recursive-validation.md
│   │   ├── JSON handoff schema (rules/json-handoff-schema.md)
│   │   └── JSON from previous move's output (NOT markdown)
│   ├── Sub-agent:
│   │   1. Researches + writes markdown move file
│   │   2. Runs self-validation loop (see below)
│   │   3. Writes move{N}_output.json
│   │   4. Appends audit data to audit_trail.md
│   └── Coordinator reads JSON output + self-validation results
├── Performs gate checks between moves (reviews self-validation results)
├── Requests user approval at gate points (Moves 1, 4)
└── Writes executive_summary.md after Move 6 completes
```

## ODI Rules Per Move

Only pass the rules each move actually needs:

| Move | Rules to Include |
|------|-----------------|
| 1 — Territory Map | `odi-job-validation.md`, `odi-core-job-statements.md`, `odi-ends-vs-means.md` |
| 2 — Disruption Screen | `disruption-cascade-rules.md` only |
| 3 — Temporal Filter | `disruption-cascade-rules.md` only |
| 4 — Build Level | `odi-abstraction-level.md`, `odi-job-map-structure.md`, `disruption-cascade-rules.md` |
| 5 — Demand Validation | ALL `odi-*.md` rules |
| 6 — Opportunity Analysis | `odi-scoring.md`, `disruption-cascade-rules.md` |

**All moves also receive:** `recursive-validation.md`, `json-handoff-schema.md`, `context-firewall.md`

## Sub-Agent Prompt Structure

When launching a sub-agent for a move, the coordinator assembles the prompt in this order:

```
## Context Firewall
[Full content of rules/context-firewall.md]

## Your Task
You are executing Move N of a Disruption Cascade v4 prototype.
Target: [C-suite role and segment from README.md]
Date: [today's date]

## Input (from previous move — JSON)
[Contents of move{N-1}_output.json — or run configuration for Move 1]

## Move Template
[Full content of the move template file]

## Rules
[Only the ODI rules listed above for this move]
[Full content of rules/disruption-cascade-rules.md]

## Self-Validation Protocol
[Full content of rules/recursive-validation.md]

## JSON Output Schema
[The relevant Move N section from rules/json-handoff-schema.md]

## Instructions
1. Do all research via web search — every claim must cite a fresh source
2. Write your complete markdown output to: [target file path]
3. Follow the template structure exactly (Input, Method, Evidence, Output, Self-Validation Results, JSON Output)
4. Do not reference any project artifacts, MEMORY.md, or project CLAUDE.md
5. If you cannot find evidence for a claim, mark it as NOT FOUND — do not fill gaps from memory
6. After drafting output, run the self-validation loop per recursive-validation.md
7. Write move{N}_output.json per the JSON handoff schema
8. Append audit data (sources, ratings, validation results, decisions) to audit_trail.md
9. Every H/M/L rating and 1-10 score must include a confidence level (High/Medium/Low)
```

---

## JSON Handoff Protocol

JSON files replace markdown Output sections as the authoritative handoff between moves. This cuts context window usage by transmitting only structured data.

1. **Sub-agent writes JSON.** After completing the markdown, the sub-agent writes `move{N}_output.json` per `rules/json-handoff-schema.md`.
2. **Coordinator reads JSON.** The coordinator reads the JSON file (not the markdown Output section) and passes it to the next sub-agent.
3. **No accumulation.** Each sub-agent receives JSON from the immediately prior move only. Exception: Move 6 receives all 5 JSON files.
4. **Markdown remains for humans.** The Output section in markdown stays for human review — it is not used for inter-move handoff.

See `rules/json-handoff-schema.md` for the complete schema per move.

---

## Self-Validation Protocol

Each sub-agent runs a recursive validation loop after drafting its output, before writing the JSON handoff. This catches rule violations before the coordinator sees the results.

1. **Identify applicable rules** for this move (from the per-move checklist in `recursive-validation.md`).
2. **Check each criterion** against the drafted output.
3. **Fix violations** found during the check.
4. **Re-check** until all criteria pass or issues are documented as unresolvable.
5. **Write validation summary** to the `## Self-Validation Results` section in the markdown and include `validation_passed: true/false` in the JSON.

The coordinator reviews self-validation results as part of the gate check. If the sub-agent reports unresolvable issues, the coordinator decides whether to retry, override, or stop.

See `rules/recursive-validation.md` for the full protocol and per-move checklists.

---

## Audit Trail

Each sub-agent appends structured audit data to `audit_trail.md` after completing self-validation. This creates a single consolidated evidence trail across all moves.

**What to append per move:**
- **Sources used** — name, URL, type (APQC/Big4/ProfAssoc/Segment/Vendor/Analyst), which moves used it
- **Ratings with evidence** — every H/M/L rating or 1-10 score, its confidence level, and the supporting evidence/source
- **Validation results** — self-validation summary (criteria checked, pass/fail, iterations)
- **Key decisions** — significant judgments made during the move, rationale, alternatives considered

The coordinator records timestamps (move start/completion, user approvals) at the top level.

---

## Handoff Rules

1. **JSON handoff only.** When passing results between moves, the coordinator passes the contents of `move{N}_output.json`. The sub-agent for the next move never sees the full markdown, research trail, or evidence details of the previous move.

2. **No accumulation.** Each sub-agent receives JSON from the immediately prior move only. Move 3 gets Move 2's JSON, not Move 1 + Move 2. Exception: Move 6 receives all 5 JSON files (assembled by the coordinator).

3. **Coordinator reads, sub-agent writes.** The coordinator reads completed JSON files and self-validation results to perform gate checks. Sub-agents write move files + JSON but do not read other move files.

---

## Gate Check Responsibilities

The coordinator (main conversation) — not the sub-agent — is responsible for:

- Reading the completed move's JSON output and self-validation results
- Verifying the gate criteria are met
- Reviewing the self-validation summary for unresolvable issues
- Requesting user approval where required (Moves 1, 4)
- Deciding whether to proceed, retry, or stop the cascade

If a gate fails, the coordinator may relaunch the sub-agent with additional guidance, but never passes the full previous attempt — only the specific failure reason and the original inputs.

---

## Web Research Efficiency

Sub-agents should minimize unnecessary web fetches to reduce execution time and approval friction.

### Batching Guidance
1. **Plan research first.** Before making any web calls, list the specific questions you need answered. Group related questions together.
2. **Batch by topic.** Research all territories within a domain together rather than switching between domains. This maximizes cache hits for overlapping sources.
3. **Prefer WebSearch over WebFetch.** WebSearch returns summaries that often suffice for H/M/L ratings and stage assessments. Only use WebFetch when you need specific data points from a known URL.
4. **Reuse sources across territories.** When a single source (e.g., a Gartner report) provides evidence for multiple territories, cite it once and reference it for each applicable rating.
5. **Cache-friendly patterns.** When researching similar territories, use consistent search terms so the 15-minute cache window covers related queries.
