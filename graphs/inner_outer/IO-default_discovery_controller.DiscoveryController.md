---
name: IO-default_discovery_controller.DiscoveryController
description: class in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# default_discovery_controller.DiscoveryController

**File:** `skydiscover/search/default_discovery_controller.py:51`  
**Kind:** class  
**Layer:** #inner-loop

## Source
````python
class DiscoveryController:
    """
    Discovery controller with a default sequential execution strategy.

    Handles the full generate-evaluate cycle: prompt building, LLM calls,
    response parsing, evaluation, and result processing.

    The default ``run_discovery`` runs iterations sequentially.  Subclasses
    (e.g. CoEvolutionController) can override it for different orchestration
    while reusing the shared iteration primitives.
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-CoEvolutionController._build_search_stats]]
- [[IO-CoEvolutionController._generate_and_validate_search_algorithm]]
- [[IO-CoEvolutionController._generate_variation_operators]]
- [[IO-CoEvolutionController._init_output_dir]]
- [[IO-CoEvolutionController._init_search_evolution_controller]]
- [[IO-CoEvolutionController._init_search_tracking]]
- [[IO-CoEvolutionController._initialize_first_search_program]]
- [[IO-CoEvolutionController._restore_fallback_database]]
- [[IO-CoEvolutionController._switch_to_new_search_algorithm]]
- [[IO-CoEvolutionController.run_discovery]]
- [[IO-Runner.__init__]]
- [[IO-controller.CoEvolutionController]]
