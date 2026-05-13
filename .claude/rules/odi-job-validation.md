# ODI: Job Validation

Every Core Job and Domain must pass three tests before proceeding. If any test fails, resolve before moving forward. After the candidate set passes all three, run the ends-vs-means test (see `odi-ends-vs-means.md`) to verify the set decomposes by end-states, not activities.

## Test 1: Universality

"If this job disappeared, would the role be fundamentally different — for *every* executor in the segment?"

- If yes → passes
- If only some executors have this job → fails. Either narrow the segment definition or demote to sub-domain
- Current priorities and initiatives are not jobs. "Lead Digital Transformation" fails universality because it's a temporary initiative, not an enduring responsibility

## Test 2: Mutual exclusivity

"Do the activities in this job overlap with activities in another job?"

- If overlap exists → merge the jobs, or tighten boundary rules until a clean single-sentence heuristic separates them
- The test is on *activities*, not *data*. Two jobs can use the same data (e.g., financial statements) as long as they do different things with it

## Test 3: Data support

"Can I map this job to a specific APQC PCF Level 2 process + 3 additional independent sources?"

- Required sources: APQC PCF mapping, plus 3 from different source categories (Big 4 frameworks, professional associations, academic/survey research)
- If no APQC L2 match exists → the job may not be a standard financial function. Evaluate whether it belongs in a domain or enabler layer instead

## Test 4: Ends vs. means

"Is the candidate set decomposed by executor end-states, or by activities that serve a shared end-state?"

- Run this test on the **full set** of candidates after each passes Tests 1–3 individually
- If candidates form a sequential chain where each output feeds the next → likely activity-level decomposition
- If a single Conclude step could evaluate success across multiple candidates → likely one job, not many
- APQC confirms that candidates represent real activities; it does not confirm they are independent jobs

See `odi-ends-vs-means.md` for the full test, supporting questions, warning signs, and resolution pattern.

## Resolution patterns

When a candidate job fails:

| Failure | Resolution |
|---|---|
| Failed universality, real for some executors | Demote to sub-domain or flag as segment-conditional |
| Failed universality, current initiative | Move to enabler layer or exclude entirely |
| Failed mutual exclusivity, heavy overlap | Merge into the broader job; expand its boundary rules |
| Failed data support, no APQC match | Evaluate as cross-cutting enabler or domain, not a core job |
| Failed ends-vs-means, activity-level decomposition | Identify the actual end-state job; recast candidates as steps or sub-jobs within it (see `odi-ends-vs-means.md`) |

## Document exclusions

Every candidate job that was considered and excluded must be documented with the specific test it failed and how it was resolved (merged, demoted, excluded). This creates an audit trail and prevents re-litigating settled decisions.

## Source diversity

Do not rely on a single survey or source for more than half of your segment-specific evidence across all jobs. If one source dominates, actively seek additional sources to triangulate. Single-source bias propagates across the entire framework.
