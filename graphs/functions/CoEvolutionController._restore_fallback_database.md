---
name: CoEvolutionController._restore_fallback_database
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._restore_fallback_database

**File:** `skydiscover/search/evox/controller.py:477`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _restore_fallback_database(self) -> None:
        """Restore the previous search strategy after a failed switch."""
        broken_db = self.database
        old_db = self._fallback_database

        # Migrate new programs found during the broken strategy's successful runs
        old_ids = set(old_db.programs)
        migrated = 0
        for pid, program in broken_db.programs.items():
            if pid not in old_ids:
                try:
                    old_db.add(program, iteration=program.iteration_found)
                    migrated += 1
                except Exception:
                    logger.debug("Migration failed for program %s", program.id, exc_info=True)

        logger.warning(
            "New search strategy caused database error — "
            f"restoring previous search strategy ({migrated} new programs preserved)"
        )
        self.database = old_db
        if self.evaluator.llm_judge:
            self.evaluator.llm_judge.database = old_db
        self._active_search_algorithm_code = self._fallback_search_code
        self._pending_search_result = None
        self._num_search_evolutions += 1  # Count the failed attempt
        self._fallback_database = None
        self._fallback_search_code = None
````

## → Calls
- [[Config.evaluator]]
- [[DiscoveryControllerInput.database]]
- [[Program.id]]
- [[Program.iteration_found]]
- [[ProgramDatabase.add]]
- [[SearchConfig.database]]
- [[UnifiedArchive.add]]
- [[discovery_utils.load_database_from_file]]
- [[evaluation.create_evaluator]]
- [[registry.setup_search]]

## ← Called by
- [[CoEvolutionController._assign_search_score]]
- [[CoEvolutionController.run_discovery]]
