---
name: AdaEvolveContextBuilder._is_multiobjective_enabled
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._is_multiobjective_enabled

**File:** `skydiscover/context_builder/adaevolve/builder.py:57`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _is_multiobjective_enabled(self) -> bool:
        return bool(getattr(self._db_config(), "pareto_objectives", None) or [])
````

## → Calls
- [[AdaEvolveContextBuilder._db_config]]

## ← Called by
- [[AdaEvolveContextBuilder._determine_outcome]]
- [[AdaEvolveContextBuilder._diversity_dimensions_text]]
- [[AdaEvolveContextBuilder._diversity_note_text]]
- [[AdaEvolveContextBuilder._format_previous_attempts]]
- [[AdaEvolveContextBuilder._identify_improvement_areas]]
- [[AdaEvolveContextBuilder._task_objective_text]]
