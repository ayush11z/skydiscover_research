---
name: IO-CoEvolutionController._finalize_pending_search
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._finalize_pending_search

**File:** `skydiscover/search/evox/controller.py:228`  
**Kind:** method  
**Layer:** #outer-loop

## What it does
Scores the search strategy that was active during the last window, stores the result in the search-strategy database, and clears `_pending_search_result`.

## Source
````python
    async def _finalize_pending_search(self) -> None:
        """Score the pending search algorithm and add it to the search strategy database."""
        pending_iteration = self._num_search_evolutions
        is_new_best = self._assign_search_score()

        await update_saved_search_algorithm_score(
            self.search_outputs_dir,
            pending_iteration,
            self._pending_search_result,
            is_new_best=is_new_best,
            db_stats=self.database.get_statistics(),
        )
        await self.search_controller.postprocess_result(
            self._pending_search_result, self._num_search_evolutions, verbose=False
        )

        self._pending_search_result = None
        self._num_search_evolutions += 1
````

## → Calls
- [[IO-CoEvolutionController._assign_search_score]]
- [[IO-DiscoveryController.postprocess_result]]
- [[IO-DiscoveryControllerInput.database]]
- [[IO-coevolve_logging.update_saved_search_algorithm_score]]

## ← Called by
- [[IO-CoEvolutionController._evolve_search]]
- [[IO-CoEvolutionController.run_discovery]]
