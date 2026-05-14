# ODI: Scoring

## Scale

Use **1–10** for both Importance and Satisfaction. Never use 1–5 — it compresses granularity and loses the distinction between "bad workaround exists" and "no solution exists."

## Formula

`Opportunity = Importance + max(Importance - Satisfaction, 0)`

- Scores above 10 = underserved (opportunity)
- Scores at or below 10 = appropriately served or overserved

## Analyst-assigned scores are hypotheses

True ODI scores come from quantitative surveys of a statistically significant executor sample. When assigning scores from secondary research:

- Label the column "Hypothesized Opp Score," not "Opp Score"
- Treat as directional input for prioritizing which outcomes to validate first
- Do not use for innovation investment decisions without survey validation

## Score each outcome independently

Never let the overall severity of the problem space bleed into individual scores. Challenge batch-scoring by asking for each outcome: "For this specific outcome, does a partial workaround exist that a respondent might rate 4–6?"

**Uniformity test:** If >60% of outcomes in a single map share the same Satisfaction score, review each individually. Uniform scores usually mean you scored the problem space, not the individual outcomes.

## Evidence requirements

- Each score must cite at least one specific data point
- Distinguish "no solution exists" (Sat 1–3) from "solutions exist but perform poorly" (Sat 4–6)
- Note when evidence comes from the specific executor population vs. adjacent populations
- No single survey or source should provide more than half of segment-specific evidence across all outcomes. If one source dominates, actively seek additional sources to triangulate

## Validation requirements

- Each Core Job requires 3+ independent sources (APQC, Big 4, professional associations, academic)
- Each Domain requires 3+ independent sources confirming standard terminology
- If validation fails, reconceive — do not proceed on unvalidated foundations
