# Move 5: Validate with Demand-Side Evidence

**Date:** {{DATE}}
**Time to complete:** ~{{TIME}} minutes agent execution (framework target: 4-8 weeks human with client interviews)
**Note:** This prototype substitutes web research (industry surveys, vendor data, analyst reports) for client interviews. A production run would use direct client ODI interviews with each job executor type.

---

## Input

From Move 4:
- **Build Level:** {{BUILD_LEVEL}}
- **Entry Point:** {{ENTRY_POINT}}
- **Converging Territories:** {{LIST_OF_TERRITORIES_THAT_CONVERGE_ON_THE_BUILD_LEVEL}}

---

## Job Executor Identification

The converging territories from Move 4 represent fundamentally different work done by different people at different points in the business cycle. This step identifies ALL major job executors involved with the entry point, then develops a verified 8-step ODI job map for each.

**Why multiple executors matter:** A single-executor model averages across executors with radically different satisfaction levels, hiding the most important signal: which executor is desperately underserved and which is reasonably well-served.

### Executor Summary

| # | Executor | Who at {{SEGMENT}} | Territory Origin | Core Job | Distinct Perspective |
|---|----------|-------------------|------------------|----------|---------------------|
| 1 | {{EXECUTOR_1_NAME}} | {{WHO_AT_SEGMENT}} | {{TERRITORY}} | {{CORE_JOB}} | {{PERSPECTIVE — strategic/governance vs operational/transactional vs compliance-driven}} |
| 2 | {{EXECUTOR_2_NAME}} | {{WHO_AT_SEGMENT}} | {{TERRITORY}} | {{CORE_JOB}} | {{PERSPECTIVE}} |
| {{N}} | {{EXECUTOR_N_NAME}} | {{WHO_AT_SEGMENT}} | {{TERRITORY}} | {{CORE_JOB}} | {{PERSPECTIVE}} |

### How Executors Interact

{{DESCRIBE_DEPENDENCIES — who governs, who operates, where failures in one executor create risk for another}}

---

## Method

1. Identified {{N}} distinct job executors from converging Move 4 territories
2. Built an independent 8-step ODI job map for each executor per `odi-job-map-structure.md`
3. Generated outcome statements per executor (3 per step, ~24 per executor) in strict ODI format per `odi-outcome-statements.md`
4. Scored each outcome on Importance (1-10) and Satisfaction (1-10) using web evidence as proxy per `odi-scoring.md`
5. Calculated opportunity scores: Opportunity = Importance + max(Importance - Satisfaction, 0)
6. Cross-referenced evidence from multiple independent sources
7. Validated each executor's job map against independent frameworks (minimum 3 sources per executor)
8. Identified emotional and social jobs per executor per `odi-executor-discipline.md`
9. Performed cross-executor analysis to identify overall opportunity patterns

---

## Executor {{N}}: {{EXECUTOR_NAME}}

### Core Job Statement

Per `odi-core-job-statements.md` — single functional job, goal framing, solution-free, stable 10+ years:

**"When [context/situation], [goal verb] [object of the job] [clarifying phrase]."**

### Boundary Rules

| Owns | Does Not Own | Boundary Test |
|------|-------------|---------------|
| {{WHAT_THIS_EXECUTOR_OWNS}} | {{ADJACENT_JOBS}} | {{SINGLE_SENTENCE_HEURISTIC}} |

### 8-Step Job Map

| Step | Job Step | Description |
|------|----------|-------------|
| 1. Define | {{DEFINE_DESCRIPTION}} | {{WHAT_HAPPENS_FROM_THIS_EXECUTOR_PERSPECTIVE}} |
| 2. Locate | {{LOCATE_DESCRIPTION}} | {{WHAT_HAPPENS}} |
| 3. Prepare | {{PREPARE_DESCRIPTION}} | {{WHAT_HAPPENS}} |
| 4. Confirm | {{CONFIRM_DESCRIPTION}} | {{WHAT_HAPPENS}} |
| 5. Execute | {{EXECUTE_DESCRIPTION}} | {{WHAT_HAPPENS}} |
| 6. Monitor | {{MONITOR_DESCRIPTION}} | {{WHAT_HAPPENS}} |
| 7. Modify | {{MODIFY_DESCRIPTION}} | {{WHAT_HAPPENS}} |
| 8. Conclude | {{CONCLUDE_DESCRIPTION}} | {{WHAT_HAPPENS}} |

### Outcome Statements and Scoring

Scored on 1-10 scale per `odi-scoring.md`. Analyst-assigned scores are labeled as **hypotheses** — true scores require quantitative survey validation.

**Step 1: Define**

