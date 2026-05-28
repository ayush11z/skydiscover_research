---
name: AdaEvolveDatabase._enforce_island_population_limit
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._enforce_island_population_limit

**File:** `skydiscover/search/adaevolve/database.py:737`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _enforce_island_population_limit(self, island_idx: int) -> None:
        """Remove worst programs if island exceeds population limit (legacy mode only)."""
        if self.use_unified_archive:
            return  # Archives handle their own limits

        population = self.islands[island_idx]

        if len(population) <= self.population_size:
            return

        # Sort by fitness (best first)
        population.sort(key=self._get_fitness, reverse=True)

        # Keep top population_size, remove rest
        removed = population[self.population_size :]
        self.islands[island_idx] = population[: self.population_size]

        # Also remove from global registry (but preserve best program)
        for prog in removed:
            if prog.id in self.programs and prog.id != self.best_program_id:
                del self.programs[prog.id]

        logger.debug(
            f"Removed {len(removed)} programs from island {island_idx} "
            f"to enforce population limit"
        )
````

## → Calls
- [[AdaEvolveDatabase._get_fitness]]
- [[AdaEvolveDatabaseConfig.population_size]]
- [[CheckpointManager.load]]
- [[GEPANativeDatabaseConfig.population_size]]
- [[OpenEvolveNativeDatabaseConfig.population_size]]

## ← Called by
- [[AdaEvolveDatabase.add]]
- [[AdaEvolveDatabase.add_merged_program]]
