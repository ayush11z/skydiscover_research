---
name: AdaEvolveContextBuilder._metric_to_maximization_value
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._metric_to_maximization_value

**File:** `skydiscover/context_builder/adaevolve/builder.py:69`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _metric_to_maximization_value(self, metric_name: str, value: Any) -> Optional[float]:
        from skydiscover.utils.metrics import normalize_metric_value

        higher_is_better = getattr(self._db_config(), "higher_is_better", None) or {}
        return normalize_metric_value(metric_name, value, higher_is_better)
````

## → Calls
- [[AdaEvolveContextBuilder._db_config]]
- [[metrics.normalize_metric_value]]

## ← Called by
_(entry point — nothing in this graph calls it)_
