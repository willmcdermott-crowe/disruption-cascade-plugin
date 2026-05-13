#!/usr/bin/env python3
"""
Disruption Cascade — Deterministic Validation Suite

Checks JSON handoff files after each move for structural integrity, math
correctness, and ODI rule compliance. Does not require external dependencies.

Usage:
    python tests/validate.py <run_folder>           # validate all completed moves
    python tests/validate.py <run_folder> --move N  # validate a specific move (1-6)

Examples:
    python tests/validate.py prototype/run_001_cfo_manufacturing/
    python tests/validate.py prototype/run_001_cfo_manufacturing/ --move 5

Exit codes:
    0  All checks pass (or only WARNINGs)
    1  One or more FAIL results
    2  Script error (bad arguments, missing run folder)
"""

import json
import re
import sys
import os
from pathlib import Path


# ── Result types ────────────────────────────────────────────────────────────

PASS = "PASS"
FAIL = "FAIL"
WARN = "WARN"
SKIP = "SKIP"

ICONS = {PASS: "✓", FAIL: "✗", WARN: "⚠", SKIP: "–"}


class Result:
    def __init__(self, status: str, message: str):
        self.status = status
        self.message = message

    def __repr__(self):
        return f"[{self.status}] {self.message}"


def passed(msg):  return Result(PASS, msg)
def failed(msg):  return Result(FAIL, msg)
def warned(msg):  return Result(WARN, msg)
def skipped(msg): return Result(SKIP, msg)


# ── Helpers ──────────────────────────────────────────────────────────────────

def load_json(path: Path):
    """Load and parse a JSON file. Returns (data, result)."""
    if not path.exists():
        return None, failed(f"File not found: {path.name}")
    try:
        with open(path) as f:
            data = json.load(f)
        return data, passed(f"JSON valid: {path.name}")
    except json.JSONDecodeError as e:
        return None, failed(f"JSON parse error in {path.name}: {e}")


def require_field(data: dict, field: str, label: str = ""):
    """Check that a required field exists and is not None/empty."""
    prefix = f"{label}." if label else ""
    if field not in data:
        return failed(f"Missing required field: {prefix}{field}")
    val = data[field]
    if val is None or val == "" or val == [] or val == {}:
        return failed(f"Field is empty: {prefix}{field}")
    return passed(f"Field present: {prefix}{field}")


def check_enum(value, allowed: list, label: str):
    """Check that a value is one of a set of allowed values."""
    if value not in allowed:
        return failed(f"{label} = {repr(value)!r}, expected one of {allowed}")
    return passed(f"{label} = {repr(value)!r} ✓")


def check_score_range(score, label: str, low=1, high=10):
    """Check that a numeric score is within a valid range."""
    try:
        s = float(score)
    except (TypeError, ValueError):
        return failed(f"{label} = {repr(score)!r} is not a number")
    if not (low <= s <= high):
        return failed(f"{label} = {s} is out of range [{low}–{high}]")
    return passed(f"{label} = {s} in range [{low}–{high}]")


CONFIDENCE_VALUES = ["high", "medium", "low"]
LEVEL_VALUES      = ["H", "M", "L"]
STAGE_VALUES      = ["complete", "in_progress", "emerging"]
OUTCOME_PREFIXES  = (
    "minimize the time it takes to",
    "minimize the likelihood of",
)


# ── Move 1 ───────────────────────────────────────────────────────────────────

