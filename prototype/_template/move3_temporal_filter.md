# Move 3: Apply the Temporal Filter

**Date:** {{DATE}}
**Time to complete:** ~{{TIME}} minutes agent execution (framework target: 1-2 hours human)

---

## Input

{{N_HOT}} hot territories from Move 2 (all with 2+ "High" disruption ratings):
1. {{TERRITORY_1}} ({{N}}H)
2. {{TERRITORY_2}} ({{N}}H)
3. ...

---

## Method

For each hot territory, assessed disruption stage (Complete / In Progress / Emerging) based on web-researched evidence. Each assessment cites 2-3 data points per the framework's evidence standard.

**Stage definitions:**
| Stage | Market Adoption | Strategic Implication |
|-------|----------------|----------------------|
| **Complete** | >70% adopted, dominant player won | Low opportunity — window closed |
| **In Progress** | 30-70% adopted, no single winner | **High opportunity — window open** |
| **Emerging** | <30% adopted, early tools only | Moderate opportunity — timing bet |

---

## Temporal Assessment

### 1. {{TERRITORY_1}}

**Stage: {{COMPLETE / IN PROGRESS / EMERGING}}**

| Evidence | Data Point | Source |
|----------|-----------|--------|
| {{EVIDENCE_CATEGORY_1}} | {{DATA_POINT}} | {{SOURCE}} |
| {{EVIDENCE_CATEGORY_2}} | {{DATA_POINT}} | {{SOURCE}} |
| {{EVIDENCE_CATEGORY_3}} | {{DATA_POINT}} | {{SOURCE}} |

**Assessment:** {{NARRATIVE_EXPLAINING_STAGE_DETERMINATION}}

---

### 2. {{TERRITORY_2}}

**Stage: {{COMPLETE / IN PROGRESS / EMERGING}}**

| Evidence | Data Point | Source |
|----------|-----------|--------|
| {{EVIDENCE_CATEGORY_1}} | {{DATA_POINT}} | {{SOURCE}} |
| {{EVIDENCE_CATEGORY_2}} | {{DATA_POINT}} | {{SOURCE}} |
| {{EVIDENCE_CATEGORY_3}} | {{DATA_POINT}} | {{SOURCE}} |

**Assessment:** {{NARRATIVE_EXPLAINING_STAGE_DETERMINATION}}

---

{{REPEAT FOR EACH HOT TERRITORY}}

---

## Temporal Summary

| Territory | Stage | Adoption Est. | Confidence |
|-----------|-------|--------------|------------|
| **{{TERRITORY_1}}** | **{{STAGE}}** | {{ADOPTION_RANGE}} | {{High/Medium/Low}} — {{CONFIDENCE_REASON}} |
| **{{TERRITORY_2}}** | **{{STAGE}}** | {{ADOPTION_RANGE}} | {{High/Medium/Low}} — {{CONFIDENCE_REASON}} |
| ... | ... | ... | ... |

### Contrast: What "Complete" Looks Like

{{PROVIDE_A_CALIBRATION_EXAMPLE — Describe a territory in the same C-suite landscape that IS Complete (>70% adopted, dominant player). This calibrates the In Progress assessments.}}

---

## Decision Gate Check

The framework requires at least 1 In Progress territory to proceed: "If no hot territories are In Progress, you have a strategic problem."

**Result:** {{HOW_MANY_IN_PROGRESS}} of {{N_HOT}} hot territories are In Progress. {{STRATEGIC_ASSESSMENT}}.

Ranked by strength of opportunity signal:

1. **{{TERRITORY_1}}** — {{WHY_RANKED_FIRST}}
2. **{{TERRITORY_2}}** — {{WHY_RANKED_SECOND}}
3. ...

---

## Output

**{{N_PRIORITY}} priority targets ({{STAGE_SUMMARY}})** passed to Move 4 for build level analysis:

1. {{TERRITORY_1}}
2. {{TERRITORY_2}}
3. ...

Move 4 will trace each target's position in the job hierarchy, assess outcome overlap with siblings, and determine build level.

---

## Self-Validation Results

Per `rules/recursive-validation.md`, Move 3 checklist:

| # | Criterion | Status | Note |
|---|-----------|:------:|------|
| 3.1 | 2-3 data points cited per territory | {{PASS/FAIL}} | {{NOTE}} |
| 3.2 | Stage definitions correctly applied | {{PASS/FAIL}} | {{NOTE}} |
| 3.3 | Every stage assessment includes confidence | {{PASS/FAIL}} | {{NOTE}} |
| 3.4 | At least 1 territory In Progress | {{PASS/FAIL}} | {{NOTE}} |
| 3.5 | Calibration example provided | {{PASS/FAIL}} | {{NOTE}} |
| 3.6 | Priority ranking explained | {{PASS/FAIL}} | {{NOTE}} |

**Iterations:** {{N}}
**Final status:** {{ALL PASS / N unresolvable issues}}

---

## JSON Output

Write `move3_output.json` per the Move 3 schema in `rules/json-handoff-schema.md`. Include all priority targets with their id, label, stage, adoption_estimate, confidence, and rank.
