# Move 6: Opportunity Analysis & Investment Decision

**Date:** {{DATE}}
**Time to complete:** ~{{TIME}} minutes agent execution (framework target: 2-4 hours human)

---

## Input

Summary of Moves 1-5 outputs:

| Move | Key Output | Metric |
|------|-----------|--------|
| 1. Map Territory | {{N_JOBS}} jobs x {{N_DOMAINS}} domains | {{N_TERRITORIES}} territories (validated) |
| 2. Disruption Screen | {{N_HOT}} hot territories | All ratings evidence-cited |
| 3. Temporal Filter | {{N_IN_PROGRESS}} In Progress | Disruption window open |
| 4. Build Level | {{BUILD_LEVEL}} | Rule-checked, user-approved |
| 5. Demand Validation | {{N_EXECUTORS}} executors, {{N_OUTCOMES}} outcomes | ODI-verified, 1-10 scale |

---

## Part 1: The Logic Chain

### WHO — The Executors

| Priority | Executor | Avg Opp Score | Top Outcomes (>=15) | Rationale |
|----------|----------|:------------:|:-------------------:|-----------|
| **1** | {{EXECUTOR_1}} | {{AVG}} | {{N}} | {{WHY_PRIORITIZED — citing Move 5 opportunity scores}} |
| **2** | {{EXECUTOR_2}} | {{AVG}} | {{N}} | {{WHY_THIS_ORDER}} |
| **3** | {{EXECUTOR_3}} | {{AVG}} | {{N}} | {{WHY_THIS_ORDER}} |

### WHAT — The Unmet Needs

**Top outcome clusters by executor:**

| Cluster | Primary Executor | Opp Range | Why Unmet |
|---------|-----------------|-----------|-----------|
| {{CLUSTER_1}} | {{EXECUTOR}} | {{RANGE}} | {{CITING_SATISFACTION_SCORES_AND_EVIDENCE}} |
| {{CLUSTER_2}} | {{EXECUTOR}} | {{RANGE}} | {{CITING_SATISFACTION_SCORES_AND_EVIDENCE}} |
| {{CLUSTER_3}} | {{EXECUTOR}} | {{RANGE}} | {{CITING_SATISFACTION_SCORES_AND_EVIDENCE}} |

### WHERE — The Investment Target

**Build level:** {{BUILD_LEVEL}} (citing Move 4 analysis)

**Entry point:** {{ENTRY_POINT}}

**Entry point rationale:** {{CITING_MOVE_4_PLUS_MOVE_5_CONVERGENCE — why this specific entry point given the build level and executor priorities}}

### WHY — The Evidence Chain

| Move | Evidence Link | Key Data |
|------|-------------|----------|
| **Move 1** | How the territory was identified | {{N_TERRITORIES}} mapped, all validated against 3 tests, {{N_JOBS}} jobs with boundary rules |
| **Move 2** | Why it's disruption-exposed | {{HOT_TERRITORY_DESCRIPTION}} — {{DISRUPTION_FACTORS}} |
| **Move 3** | Why the timing is right | {{STAGE_ASSESSMENT}} — {{ADOPTION_EVIDENCE}} |
| **Move 4** | Why this abstraction level | {{OVERLAP_PERCENTAGE}} sibling overlap → {{BUILD_LEVEL}} — {{MARKET_VALIDATION}} |
| **Move 5** | Why these executors and outcomes | {{TOP_OPP_SCORES}} — {{EXECUTOR_DIFFERENTIATION}} |

### HOW — The Opportunity Thesis

**Why this entry point has the greatest opportunity:**
{{THESIS_STATEMENT — synthesizing all five moves into a coherent argument}}

**What makes it defensible:**
- {{DEFENSIBILITY_1}}
- {{DEFENSIBILITY_2}}
- {{DEFENSIBILITY_3}}

**Key assumptions that could invalidate the thesis:**
- {{ASSUMPTION_1}}
- {{ASSUMPTION_2}}
- {{ASSUMPTION_3}}

**What would need to be true for this to succeed:**
- {{CONDITION_1}}
- {{CONDITION_2}}
- {{CONDITION_3}}

---

## Part 2: Thesis Evaluation Rubric

Scored on 1-10 scale with evidence per dimension per `odi-scoring.md`.

| Dimension | Score | Confidence | Evidence | Weight |
|-----------|:-----:|:----------:|----------|:------:|
| **Evidence Strength** — How well-sourced is the thesis? | {{1-10}} | {{H/M/L}} | {{PER_MOVE_EVIDENCE_QUALITY}} | 25% |
| **Market Timing** — Is the disruption window open? | {{1-10}} | {{H/M/L}} | {{MOVE_3_TEMPORAL_DATA}} | 20% |
| **Defensibility** — Is this hard for competitors to replicate? | {{1-10}} | {{H/M/L}} | {{COMPETITIVE_MOAT_ANALYSIS}} | 20% |
| **Executor Pain Severity** — How underserved are the target executors? | {{1-10}} | {{H/M/L}} | {{MOVE_5_OPPORTUNITY_SCORES}} | 20% |
| **Feasibility** — Can this realistically be built/delivered? | {{1-10}} | {{H/M/L}} | {{BUILD_LEVEL_AND_ENTRY_POINT_ANALYSIS}} | 15% |

