---
name: AdaEvolveContextBuilder._objective_descriptions
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._objective_descriptions

**File:** `skydiscover/context_builder/adaevolve/builder.py:60`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _objective_descriptions(self) -> List[str]:
        db_config = self._db_config()
        higher_is_better = getattr(db_config, "higher_is_better", None) or {}
        descriptions = []
        for objective in getattr(db_config, "pareto_objectives", None) or []:
            direction = "maximize" if higher_is_better.get(objective, True) else "minimize"
            descriptions.append(f"{objective} ({direction})")
        return descriptions
````

## → Calls
- [[AdaEvolveContextBuilder._db_config]]

## ← Called by
- [[AdaEvolveContextBuilder._identify_improvement_areas]]
- [[AdaEvolveContextBuilder._task_objective_text]]