def check_move1(run_dir: Path) -> list:
    results = []
    path = run_dir / "move1_output.json"

    data, load_result = load_json(path)
    results.append(load_result)
    if data is None:
        return results

    # Required top-level fields
    for field in ["move", "target", "jobs", "domains", "territory_count"]:
        results.append(require_field(data, field))

    # territory_count = jobs × domains
    jobs    = data.get("jobs", [])
    domains = data.get("domains", [])
    tc      = data.get("territory_count")
    if isinstance(tc, int) and isinstance(jobs, list) and isinstance(domains, list):
        expected = len(jobs) * len(domains)
        if tc == expected:
            results.append(passed(
                f"territory_count ({tc}) = {len(jobs)} jobs × {len(domains)} domains"
            ))
        else:
            results.append(failed(
                f"territory_count ({tc}) ≠ {len(jobs)} jobs × {len(domains)} domains "
                f"(expected {expected})"
            ))

    # At least 1 job and 1 domain
    if isinstance(jobs, list):
        if len(jobs) == 0:
            results.append(failed("jobs array is empty"))
        else:
            results.append(passed(f"{len(jobs)} jobs defined"))

    if isinstance(domains, list):
        if len(domains) == 0:
            results.append(failed("domains array is empty"))
        else:
            results.append(passed(f"{len(domains)} domains defined"))

    # Job field checks
    if isinstance(jobs, list):
        for job in jobs:
            jid = job.get("id", "?")
            for field in ["id", "name", "statement", "boundary_test"]:
                if field not in job:
                    results.append(failed(f"Job {jid}: missing field '{field}'"))

            # Compound connector check on statement
            stmt = job.get("statement", "")
            # "while" is a near-certain ODI violation in a job statement
            if re.search(r'\bwhile\b', stmt, re.IGNORECASE):
                results.append(warned(
                    f"Job {jid}: statement contains 'while' — possible compound job. "
                    f"Review: \"{stmt[:90]}...\""
                ))
            # "and" linking two verb phrases is a violation; noun-phrase "and" is fine.
            # Heuristic: flag if "and" appears between two verb-like clauses (ensure…and ensure, protect…and protect)
            if re.search(
                r'\b(ensure|protect|produce|maintain|provide|enable)\b.{5,80}\band\b.{5,80}'
                r'\b(ensure|protect|produce|maintain|provide|enable)\b',
                stmt, re.IGNORECASE
            ):
                results.append(warned(
                    f"Job {jid}: statement may join two objectives with 'and'. "
                    f"Review: \"{stmt[:90]}...\""
                ))

    # Domain field checks
    if isinstance(domains, list):
        for domain in domains:
            did = domain.get("id", "?")
            for field in ["id", "name", "definition"]:
                if field not in domain:
                    results.append(failed(f"Domain {did}: missing field '{field}'"))

    return results


# ── Move 2 ───────────────────────────────────────────────────────────────────

def check_move2(run_dir: Path) -> list:
    results = []
    path = run_dir / "move2_output.json"

    data, load_result = load_json(path)
    results.append(load_result)
    if data is None:
        return results

    for field in ["move", "hot_territories", "totals"]:
        results.append(require_field(data, field))

    hot = data.get("hot_territories", [])
    totals = data.get("totals", {})

    # hot_count in totals must match actual array length
    if isinstance(hot, list) and isinstance(totals, dict):
        stated_count = totals.get("hot_count")
        if stated_count is not None:
            if stated_count == len(hot):
                results.append(passed(
                    f"totals.hot_count ({stated_count}) matches hot_territories array length"
                ))
            else:
                results.append(failed(
                    f"totals.hot_count ({stated_count}) ≠ len(hot_territories) ({len(hot)})"
                ))

    # Every hot territory: required fields, valid level/confidence, high_count >= 2, high_count math
    FACTORS = ["automation", "optionality", "regulatory", "cost"]
    if isinstance(hot, list):
        for t in hot:
            tid = t.get("id", "?")
            for field in ["id", "label", "ratings", "high_count"]:
                if field not in t:
                    results.append(failed(f"Territory {tid}: missing field '{field}'"))
                    continue

            ratings = t.get("ratings", {})

            # All 4 factors must be present
            for factor in FACTORS:
                if factor not in ratings:
                    results.append(failed(f"Territory {tid}: missing rating for '{factor}'"))
                else:
                    r = ratings[factor]
                    results.append(check_enum(r.get("level"),      LEVEL_VALUES,      f"{tid}.{factor}.level"))
                    results.append(check_enum(r.get("confidence"),  CONFIDENCE_VALUES, f"{tid}.{factor}.confidence"))

            # high_count >= 2 (hot territory threshold)
            stated_high = t.get("high_count")
            if isinstance(stated_high, int):
                if stated_high < 2:
                    results.append(failed(
                        f"Territory {tid}: high_count ({stated_high}) < 2 — "
                        f"does not meet hot territory threshold"
                    ))

                # high_count must match actual count of "H" levels in ratings
                actual_high = sum(
                    1 for f in FACTORS
                    if isinstance(ratings.get(f), dict)
                    and ratings[f].get("level") == "H"
                )
                if stated_high == actual_high:
                    results.append(passed(f"Territory {tid}: high_count ({stated_high}) matches H-rating count"))
                else:
                    results.append(failed(
                        f"Territory {tid}: high_count ({stated_high}) ≠ "
                        f"actual H-rating count ({actual_high})"
                    ))

    return results


