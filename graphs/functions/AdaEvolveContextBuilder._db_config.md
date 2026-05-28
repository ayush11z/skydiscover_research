---
name: AdaEvolveContextBuilder._db_config
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._db_config

**File:** `skydiscover/context_builder/adaevolve/builder.py:54`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _db_config(self) -> Any:
        return getattr(self.config.search, "database", None)
````

## → Calls
- [[DiscoveryControllerInput.config]]

## ← Called by
- [[AdaEvolveContextBuilder._get_progress_score]]
- [[AdaEvolveContextBuilder._is_multiobjective_enabled]]
- [[AdaEvolveContextBuilder._metric_to_maximization_value]]
- [[AdaEvolveContextBuilder._objective_descriptions]]
