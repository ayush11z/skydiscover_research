---
name: discovery_utils.SerializableResult
description: class in skydiscover/search/utils/discovery_utils.py (search-utils)
metadata:
  type: project
---

# discovery_utils.SerializableResult

**File:** `skydiscover/search/utils/discovery_utils.py:59`  
**Kind:** class  
**Layer:** #search-utils

## Source
````python
class SerializableResult:
    """Result that can be pickled and sent between processes"""

    child_program_dict: Optional[Dict[str, Any]] = None
    parent_id: Optional[str] = None
    other_context_ids: Optional[List[str]] = None

    iteration_time: float = 0.0
    llm_generation_time: float = 0.0
    eval_time: float = 0.0
    prompt: Optional[Dict[str, str]] = None
    llm_response: Optional[str] = None
    iteration: int = 0
    error: Optional[str] = None
    attempts_used: int = 1
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveController._execute_generation]]
- [[AdaEvolveController._generate_child]]
- [[AdaEvolveController._process_result]]
- [[AdaEvolveController._run_normal_step]]
- [[CoEvolutionController._init_search_tracking]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[CoEvolutionController._switch_to_new_search_algorithm]]
- [[DiscoveryController._run_discovery_parallel]]
- [[DiscoveryController._run_discovery_sequential]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
- [[DiscoveryController.postprocess_result]]
- [[DiscoveryController.run_discovery]]
- [[GEPANativeController._acceptance_gate]]
- [[GEPANativeController.run_discovery]]
- [[_run_discovery_parallel._bounded_iteration]]
- [[coevolve_logging.handle_generation_failure]]
- [[coevolve_logging.log_failed_attempt]]
- [[coevolve_logging.log_search_algorithm_generated]]
- [[coevolve_logging.update_saved_search_algorithm_score]]