# ── Move 3 ───────────────────────────────────────────────────────────────────

def check_move3(run_dir: Path) -> list:
    results = []
    path = run_dir / "move3_output.json"

    data, load_result = load_json(path)
    results.append(load_result)
    if data is None:
        return results

    for field in ["move", "priority_targets"]:
        results.append(require_field(data, field))

    targets = data.get("priority_targets", [])

    if not isinstance(targets, list):
        results.append(failed("priority_targets is not an array"))
        return results

    # GATE: at least 1 in_progress (hard stop)
    in_progress = [t for t in targets if t.get("stage") == "in_progress"]
    if len(in_progress) >= 1:
        results.append(passed(
            f"GATE: {len(in_progress)} in_progress target(s) — window is open"
        ))
    else:
        results.append(failed(
            "GATE FAIL: No in_progress targets — "
            "all territories are Complete or Emerging. Hard stop."
        ))

    # gate_result counts must match actual counts (if field is present)
    gate = data.get("gate_result", {})
    if gate:
        actual_ip  = sum(1 for t in targets if t.get("stage") == "in_progress")
        actual_em  = sum(1 for t in targets if t.get("stage") == "emerging")
        actual_com = sum(1 for t in targets if t.get("stage") == "complete")

        for key, actual in [
            ("in_progress_count", actual_ip),
            ("emerging_count",    actual_em),
            ("complete_count",    actual_com),
        ]:
            stated = gate.get(key)
            if stated is not None:
                if stated == actual:
                    results.append(passed(f"gate_result.{key} ({stated}) matches actual count"))
                else:
                    results.append(failed(
                        f"gate_result.{key} ({stated}) ≠ actual count ({actual})"
                    ))

    # Per-target checks
    seen_ranks = []
    for t in targets:
        tid = t.get("id", "?")
        for field in ["id", "label", "stage", "confidence", "rank"]:
            if field not in t:
                results.append(failed(f"Target {tid}: missing field '{field}'"))

        results.append(check_enum(t.get("stage"),      STAGE_VALUES,      f"Target {tid}.stage"))
        results.append(check_enum(t.get("confidence"), CONFIDENCE_VALUES, f"Target {tid}.confidence"))

        rank = t.get("rank")
        if isinstance(rank, int):
            seen_ranks.append(rank)

    # Ranks must be sequential integers starting at 1
    if seen_ranks:
        expected_ranks = list(range(1, len(seen_ranks) + 1))
        if sorted(seen_ranks) == expected_ranks:
            results.append(passed(f"Ranks are sequential 1–{len(seen_ranks)}"))
        else:
            results.append(failed(
                f"Ranks are not sequential 1–{len(seen_ranks)}: found {sorted(seen_ranks)}"
            ))

    return results


# ── Move 4 ───────────────────────────────────────────────────────────────────

def check_move4(run_dir: Path) -> list:
    results = []
    path = run_dir / "move4_output.json"

    data, load_result = load_json(path)
    results.append(load_result)
    if data is None:
        return results

    for field in ["move", "primary"]:
        results.append(require_field(data, field))

    primary = data.get("primary", {})
    if isinstance(primary, dict):
        for field in ["build_level", "entry_point", "overlap_pct", "converging_territories"]:
            results.append(require_field(primary, field, label="primary"))

        # overlap_pct must be a number between 0 and 100
        pct = primary.get("overlap_pct")
        results.append(check_score_range(pct, "primary.overlap_pct", low=0, high=100))

        # If overlap_pct >= 60, build_level should indicate a platform/higher level
        if isinstance(pct, (int, float)) and pct >= 60:
            bl = str(primary.get("build_level", "")).lower()
            platform_signals = ["platform", "level up", "one level up", "domain"]
            if any(s in bl for s in platform_signals):
                results.append(passed(
                    f"overlap_pct ({pct}%) ≥ 60 and build_level indicates platform/higher level"
                ))
            else:
                results.append(warned(
                    f"overlap_pct ({pct}%) ≥ 60 but build_level "
                    f"({primary.get('build_level')!r}) does not clearly indicate "
                    f"a platform or higher-level recommendation. Review for correctness."
                ))

        # converging_territories must be a non-empty list
        ct = primary.get("converging_territories")
        if isinstance(ct, list):
            if len(ct) == 0:
                results.append(failed("primary.converging_territories is empty"))
            else:
                results.append(passed(f"primary.converging_territories has {len(ct)} entries"))

    return results


