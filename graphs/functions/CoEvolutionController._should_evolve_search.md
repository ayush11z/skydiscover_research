---
name: CoEvolutionController._should_evolve_search
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._should_evolve_search

**File:** `skydiscover/search/evox/controller.py:189`  
**Kind:** method  
**Layer:** #outer-loop

## What it does
Stagnation gate. After every inner-loop iteration, compares the current best score to the last tracked best:
- If improvement > 0.01 → reset `_stagnant_count` to 0
- Otherwise → increment `_stagnant_count`
- If `_stagnant_count >= _switch_interval` → return `True` (trigger outer loop)

`_switch_interval` defaults to 10% of `max_iterations`.

## Source
````python
    def _should_evolve_search(self) -> bool:
        """Check if it's time to evolve the search algorithm (stagnation-based)."""
        current = self._get_best_score()

        if self._last_tracked_best_score is None:
            self._stagnant_count = 0
        elif (current - self._last_tracked_best_score) > self.DEFAULT_IMPROVEMENT_THRESHOLD:
            self._stagnant_count = 0
        else:
            self._stagnant_count += 1

        self._last_tracked_best_score = current

        if self._stagnant_count >= self._switch_interval:
            self._stagnant_count = 0
            return True

        return False
````

## → Calls
- [[CoEvolutionController._get_best_score]]

## ← Called by
- [[CoEvolutionController.run_discovery]]
