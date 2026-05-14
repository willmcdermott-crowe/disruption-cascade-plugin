# Move 4: Find the Build Level

**Date:** {{DATE}}
**Time to complete:** ~{{TIME}} minutes agent execution (framework target: 2-4 hours human)

---

## Input

{{N_PRIORITY}} priority targets from Move 3 (all In Progress):
1. {{TERRITORY_1}} ({{N}}H, {{RANKING_NOTE}})
2. {{TERRITORY_2}} ({{N}}H)
3. ...

---

## Method

For each priority target:
1. Traced position in JTBD hierarchy (APQC PCF v7.x as reference framework)
2. Identified sibling nodes at each level
3. Assessed outcome overlap with siblings (using process step comparison and vendor product architecture as market validation)
4. Determined build level, and entry point

---

## Framework Decomposition Note

This move traces territories through a hierarchy to find the right build level. Three distinct frameworks provide structure, and they must not be conflated:

| Framework | What It Structures | Decomposition Type | Example |
|-----------|-------------------|-------------------|---------|
| **ODI / JTBD** | The job side — what the customer is trying to accomplish | Job maps (8 universal steps), outcome statements | Define -> Locate -> ... -> Monitor -> Conclude |
| **APQC PCF** | The process/domain side — how activities are organized | Process categories -> groups -> activities | 9.9 Manage Taxes -> 9.9.2 Process Taxes |
| **Subject matter classification** | The content — what's being processed or what the job is done *on* | Type categories, standards, transaction types | {{EXAMPLE_FROM_THIS_RUN}} |

These are **orthogonal axes**, not a single nested hierarchy. See `rules/disruption-cascade-rules.md` for full framework separation rules.

---

## Analysis by Territory

### Territory 1: {{TERRITORY_1}}

**Hierarchy Trace:**

*APQC process decomposition (levels 1-3):*
```
{{C_SUITE_ROLE}} (C-suite)
  └── {{JOB}}: {{JOB_NAME}} (APQC {{CODE}})
       └── {{DOMAIN}}: {{DOMAIN_NAME}} (APQC {{CODE}})
            └── {{APQC_LEVEL_3}}
```

*Subject matter classification (types under {{DOMAIN_NAME}}):*
```
{{PARENT_TYPE}} (sub-domain of {{DOMAIN}})
  ├── {{TYPE_A}} <- TARGET
  ├── {{TYPE_B}}
  ├── {{TYPE_C}}
  └── {{TYPE_D}}
```

**Depth:** {{N}} levels — {{DEPTH_CHARACTERIZATION}}.

**Sibling Overlap Analysis:**

| {{TARGET}} Process Step | vs. {{SIBLING_1}} | vs. {{SIBLING_2}} | vs. {{SIBLING_3}} |
|------------------------|:-----------------:|:-----------------:|:-----------------:|
| 1. {{STEP_1}} | {{Identical/Analogous/Divergent}} | {{...}} | {{...}} |
| 2. {{STEP_2}} | {{...}} | {{...}} | {{...}} |
| ... | ... | ... | ... |

**Overlap estimates:**
- {{TARGET}} <-> {{SIBLING_1}}: **~{{N}}%** ({{RATIONALE}})
- {{TARGET}} <-> {{SIBLING_2}}: **~{{N}}%** ({{RATIONALE}})
- {{TARGET}} <-> {{SIBLING_3}}: **~{{N}}%** ({{RATIONALE}})

**Market validation:** {{HOW_DO_EXISTING_VENDORS_BUILD? — Do they build at target level, one level up, or one level down? What does their product architecture suggest?}}

**Build Level Determination:**

| Question | Answer |
|----------|--------|
| How deep is the territory? | {{DEPTH_ASSESSMENT}} |
| Outcome overlap with siblings? | **{{N}}% with {{SIBLING}}** — {{EXCEEDS/BELOW}} 60% threshold |
| Build at target level or higher? | **{{BUILD_LEVEL_RECOMMENDATION}}** |
| Entry point? | **{{ENTRY_POINT}}** — {{RATIONALE}} |

---

### Territory 2: {{TERRITORY_2}}

{{REPEAT SAME STRUCTURE FOR EACH TERRITORY}}

---

## Rule Check

Per workflow plan step 4b, verify the following before proceeding.

### Framework Separation

| Check | Status | Evidence |
|-------|:------:|----------|
| ODI/JTBD used only for job structure (not nested in APQC or subject matter) | {{PASS/FAIL}} | {{WHERE_VERIFIED}} |
| APQC PCF used only for process/domain structure | {{PASS/FAIL}} | {{WHERE_VERIFIED}} |
| Subject matter classification used only for content categorization | {{PASS/FAIL}} | {{WHERE_VERIFIED}} |
| No nesting of subject matter types inside JTBD steps | {{PASS/FAIL}} | {{WHERE_VERIFIED}} |
| No nesting of subject matter types inside APQC process activities | {{PASS/FAIL}} | {{WHERE_VERIFIED}} |
| Axis transitions explicitly called out in hierarchy traces | {{PASS/FAIL}} | {{WHERE_VERIFIED}} |

