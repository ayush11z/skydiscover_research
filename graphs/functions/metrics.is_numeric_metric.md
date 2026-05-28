---
name: metrics.is_numeric_metric
description: function in skydiscover/utils/metrics.py (utils)
metadata:
  type: project
---

# metrics.is_numeric_metric

**File:** `skydiscover/utils/metrics.py:9`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def is_numeric_metric(value: Any) -> bool:
    """Return True for real numeric values, excluding bools.

    Python's ``bool`` is a subclass of ``int``, so ``isinstance(True, int)``
    is ``True``.  Flag metrics like ``timeout: True`` must not be treated as
    numeric fitness contributions.
    """
    return isinstance(value, (int, float)) and not isinstance(value, bool)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[metrics.compute_proxy_score]]
- [[metrics.format_improvement]]
- [[metrics.format_metrics]]
- [[metrics.get_score]]
- [[metrics.normalize_metric_value]]
