---
name: IO-CoEvolutionController._record_search_window_step
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._record_search_window_step

**File:** `skydiscover/search/evox/controller.py:544`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _record_search_window_step(self) -> None:
        """Record current best score for search algorithm scoring."""

        if self.search_scorer.get_start_score() is None:
            self._reset_search_window()

        self.search_scorer.record_step(self._get_best_score())
````

## → Calls
- [[IO-CoEvolutionController._get_best_score]]
- [[IO-CoEvolutionController._reset_search_window]]
- [[IO-LogWindowScorer.get_start_score]]
- [[IO-LogWindowScorer.record_step]]

## ← Called by
- [[IO-CoEvolutionController.run_discovery]]
