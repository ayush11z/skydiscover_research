---
name: CodeDiversity.distance
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# CodeDiversity.distance

**File:** `skydiscover/search/adaevolve/archive/diversity.py:83`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def distance(self, a: Program, b: Program) -> float:
        solution1, solution2 = a.solution, b.solution

        if solution1 == solution2:
            return 0.0

        # 1. Token-based Jaccard distance (0 to 1)
        tokens1 = self._tokenize(solution1)
        tokens2 = self._tokenize(solution2)
        token_dist = self._jaccard_distance(tokens1, tokens2)

        # 2. Structural feature distance (0 to 1)
        struct_dist = self._structural_distance(solution1, solution2)

        # 3. Normalized length distance (0 to 1)
        max_len = max(len(solution1), len(solution2), 1)
        len_dist = abs(len(solution1) - len(solution2)) / max_len

        return (
            token_dist * self.token_weight
            + struct_dist * self.structure_weight
            + len_dist * self.length_weight
        )
````

## → Calls
- [[CodeDiversity._jaccard_distance]]
- [[CodeDiversity._structural_distance]]
- [[CodeDiversity._tokenize]]
- [[Program.solution]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
