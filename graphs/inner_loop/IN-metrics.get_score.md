---
name: IN-metrics.get_score
description: function in skydiscover/utils/metrics.py (utils)
metadata:
  type: project
---

# metrics.get_score

**File:** `skydiscover/utils/metrics.py:19`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def get_score(metrics: Dict[str, Any]) -> float:
    """Return combined_score if available, otherwise average of all numeric metric values."""
    if not metrics:
        return 0.0
    if "combined_score" in metrics:
        try:
            return float(metrics["combined_score"])
        except (ValueError, TypeError):
            pass
    numeric_values = [v for v in metrics.values() if is_numeric_metric(v)]
    return sum(numeric_values) / len(numeric_values) if numeric_values else 0.0
````

## → Calls
- [[IN-metrics.is_numeric_metric]]

## ← Called by
- [[IN-ProgramDatabase._is_better]]
- [[IN-ProgramDatabase.get_best_program]]
- [[IN-ProgramDatabase.get_top_programs]]
- [[IN-metrics.compute_proxy_score]]
