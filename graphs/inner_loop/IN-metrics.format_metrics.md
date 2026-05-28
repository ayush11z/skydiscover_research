---
name: IN-metrics.format_metrics
description: function in skydiscover/utils/metrics.py (utils)
metadata:
  type: project
---

# metrics.format_metrics

**File:** `skydiscover/utils/metrics.py:32`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def format_metrics(metrics: Dict[str, Any]) -> str:
    """Format a metrics dict for logging, handling both numeric and string values."""
    if not metrics:
        return ""

    parts = []
    for name, value in metrics.items():
        if is_numeric_metric(value):
            try:
                parts.append(f"{name}={value:.4f}")
            except (ValueError, TypeError):
                parts.append(f"{name}={value}")
        else:
            parts.append(f"{name}={value}")

    return ", ".join(parts)
````

## → Calls
- [[IN-metrics.is_numeric_metric]]

## ← Called by
- [[IN-Evaluator.evaluate_program]]
- [[IN-ProgramDatabase.log_status]]
