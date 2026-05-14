# Disruption Cascade v4 — Workflow Plan

**Purpose:** A 6-move agentic workflow that takes a blank-slate C-suite proxy and produces a defensible investment thesis with territory mapping, disruption screening, temporal filtering, build level determination, demand-side validation via ODI job mapping, and opportunity analysis with a go/no-go recommendation.

**Design principle:** Each move narrows the decision space. Start broad (all territories), screen for disruption, filter by timing, find the right abstraction level, validate demand, then synthesize into an investment decision. No move requires output from a later move — strictly sequential.

**ODI methodology:** The `.claude/rules/odi-*.md` files are the authoritative source for ODI/JTBD methodology. This workflow applies ODI within the Disruption Cascade structure. If there is a conflict between this file and the ODI rules, the ODI rules take precedence.

---

## Sub-Agent Execution Model

Each move runs as an independent sub-agent (Task tool, general-purpose) with its own context window. The main conversation acts as **coordinator** — it plans, delegates, checks gates, and requests user approval, but does not perform research or write move content.

**Why:** Two problems kill prototypes run in a single context: (1) context contamination from project-specific knowledge leaking in, and (2) context exhaustion from research + writing filling the window before the workflow completes, triggering compaction and losing detail.

**Audit trail:** A single `audit_trail.md` accumulates across all moves — sources, ratings with evidence, validation results, and key decisions. Each sub-agent appends to it after completing self-validation.

### How It Works

1. **Coordinator reads** `README.md`, `workflow-plan.md`, and `rules/` to understand the run configuration.
2. **For each move**, the coordinator launches a sub-agent with a structured prompt containing:
   - The context firewall rule (`rules/context-firewall.md`)
   - The move template file
   - Only the ODI rules needed for that move (see mapping below)
   - The disruption cascade rules
   - The structured Output section from the previous move (not the full file)
3. **Sub-agent executes** the move: researches via web search, writes the markdown move file, runs self-validation (see `rules/recursive-validation.md`), writes `move{N}_output.json` per `rules/json-handoff-schema.md`, and appends audit data to `audit_trail.md`.
4. **Coordinator reads** the JSON output and self-validation results, performs the gate check, and decides whether to proceed.
5. **User approval** is requested at Moves 1 and 4 before continuing.

### Handoff Between Moves

- The **JSON handoff file** (`move{N}_output.json`) is the authoritative handoff between moves — not the markdown Output section.
- Each sub-agent receives JSON from the immediately prior move only — no accumulation.
- Exception: Move 6 receives all 5 JSON files (assembled by the coordinator).
- The markdown Output section remains for human review only.

See `rules/json-handoff-schema.md` for the JSON structure per move.

See `rules/agent-architecture.md` for the full prompt structure and handoff rules.

---

## Move 1: Map the Territory

**Objective:** Define the job-domain matrix for the target C-suite role and segment, with validated jobs and domains.

**Input:** C-suite proxy (role + segment, e.g., "{{C_SUITE_ROLE}}, {{SEGMENT}}")

**Steps:**

**1a. Map core jobs** — Research core functional jobs via 4 source categories: APQC PCF, Big 4 frameworks, professional association standards, segment-specific research. Frame each job using goal language ("Ensure/Protect/Produce"), not responsibility language ("Manage/Oversee"). Document boundary rules for each job (Owns / Does not own / Boundary test).

**1b. Validate core jobs (GATE)** — Apply three tests to every job per `odi-job-validation.md`:
- **Universality:** If this job disappeared, would the role be fundamentally different for *every* executor in the segment?
- **Mutual exclusivity:** Do activities in this job overlap with another job? If so, merge or tighten boundary rules.
- **Data support:** Can this job map to a specific APQC PCF Level 2 process + 3 additional independent sources?

Each job must have 3+ cited sources from different categories. Document all excluded candidates with failure reason and resolution. Verify core job statements per `odi-core-job-statements.md`: single functional job, no "while"/"and" compounds, solution-free, stable 10+ years, goal framing.

> **Validation gate:** All jobs must pass all three tests. If any job fails, resolve before proceeding.

**1c. Map domains** — Research cross-cutting domains via the same 4 source categories. Each domain must create a substantively different work context.

**1d. Validate domains (GATE)** — Apply the same three tests to every domain. Each domain must have 3+ cited sources. Document excluded domains with failure reason.

> **Validation gate:** All domains must pass all three tests. If any domain fails, resolve before proceeding.

**1e. Build territory matrix** — Only after both job and domain validations pass, build the territory matrix at the intersection (Jobs x Domains). Flag blurred boundary intersections as high-priority per `odi-job-map-structure.md`.

**Output:** Validated territory matrix (e.g., {{N_JOBS}} jobs x {{N_DOMAINS}} domains = {{N_TERRITORIES}} territories)

