---
name: IO-metrics.normalize_metric_value
description: function in skydiscover/utils/metrics.py (utils)
metadata:
  type: project
---

# metrics.normalize_metric_value

**File:** `skydiscover/utils/metrics.py:50`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def normalize_metric_value(
    key: str,
    value: Any,
    higher_is_better: Dict[str, bool],
) -> Optional[float]:
    """Convert a metric to an internal score where larger is always better.

    Args:
        key: Metric name used to look up direction in *higher_is_better*.
        value: Raw metric value (must be numeric, else returns ``None``).
        higher_is_better: Mapping of metric names to direction.  Missing keys
            default to ``True`` (i.e. higher is better).

    Returns:
        Normalised float (negated when the metric should be minimised), or
        ``None`` when *value* is not numeric.
    """
    if not is_numeric_metric(value):
        return None
    normalized = float(value)
    if math.isnan(normalized):
        return None
    if not higher_is_better.get(key, True):
        normalized = -normalized
    return normalized
````

## → Calls
- [[IO-metrics.is_numeric_metric]]

## ← Called by
- [[IO-metrics.compute_proxy_score]]
