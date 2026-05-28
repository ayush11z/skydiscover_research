---
name: IO-search_strategy_evaluator._check_forbidden_attributes
description: function in skydiscover/search/evox/database/search_strategy_evaluator.py (evox)
metadata:
  type: project
---

# search_strategy_evaluator._check_forbidden_attributes

**File:** `skydiscover/search/evox/database/search_strategy_evaluator.py:23`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def _check_forbidden_attributes(code: str) -> List[str]:
    """
    Scan generated code for forbidden attribute accesses before executing it.
    Returns a list of human-readable violation descriptions.
    """
    violations: List[str] = []
    for line_num, line in enumerate(code.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith('#'):
            continue

        # .combined_score used as a direct attribute (not through .metrics.get/[])
        if re.search(r'\.\s*combined_score\b', stripped):
            if not re.search(
                r'metrics\s*\.?\s*get\s*\(\s*[\'"]combined_score', stripped
            ) and not re.search(r'metrics\s*\[\s*[\'"]combined_score', stripped):
                violations.append(
                    f"line {line_num}: `.combined_score` — "
                    f"use program.metrics.get('combined_score', 0.0) instead"
                )

        # .best_score — never valid on program or database objects
        if re.search(r'\.\s*best_score\b', stripped):
            violations.append(
                f"line {line_num}: `.best_score` — self.best_score does not exist; "
                f"use max(p.metrics.get('combined_score', 0.0) for p in "
                f"self.programs.values()) if self.programs else 0.0"
            )

        # .best_program — never valid
        if re.search(r'\.\s*best_program\b', stripped):
            violations.append(
                f"line {line_num}: `.best_program` — "
                f"self.best_program does not exist on EvolvedProgramDatabase"
            )

        # program.score / p.score etc. (direct .score on program-like vars)
        m = _FORBIDDEN_SCORE_VARS.search(stripped)
        if m:
            if not re.search(
                r'metrics\s*\.?\s*get\s*\(\s*[\'"]score', stripped
            ) and not re.search(r'metrics\s*\[\s*[\'"]score', stripped):
                violations.append(
                    f"line {line_num}: `{m.group(1)}.score` — "
                    f"program objects have no .score attribute; "
                    f"use program.metrics.get('combined_score', 0.0)"
                )

    return violations
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-search_strategy_evaluator.evaluate]]
