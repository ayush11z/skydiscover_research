---
name: openevolve_backend._score_of
description: function in skydiscover/extras/external/openevolve_backend.py (external)
metadata:
  type: project
---

# openevolve_backend._score_of

**File:** `skydiscover/extras/external/openevolve_backend.py:131`  
**Kind:** function  
**Layer:** #external

## Source
````python
def _score_of(metrics: dict) -> Optional[float]:
    if not metrics:
        return None
    if "combined_score" in metrics:
        return float(metrics["combined_score"])
    nums = [
        float(v)
        for v in metrics.values()
        if isinstance(v, (int, float)) and not isinstance(v, bool)
    ]
    return sum(nums) / len(nums) if nums else None
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[openevolve_backend._get_initial_score]]
- [[openevolve_backend.run]]
