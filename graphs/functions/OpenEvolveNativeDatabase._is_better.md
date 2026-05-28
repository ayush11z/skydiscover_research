---
name: OpenEvolveNativeDatabase._is_better
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._is_better

**File:** `skydiscover/search/openevolve_native/database.py:605`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _is_better(self, program1: Program, program2: Program) -> bool:
        if not program1.metrics and not program2.metrics:
            return program1.timestamp > program2.timestamp
        if program1.metrics and not program2.metrics:
            return True
        if not program1.metrics and program2.metrics:
            return False
        return _get_fitness(program1.metrics, self.feature_dimensions) > _get_fitness(
            program2.metrics, self.feature_dimensions
        )
````

## → Calls
- [[EvaluationResult.metrics]]
- [[Program.metrics]]
- [[Program.timestamp]]
- [[base_database.Program]]
- [[database._get_fitness]]

## ← Called by
- [[OpenEvolveNativeDatabase._update_archive]]
- [[OpenEvolveNativeDatabase._update_best_program]]
- [[OpenEvolveNativeDatabase._update_island_best_program]]
- [[OpenEvolveNativeDatabase.add]]