# ── Move 5 ───────────────────────────────────────────────────────────────────

def check_move5(run_dir: Path) -> list:
    results = []
    path = run_dir / "move5_output.json"

    data, load_result = load_json(path)
    results.append(load_result)
    if data is None:
        return results

    for field in ["move", "executors", "top_15_outcomes", "investment_target"]:
        results.append(require_field(data, field))

    executors = data.get("executors", [])
    outcomes  = data.get("top_15_outcomes", [])
    inv       = data.get("investment_target", {})

    # At least 1 executor
    if isinstance(executors, list):
        if len(executors) == 0:
            results.append(failed("executors array is empty"))
        else:
            results.append(passed(f"{len(executors)} executor(s) defined"))
        for ex in executors:
            eid = ex.get("name", ex.get("id", "?"))
            for field in ["id", "name", "core_job"]:
                if field not in ex:
                    results.append(failed(f"Executor '{eid}': missing field '{field}'"))

    # Outcomes: scoring math, statement format, confidence values
    math_errors = 0
    format_errors = 0
    if isinstance(outcomes, list):
        if len(outcomes) == 0:
            results.append(failed("top_15_outcomes array is empty"))

        for o in outcomes:
            oid = o.get("id", "?")

            # Statement format — must start with an allowed prefix
            stmt = str(o.get("statement", "")).strip().lower()
            if not any(stmt.startswith(prefix) for prefix in OUTCOME_PREFIXES):
                results.append(failed(
                    f"Outcome {oid}: statement does not start with "
                    f"'Minimize the time...' or 'Minimize the likelihood...': "
                    f"\"{o.get('statement', '')[:80]}\""
                ))
                format_errors += 1

            # Importance and satisfaction score range (must be 1-10, not 1-5)
            imp_obj  = o.get("importance", {})
            sat_obj  = o.get("satisfaction", {})
            imp = imp_obj.get("score") if isinstance(imp_obj, dict) else None
            sat = sat_obj.get("score") if isinstance(sat_obj, dict) else None

            if imp is not None:
                results.append(check_score_range(imp, f"Outcome {oid} importance.score"))
                if isinstance(imp, (int, float)) and 1 <= imp <= 5:
                    # Could be a 1-5 scale violation — warn if all scores cluster low
                    pass

            if sat is not None:
                results.append(check_score_range(sat, f"Outcome {oid} satisfaction.score"))

            # Confidence values
            for score_type, obj in [("importance", imp_obj), ("satisfaction", sat_obj)]:
                if isinstance(obj, dict):
                    conf = obj.get("confidence")
                    if conf is not None:
                        results.append(check_enum(
                            conf, CONFIDENCE_VALUES,
                            f"Outcome {oid} {score_type}.confidence"
                        ))

            # Opportunity math: opportunity = importance + max(importance - satisfaction, 0)
            stated_opp = o.get("opportunity")
            if imp is not None and sat is not None and stated_opp is not None:
                try:
                    expected_opp = imp + max(imp - sat, 0)
                    if abs(float(stated_opp) - expected_opp) < 0.01:
                        # Don't emit a pass for every outcome — it's too verbose
                        pass
                    else:
                        results.append(failed(
                            f"Outcome {oid}: opportunity math error — "
                            f"stated {stated_opp}, expected {expected_opp} "
                            f"(imp={imp}, sat={sat})"
                        ))
                        math_errors += 1
                except (TypeError, ValueError):
                    results.append(failed(
                        f"Outcome {oid}: could not compute opportunity score — "
                        f"non-numeric value (imp={imp}, sat={sat}, opp={stated_opp})"
                    ))

    # Summary lines for math and format (less noise than per-outcome pass lines)
    if math_errors == 0 and isinstance(outcomes, list) and len(outcomes) > 0:
        results.append(passed(
            f"Opportunity math correct for all {len(outcomes)} outcomes"
        ))
    if format_errors == 0 and isinstance(outcomes, list) and len(outcomes) > 0:
        results.append(passed(
            f"Outcome statement format correct for all {len(outcomes)} outcomes"
        ))

    # investment_target required fields
    if isinstance(inv, dict):
        for field in ["where", "who", "what", "enter", "lead_with"]:
            results.append(require_field(inv, field, label="investment_target"))

    # 1-5 scale detection: if ALL importance scores are <= 5, flag it
    if isinstance(outcomes, list) and len(outcomes) > 3:
        imp_scores = [
            o.get("importance", {}).get("score")
            for o in outcomes
            if isinstance(o.get("importance"), dict)
        ]
        valid_scores = [s for s in imp_scores if isinstance(s, (int, float))]
        if valid_scores and all(s <= 5 for s in valid_scores):
            results.append(failed(
                "All importance scores are ≤ 5 — possible 1-5 scale violation. "
                "ODI requires a 1-10 scale."
            ))

    return results


