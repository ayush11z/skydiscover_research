---
name: MetricDiversity.update
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# MetricDiversity.update

**File:** `skydiscover/search/adaevolve/archive/diversity.py:210`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def update(self, programs: List[Program]) -> None:
        """Update metric bounds from current archive."""
        self._bounds.clear()

        for p in programs:
            for key, val in p.metrics.items():
                if not isinstance(val, (int, float)):
                    continue
                val = float(val)
                if key not in self._bounds:
                    self._bounds[key] = (val, val)
                else:
                    lo, hi = self._bounds[key]
                    self._bounds[key] = (min(lo, val), max(hi, val))
````

## → Calls
- [[EvaluationResult.metrics]]
- [[MetricDiversity.__init__]]
- [[Program.metrics]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
