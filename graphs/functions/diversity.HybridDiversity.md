---
name: diversity.HybridDiversity
description: class in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# diversity.HybridDiversity

**File:** `skydiscover/search/adaevolve/archive/diversity.py:305`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class HybridDiversity(DiversityStrategy):
    """
    Combines multiple diversity strategies with weights.

    Useful for balancing code-based and metric-based diversity.

    Example:
        hybrid = HybridDiversity([
            (CodeDiversity(), 0.5),
            (MetricDiversity(), 0.5),
        ])
    """

````

## → Calls
- [[diversity.DiversityStrategy]]

## ← Called by
- [[diversity.create_diversity_strategy]]
