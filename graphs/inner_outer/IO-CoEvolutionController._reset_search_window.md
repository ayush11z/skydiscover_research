---
name: IO-CoEvolutionController._reset_search_window
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._reset_search_window

**File:** `skydiscover/search/evox/controller.py:540`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _reset_search_window(self, start_iteration: Optional[int] = None) -> None:
        """Start a fresh scoring window for the active search algorithm."""
        self.search_scorer.reset_window(self._get_best_score(), start_iteration=start_iteration)
````

## → Calls
- [[IO-CoEvolutionController._get_best_score]]
- [[IO-LogWindowScorer.reset_window]]

## ← Called by
- [[IO-CoEvolutionController._evolve_search]]
- [[IO-CoEvolutionController._generate_and_validate_search_algorithm]]
- [[IO-CoEvolutionController._initialize_first_search_program]]
- [[IO-CoEvolutionController._record_search_window_step]]
- [[IO-CoEvolutionController.run_discovery]]
