---
name: ParadigmGenerator._is_multiobjective
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._is_multiobjective

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:81`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _is_multiobjective(self) -> bool:
        """Return True when explicit Pareto objectives are configured."""
        return bool(self.objective_names)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[ParadigmGenerator._optimization_targets_text]]
- [[ParadigmGenerator._score_label]]
