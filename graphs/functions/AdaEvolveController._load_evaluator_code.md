---
name: AdaEvolveController._load_evaluator_code
description: method in skydiscover/search/adaevolve/controller.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveController._load_evaluator_code

**File:** `skydiscover/search/adaevolve/controller.py:108`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _load_evaluator_code(self) -> str:
        """Load evaluator source code for paradigm generation context."""
        from skydiscover.search.utils.discovery_utils import load_evaluator_code

        return load_evaluator_code(self.evaluation_file)
````

## → Calls
- [[DiscoveryControllerInput.evaluation_file]]
- [[EvaluatorConfig.evaluation_file]]
- [[EvoxDatabaseConfig.evaluation_file]]
- [[default_discovery_controller.DiscoveryController]]
- [[discovery_utils.load_evaluator_code]]

## ← Called by
- [[AdaEvolveController.__init__]]
