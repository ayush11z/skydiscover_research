---
name: AdaEvolveDatabase.is_multiobjective_enabled
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.is_multiobjective_enabled

**File:** `skydiscover/search/adaevolve/database.py:1506`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def is_multiobjective_enabled(self) -> bool:
        """Return True when explicit Pareto objectives are configured."""
        return bool(self.pareto_objectives)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._get_multiobjective_proxy_score]]
- [[AdaEvolveDatabase._get_objective_vector]]
- [[AdaEvolveDatabase._sample_global_top]]
- [[AdaEvolveDatabase._update_best_program]]
- [[AdaEvolveDatabase.get_best_program]]
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[AdaEvolveDatabase.get_global_pareto_front]]
- [[AdaEvolveDatabase.get_pareto_front]]
- [[AdaEvolveDatabase.get_top_programs]]
