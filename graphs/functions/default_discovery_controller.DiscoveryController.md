---
name: default_discovery_controller.DiscoveryController
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
- [[AdaEvolveController.__init__]]
- [[AdaEvolveController._ensure_all_islands_seeded]]
- [[AdaEvolveController._execute_generation]]
- [[AdaEvolveController._generate_child]]
- [[AdaEvolveController._generate_paradigms_if_needed]]
- [[AdaEvolveController._load_evaluator_code]]
- [[AdaEvolveController._log_iteration_stats]]
- [[AdaEvolveController._process_result]]
- [[AdaEvolveController._run_iteration]]
- [[AdaEvolveController._setup_iteration_stats_logging]]
- [[AdaEvolveController.run_discovery]]
- [[CoEvolutionController._build_search_stats]]
- [[CoEvolutionController._generate_and_validate_search_algorithm]]
- [[CoEvolutionController._generate_variation_operators]]
- [[CoEvolutionController._init_output_dir]]
- [[CoEvolutionController._init_search_evolution_controller]]
- [[CoEvolutionController._init_search_tracking]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[CoEvolutionController._switch_to_new_search_algorithm]]
- [[CoEvolutionController.run_discovery]]
- [[GEPANativeController.__init__]]
- [[GEPANativeController._acceptance_gate]]
- [[GEPANativeController._attempt_merge]]
- [[GEPANativeController._build_prompt]]
- [[GEPANativeController.run_discovery]]
- [[Runner.__init__]]
- [[controller.AdaEvolveController]]
- [[controller.ClaudeCodeController]]
- [[controller.CoEvolutionController]]
- [[controller.GEPANativeController]]
- [[registry.register_controller]]
- [[route.get_discovery_controller]]