| # | Outcome Statement | Imp | Imp Conf | Sat | Sat Conf | Opp | Evidence |
|---|-------------------|-----|----------|-----|----------|-----|----------|
| {{N}}.1.1 | Minimize the time it takes to [verb] [object] [context] | {{1-10}} | {{H/M/L}} | {{1-10}} | {{H/M/L}} | {{OPP}} | {{EVIDENCE_WITH_SOURCES}} |
| {{N}}.1.2 | Minimize the likelihood of [undesired outcome] [context] | {{1-10}} | {{H/M/L}} | {{1-10}} | {{H/M/L}} | {{OPP}} | {{EVIDENCE_WITH_SOURCES}} |
| {{N}}.1.3 | {{OUTCOME_STATEMENT}} | {{1-10}} | {{H/M/L}} | {{1-10}} | {{H/M/L}} | {{OPP}} | {{EVIDENCE_WITH_SOURCES}} |

**Step 2: Locate**

| # | Outcome Statement | Imp | Imp Conf | Sat | Sat Conf | Opp | Evidence |
|---|-------------------|-----|----------|-----|----------|-----|----------|
| ... | ... | ... | ... | ... | ... | ... | ... |

{{REPEAT FOR ALL 8 STEPS}}

### Emotional and Social Jobs

Per `odi-executor-discipline.md`, every functional job map must include emotional and social jobs:

**Emotional jobs** — how the executor wants to feel or avoid feeling:

| # | Emotional Job | Context |
|---|--------------|---------|
| E1 | {{Feel/Avoid feeling [emotional state]}} | {{When/while [context]}} |
| E2 | {{Feel/Avoid feeling [emotional state]}} | {{When/while [context]}} |

**Social jobs** — how the executor wants to be perceived:

| # | Social Job | By Whom |
|---|-----------|---------|
| S1 | {{Be seen as / Avoid being seen as [perception]}} | {{BY_WHOM}} |
| S2 | {{Be seen as / Avoid being seen as [perception]}} | {{BY_WHOM}} |

---

{{REPEAT FULL EXECUTOR SECTION FOR EACH IDENTIFIED EXECUTOR}}

---

## ODI Checklist Verification

Per `odi-checklist.md`, run the full checklist against each executor's map before proceeding.

### Executor {{N}}: {{EXECUTOR_NAME}}

**Core Job Statement Check:**

| Check | Status | Note |
|-------|:------:|------|
| Single functional job — no "while" or "and" linking two objectives | {{PASS/FAIL}} | {{NOTE}} |
| Solution-free and stable for 10+ years | {{PASS/FAIL}} | {{NOTE}} |
| Uses goal framing ("Ensure/Protect/Produce"), not responsibility framing ("Manage/Oversee") | {{PASS/FAIL}} | {{NOTE}} |
| Boundary rules documented (Owns / Does not own / Boundary test) | {{PASS/FAIL}} | {{NOTE}} |

**Outcome Statement Check:**

| Check | Status | Note |
|-------|:------:|------|
| Every outcome passes the solution-free test (survives complete solution change) | {{PASS/FAIL}} | {{NOTE}} |
| Every outcome measures a metric of success, not a task or activity | {{PASS/FAIL}} | {{NOTE}} |
| No outcome contains contextual constraints that belong in Evidence | {{PASS/FAIL}} | {{NOTE}} |
| No two outcomes across different steps scored identically for the same reason (MECE) | {{PASS/FAIL}} | {{NOTE}} |
| Every outcome placed in the correct step per step boundary definitions | {{PASS/FAIL}} | {{NOTE}} |
| Conclude step evaluates job success, not downstream handoff | {{PASS/FAIL}} | {{NOTE}} |

**Executor Discipline Check:**

| Check | Status | Note |
|-------|:------:|------|
| All outcomes describe the experience of the same executor | {{PASS/FAIL}} | {{NOTE}} |
| Emotional jobs documented | {{PASS/FAIL}} | {{NOTE}} |
| Social jobs documented | {{PASS/FAIL}} | {{NOTE}} |

**Scoring Check:**

| Check | Status | Note |
|-------|:------:|------|
| 1-10 scale used (not 1-5) | {{PASS/FAIL}} | {{NOTE}} |
| Analyst-assigned scores labeled as hypotheses | {{PASS/FAIL}} | {{NOTE}} |
| Satisfaction scores show reasonable variance (<60% sharing same score) | {{PASS/FAIL}} | {{SAT_DISTRIBUTION}} |
| Each score cites at least one data point | {{PASS/FAIL}} | {{NOTE}} |
| No single source provides >50% of segment-specific evidence | {{PASS/FAIL}} | {{SOURCE_DISTRIBUTION}} |

**Source Validation:**

| Check | Status | Note |
|-------|:------:|------|
| 3+ independent sources from different categories | {{PASS/FAIL}} | {{SOURCES_LISTED}} |

**Executor {{N}} checklist result:** {{ALL_PASS / N_FAILURES}} — {{SUMMARY}}

