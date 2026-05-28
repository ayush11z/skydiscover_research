---
name: HybridDiversity.distance
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# HybridDiversity.distance

**File:** `skydiscover/search/adaevolve/archive/diversity.py:340`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def distance(self, a: Program, b: Program) -> float:
        """Weighted sum of sub-strategy distances."""
        total = 0.0
        for strategy, weight in zip(self.strategies, self.weights):
            total += strategy.distance(a, b) * weight
        return total
````

## → Calls
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