**Composite score:** {{WEIGHTED_AVERAGE}}/10

**Confidence tier:**
- 8-10: Strong conviction — proceed to validation
- 5-7: Moderate conviction — proceed with caution, address gaps
- 1-4: Weak conviction — revisit assumptions before proceeding

**This thesis scores: {{SCORE}}/10 — {{TIER}}**

### Score Justification

**Strongest dimensions:**
- {{DIMENSION}}: {{WHY_STRONG}}

**Weakest dimensions:**
- {{DIMENSION}}: {{WHY_WEAK}} — {{WHAT_WOULD_IMPROVE_IT}}

---

## Part 3: Alternative Investment Targets

For each territory cluster that was NOT selected as primary:

### Alternative 1: {{TERRITORY_CLUSTER}}

| Dimension | Assessment |
|-----------|-----------|
| **Alternative thesis** | {{WHAT_THE_THESIS_WOULD_BE}} |
| **Why it scored lower** | {{SPECIFIC_WEAKNESSES_VS_PRIMARY}} |
| **When it becomes primary** | {{CONDITIONS_THAT_WOULD_ELEVATE_IT}} |
| **Relationship to primary** | {{COMPLEMENTS/CONFLICTS — explanation}} |

### Alternative 2: {{TERRITORY_CLUSTER}}

{{REPEAT SAME STRUCTURE}}

---

## Part 4: Go / No-Go Recommendation

### Recommendation: {{GO / CONDITIONAL GO / NO-GO}}

**Composite score: {{SCORE}}/10** — {{ABOVE/BELOW}} the 5/10 threshold for GO.

{{IF GO:}}

**Recommended next steps:**
1. {{NEXT_STEP_1 — e.g., client interview design per executor type}}
2. {{NEXT_STEP_2 — e.g., prototype scope definition}}
3. {{NEXT_STEP_3 — e.g., team requirements}}

**Key risks to monitor:**
- {{RISK_1}}
- {{RISK_2}}

**Timeline to signal gate:** {{TIMELINE — e.g., 4-6 weeks for 8 client interviews}}

{{IF CONDITIONAL GO:}}

**Specific conditions that must be met:**
1. {{CONDITION_1}}
2. {{CONDITION_2}}

**What additional evidence is needed:**
- {{EVIDENCE_GAP_1}}
- {{EVIDENCE_GAP_2}}

**Recommended validation approach:**
{{APPROACH_DESCRIPTION}}

{{IF NO-GO:}}

**Why the evidence doesn't support proceeding:**
- {{REASON_1}}
- {{REASON_2}}

**What would need to change:**
- {{CHANGE_1}}
- {{CHANGE_2}}

**Alternative directions to explore:**
- {{DIRECTION_1}}
- {{DIRECTION_2}}

---

## Cascade Summary

```
DISRUPTION CASCADE v4 — {{RUN_NAME}}
Target: {{C_SUITE_ROLE}}, {{SEGMENT}}

Move 1: {{N_JOBS}} Jobs x {{N_DOMAINS}} Domains = {{N_TERRITORIES}} territories (validated)
Move 2: {{N_HOT}} hot territories (2+ Highs, all evidence-cited)
Move 3: {{N_IN_PROGRESS}} In Progress -> priority targets
Move 4: Build at {{BUILD_LEVEL}}, enter at {{ENTRY_POINT}} (rule-checked)
Move 5: {{N_EXECUTORS}} job executors, {{N_OUTCOMES}} total outcomes (1-10 scale), ODI-verified
Move 6: Thesis score {{SCORE}}/10 -> {{GO/CONDITIONAL/NO-GO}}

RESULT:
├── WHERE: {{BUILD_LEVEL}} ({{SEGMENT}})
├── WHO: {{N_EXECUTORS}} job executors ({{EXECUTOR_NAMES}})
├── WHAT: {{KEY_CAPABILITIES_BY_EXECUTOR}}
├── ENTER: {{ENTRY_POINT}}
├── LEAD WITH: {{VALUE_PROPOSITION_LEAD}}
└── DECISION: {{GO/CONDITIONAL/NO-GO}} ({{SCORE}}/10)
```

**Total evidence citations:** {{N_CITATIONS}} across {{N_SOURCES}} unique sources

---

## Self-Validation Results

Per `rules/recursive-validation.md`, Move 6 checklist:

| # | Criterion | Status | Note |
|---|-----------|:------:|------|
| 6.1 | Logic chain cites evidence from all prior moves | {{PASS/FAIL}} | {{NOTE}} |
| 6.2 | Every rubric score is evidence-backed | {{PASS/FAIL}} | {{NOTE}} |
| 6.3 | Every rubric score includes confidence level | {{PASS/FAIL}} | {{NOTE}} |
| 6.4 | Composite score correctly calculated | {{PASS/FAIL}} | {{NOTE}} |
| 6.5 | GO/NO-GO matches threshold (>=5 for GO) | {{PASS/FAIL}} | {{NOTE}} |
| 6.6 | Alternative targets analyzed | {{PASS/FAIL}} | {{NOTE}} |
| 6.7 | Key invalidating assumptions documented | {{PASS/FAIL}} | {{NOTE}} |

**Iterations:** {{N}}
**Final status:** {{ALL PASS / N unresolvable issues}}
