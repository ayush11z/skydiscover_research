---
name: diversity.MetricDiversity
description: class in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# diversity.MetricDiversity

**File:** `skydiscover/search/adaevolve/archive/diversity.py:191`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class MetricDiversity(DiversityStrategy):
    """
    Diversity based on evaluator metrics.

    Computes normalized Euclidean distance in metric space.
    Each metric is normalized to [0, 1] based on observed min/max.

    Good for: When evaluator returns multiple meaningful metrics.
    """

````

## → Calls
- [[diversity.DiversityStrategy]]

## ← Called by
- [[diversity.create_diversity_strategy]]
