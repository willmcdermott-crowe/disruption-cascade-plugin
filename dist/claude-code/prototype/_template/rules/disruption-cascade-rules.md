# Disruption Cascade Rules

Governs the Disruption Cascade v4 workflow across Moves 2, 3, 4, and 6. Operates alongside the ODI rules in `.claude/rules/odi-*.md`. When there is a conflict, ODI rules take precedence.

---

## The Three Frameworks

Three distinct frameworks structure this analysis. They must never be conflated:

| Framework | What It Structures | Used In |
|-----------|-------------------|---------|
| **ODI/JTBD** | The job side — what the executor is trying to accomplish | Moves 1, 5 |
| **APQC PCF** | The process/domain side — how activities are organized | Moves 1, 4 |
| **Subject matter classification** | The content side — what is being processed or transformed | Move 4 |

**Conflation violations (fail gate):**
- Do NOT nest subject matter types inside JTBD job steps
- Do NOT nest JTBD steps inside APQC process hierarchy
- Do NOT use APQC as a proxy for JTBD job structure

---

## Move 2: Disruption Screening

### The Four Disruption Factors

Screen every territory on these four factors from the target executor's perspective:

| Factor | High (Exposed) | Low (Protected) |
|--------|----------------|-----------------|
| **Automation Readiness** | Rule-determined, data-structured, AI/ML engines exist or deployed | Judgment-heavy, ambiguous, bespoke, requires human discretion |
| **Optionality** | Multiple powerful platforms, self-service viable, many competing tools | Few alternatives, high complexity, executor cannot easily self-serve |
| **Regulatory Tailwind** | New rules expanding scope/volume/complexity, growing compliance burden | Stable regulatory environment, flat or declining burden |
| **Cost Burden** | High spend, growing costs, significant staff/technology investment | Low spend, stable costs, minimal resource drain |

### Hot Territory Threshold

A territory is **hot** if it has **2 or more High ratings** across the four factors.

Expected range: 4–8 hot territories for a typical matrix. If fewer than 4, review for over-conservatism. If more than 8, review for under-discrimination. Document deviations.

### Evidence Standard

- Every H/M/L rating must cite specific evidence — named source, data point, or observable market fact
- Every rating must include a confidence level (High/Medium/Low) based on source quality
- High confidence requires 2+ independent sources
- Do NOT assign from memory or general industry knowledge without citation

---

## Move 3: Temporal Filter

### Disruption Stage Definitions

| Stage | Adoption Level | Window |
|-------|---------------|--------|
| **Emerging** | <30% adopted — early tools only, no dominant approach | Too early — timing bet |
| **In Progress** | 30–70% adopted — multiple vendors gaining share, no single winner | Open — act now |
| **Complete** | >70% adopted — dominant player(s) have won, market consolidated | Closed — too late |

### Hard Stop Rule

**At least one hot territory must be In Progress.** If all are Complete or Emerging, the cascade cannot proceed. Report findings and offer to: (a) pivot to a different segment/role, or (b) revisit Move 2 screening criteria.

### Evidence Standard

Cite 2–3 data points per territory. Acceptable: adoption rate data, market share reports, vendor landscape analyses, analyst estimates. Label estimates as "directional" when sourced from non-primary data.

---

## Move 4: Build Level

### The 60% Overlap Threshold

1. Identify sibling nodes at the subject matter classification level
2. Assess outcome overlap with siblings via process step comparison and vendor product architecture
3. Apply threshold:
   - **Overlap ≥ 60% with siblings** → build one level up (platform opportunity)
   - **Overlap < 60%** → build at current level (point solution)

Overlap must be evidence-based, not assumed. Vendor product architectures are the primary market validation source.

### Abstraction Level Rule

Build at the **client level** — the executor as job performer — not the solution provider level. See `odi-abstraction-level.md`.

### Required Gate Checks (all must pass before proceeding)

- [ ] ODI/JTBD, APQC PCF, and subject matter classification are not conflated
- [ ] Build level targets the client (executor), not the service provider
- [ ] 60% overlap threshold is evidence-based with documented calculation
- [ ] Cross-cutting capabilities handled as domains, not jobs

---

## Move 6: Thesis Scoring Rubric

Score on five weighted dimensions using 1–10 scale. Each score must cite evidence from move outputs.

| Dimension | Weight | 8–10 | 4–7 | 1–3 |
|-----------|--------|------|-----|-----|
| **Market Disruption Signal** | 25% | 3+ hot territories, high confidence | 2 hot, mixed confidence | 1 hot, weak evidence |
| **Timing Window** | 20% | Multiple In Progress territories | 1 In Progress | All Complete or Emerging |
| **Demand Evidence** | 25% | Multiple executors, high opportunity scores, 3+ sources each | 1–2 executors, moderate scores | Weak job maps, low scores |
| **Build Level Defensibility** | 15% | Platform opportunity confirmed, strong overlap evidence | Point solution, some competitive risk | No clear differentiation |
| **Strategic Fit** | 15% | Clear entry point, differentiated offering, strong logic chain | Moderate fit, some gaps | Unclear entry, weak chain |

### Composite Score → Recommendation

| Composite Score | Recommendation |
|-----------------|----------------|
| 8–10 | **GO** — Strong conviction, proceed to validation |
| 5–7 | **CONDITIONAL GO** — List explicit conditions that must be resolved before proceeding |
| 1–4 | **NO-GO** — Revisit assumptions or pivot |

**Hard floor:** The agent cannot recommend GO with a composite score below 5. A CONDITIONAL GO must list each condition explicitly.

Each dimension score must cite at least one specific data point from the move outputs. Composite score = Σ(score × weight) across all five dimensions.
