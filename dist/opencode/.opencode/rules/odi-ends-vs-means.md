# ODI: Ends vs. Means Test

The three validation tests (universality, mutual exclusivity, data support) evaluate candidate jobs individually. This test evaluates whether the **set** of candidate jobs is decomposed at the right level — end-states the executor is trying to achieve, not activities the executor performs to achieve them.

## The problem

Process frameworks (APQC, value chains, internal workflows) decompose work into activities. ODI decomposes work into jobs — independent end-states an executor is trying to achieve. These produce different structures:

- **Activity decomposition:** "Capture the transaction → Determine the tax → Remit the payment → Report the results" — a sequence of dependent steps toward one goal
- **Job decomposition:** "Ensure tax obligations are fulfilled" and "Protect the organization from financial loss" — independent goals that happen to share some inputs

Activity decomposition passes the existing tests. Each activity is universal (every executor does it), mutually exclusive (clean boundaries between steps), and data-supported (APQC maps activities). But passing those tests does not make them independent jobs.

## The test

For any set of candidate Core Jobs, ask:

**"If the executor could only describe what they're trying to accomplish in one sentence, would multiple candidates collapse into that sentence?"**

If yes, the candidates are means (steps/activities) toward a single end (job). The sentence they collapse into is the actual job. The candidates become steps in the job map or sub-jobs within it.

### Supporting questions

| Question | If yes → | If no → |
|---|---|---|
| Does Candidate A's output become Candidate B's required input? | Likely sequential steps in one job | May be independent jobs |
| Would failure of Candidate A make Candidate B meaningless? | Likely the same job | May be independent jobs |
| Does the executor experience these as "phases of my work" rather than "different things I'm responsible for"? | Likely the same job | May be independent jobs |
| Could you write a single Conclude step that evaluates success across all candidates? | Likely the same job | Likely independent jobs |

All four questions pointing the same direction is strong signal. Mixed results require judgment — document the reasoning either way.

## The APQC trap

APQC PCF is a process classification framework. It tells you how organizations structure activities, not what executors are trying to accomplish. Using APQC as a primary validation source for job independence creates a specific failure mode:

- APQC Level 2 processes map cleanly to candidate jobs → feels like validation
- But APQC decomposes by activity, not by executor end-state
- So the "validation" may confirm that you've correctly identified real activities while missing that those activities serve a single job

**Revised role of APQC in validation:** APQC confirms that a candidate represents a *real, recognized activity*. It does not confirm that the activity is an *independent job*. Use APQC to verify that your decomposition maps to real work, then apply the ends-vs-means test separately to determine whether that work constitutes one job or many.

This also applies to other process-oriented frameworks (value chains, capability models, maturity models). Any framework that organizes by "what gets done" rather than "what the executor is trying to achieve" has the same limitation.

## Warning signs of activity-level decomposition

- **Sequential dependency:** Candidates form a natural sequence where each feeds the next
- **Shared executor goal:** All candidates serve the same ultimate purpose from the executor's perspective
- **Clean boundaries that follow process flow:** Boundary rules read like handoff points between process steps rather than separations between independent goals
- **Uniform validation sources:** The same APQC branch or the same industry framework validates all candidates (suggesting they're sub-processes of one process, not independent jobs)
- **Conclude steps that evaluate handoff quality:** If a candidate's Conclude step measures "ready for the next step" rather than "this job succeeded independently," it's a step, not a job

## Resolution

When the ends-vs-means test reveals activity-level decomposition:

1. **Identify the actual job.** Write the one-sentence end-state that the candidates collectively serve.
2. **Recast candidates as job map content.** Former "jobs" may become steps, sub-jobs, or domains depending on their nature.
3. **Re-validate the new job.** The consolidated job must still pass universality, mutual exclusivity, and data support — but now data support should emphasize job-level sources (executor research, JTBD literature) over process-level sources (APQC alone).
4. **Check for over-consolidation.** If the new job fails the breadth test in `odi-core-job-statements.md` (disconnected outcome clusters, "full spectrum" boundary language), you've gone too far. Find the natural split point — but the split should be between end-states, not between activities.

## Relationship to other rules

- **`odi-job-validation.md`:** The three existing tests remain necessary but are no longer sufficient. Run ends-vs-means after a candidate set passes all three.
- **`odi-core-job-statements.md`:** Job framing (goal language) reduces but does not eliminate the risk. You can write goal-framed statements for activities ("Ensure transactions are captured accurately") that still represent means, not ends.
- **`odi-job-map-structure.md`:** When candidates are recast as steps, use the step boundary definitions to place them correctly.
- **`odi-checklist.md`:** Add an ends-vs-means check to the job validation section.

## Example

Consider three candidate jobs for a tax compliance executor:

- C1: "Ensure all taxable transactions are identified and classified correctly"
- C2: "Ensure tax obligations are calculated and remitted accurately"
- C3: "Ensure tax positions are documented and defensible under examination"

These pass universality (every executor has them), mutual exclusivity (clean boundaries: identification → calculation → defense), and data support (each maps to distinct APQC processes).

**Ends-vs-means test:** If you ask the executor "what are you trying to accomplish?", they say: "I need to make sure we're compliant — that we find everything that's taxable, pay the right amount, and can defend it if we're audited." That's one job with three phases, not three independent jobs. C1's output feeds C2, C2's output feeds C3, and a single Conclude step ("Are we audit-ready and compliant?") evaluates all three.

**Resolution:** The actual job is something like "Ensure the organization's indirect tax obligations are correctly fulfilled and defensible." C1, C2, and C3 become steps or sub-jobs within that job map.
