---
name: AdaEvolveDatabase.get_best_program
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_best_program

**File:** `skydiscover/search/adaevolve/database.py:1751`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_best_program(self, metric: Optional[str] = None) -> Optional[Program]:
        """
        Get the best program across all islands.

        Uses tracked best_program_id as authoritative source, falling back to
        archive/island search. This prevents silent data loss when the best program
        has been evicted from archives but is still tracked.
        """
        if metric is None and self.is_multiobjective_enabled():
            front = self.get_global_pareto_front()
            representative = self._choose_pareto_representative(front)
            if representative is not None:
                self.best_program_id = representative.id
                self._global_best_score = self._get_fitness(representative)
            return representative

        # First, check if we have a tracked best program (authoritative)
        # This handles the case where best program was evicted from archives
        if self.best_program_id and self.best_program_id in self.programs:
            tracked_best = self.programs[self.best_program_id]
            tracked_fitness = self._get_fitness(tracked_best)

            # Verify it's still actually the best by checking archives/islands
            population_best = None
            population_best_fitness = float("-inf")

            if self.use_unified_archive and self.archives:
                for archive in self.archives:
                    if hasattr(archive, "get_best"):
                        candidate = archive.get_best()
                    else:
                        all_progs = archive.get_all()
                        candidate = max(all_progs, key=self._get_fitness) if all_progs else None

                    if candidate:
                        fitness = self._get_fitness(candidate)
                        if fitness > population_best_fitness:
                            population_best_fitness = fitness
                            population_best = candidate
            else:
                for island in self.islands:
                    if island:
                        candidate = max(island, key=self._get_fitness)
                        fitness = self._get_fitness(candidate)
                        if fitness > population_best_fitness:
                            population_best_fitness = fitness
                            population_best = candidate

            # Return the better of tracked vs population best
            if tracked_fitness >= population_best_fitness:
                return tracked_best
            else:
                # Population has a better program - update tracking
                self.best_program_id = population_best.id
                self._global_best_score = population_best_fitness
                return population_best

        # Fallback: search archives/islands (for cases where tracking is not set)
        best = None
        best_fitness = float("-inf")

        if self.use_unified_archive and self.archives:
            for archive in self.archives:
                if hasattr(archive, "get_best"):
                    candidate = archive.get_best()
                else:
                    all_progs = archive.get_all()
                    candidate = max(all_progs, key=self._get_fitness) if all_progs else None

                if candidate:
                    fitness = self._get_fitness(candidate)
                    if fitness > best_fitness:
                        best_fitness = fitness
                        best = candidate
        else:
            for island in self.islands:
                if island:
                    candidate = max(island, key=self._get_fitness)
                    fitness = self._get_fitness(candidate)
                    if fitness > best_fitness:
                        best_fitness = fitness
                        best = candidate

        return best
````

## → Calls
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._choose_pareto_representative]]
- [[AdaEvolveDatabase._get_fitness]]
- [[AdaEvolveDatabase.get_global_pareto_front]]
- [[AdaEvolveDatabase.is_multiobjective_enabled]]
- [[CheckpointManager.load]]
- [[Program.id]]
- [[UnifiedArchive.get_all]]
- [[UnifiedArchive.get_best]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
