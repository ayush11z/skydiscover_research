---
name: CodeDiversity._jaccard_distance
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# CodeDiversity._jaccard_distance

**File:** `skydiscover/search/adaevolve/archive/diversity.py:121`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _jaccard_distance(self, set1: set, set2: set) -> float:
        """Compute Jaccard distance: 1 - |intersection| / |union|"""
        if not set1 and not set2:
            return 0.0
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        if union == 0:
            return 0.0
        return 1.0 - (intersection / union)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[CodeDiversity._structural_distance]]
- [[CodeDiversity.distance]]
