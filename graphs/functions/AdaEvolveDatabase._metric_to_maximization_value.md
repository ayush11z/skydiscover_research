---
name: AdaEvolveDatabase._metric_to_maximization_value
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._metric_to_maximization_value

**File:** `skydiscover/search/adaevolve/database.py:1510`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _metric_to_maximization_value(self, metric_name: str, value: Any) -> Optional[float]:
        """Convert a metric to an internal score where larger is always better."""
        from skydiscover.utils.metrics import normalize_metric_value

        return normalize_metric_value(metric_name, value, self.higher_is_better)
````

## → Calls
- [[AdaEvolveDatabaseConfig.higher_is_better]]
- [[ArchiveConfig.higher_is_better]]
- [[metrics.normalize_metric_value]]

## ← Called by
- [[AdaEvolveDatabase._get_objective_vector]]
- [[get_top_programs._metric_key]]