{{REPEAT FOR EACH EXECUTOR}}

---

## Cross-Executor Analysis

### Top 15 Opportunities (All Executors Combined)

| Rank | Outcome | Executor | Step | Opp Score |
|------|---------|----------|------|-----------|
| 1 | {{OUTCOME_DESCRIPTION}} | {{EXECUTOR_N}}: {{NAME}} | {{STEP}} | {{SCORE}} |
| ... | ... | ... | ... | ... |

### Distribution by Executor

| Executor | Outcomes Scored | Avg Opportunity | Outcomes >= 15 | % of Top 15 |
|----------|----------------|-----------------|----------------|-------------|
| {{EXECUTOR_1}} | {{N}} | {{AVG}} | {{N}} | {{%}} |
| {{EXECUTOR_2}} | {{N}} | {{AVG}} | {{N}} | {{%}} |
| ... | ... | ... | ... | ... |

### Distribution by Job Step (All Executors)

| Step | Outcomes | Avg Opportunity | Top 15 Count |
|------|----------|-----------------|--------------|
| 1. Define | {{N}} | {{AVG}} | {{N}} |
| 2. Locate | {{N}} | {{AVG}} | {{N}} |
| 3. Prepare | {{N}} | {{AVG}} | {{N}} |
| 4. Confirm | {{N}} | {{AVG}} | {{N}} |
| 5. Execute | {{N}} | {{AVG}} | {{N}} |
| 6. Monitor | {{N}} | {{AVG}} | {{N}} |
| 7. Modify | {{N}} | {{AVG}} | {{N}} |
| 8. Conclude | {{N}} | {{AVG}} | {{N}} |

### Key Patterns

**1. {{PATTERN_1_TITLE — Where do top outcomes cluster by executor and step?}}**
{{PATTERN_1_DESCRIPTION}}

**2. {{PATTERN_2_TITLE — "Likelihood of" vs "time to" outcomes}}**
{{PATTERN_2_DESCRIPTION — which score higher and what does that imply for value proposition?}}

