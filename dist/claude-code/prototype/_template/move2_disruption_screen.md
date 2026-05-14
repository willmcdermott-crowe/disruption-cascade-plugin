# Move 2: Screen for Disruption Exposure

**Date:** {{DATE}}
**Time to complete:** ~{{TIME}} minutes agent execution (framework target: 60-90 minutes human)

---

## Input

Territory matrix from Move 1: {{N_JOBS}} jobs x {{N_DOMAINS}} domains = {{N_TERRITORIES}} territories, {{C_SUITE_ROLE}} {{SEGMENT}}.

---

## Method

**Perspective:** All factors are screened from the {{C_SUITE_ROLE}}'s perspective as job executor — what is disrupting the {{C_SUITE_ROLE}}'s ability to perform these jobs, what new options the {{C_SUITE_ROLE}} has, and what forces are expanding or burdening the {{C_SUITE_ROLE}}'s workload.

Screened each territory on four disruption factors using H/M/L scale. Research via web search across automation technology landscape, competitive dynamics, regulatory developments, and cost/resource burden.

**Reminder:** This is a screening pass, not a scoring exercise. Ratings reflect judgment informed by research. Every cell is marked "screened" not "scored." The goal is to identify territories with 2+ "High" ratings — the hot territories.

---

## Four Disruption Factors

| Factor | What It Captures ({{C_SUITE_ROLE}} Perspective) | High (Exposed) | Low (Protected) |
|--------|-----------------|-----------------|------------------|
| **Automation Readiness** | Can machines do the {{C_SUITE_ROLE}}'s work in this territory today or soon? | Rule-determined, data-structured, engines exist | Judgment-heavy, ambiguous, bespoke |
| **Optionality** | Does the {{C_SUITE_ROLE}} now have more and better options for getting this job done? | Multiple powerful platforms, self-service viable, many competing options | Few alternatives, high complexity, {{C_SUITE_ROLE}} cannot easily self-serve |
| **Regulatory Tailwind** | Are regulations expanding the volume/complexity of this job for the {{C_SUITE_ROLE}}? | New rules expanding scope, complexity growing, more work required | Stable environment, declining burden |
| **Cost Burden** | Is this territory expensive or resource-intensive for the {{C_SUITE_ROLE}}? | High spend, growing costs, significant staff/technology investment | Low spend, stable costs, minimal resource drain |

---

## Domain-Level Screening Rationale

Before scoring individual territories, each domain has a baseline disruption profile:

### D1: {{DOMAIN_1}}
- **Automation:** {{H/M/L}} (confidence: {{High/Medium/Low}}) — {{EVIDENCE}}
- **Optionality:** {{H/M/L}} (confidence: {{High/Medium/Low}}) — {{EVIDENCE}}
- **Regulatory:** {{H/M/L}} (confidence: {{High/Medium/Low}}) — {{EVIDENCE}}
- **Cost:** {{H/M/L}} (confidence: {{High/Medium/Low}}) — {{EVIDENCE}}

### D2: {{DOMAIN_2}}
- **Automation:** {{H/M/L}} (confidence: {{High/Medium/Low}}) — {{EVIDENCE}}
- **Optionality:** {{H/M/L}} (confidence: {{High/Medium/Low}}) — {{EVIDENCE}}
- **Regulatory:** {{H/M/L}} (confidence: {{High/Medium/Low}}) — {{EVIDENCE}}
- **Cost:** {{H/M/L}} (confidence: {{High/Medium/Low}}) — {{EVIDENCE}}

{{REPEAT FOR EACH DOMAIN}}

---

## Full Screening Matrix

### Automation Readiness

|  | D1: {{DOMAIN_1}} | D2: {{DOMAIN_2}} | D3: {{DOMAIN_3}} | ... |
|--|:-:|:-:|:-:|:-:|
| **C1: {{JOB_1}}** | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | ... |
| **C2: {{JOB_2}}** | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | ... |
| ... | ... | ... | ... | ... |

### Optionality

