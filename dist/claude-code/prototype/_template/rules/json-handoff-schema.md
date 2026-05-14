# JSON Handoff Schema

Each move (1-5) produces a `move{N}_output.json` file alongside its markdown. The coordinator passes JSON contents — not markdown Output sections — to the next sub-agent. This reduces context window usage by ~60% compared to parsing markdown.

---

## Protocol

1. After completing the markdown output, the sub-agent writes a `move{N}_output.json` file in the run folder.
2. The coordinator reads the JSON file and passes its contents as the `## Input` block for the next sub-agent.
3. Move 6 receives all 5 JSON files (assembled by coordinator).
4. The JSON is the **authoritative handoff** — the markdown Output section remains for human review only.

---

## Move 1: Territory Map

```json
{
  "move": 1,
  "target": {
    "role": "{{C_SUITE_ROLE}}",
    "segment": "{{SEGMENT}}"
  },
  "jobs": [
    {
      "id": "C1",
      "name": "{{JOB_NAME}}",
      "statement": "When [context], [goal verb] [object] [clarifying phrase].",
      "boundary_test": "{{SINGLE_SENTENCE_HEURISTIC}}"
    }
  ],
  "domains": [
    {
      "id": "D1",
      "name": "{{DOMAIN_NAME}}",
      "definition": "{{DOMAIN_DEFINITION}}"
    }
  ],
  "territory_count": 0,
  "blurred_boundaries": [
    {
      "territory": "{{C_x_D}}",
      "jobs_involved": ["C1", "C2"],
      "reason": "{{WHY_BLURRED}}"
    }
  ]
}
```

---

## Move 2: Disruption Screen

```json
{
  "move": 2,
  "hot_territories": [
    {
      "id": "C1xD3",
      "label": "{{JOB_NAME}} x {{DOMAIN_NAME}}",
      "ratings": {
        "automation": { "level": "H", "confidence": "high" },
        "optionality": { "level": "M", "confidence": "medium" },
        "regulatory": { "level": "H", "confidence": "high" },
        "cost": { "level": "H", "confidence": "low" }
      },
      "high_count": 3
    }
  ],
  "totals": {
    "territories_screened": 0,
    "hot_count": 0,
    "narrowly_missed_count": 0
  }
}
```

---

## Move 3: Temporal Filter

```json
{
  "move": 3,
  "priority_targets": [
    {
      "id": "C1xD3",
      "label": "{{JOB_NAME}} x {{DOMAIN_NAME}}",
      "stage": "in_progress",
      "adoption_estimate": "30-50%",
      "confidence": "medium",
      "rank": 1
    }
  ]
}
```

---

## Move 4: Build Level

```json
{
  "move": 4,
  "primary": {
    "build_level": "{{BUILD_LEVEL}}",
    "entry_point": "{{ENTRY_POINT}}",
    "overlap_pct": 0,
    "converging_territories": ["C1xD3", "C2xD3", "C3xD3"]
  },
  "secondary_targets": [
    {
      "territory": "C1xD5",
      "relationship": "{{RELATIONSHIP}}",
      "build_level": "{{BUILD_LEVEL}}"
    }
  ]
}
```

---

## Move 5: Demand Validation

```json
{
  "move": 5,
  "executors": [
    {
      "id": 1,
      "name": "{{EXECUTOR_NAME}}",
      "core_job": "{{CORE_JOB_STATEMENT}}",
      "outcomes_scored": 0,
      "avg_opportunity": 0.0,
      "top_outcomes_gte_15": 0
    }
  ],
  "top_15_outcomes": [
    {
      "id": "1.3.2",
      "statement": "Minimize the time it takes to...",
      "executor": "{{EXECUTOR_NAME}}",
      "step": "Prepare",
      "importance": { "score": 9, "confidence": "high" },
      "satisfaction": { "score": 3, "confidence": "medium" },
      "opportunity": 15
    }
  ],
  "investment_target": {
    "where": "{{BUILD_LEVEL}}",
    "who": ["{{EXECUTOR_1}}", "{{EXECUTOR_2}}"],
    "what": "{{KEY_CAPABILITIES}}",
    "enter": "{{ENTRY_POINT}}",
    "lead_with": "{{VALUE_PROPOSITION}}"
  }
}
```

---

## Move 6: No JSON

Move 6 is the terminal move. It produces the final markdown output (opportunity analysis + go/no-go recommendation) but no JSON handoff file. The executive summary is assembled by the coordinator after Move 6 completes.

---

## Validation Rules

- All JSON must be valid (parseable by any JSON parser).
- Field names use snake_case.
- Confidence values are lowercase strings: `"high"`, `"medium"`, `"low"`.
- H/M/L ratings are uppercase single characters: `"H"`, `"M"`, `"L"`.
- Stage values are lowercase: `"complete"`, `"in_progress"`, `"emerging"`.
- Arrays preserve the ordering from the markdown (ranked/priority order).
- The `id` field for territories uses the `CxDy` convention (e.g., `C1xD3`).