**Gate:** User approval required before proceeding. Review job definitions, domain definitions, validation results, and matrix completeness.

**Time:** ~25 min agent / 2-4 hrs human

---

## Move 2: Screen for Disruption Exposure

**Objective:** Identify which territories are most exposed to disruption, screened from the C-suite perspective.

**Input:** Validated territory matrix from Move 1

**Steps:**
1. Screen each territory on four disruption factors using H/M/L scale (all from the {{C_SUITE_ROLE}}'s perspective as job executor):
   - **Automation Readiness** — Can machines do the {{C_SUITE_ROLE}}'s work in this territory today or soon?
   - **Optionality** — Does the {{C_SUITE_ROLE}} now have more and better options for getting this job done?
   - **Regulatory Tailwind** — Are regulations expanding the volume/complexity of this job for the {{C_SUITE_ROLE}}?
   - **Cost Burden** — Is this territory expensive or resource-intensive for the {{C_SUITE_ROLE}}?
2. Research each factor via web search across technology landscape, competitive dynamics, regulatory developments, and cost/resource burden
3. Identify "hot territories" with 2+ High ratings

**Output:** Ranked list of hot territories with disruption ratings and evidence

**Gate: Evidence quality** — Every H/M/L rating must cite specific evidence. If any rating lacks a source, the move fails and the agent must re-research that territory before proceeding.

**Time:** ~15 min agent / 60-90 min human

---

## Move 3: Apply the Temporal Filter

**Objective:** Assess whether each hot territory's disruption window is open, closed, or too early.

**Input:** Hot territories from Move 2

**Steps:**
1. For each hot territory, assess disruption stage using web-researched evidence:
   - **Complete** (>70% adopted, dominant player won) — window closed
   - **In Progress** (30-70% adopted, no single winner) — window open
   - **Emerging** (<30% adopted, early tools only) — timing bet
2. Cite 2-3 data points per territory per the evidence standard
3. Rank by signal strength within the "In Progress" band

**Output:** Priority-ranked territories with stage assessments and evidence

**Gate: At least 1 In Progress** — At least one hot territory must be assessed as "In Progress" (30-70% adopted). If all are Complete or Emerging, the cascade stops or pivots to a different segment/role. This is a hard stop — do not proceed without an open disruption window.

**Time:** ~10 min agent / 1-2 hrs human

---

## Move 4: Find the Build Level

**Objective:** Determine the correct level of abstraction for building — should you build at the target level, or one level up/down?

**Input:** Priority territories from Move 3

**Steps:**

**4a. Trace hierarchy and assess overlap:**
1. For each territory, trace position using two decomposition axes:
   - **APQC PCF** — navigate process hierarchy from C-suite to domain level
   - **Subject matter classification** — identify type categories and siblings within the domain
2. Identify sibling nodes at the subject matter level
3. Assess outcome overlap with siblings (process step comparison + vendor product architecture as market validation)
4. Apply the 60% threshold rule:
   - Overlap >=60% with siblings -> build one level up (platform opportunity)
   - Overlap <60% -> build at current level
5. Determine build level and entry point for each territory

**4b. Check rules (GATE):**
- **Framework separation:** Three axes (ODI/JTBD, APQC PCF, Subject matter classification) are not conflated. No nesting of subject matter types inside JTBD steps or APQC activities.
- **Abstraction level:** Build level targets the client level (client as job executor), not the solution provider level, per `odi-abstraction-level.md`.
- **60% threshold:** Correctly applied — overlap percentages are evidence-based, not assumed.
- **Cross-cutting capabilities:** Handled as domains, not jobs, per `odi-job-map-structure.md`.

> **Validation gate:** All rule checks must pass. If framework separation is violated, restructure before proceeding.

**Output:** Build level recommendation per territory with primary/secondary ranking

**Gate:** User approval required. This is the key strategic decision — build level determines everything downstream.

**Time:** ~25 min agent / 2-4 hrs human

**Framework note:** Three distinct frameworks structure this analysis (see `rules/disruption-cascade-rules.md`). They must not be conflated:
- ODI/JTBD structures the job side (what the customer accomplishes)
- APQC PCF structures the process/domain side (how activities are organized)
- Subject matter classification identifies the content (what's being processed)

---

## Move 5: Validate with Demand-Side Evidence

**Objective:** Identify all major job executors for the entry point, build verified ODI job maps for each, and confirm the recommended build level addresses real, underserved needs.

**Input:** Primary build level recommendation and converging territories from Move 4

**Steps:**

**5a. Identify executors and build job maps:**
1. Identify ALL distinct job executors involved with the entry point from converging territories (different territories often represent different executors — governance vs operational vs compliance roles)
2. For each job executor, build an independent 8-step ODI job map (Define -> Locate -> Prepare -> Confirm -> Execute -> Monitor -> Modify -> Conclude) per `odi-job-map-structure.md`
3. Generate outcome statements at each step using strict ODI format per `odi-outcome-statements.md`:
   - "Minimize the time it takes to [verb] [object] [context]"
   - "Minimize the likelihood of [undesired outcome] [context]"
4. Score outcomes on Importance (1-10) and Satisfaction (1-10) using evidence per `odi-scoring.md` — differentiate satisfaction across executors
5. Calculate opportunity scores: Opportunity = Importance + max(Importance - Satisfaction, 0)
6. Validate each executor's job map against independent frameworks (minimum 3 sources per executor)
7. Perform cross-executor analysis: identify which executor has the most underserved outcomes, cross-executor dependencies, and what the multi-executor view reveals
8. Include emotional and social jobs per executor per `odi-executor-discipline.md`
9. Synthesize investment target: WHERE, WHO, WHAT, ENTER, LEAD WITH, and executor priority

**5b. Verify maps against ODI rules (GATE):**
Run the full `odi-checklist.md` against each executor's map:
- **Core job statement:** Single functional job, solution-free, goal framing (not responsibility framing), boundary rules documented, no "while"/"and" compounds
- **Outcome statements:** Solution-free (survives complete solution change), measures a metric not a task, MECE across steps, correct step placement per step boundary definitions
- **Executor discipline:** One executor per map, emotional and social jobs included per `odi-executor-discipline.md`
- **Scoring:** 1-10 scale, analyst scores labeled as hypotheses, satisfaction scores show reasonable variance (<60% same score), each score cites evidence, no single source >50% of evidence per `odi-scoring.md`
- **Source validation:** 3+ cited sources per executor map from different categories

> **Validation gate:** All checklist items must pass for each executor's map. Fix violations before proceeding.

**Output:** Multi-executor demand validation with scored outcomes per executor, cross-executor opportunity analysis, executor priority ranking, and investment target recommendation

**Gate:** Signal gate — in production, requires 70% job map adherence across client interviews with each executor type. In prototype mode, uses web evidence as proxy.

**Time:** ~90 min agent / 4-8 weeks human (client interviews with multiple executor types)

---

## Move 6: Opportunity Analysis & Investment Decision

**Objective:** Synthesize all findings into a defensible investment thesis with a structured go/no-go recommendation.

**Input:** All 5 JSON handoff files from Moves 1-5 (assembled by coordinator)

**Steps:**
1. Build the logic chain (WHO/WHAT/WHERE/WHY/HOW) with citations tracing through each move
2. Score the thesis on 5 weighted dimensions using the evaluation rubric (1-10 scale with evidence per dimension)
3. Analyze alternative investment targets — what else was considered and why it scored lower
4. Produce explicit GO / CONDITIONAL GO / NO-GO recommendation based on composite score

**Output:** Full decision document with logic chain, scored rubric, alternatives analysis, and recommendation

**Gate: Composite score threshold** — Rubric composite score must reach minimum 5/10 for GO recommendation.
- Score 8-10: Strong conviction — GO, proceed to validation
- Score 5-7: Moderate conviction — CONDITIONAL GO, address gaps
- Score 1-4: Weak conviction — NO-GO, revisit assumptions
The agent cannot recommend GO with a composite score below 5.

**Time:** ~20 min agent / 2-4 hrs human

---

## End-to-End Summary

```
Move 1: Map Territory       -> {{N_TERRITORIES}} territories ({{N_JOBS}} jobs x {{N_DOMAINS}} domains), validated
Move 2: Disruption Screen   -> {{N_HOT}} hot territories (2+ High ratings, all evidence-cited)
Move 3: Temporal Filter     -> {{N_PRIORITY}} priority targets (at least 1 In Progress confirmed)
Move 4: Build Level         -> Primary recommendation, rule-checked
Move 5: Demand Validation   -> {{N_EXECUTORS}} job executors, ODI-verified maps, scored outcomes (1-10)
Move 6: Opportunity Analysis -> Investment thesis, rubric score {{SCORE}}/10, {{GO/CONDITIONAL/NO-GO}}
```

**Total agent time:** ~120 minutes
**Equivalent human time:** ~3-6 weeks (research + analysis + interviews)

---

## Data Sources

- All research via web search (no pre-existing corpus required)
- APQC PCF v7.x as process reference framework
- ODI/JTBD as job mapping methodology (authoritative rules: `.claude/rules/odi-*.md`)
- Big 4 frameworks, professional associations, vendor architectures, analyst reports as validation sources
- In production: client ODI interviews replace web evidence in Move 5
