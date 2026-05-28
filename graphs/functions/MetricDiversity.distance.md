---
name: MetricDiversity.distance
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# MetricDiversity.distance

**File:** `skydiscover/search/adaevolve/archive/diversity.py:240`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def distance(self, a: Program, b: Program) -> float:
        # If bounds are empty, compute distance directly from programs' metrics
        if not self._bounds:
            return self._compute_fallback_distance(a, b)

        dist_sq = 0.0
        count = 0

        for key, (lo, hi) in self._bounds.items():
            # Get values safely (skip if either is non-numeric)
            mid = (lo + hi) / 2
            val_a = self._safe_get_numeric(a.metrics, key, mid)
            val_b = self._safe_get_numeric(b.metrics, key, mid)

            # Skip this metric if either value is non-numeric
            if val_a is None or val_b is None:
                continue

            # Normalize to [0, 1]
            if hi > lo:
                norm_a = (val_a - lo) / (hi - lo)
                norm_b = (val_b - lo) / (hi - lo)
            else:
                norm_a = norm_b = 0.5

            dist_sq += (norm_a - norm_b) ** 2
            count += 1

        if count == 0:
            return self._compute_fallback_distance(a, b)

        # Return normalized Euclidean distance
        return (dist_sq / count) ** 0.5
````

## → Calls
- [[EvaluationResult.metrics]]
- [[MetricDiversity.__init__]]
- [[MetricDiversity._compute_fallback_distance]]
- [[MetricDiversity._safe_get_numeric]]
- [[Program.metrics]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