|  | D1: {{DOMAIN_1}} | D2: {{DOMAIN_2}} | D3: {{DOMAIN_3}} | ... |
|--|:-:|:-:|:-:|:-:|
| **C1: {{JOB_1}}** | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | ... |
| **C2: {{JOB_2}}** | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | ... |
| ... | ... | ... | ... | ... |

### Regulatory Tailwind

|  | D1: {{DOMAIN_1}} | D2: {{DOMAIN_2}} | D3: {{DOMAIN_3}} | ... |
|--|:-:|:-:|:-:|:-:|
| **C1: {{JOB_1}}** | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | ... |
| **C2: {{JOB_2}}** | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | ... |
| ... | ... | ... | ... | ... |

### Cost Burden

|  | D1: {{DOMAIN_1}} | D2: {{DOMAIN_2}} | D3: {{DOMAIN_3}} | ... |
|--|:-:|:-:|:-:|:-:|
| **C1: {{JOB_1}}** | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | ... |
| **C2: {{JOB_2}}** | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | ... |
| ... | ... | ... | ... | ... |

---

## Hot Territories (2+ Highs)

| Territory | Auto | Opt | Reg | Cost | Highs | Avg Conf | Hot? |
|-----------|:----:|:----:|:---:|:-----:|:----:|:--------:|:----:|
| **{{TERRITORY_1}}** | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | **{{N}}** | {{High/Med/Low}} | **HOT** |
| **{{TERRITORY_2}}** | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | **{{N}}** | {{High/Med/Low}} | **HOT** |
| ... | ... | ... | ... | ... | ... | ... | ... |

**{{N_HOT}} hot territories out of {{N_TERRITORIES}}.** Within the framework's expected range of 4-8.

### Pattern Observation

{{DESCRIBE_PATTERNS — Where do hot territories cluster? Which jobs/domains are protected? What does the pattern suggest about the nature of disruption?}}

---

## Territories That Narrowly Missed

| Territory | Auto | Opt | Reg | Cost | Highs | Avg Conf | Note |
|-----------|:----:|:----:|:---:|:----:|:-----:|:--------:|------|
| {{TERRITORY}} | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | {{H/M/L}} | {{N}} | {{High/Med/Low}} | {{WHY_IT_MISSED}} |
| ... | ... | ... | ... | ... | ... | ... | ... |

---

## Evidence Sources

{{ORGANIZED_BY_CATEGORY — cite key sources with quantified data where possible.}}

---

## Output

**{{N_HOT}} hot territories** (2+ Highs across four factors: automation, optionality, regulation, cost burden) passed to Move 3 for temporal assessment:
1. {{TERRITORY_1}} ({{N}}H)
2. {{TERRITORY_2}} ({{N}}H)
3. ...

---

## Self-Validation Results

Per `rules/recursive-validation.md`, Move 2 checklist:

| # | Criterion | Status | Note |
|---|-----------|:------:|------|
| 2.1 | Every H/M/L rating cites specific evidence | {{PASS/FAIL}} | {{NOTE}} |
| 2.2 | Every rating includes confidence level | {{PASS/FAIL}} | {{NOTE}} |
| 2.3 | All four factors assessed per territory | {{PASS/FAIL}} | {{NOTE}} |
| 2.4 | Hot threshold correct (2+ Highs) | {{PASS/FAIL}} | {{NOTE}} |
| 2.5 | Validation levels labeled | {{PASS/FAIL}} | {{NOTE}} |
| 2.6 | Domain-level rationale provided | {{PASS/FAIL}} | {{NOTE}} |
| 2.7 | Hot count in expected range or deviation explained | {{PASS/FAIL}} | {{NOTE}} |

**Iterations:** {{N}}
**Final status:** {{ALL PASS / N unresolvable issues}}

---

## JSON Output

Write `move2_output.json` per the Move 2 schema in `rules/json-handoff-schema.md`. Include all hot territories with their ratings (each with H/M/L level and confidence), high_count, and totals.
