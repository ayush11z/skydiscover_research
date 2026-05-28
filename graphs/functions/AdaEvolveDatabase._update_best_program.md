---
name: AdaEvolveDatabase._update_best_program
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._update_best_program

**File:** `skydiscover/search/adaevolve/database.py:1671`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _update_best_program(self, program: Program) -> bool:
        """
        Update global best program tracking.

        Returns:
            True if this program is a new global best, False otherwise
        """
        if self.is_multiobjective_enabled():
            previous_best_id = self.best_program_id
            previous_best_score = self._global_best_score

            # Read the STALE cache (snapshot of the front before this program
            # was added).  The cache was invalidated by add() but the old list
            # is intentionally preserved for exactly this comparison.
            previous_front_ids: Set[str] = (
                {p.id for p in (self._global_pareto_cache or [])}
                if not self._global_pareto_cache_valid
                else set()
            )

            # Now recompute (cache is invalid, so this triggers O(n²) rebuild).
            front = self.get_global_pareto_front()
            representative = self._choose_pareto_representative(front)
            if representative is None:
                return False

            self.best_program_id = representative.id
            self._global_best_score = self._get_fitness(representative)

            front_ids = {p.id for p in front}
            entered_front = program.id in front_ids and program.id not in previous_front_ids
            representative_changed = representative.id != previous_best_id
            score_improved = self._global_best_score > previous_best_score
            return entered_front or representative_changed or score_improved

        fitness = self._get_fitness(program)
        if fitness > self._global_best_score:
            self._global_best_score = fitness
            self.best_program_id = program.id
            logger.debug(f"New global best: {program.id[:8]} with fitness {fitness:.6f}")
            return True
        return False
````

## → Calls
- [[AdaEvolveDatabase._choose_pareto_representative]]
- [[AdaEvolveDatabase._compute_global_pareto_front]]
- [[AdaEvolveDatabase._get_fitness]]
- [[AdaEvolveDatabase.get_global_pareto_front]]
- [[AdaEvolveDatabase.is_multiobjective_enabled]]
- [[LangFuseTracer.get]]
- [[Program.id]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase.add]]
- [[AdaEvolveDatabase.add_merged_program]]
