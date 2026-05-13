# ODI: Core Job Statements

A core job statement is ONE functional job. One verb, one object, one context.

## Format

`When [context/situation], [verb] [object of the job] [clarifying phrase].`

## Rules

- Never use "while" clauses. If you wrote "minimize X while minimizing Y," the second objective is an outcome statement, not part of the job. Split it.
- Never join two objectives with "and." Pick the primary job; move the other to outcomes.
- Write from the executor's perspective, not a solution's. If it reads like product positioning, rewrite as what the executor is trying to accomplish.
- The job must be stable across solution changes. Ask: "Would this statement be true 10 years from now regardless of technology?"

## Job framing, not responsibility framing

Frame jobs as what the executor is *trying to accomplish* (goal), not as organizational accountability (responsibility). Responsibility framing mirrors org charts and pulls outcome statements toward tasks.

- "Manage X" or "Oversee X" = responsibility framing. Rewrite as goal language.
- "Ensure Y," "Protect Y," "Produce Y" = job framing. Preferred.

**Note:** Goal framing is necessary but not sufficient. You can write goal-framed statements for activities ("Ensure transactions are captured accurately") that still represent means, not ends. After reframing verbs, apply the ends-vs-means test (see `odi-ends-vs-means.md`) to verify the job is an end-state, not a goal-framed activity.

| Responsibility framing (avoid) | Job framing (use) |
|---|---|
| Manage Financial Risk | Protect the organization's financial position from preventable losses |
| Manage Treasury & Cash Operations | Ensure the organization can fund its operations and growth obligations |
| Manage Transaction Processing Operations | Ensure revenue and expense transactions are captured accurately and completely |

## Boundary rules are required

Every job at the Core Job level must include explicit boundary rules with three components:

1. **Owns:** What activities and decisions belong to this job
2. **Does not own:** What adjacent activities belong to other jobs (name them)
3. **Boundary test:** A single-sentence heuristic for resolving ambiguity (e.g., "If there's an external authority requiring it, it's C5; if it's about protecting against a potential loss, it's C3")

## Job breadth after merges

When merging two candidate jobs, check whether the result is too broad. Warning signs:
- The boundary rule uses "full spectrum" language
- Outcome statements under the job would cluster into two disconnected groups with nothing linking them
- Sub-domain mapping naturally splits the job into two coherent halves

If outcome clusters under one job are disconnected, the job is too broad. Split it.

## Quick test

If describing the job requires "and" or "while," it's compound. The secondary clause becomes an outcome statement.

**Bad:** "Minimize non-compliance penalties while minimizing the cost of compliance oversight"
**Good:** "Ensure indirect tax obligations are correctly fulfilled across all applicable jurisdictions"