# ── Move 6 (markdown only — no JSON) ─────────────────────────────────────────

def check_move6(run_dir: Path) -> list:
    results = []
    path = run_dir / "move6_opportunity_analysis.md"

    if not path.exists():
        results.append(skipped("move6_opportunity_analysis.md not found — move 6 not complete"))
        return results

    results.append(passed("move6_opportunity_analysis.md exists"))
    text = path.read_text(encoding="utf-8", errors="replace")

    # Detect recommendation from authoritative lines only (score line, decision line,
    # or recommendation header). Avoids false matches in conditional/hypothetical text.
    REC_PATTERNS = [
        # "### Recommendation: CONDITIONAL GO" or "Recommendation: NO-GO"
        r'(?:^|\n)\s*#{1,4}\s*Recommendation\s*[:\-]\s*(CONDITIONAL\s+GO|NO-GO|GO)\b',
        # "DECISION: CONDITIONAL GO" or "└── DECISION: NO-GO"
        r'DECISION\s*[:\-]\s*(CONDITIONAL\s+GO|NO-GO|GO)\b',
        # "7.3/10 — CONDITIONAL GO" or "scores: 7.1/10 – NO-GO"
        r'\d+(?:\.\d+)?\s*/\s*10\s*[\-–—]+\s*(CONDITIONAL\s+GO|NO-GO|GO)\b',
        # "Thesis score ... -> CONDITIONAL GO"
        r'Thesis score[^\n]*?->\s*(CONDITIONAL\s+GO|NO-GO|GO)\b',
    ]
    recommendation = None
    for pattern in REC_PATTERNS:
        m = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if m:
            raw = m.group(1).strip().upper()
            recommendation = re.sub(r'\s+', ' ', raw)  # normalise whitespace
            break

    if recommendation:
        results.append(passed(f"Recommendation found: {recommendation}"))
    else:
        results.append(failed(
            "No GO / CONDITIONAL GO / NO-GO recommendation found in move6 output. "
            "Expected patterns: '### Recommendation: …', 'DECISION: …', or 'X/10 — …'"
        ))

    # Try to extract composite score (looks for patterns like "7.5/10", "score: 7.5", "7.5 out of 10")
    score_match = (
        re.search(r'composite[^\n]*?(\d+(?:\.\d+)?)\s*/\s*10', text, re.IGNORECASE) or
        re.search(r'(\d+(?:\.\d+)?)\s*/\s*10', text) or
        re.search(r'score[:\s]+(\d+(?:\.\d+)?)', text, re.IGNORECASE)
    )
    if score_match:
        try:
            score = float(score_match.group(1))
            results.append(passed(f"Composite score found: {score}/10"))
            # Cross-check score vs recommendation
            if recommendation == "NO-GO" and score >= 5:
                results.append(failed(
                    f"Score {score} ≥ 5 but recommendation is NO-GO — "
                    f"threshold violation (≥5 required for GO)"
                ))
            elif recommendation in ("GO", "CONDITIONAL GO") and score < 5:
                results.append(failed(
                    f"Score {score} < 5 but recommendation is {recommendation} — "
                    f"threshold violation (≥5 required for GO)"
                ))
            else:
                results.append(passed(
                    f"Score ({score}) is consistent with recommendation ({recommendation})"
                ))
        except ValueError:
            results.append(warned("Composite score found but could not parse as number"))
    else:
        results.append(warned(
            "Could not extract composite score from move6 output — verify manually"
        ))

    return results


