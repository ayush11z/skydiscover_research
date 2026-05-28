---
name: search_strategy_evaluator._verify_metrics_preserved
description: function in skydiscover/search/evox/database/search_strategy_evaluator.py (evox)
metadata:
  type: project
---

# search_strategy_evaluator._verify_metrics_preserved

**File:** `skydiscover/search/evox/database/search_strategy_evaluator.py:88`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def _verify_metrics_preserved(
    original_metrics: Dict[str, Any],
    stored_metrics: Dict[str, Any],
    operation: str,
    program_id: str,
) -> str:
    """
    Verify that all metrics from original_metrics are present in stored_metrics
    with the same values. Returns error message if verification fails, empty string if OK.
    """
    original_keys = set(original_metrics.keys())

    for key in original_keys:
        if key not in stored_metrics:
            return (
                f"Metric '{key}' was deleted from program '{program_id}' during {operation}. "
                f"Original metrics: {list(original_keys)}, stored metrics: {list(stored_metrics.keys())}"
            )

        original_value = original_metrics[key]
        stored_value = stored_metrics[key]

        if isinstance(original_value, (int, float)) and isinstance(stored_value, (int, float)):
            if abs(float(original_value) - float(stored_value)) > 1e-10:
                return (
                    f"Metric '{key}' value was modified in program '{program_id}' during {operation}: "
                    f"original={original_value}, stored={stored_value}. "
                    f"Metric values must remain unchanged."
                )
        elif original_value != stored_value:
            return (
                f"Metric '{key}' value was modified in program '{program_id}' during {operation}: "
                f"original={original_value!r}, stored={stored_value!r}. "
                f"Metric values must remain unchanged."
            )

    return ""
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[search_strategy_evaluator.evaluate]]