**3. {{PATTERN_3_TITLE — Cross-executor dependencies}}**
{{PATTERN_3_DESCRIPTION — where one executor's failure creates risk for another}}

**4. {{PATTERN_4_TITLE — Standout pain points / entry wedges}}**
{{PATTERN_4_DESCRIPTION}}

**5. {{PATTERN_5_TITLE — What the multi-executor view reveals that a single-executor view misses}}**
{{PATTERN_5_DESCRIPTION}}

---

## Signal Gate Check

The framework sets a 70% job map adherence threshold: "If fewer than 70% of clients recognize the job map as valid, your hierarchy is wrong."

### Executor {{N}} Job Map Validation

| Validation Source | Alignment |
|-------------------|-----------|
| {{SOURCE_1}} | {{ALIGNMENT_ASSESSMENT}} |
| {{SOURCE_2}} | {{ALIGNMENT_ASSESSMENT}} |
| {{SOURCE_3}} | {{ALIGNMENT_ASSESSMENT}} |
| {{SOURCE_4}} | {{ALIGNMENT_ASSESSMENT}} |

**Verdict:** {{STRONG/MODERATE/WEAK}} validation. {{SUMMARY}}.

{{REPEAT FOR EACH EXECUTOR}}

### Overall Multi-Executor Model Coherence

{{ASSESS_WHETHER_EXECUTORS_ARE_NON_OVERLAPPING_AND_DEPENDENCIES_ARE_CLEAR}}

**Proxy signal:** {{ASSESSMENT_OF_JOB_MAP_VALIDITY_BASED_ON_WEB_EVIDENCE}}

**Recommendation:** {{PROCEED_OR_REVISE}}

---

## Investment Target Summary

### Where to Invest
**{{BUILD_LEVEL}}** — build at this level, serving {{N}} distinct job executors.

### What to Build For (Top 5 Outcome Clusters by Executor)

| Priority | Cluster | Primary Executor | Opportunity Range | Description |
|----------|---------|-----------------|-------------------|-------------|
| **1** | {{CLUSTER_NAME}} | {{EXECUTOR_N}}: {{NAME}} | {{OPP_RANGE}} | {{DESCRIPTION}} |
| **2** | {{CLUSTER_NAME}} | {{EXECUTOR_N}}: {{NAME}} | {{OPP_RANGE}} | {{DESCRIPTION}} |
| **3** | {{CLUSTER_NAME}} | {{EXECUTOR_N}}: {{NAME}} | {{OPP_RANGE}} | {{DESCRIPTION}} |
| **4** | {{CLUSTER_NAME}} | {{EXECUTOR_N}}: {{NAME}} | {{OPP_RANGE}} | {{DESCRIPTION}} |
| **5** | {{CLUSTER_NAME}} | {{EXECUTOR_N}}: {{NAME}} | {{OPP_RANGE}} | {{DESCRIPTION}} |

### How to Frame It

{{STRATEGY_DESCRIPTION — describe directly without path labels}}:
- Enter at {{ENTRY_POINT}} ({{ENTRY_RATIONALE}})
- Architecture for {{BUILD_LEVEL}} ({{ARCHITECTURE_RATIONALE}})
- Lead with {{VALUE_PROPOSITION_LEAD}} ({{VP_RATIONALE}})
- {{SHARPEST_ENTRY_WEDGE}} is the sharpest entry wedge

### Where to Enter
**{{ENTRY_POINT}}** — because:
- {{REASON_1}}
- {{REASON_2}}
- {{REASON_3}}
- {{REASON_4}}
- {{REASON_5}}

### Executor Priority

| Priority | Executor | Rationale |
|----------|----------|-----------|
| **1st** | {{EXECUTOR}} | {{WHY_FIRST}} |
| **2nd** | {{EXECUTOR}} | {{WHY_SECOND}} |
| **3rd** | {{EXECUTOR}} | {{WHY_THIRD}} |

---

## Evidence Quality Assessment

| Source Type | Sources Used | Confidence |
|-------------|-------------|------------|
| {{TYPE_1}} | {{SOURCES}} | {{High/Medium/Low}} — {{REASON}} |
| {{TYPE_2}} | {{SOURCES}} | {{High/Medium/Low}} — {{REASON}} |
| ... | ... | ... |

**Limitations:**
- {{LIMITATION_1}}
- {{LIMITATION_2}}
- {{LIMITATION_3}}

---

## Cascade Progress

```
Move 1: {{N_JOBS}} Jobs x {{N_DOMAINS}} Domains = {{N_TERRITORIES}} territories (validated)
Move 2: {{N_HOT}} hot territories (2+ Highs, all evidence-cited)
Move 3: {{N_IN_PROGRESS}} In Progress -> priority targets
Move 4: Build at {{BUILD_LEVEL}}, enter at {{ENTRY_POINT}} (rule-checked)
Move 5: {{N_EXECUTORS}} job executors, {{N_OUTCOMES}} total outcomes (1-10 scale), ODI-verified

RESULT:
├── WHERE: {{BUILD_LEVEL}} ({{SEGMENT}})
├── WHO: {{N_EXECUTORS}} job executors ({{EXECUTOR_NAMES}})
├── WHAT: {{KEY_CAPABILITIES_BY_EXECUTOR}}
├── ENTER: {{ENTRY_POINT}}
└── LEAD WITH: {{VALUE_PROPOSITION_LEAD}}
```

This output passes to Move 6 for opportunity analysis and investment decision.

---

## Self-Validation Results

Per `rules/recursive-validation.md`, Move 5 checklist:

| # | Criterion | Status | Note |
|---|-----------|:------:|------|
| 5.1 | Core job statement: single job, goal framing, boundary rules | {{PASS/FAIL}} | {{NOTE}} |
| 5.2 | Every outcome passes solution-free test | {{PASS/FAIL}} | {{NOTE}} |
| 5.3 | Every outcome measures a metric, not a task | {{PASS/FAIL}} | {{NOTE}} |
| 5.4 | Outcomes MECE across steps | {{PASS/FAIL}} | {{NOTE}} |
| 5.5 | Correct step placement per boundary definitions | {{PASS/FAIL}} | {{NOTE}} |
| 5.6 | Conclude evaluates job success, not downstream handoff | {{PASS/FAIL}} | {{NOTE}} |
| 5.7 | One executor per map | {{PASS/FAIL}} | {{NOTE}} |
| 5.8 | Emotional and social jobs included | {{PASS/FAIL}} | {{NOTE}} |
| 5.9 | 1-10 scale used | {{PASS/FAIL}} | {{NOTE}} |
| 5.10 | Analyst scores labeled as hypotheses | {{PASS/FAIL}} | {{NOTE}} |
| 5.11 | Satisfaction variance <60% same score | {{PASS/FAIL}} | {{NOTE}} |
| 5.12 | Each score cites evidence | {{PASS/FAIL}} | {{NOTE}} |
| 5.13 | Every score includes confidence level | {{PASS/FAIL}} | {{NOTE}} |
| 5.14 | No single source >50% of evidence | {{PASS/FAIL}} | {{NOTE}} |
| 5.15 | 3+ sources per executor from different categories | {{PASS/FAIL}} | {{NOTE}} |

**Iterations:** {{N}}
**Final status:** {{ALL PASS / N unresolvable issues}}

---

## JSON Output

Write `move5_output.json` per the Move 5 schema in `rules/json-handoff-schema.md`. Include executors summary, top_15_outcomes (with importance/satisfaction scores and confidence), and investment_target (WHERE/WHO/WHAT/ENTER/LEAD_WITH).
