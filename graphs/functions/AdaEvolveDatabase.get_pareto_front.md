---
name: AdaEvolveDatabase.get_pareto_front
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_pareto_front

**File:** `skydiscover/search/adaevolve/database.py:1887`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_pareto_front(self, island_idx: Optional[int] = None) -> List[Program]:
        """Get the Pareto front for a specific island or globally across all islands."""
        if not self.is_multiobjective_enabled():
            return self.get_top_programs_for_island(island_idx)

        if island_idx is None:
            return self.get_global_pareto_front()

        if 0 <= island_idx < self.num_islands:
            if self.use_unified_archive and self.archives:
                return self.archives[island_idx].get_pareto_front()

            population = self.get_island_population(island_idx)
            if not population:
                return []

            front = []
            objective_vectors = {
                program.id: self._get_objective_vector(program) or [] for program in population
            }
            for candidate in population:
                dominated = False
                for challenger in population:
                    if challenger.id == candidate.id:
                        continue
                    if self._dominates(
                        objective_vectors[challenger.id], objective_vectors[candidate.id]
                    ):
                        dominated = True
                        break
                if not dominated:
                    front.append(candidate)
            return sorted(front, key=self._get_pareto_representative_sort_key, reverse=True)

        return []
````

## → Calls
- [[AdaEvolveDatabase._dominates]]
- [[AdaEvolveDatabase._get_objective_vector]]
- [[AdaEvolveDatabase._get_pareto_representative_sort_key]]
- [[AdaEvolveDatabase.get_global_pareto_front]]
- [[AdaEvolveDatabase.get_island_population]]
- [[AdaEvolveDatabase.get_top_programs_for_island]]
- [[AdaEvolveDatabase.is_multiobjective_enabled]]
- [[LangFuseTracer.get]]
- [[Program.id]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
