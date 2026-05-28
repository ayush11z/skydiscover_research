---
name: AdaEvolveDatabase._sample_global_top
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._sample_global_top

**File:** `skydiscover/search/adaevolve/database.py:713`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _sample_global_top(self, exclude_id: str, n: int) -> List[Program]:
        """Sample top programs from ALL islands for cross-pollination."""
        all_programs = self._all_population_programs()
        candidates = [p for p in all_programs if p.id != exclude_id]

        if len(candidates) <= n:
            return candidates

        if self.is_multiobjective_enabled():
            pareto_front = [p for p in self.get_global_pareto_front() if p.id != exclude_id]
            if len(pareto_front) >= n:
                return pareto_front[:n]

            front_ids = {program.id for program in pareto_front}
            remaining = sorted(
                [program for program in candidates if program.id not in front_ids],
                key=self._get_fitness,
                reverse=True,
            )
            return pareto_front + remaining[: max(0, n - len(pareto_front))]

        sorted_candidates = sorted(candidates, key=self._get_fitness, reverse=True)
        return sorted_candidates[:n]
````

## → Calls
- [[AdaEvolveDatabase._all_population_programs]]
- [[AdaEvolveDatabase._get_fitness]]
- [[AdaEvolveDatabase.get_global_pareto_front]]
- [[AdaEvolveDatabase.is_multiobjective_enabled]]
- [[Program.id]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._sample_from_archive]]
- [[AdaEvolveDatabase._sample_legacy]]
