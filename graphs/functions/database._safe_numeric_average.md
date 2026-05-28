---
name: database._safe_numeric_average
description: function in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# database._safe_numeric_average

**File:** `skydiscover/search/openevolve_native/database.py:42`  
**Kind:** function  
**Layer:** #openevolve

## Source
````python
def _safe_numeric_average(metrics: Dict[str, Any]) -> float:
    """Average of numeric metric values, ignoring non-numeric entries."""
    if not metrics:
        return 0.0
    numeric_values = []
    for value in metrics.values():
        if isinstance(value, (int, float)):
            try:
                fv = float(value)
                if fv == fv:  # NaN guard
                    numeric_values.append(fv)
            except (ValueError, TypeError, OverflowError):
                continue
    return sum(numeric_values) / len(numeric_values) if numeric_values else 0.0
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[database._get_fitness]]
