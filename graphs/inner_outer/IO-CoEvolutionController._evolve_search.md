---
name: IO-CoEvolutionController._evolve_search
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._evolve_search

**File:** `skydiscover/search/evox/controller.py:214`  
**Kind:** method  
**Layer:** #outer-loop

## What it does
Entry point for the outer loop when stagnation is detected. On the very first call it initialises the search strategy database; on subsequent calls it:
1. Finalises and scores the previous search strategy via CoEvolutionController._finalize_pending_search
2. Resets the score window
3. Generates a new search algorithm via CoEvolutionController._generate_and_validate_search_algorithm

## Source
````python
    async def _evolve_search(self, solution_iter: int) -> None:
        """Handle search evolution: score previous algorithm, generate and switch to new one."""

        if not self.search_controller.database.programs:
            await self._initialize_first_search_program(solution_iter)
            return

        # If there is a pending search result, finalize it (as search window is reset)
        if self._pending_search_result:
            await self._finalize_pending_search()

        self._reset_search_window()
        await self._generate_and_validate_search_algorithm(solution_iter)
````

## → Calls
- [[IO-CoEvolutionController._finalize_pending_search]]
- [[IO-CoEvolutionController._generate_and_validate_search_algorithm]]
- [[IO-CoEvolutionController._initialize_first_search_program]]
- [[IO-CoEvolutionController._reset_search_window]]

## ← Called by
- [[IO-CoEvolutionController.run_discovery]]
