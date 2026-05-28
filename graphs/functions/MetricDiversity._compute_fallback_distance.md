---
name: MetricDiversity._compute_fallback_distance
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# MetricDiversity._compute_fallback_distance

**File:** `skydiscover/search/adaevolve/archive/diversity.py:274`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _compute_fallback_distance(self, a: Program, b: Program) -> float:
        """
        Compute distance when bounds are unavailable.

        Falls back to unnormalized Euclidean distance on shared numeric metrics.
        """
        # Find shared numeric metrics
        shared_keys = set()
        for key, val in a.metrics.items():
            if isinstance(val, (int, float)) and key in b.metrics:
                if isinstance(b.metrics[key], (int, float)):
                    shared_keys.add(key)

        if not shared_keys:
            # No shared numeric metrics - use code length difference as proxy
            len_diff = abs(len(a.solution) - len(b.solution))
            return min(len_diff / 1000.0, 1.0)  # Normalize roughly

        # Compute unnormalized distance on shared metrics
        dist_sq = 0.0
        for key in shared_keys:
            val_a = float(a.metrics[key])
            val_b = float(b.metrics[key])
            # Use relative difference to handle different scales
            max_val = max(abs(val_a), abs(val_b), 1e-10)
            diff = (val_a - val_b) / max_val
            dist_sq += diff**2

        return (dist_sq / len(shared_keys)) ** 0.5
````

## → Calls
- [[EvaluationResult.metrics]]
- [[Program.metrics]]
- [[Program.solution]]
- [[base_database.Program]]

## ← Called by
- [[MetricDiversity.distance]]
