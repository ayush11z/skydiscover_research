---
name: get_top_programs._metric_key
description: function in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# get_top_programs._metric_key

**File:** `skydiscover/search/adaevolve/database.py:1848`  
**Kind:** function  
**Layer:** #adaevolve

## Source
````python
            def _metric_key(p: Program) -> float:
                val = (getattr(p, "metrics", None) or {}).get(metric)
                normalized = self._metric_to_maximization_value(metric, val)
                return normalized if normalized is not None else float("-inf")
````

## → Calls
- [[AdaEvolveDatabase._metric_to_maximization_value]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase.get_top_programs]]
