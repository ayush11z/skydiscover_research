---
name: callback._safe_metrics
description: function in skydiscover/extras/monitor/callback.py (monitor)
metadata:
  type: project
---

# callback._safe_metrics

**File:** `skydiscover/extras/monitor/callback.py:231`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def _safe_metrics(metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Return a JSON-safe copy of metrics."""
    safe = {}
    for k, v in metrics.items():
        if isinstance(v, (int, float, str, bool, type(None))):
            safe[k] = v
        else:
            safe[k] = str(v)
    return safe
````

## → Calls
- [[SearchConfig.type]]

## ← Called by
- [[callback._push_program_event]]
- [[create_external_callback._callback]]
- [[viewer._to_monitor_format]]
