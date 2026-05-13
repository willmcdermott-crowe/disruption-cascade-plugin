# /run — Start a New Prototype Run

Initialize a new Disruption Cascade v4 prototype run from the @prototype/_template template.

## Instructions

### 1. Gather Run Configuration

Ask the user for the following (accept as arguments if provided after `/run`):

- **C-suite role** — e.g., CFO, CRO, CTO, CHRO
- **Industry** — e.g., Manufacturing, Banking, Insurance, Healthcare
- **Segment** — e.g., "Mid-Market ($100M–$1B revenue)", "Enterprise ($1B+)", "Mid-Market ($1B–$10B assets)"
- **Purpose** (optional) — Custom purpose statement. Default: "Run the 6-move Disruption Cascade v4 workflow to produce a defensible investment thesis, build level, job mapping, and go/no-go recommendation from scratch."

**Auto-derive the folder short name** from role + industry in lowercase snake_case:
- CFO + Manufacturing → `cfo_manufacturing`
- CRO + Banking → `cro_banking`
- CTO + Insurance → `cto_insurance`

### 2. Determine Run Number

Scan @prototype for existing `run_NNN_*` folders. The new run gets the next sequential number, zero-padded to 3 digits (e.g., `run_001`, `run_002`).

### 3. Create the Run Folder

Copy from @prototype/_template to a new folder:

```
prototype/run_{NNN}_{short_name}/
```

**Copy these files and folders from @prototype/_template :**
- @prototype/_template/README.md
- @prototype/_template/workflow-plan.md
- @prototype/_template/executive_summary.md
- @prototype/_template/audit_trail.md
- @prototype/_template/move1_territory_map.md
- @prototype/_template/move2_disruption_screen.md
- @prototype/_template/move3_temporal_filter.md
- @prototype/_template/move4_build_level.md
- @prototype/_template/move5_demand_validation.md
- @prototype/_template/move6_opportunity_analysis.md
- @prototype/_template/rules (entire directory, includes @prototype/_template/rules/agent-architecture.md , @prototype/_template/rules/context-firewall.md , @prototype/_template/rules/disruption-cascade-rules.md , @prototype/_template/rules/json-handoff-schema.md , @prototype/_template/rules/recursive-validation.md )

**Do NOT copy:**
- Any existing `run_*` sub-folders inside `_template/` (those are previous runs, not template material)

### 4. Fill in the README and Audit Trail

Replace the `{{placeholders}}` in the new run's `README.md` and `audit_trail.md` with the run configuration:

| Placeholder | Value |
|-------------|-------|
| `{{RUN_NAME}}` | Human-readable name combining role + segment + industry (e.g., "CFO Mid-Market Manufacturing") |
| `{{C_SUITE_ROLE}}` | The C-suite role (e.g., "CFO") |
| `{{SEGMENT}}` | Full segment string including industry (e.g., "Mid-Market Manufacturing ($100M–$1B revenue)") |
| `{{DATE}}` | Today's date (YYYY-MM-DD) |
| `{{PURPOSE}}` | The purpose statement, incorporating the role and segment |

Remove the "How to Run" section's step 1-2 (copy/fill instructions) since those are done. Keep steps 3-5 (how to execute).

### 5. Confirm and Start the Workflow

Present the user with:
- The new folder path
- The filled-in README summary (target, date, purpose)
- Confirmation that all template files are in place

Then ask: **"Ready to start Move 1: Map the Territory?"**

If the user confirms, begin acting as the **coordinator** per @prototype/_template/rules/agent-architecture.md :
1. Read the run's `README.md`, `workflow-plan.md`, and `rules/` files
2. Launch a sub-agent for Move 1 with the proper prompt structure (see @prototype/_template/rules/agent-architecture.md for prompt assembly, ODI rules-per-move mapping, and JSON handoff protocol)
3. Enforce the @prototype/_template/rules/context-firewall.md — pass it to every sub-agent
4. Pass JSON handoff files between moves (not markdown Output sections) — see @prototype/_template/rules/json-handoff-schema.md
5. Each sub-agent runs self-validation per @prototype/_template/rules/recursive-validation.md before writing JSON output
6. Each sub-agent appends audit data to `audit_trail.md`
7. **After each sub-agent completes**, run the deterministic validation suite before proceeding to the gate check:
   ```
   python tests/validate.py <run_folder> --move N
   ```
   - If any **FAIL** results appear: do not proceed. Report the failures to the user, relaunch the sub-agent with specific correction guidance, and re-run validation after the retry.
   - If only **WARN** results appear: surface them to the user for review, then proceed.
   - If all **PASS**: proceed to the gate check as normal.
8. Follow the gate check and handoff protocol for each subsequent move (see @prototype/_template/workflow-plan.md for gate criteria per move)

## Key References

| File | Purpose |
|------|---------|
| @prototype/_template/README.md | Template README with `{{placeholders}}` |
| @prototype/_template/workflow-plan.md | 6-move workflow with gates, timing, and handoff rules |
| @prototype/_template/rules/agent-architecture.md | Sub-agent prompt structure, ODI rules-per-move mapping, handoff rules |
| @prototype/_template/rules/context-firewall.md | Isolation rules — what sub-agents can and cannot reference |
| @prototype/_template/rules/disruption-cascade-rules.md | Disruption screening and scoring rules |
| @.claude/rules/odi-job-validation.md | 4-test job validation (Moves 1, 5) |
| @.claude/rules/odi-core-job-statements.md | Job statement format and boundary rules (Moves 1, 5) |
| @.claude/rules/odi-ends-vs-means.md | Ends-vs-means test for candidate job sets (Move 1) |
| @.claude/rules/odi-abstraction-level.md | Client-level mapping (Move 4) |
| @.claude/rules/odi-job-map-structure.md | 8-step map structure, cross-cutting capabilities (Moves 4, 5) |
| @.claude/rules/odi-outcome-statements.md | Outcome format and MECE rules (Move 5) |
| @.claude/rules/odi-executor-discipline.md | One executor per map, emotional/social jobs (Move 5) |
| @.claude/rules/odi-scoring.md | 1-10 scale, hypothesis labeling, variance checks (Moves 5, 6) |
| @.claude/rules/odi-checklist.md | Full pre-submission checklist (Move 5) |

## Notes

- The coordinator (main conversation) does NOT do research or write move content — sub-agents do
- User approval is required at gate points (Moves 1 and 4) before proceeding