# ── Orchestration ─────────────────────────────────────────────────────────────

MOVE_CHECKS = {
    1: check_move1,
    2: check_move2,
    3: check_move3,
    4: check_move4,
    5: check_move5,
    6: check_move6,
}

MOVE_LABELS = {
    1: "Move 1 — Territory Map",
    2: "Move 2 — Disruption Screen",
    3: "Move 3 — Temporal Filter",
    4: "Move 4 — Build Level",
    5: "Move 5 — Demand Validation",
    6: "Move 6 — Opportunity Analysis",
}


def run_move(move_num: int, run_dir: Path) -> tuple:
    """Run checks for a single move. Returns (results, fail_count, warn_count)."""
    check_fn = MOVE_CHECKS[move_num]
    results  = check_fn(run_dir)
    fails    = sum(1 for r in results if r.status == FAIL)
    warns    = sum(1 for r in results if r.status == WARN)
    return results, fails, warns


def print_move_results(move_num: int, results: list, fails: int, warns: int):
    label = MOVE_LABELS[move_num]
    bar   = "─" * (len(label) + 4)
    print(f"\n{bar}")
    print(f"  {label}")
    print(bar)
    for r in results:
        icon = ICONS.get(r.status, "?")
        print(f"  {icon} [{r.status}] {r.message}")
    status = "ALL PASS" if fails == 0 else f"{fails} FAIL(S)"
    if warns:
        status += f", {warns} WARNING(S)"
    print(f"\n  → {status}")


def detect_completed_moves(run_dir: Path) -> list:
    """Return list of move numbers that have output files present."""
    completed = []
    for n in range(1, 6):
        if (run_dir / f"move{n}_output.json").exists():
            completed.append(n)
    if (run_dir / "move6_opportunity_analysis.md").exists():
        completed.append(6)
    return completed


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    run_dir = Path(args[0])
    if not run_dir.exists():
        print(f"Error: run folder not found: {run_dir}", file=sys.stderr)
        sys.exit(2)

    # Determine which moves to run
    if "--move" in args:
        idx = args.index("--move")
        try:
            target_move = int(args[idx + 1])
        except (IndexError, ValueError):
            print("Error: --move requires an integer argument (1-6)", file=sys.stderr)
            sys.exit(2)
        if target_move not in MOVE_CHECKS:
            print(f"Error: --move must be 1-6, got {target_move}", file=sys.stderr)
            sys.exit(2)
        moves_to_run = [target_move]
    else:
        moves_to_run = detect_completed_moves(run_dir)
        if not moves_to_run:
            print(f"No completed move output files found in: {run_dir}")
            print("Run /run in Claude Code and complete at least Move 1 first.")
            sys.exit(0)

    print(f"\nDisruption Cascade — Validation")
    print(f"Run folder: {run_dir}")
    print(f"Checking moves: {moves_to_run}")

    total_fails = 0
    total_warns = 0

    for move_num in moves_to_run:
        results, fails, warns = run_move(move_num, run_dir)
        print_move_results(move_num, results, fails, warns)
        total_fails += fails
        total_warns += warns

    # Final summary
    print(f"\n{'═' * 50}")
    print(f"  SUMMARY")
    print(f"{'═' * 50}")
    print(f"  Moves checked : {len(moves_to_run)}")
    print(f"  Total FAILs   : {total_fails}")
    print(f"  Total WARNINGs: {total_warns}")
    if total_fails == 0:
        print(f"\n  ✓ All checks passed")
    else:
        print(f"\n  ✗ {total_fails} check(s) failed — fix before proceeding")
    print()

    sys.exit(1 if total_fails > 0 else 0)


if __name__ == "__main__":
    main()
