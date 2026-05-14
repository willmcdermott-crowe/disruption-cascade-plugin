# ODI: Job Map Structure

## Step purposes (use these to place outcomes correctly)

| Step | Outcomes measure... |
|------|-------------------|
| Define | Completeness/accuracy of the executor's understanding of what needs to be done |
| Locate | Speed/reliability of finding needed inputs, resources, and information |
| Prepare | Readiness of inputs and conditions for execution |
| Confirm | Accuracy of verification before the point of no return |
| Execute | Speed/reliability of the core action itself |
| Monitor | Speed/reliability of detecting problems post-execution |
| Modify | Speed/reliability of fixing errors or adapting to change |
| Conclude | Assessment of job completion quality and readiness for next cycle |

## Boundary rules

- If a Locate outcome describes making a determination (not just finding information), move it to Confirm.
- If a Conclude outcome describes downstream handoff work (not evaluating this job's success), it likely belongs in a separate job map.

## The Conclude step trap

Conclude answers: "Did I do the job well?" It does NOT capture "what happens next."

These are separate jobs, not Conclude outcomes:
- Reconciliation for downstream reporting
- Audit documentation preparation
- Period close and handoff to another executor

## Hierarchy

```
Core Job × Domain = Territory
└── Sub-domain (where Job Maps live)
    └── Job Map (8 steps) → Outcome Statements
        ├── Emotional Jobs (per executor)
        └── Social Jobs (per executor)
```

Sub-domains are the working unit. The matrix gives territory; sub-domains are where you do the work.

## Cross-cutting capabilities belong in the domain layer

When a capability (e.g., technology, data management) intersects every job, do not create a separate job for it. Represent it as a domain. The job-domain intersections in the territory matrix capture the specific decisions naturally (e.g., C2 × D12 = close automation, C5 × D12 = tax engine selection). Do not invent a separate "enabler" entity type — the domain layer handles this.

## Flag blurred boundary intersections

When two Core Jobs share a boundary that blurs at the executor level (e.g., the person processing a transaction is also making a tax determination), flag that intersection in the territory matrix as high-priority. These intersections often produce the richest outcome maps because the executor experiences both jobs simultaneously and current solutions serve neither well.
