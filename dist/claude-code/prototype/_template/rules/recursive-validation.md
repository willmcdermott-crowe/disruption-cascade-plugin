# Recursive Self-Validation Protocol

After drafting a move's output, the sub-agent runs a validation loop before writing the JSON handoff. This catches rule violations before the coordinator reviews the work.

---

## Protocol (5 Steps)

### Step 1: Identify Applicable Rules

Consult the per-move checklist below. Each move has a specific set of criteria based on the ODI rules and disruption cascade rules that apply to it.

### Step 2: Check Each Criterion

For every criterion in the checklist, verify the drafted output against it. Record PASS, FAIL, or N/A with a brief note.

### Step 3: Fix Violations

For each FAIL, revise the drafted output to resolve the violation. If a violation cannot be resolved (e.g., evidence not found despite research), document it as UNRESOLVABLE with an explanation.

### Step 4: Re-Check

After fixing, re-run the checklist. Repeat Steps 2-3 until all criteria pass or remaining issues are documented as unresolvable. Maximum 3 iterations — if issues persist after 3 passes, document them and proceed.

### Step 5: Write Validation Summary

Add the results to the `## Self-Validation Results` section in the markdown file, and include validation status in the JSON output.

---

## Per-Move Checklists

### Move 1: Territory Map

| # | Criterion | Rule Source |
|---|-----------|------------|
| 1.1 | Every core job passes universality test | `odi-job-validation.md` |
| 1.2 | Every core job passes mutual exclusivity test | `odi-job-validation.md` |
| 1.3 | Every core job passes data support test (APQC L2 + 3 sources) | `odi-job-validation.md` |
| 1.4 | Candidate set passes ends-vs-means test | `odi-ends-vs-means.md` |
| 1.5 | Every core job statement: single functional job, no "while"/"and" | `odi-core-job-statements.md` |
| 1.6 | Every core job uses goal framing (Ensure/Protect/Produce), not responsibility framing | `odi-core-job-statements.md` |
| 1.7 | Every core job has boundary rules (Owns / Does not own / Boundary test) | `odi-core-job-statements.md` |
| 1.8 | Every domain passes all three validation tests | `odi-job-validation.md` |
| 1.9 | Every domain has 3+ cited sources from different categories | `disruption-cascade-rules.md` |
| 1.10 | All excluded candidates documented with failure reason and resolution | `odi-job-validation.md` |
| 1.11 | Blurred boundary intersections flagged as high-priority | `odi-job-map-structure.md` |

### Move 2: Disruption Screen

| # | Criterion | Rule Source |
|---|-----------|------------|
| 2.1 | Every H/M/L rating cites specific evidence | `disruption-cascade-rules.md` |
| 2.2 | Every H/M/L rating includes a confidence level (High/Medium/Low) | `disruption-cascade-rules.md` |
| 2.3 | All four factors assessed for every territory (Automation, Optionality, Regulatory, Cost) | Move 2 template |
| 2.4 | Hot territory threshold correct (2+ Highs) | Move 2 template |
| 2.5 | Validation levels labeled (VALIDATED/INFERRED/NOT FOUND) | `disruption-cascade-rules.md` |
| 2.6 | Domain-level screening rationale provided before territory-level | Move 2 template |
| 2.7 | Hot territory count within expected range (4-8) or deviation explained | Move 2 template |

### Move 3: Temporal Filter

| # | Criterion | Rule Source |
|---|-----------|------------|
| 3.1 | 2-3 data points cited per territory | `disruption-cascade-rules.md` |
| 3.2 | Stage definitions correctly applied (Complete >70%, In Progress 30-70%, Emerging <30%) | Move 3 template |
| 3.3 | Every stage assessment includes a confidence level | `disruption-cascade-rules.md` |
| 3.4 | At least 1 territory assessed as In Progress | Workflow gate |
| 3.5 | Calibration example provided (what "Complete" looks like) | Move 3 template |
| 3.6 | Priority ranking explained with rationale | Move 3 template |

### Move 4: Build Level

| # | Criterion | Rule Source |
|---|-----------|------------|
| 4.1 | Three frameworks (ODI, APQC, Subject matter) not conflated | `disruption-cascade-rules.md` |
| 4.2 | Axis transitions explicitly called out in hierarchy traces | `disruption-cascade-rules.md` |
| 4.3 | Build level targets client level, not solution provider level | `odi-abstraction-level.md` |
| 4.4 | 60% overlap threshold evidence-based (process step comparison + market validation) | `disruption-cascade-rules.md` |
| 4.5 | Cross-cutting capabilities handled as domains, not jobs | `odi-job-map-structure.md` |
| 4.6 | APQC codes verified, not fabricated | `disruption-cascade-rules.md` |
| 4.7 | All rule check table items pass | Move 4 template |

### Move 5: Demand Validation

| # | Criterion | Rule Source |
|---|-----------|------------|
| 5.1 | Core job statement: single job, goal framing, boundary rules, no compounds | `odi-core-job-statements.md` |
| 5.2 | Every outcome passes solution-free test | `odi-outcome-statements.md` |
| 5.3 | Every outcome measures a metric, not a task | `odi-outcome-statements.md` |
| 5.4 | Outcomes are MECE across steps (no identical scoring for same reason) | `odi-outcome-statements.md` |
| 5.5 | Every outcome placed in correct step per boundary definitions | `odi-job-map-structure.md` |
| 5.6 | Conclude step evaluates job success, not downstream handoff | `odi-job-map-structure.md` |
| 5.7 | One executor per map — all outcomes describe same person | `odi-executor-discipline.md` |
| 5.8 | Emotional and social jobs included per executor | `odi-executor-discipline.md` |
| 5.9 | 1-10 scale used (not 1-5) | `odi-scoring.md` |
| 5.10 | Analyst scores labeled as hypotheses | `odi-scoring.md` |
| 5.11 | Satisfaction scores show reasonable variance (<60% sharing same score) | `odi-scoring.md` |
| 5.12 | Each score cites at least one data point | `odi-scoring.md` |
| 5.13 | Every Importance and Satisfaction score includes confidence level | `disruption-cascade-rules.md` |
| 5.14 | No single source >50% of segment-specific evidence | `odi-scoring.md` |
| 5.15 | 3+ independent sources per executor map from different categories | `odi-scoring.md` |

### Move 6: Opportunity Analysis

| # | Criterion | Rule Source |
|---|-----------|------------|
| 6.1 | Logic chain (WHO/WHAT/WHERE/WHY/HOW) cites evidence from all prior moves | Move 6 template |
| 6.2 | Every rubric dimension score (1-10) is evidence-backed | `odi-scoring.md` |
| 6.3 | Every rubric dimension score includes confidence level | `disruption-cascade-rules.md` |
| 6.4 | Composite score correctly calculated (weighted average) | Move 6 template |
| 6.5 | GO/NO-GO recommendation matches threshold (>=5 for GO) | Workflow gate |
| 6.6 | Alternative investment targets analyzed with specific weaknesses | Move 6 template |
| 6.7 | Key assumptions that could invalidate thesis are documented | Move 6 template |

---

## Validation Summary Template

Use this format in the `## Self-Validation Results` section:

```markdown
| # | Criterion | Status | Note |
|---|-----------|:------:|------|
| X.1 | [criterion description] | PASS/FAIL | [brief note] |
| ... | ... | ... | ... |

**Iterations:** {{N}} (max 3)
**Final status:** {{ALL PASS / N unresolvable issues}}
**Unresolvable issues:** {{list if any, with explanation}}
```
