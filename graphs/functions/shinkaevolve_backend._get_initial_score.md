---
name: shinkaevolve_backend._get_initial_score
description: function in skydiscover/extras/external/shinkaevolve_backend.py (external)
metadata:
  type: project
---

# shinkaevolve_backend._get_initial_score

**File:** `skydiscover/extras/external/shinkaevolve_backend.py:110`  
**Kind:** function  
**Layer:** #external

## Source
````python
def _get_initial_score(all_programs: list) -> float:
    """Extract initial (generation 0) score from ShinkaEvolve programs list."""
    initial_score = 0.0
    for p in all_programs:
        gen = getattr(p, "generation", 0)
        if gen == 0:
            score = getattr(p, "combined_score", None)
            if score is not None:
                initial_score = max(initial_score, float(score))
    return initial_score
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[shinkaevolve_backend.run]]
