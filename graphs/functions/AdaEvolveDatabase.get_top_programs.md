---
name: AdaEvolveDatabase.get_top_programs
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_top_programs

**File:** `skydiscover/search/adaevolve/database.py:1836`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_top_programs(self, n: int = 10, metric: Optional[str] = None) -> List[Program]:
        """Get top n programs across all islands.

        When *metric* is provided, programs are sorted by that specific metric
        (respecting ``higher_is_better`` if configured).  Otherwise, multiobjective
        mode returns the non-dominated front padded with proxy-score-ranked
        programs, and scalar mode sorts by the default proxy fitness.
        """
        all_programs = self._all_population_programs()

        if metric:
            # Sort by the requested metric, applying direction normalisation.
            def _metric_key(p: Program) -> float:
                val = (getattr(p, "metrics", None) or {}).get(metric)
                normalized = self._metric_to_maximization_value(metric, val)
                return normalized if normalized is not None else float("-inf")

            sorted_programs = sorted(all_programs, key=_metric_key, reverse=True)
            return sorted_programs[:n]

        if not self.is_multiobjective_enabled():
            sorted_programs = sorted(all_programs, key=self._get_fitness, reverse=True)
            return sorted_programs[:n]

        pareto_front = self.get_global_pareto_front()
        if len(pareto_front) >= n:
            return pareto_front[:n]

        front_ids = {program.id for program in pareto_front}
        remaining = sorted(
            [program for program in all_programs if program.id not in front_ids],
            key=self._get_fitness,
            reverse=True,
        )
        return pareto_front + remaining[: max(0, n - len(pareto_front))]
````

## → Calls
- [[AdaEvolveDatabase._all_population_programs]]
- [[AdaEvolveDatabase._get_fitness]]
- [[AdaEvolveDatabase.get_global_pareto_front]]
- [[AdaEvolveDatabase.is_multiobjective_enabled]]
- [[Program.id]]
- [[base_database.Program]]
- [[get_top_programs._metric_key]]

## ← Called by
_(entry point — nothing in this graph calls it)_
