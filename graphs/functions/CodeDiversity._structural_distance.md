---
name: CodeDiversity._structural_distance
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# CodeDiversity._structural_distance

**File:** `skydiscover/search/adaevolve/archive/diversity.py:131`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _structural_distance(self, solution1: str, solution2: str) -> float:
        """
        Compare structural features of two code snippets.

        Looks at imports, function definitions, class definitions.
        """
        # Extract structural features
        features1 = self._extract_features(solution1)
        features2 = self._extract_features(solution2)

        # Compare feature sets using Jaccard
        return self._jaccard_distance(features1, features2)
````

## → Calls
- [[CodeDiversity._extract_features]]
- [[CodeDiversity._jaccard_distance]]

## ← Called by
- [[CodeDiversity.distance]]