### Abstraction Level

Per `odi-abstraction-level.md`:

| Check | Status | Evidence |
|-------|:------:|----------|
| Build level targets the client (client as job executor), not solution provider | {{PASS/FAIL}} | {{HOW_CONFIRMED}} |
| Mapping targets a platform opportunity, not optimization of existing offerings | {{PASS/FAIL}} | {{HOW_CONFIRMED}} |

### 60% Threshold Application

| Check | Status | Evidence |
|-------|:------:|----------|
| Overlap percentages are evidence-based (process step comparison + market validation) | {{PASS/FAIL}} | {{METHODOLOGY_USED}} |
| Threshold correctly applied (>=60% = build up, <60% = build at level) | {{PASS/FAIL}} | {{SPECIFIC_PERCENTAGES}} |

### Cross-Cutting Capabilities

Per `odi-job-map-structure.md`:

| Check | Status | Evidence |
|-------|:------:|----------|
| Capabilities that intersect every job are represented as domains, not separate jobs | {{PASS/FAIL}} | {{WHICH_CAPABILITIES_CHECKED}} |
| No "enabler" entity type invented outside the domain layer | {{PASS/FAIL}} | {{CONFIRMED}} |

**Rule check result:** {{ALL_PASS / N_FAILURES}} — {{SUMMARY}}

---

## Synthesis: Build Level Recommendations

| Territory | Build Level | Entry Point | Strategic Character |
|-----------|------------|-------------|---------------------|
| **{{TERRITORY_1}}** | **{{BUILD_LEVEL}}** | {{ENTRY_POINT}} | {{CHARACTER}} |
| {{TERRITORY_2}} | {{BUILD_LEVEL}} | {{ENTRY_POINT}} | {{CHARACTER}} |
| ... | ... | ... | ... |

---

## The Primary Recommendation

**{{BUILD_LEVEL_STATEMENT}}. {{ENTRY_POINT_STATEMENT}}. {{PATH_STATEMENT}}.**

This is the standout result for {{N}} reasons:

### 1. {{REASON_1_TITLE}}
{{REASON_1_EVIDENCE}}

### 2. {{REASON_2_TITLE}}
{{REASON_2_EVIDENCE}}

### 3. {{REASON_3_TITLE}}
{{REASON_3_EVIDENCE}}

### 4. {{REASON_4_TITLE}}
{{REASON_4_EVIDENCE}}

### What This Means

{{EXPLAIN_WHAT_THE_BUILD_LEVEL_DETERMINATION_IMPLIES_FOR_STRATEGY}}

---

## The Other Territories: Role in Portfolio

| Territory | Relationship to Primary | Note |
|-----------|------------------------|------|
| **{{TERRITORY_2}}** | **{{RELATIONSHIP}}** — {{EXPLANATION}} | {{PHASE_NOTE}} |
| **{{TERRITORY_3}}** | **{{RELATIONSHIP}}** — {{EXPLANATION}} | {{PHASE_NOTE}} |
| ... | ... | ... |

---

## Output

**Primary recommendation:**
- **Build Level:** {{BUILD_LEVEL}}
- **Entry Point:** {{ENTRY_POINT}}
- **Rationale:** {{KEY_REASONS_SUMMARY}}
- **Rule check:** All passed

**Secondary recommendations:**
- {{TERRITORY_2}} ({{RELATIONSHIP}})
- {{TERRITORY_3}} ({{RELATIONSHIP}})
- ...

This output passes to Move 5 for demand-side validation: Do {{SEGMENT}} {{C_SUITE_ROLE}}s actually have unmet needs in {{BUILD_LEVEL}}? Are the specific outcomes we've identified actually underserved?

---

## Self-Validation Results

Per `rules/recursive-validation.md`, Move 4 checklist:

| # | Criterion | Status | Note |
|---|-----------|:------:|------|
| 4.1 | Three frameworks not conflated | {{PASS/FAIL}} | {{NOTE}} |
| 4.2 | Axis transitions explicitly called out | {{PASS/FAIL}} | {{NOTE}} |
| 4.3 | Client-level abstraction (not solution provider) | {{PASS/FAIL}} | {{NOTE}} |
| 4.4 | 60% threshold evidence-based | {{PASS/FAIL}} | {{NOTE}} |
| 4.5 | Cross-cutting capabilities as domains | {{PASS/FAIL}} | {{NOTE}} |
| 4.6 | APQC codes verified | {{PASS/FAIL}} | {{NOTE}} |
| 4.7 | All rule check items pass | {{PASS/FAIL}} | {{NOTE}} |

**Iterations:** {{N}}
**Final status:** {{ALL PASS / N unresolvable issues}}

---

## JSON Output

Write `move4_output.json` per the Move 4 schema in `rules/json-handoff-schema.md`. Include primary (build_level, entry_point, overlap_pct, converging_territories) and secondary_targets.
