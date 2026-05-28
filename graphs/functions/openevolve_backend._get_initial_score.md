---
name: openevolve_backend._get_initial_score
description: function in skydiscover/extras/external/openevolve_backend.py (external)
metadata:
  type: project
---

# openevolve_backend._get_initial_score

**File:** `skydiscover/extras/external/openevolve_backend.py:119`  
**Kind:** function  
**Layer:** #external

## Source
````python
def _get_initial_score(programs) -> float:
    """Extract initial (iteration 0) score from OpenEvolve programs dict."""
    initial_score = 0.0
    for p in programs.values():
        it = getattr(p, "iteration_found", None)
        if it == 0:
            score = _score_of(p.metrics)
            if score is not None:
                initial_score = max(initial_score, score)
    return initial_score
````

## → Calls
- [[EvaluationResult.metrics]]
- [[Program.metrics]]
- [[openevolve_backend._score_of]]

## ← Called by
- [[openevolve_backend.run]]
