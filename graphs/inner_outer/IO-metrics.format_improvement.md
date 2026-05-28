---
name: IO-metrics.format_improvement
description: function in skydiscover/utils/metrics.py (utils)
metadata:
  type: project
---

# metrics.format_improvement

**File:** `skydiscover/utils/metrics.py:123`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def format_improvement(parent_metrics: Dict[str, Any], child_metrics: Dict[str, Any]) -> str:
    """Format the per-metric delta between parent and child for logging."""
    if not parent_metrics or not child_metrics:
        return ""

    parts = []
    for metric, child_value in child_metrics.items():
        if metric in parent_metrics:
            parent_value = parent_metrics[metric]
            if is_numeric_metric(child_value) and is_numeric_metric(parent_value):
                try:
                    parts.append(f"{metric}={child_value - parent_value:+.4f}")
                except (ValueError, TypeError):
                    continue

    return ", ".join(parts)
````

## → Calls
- [[IO-metrics.is_numeric_metric]]

## ← Called by
_(entry point — nothing in this graph calls it)_
