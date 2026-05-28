---
name: IO-CoEvolutionController._build_search_stats
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._build_search_stats

**File:** `skydiscover/search/evox/controller.py:403`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _build_search_stats(self, solution_iter: int) -> Dict[str, Any]:
        """Build statistics dict for search algorithm generation."""
        return {
            "search_algorithm_stats": {
                "window_start_iteration": solution_iter,
                "total_iterations": self._max_solution_iterations,
                "search_window_horizon": self._switch_interval,
                "problem_description": self.config.context_builder.system_message,
                "evaluator_context": self.evaluation_file,
                "improvement_threshold": self.DEFAULT_IMPROVEMENT_THRESHOLD,
            },
            "db_stats": self.database.get_statistics(
                improvement_threshold=self.DEFAULT_IMPROVEMENT_THRESHOLD
            ),
        }
````

## → Calls
- [[IO-DiscoveryControllerInput.config]]
- [[IO-DiscoveryControllerInput.database]]
- [[IO-DiscoveryControllerInput.evaluation_file]]
- [[IO-default_discovery_controller.DiscoveryController]]

## ← Called by
- [[IO-CoEvolutionController._generate_and_validate_search_algorithm]]
