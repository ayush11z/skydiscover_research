---
name: AdaEvolveDatabase._compute_global_pareto_front
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._compute_global_pareto_front

**File:** `skydiscover/search/adaevolve/database.py:1632`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _compute_global_pareto_front(self) -> List[Program]:
        """O(n²) computation of the non-dominated front across all islands."""
        programs = self._all_population_programs()
        if not programs:
            return []

        objective_vectors = {
            program.id: self._get_objective_vector(program) or [] for program in programs
        }
        front = []
        for candidate in programs:
            vec_candidate = objective_vectors[candidate.id]
            dominated = False
            for challenger in programs:
                if challenger.id == candidate.id:
                    continue
                if self._dominates(objective_vectors[challenger.id], vec_candidate):
                    dominated = True
                    break
            if not dominated:
                front.append(candidate)

        return sorted(front, key=self._get_pareto_representative_sort_key, reverse=True)
````

## → Calls
- [[AdaEvolveDatabase._all_population_programs]]
- [[AdaEvolveDatabase._dominates]]
- [[AdaEvolveDatabase._get_objective_vector]]
- [[AdaEvolveDatabase._get_pareto_representative_sort_key]]
- [[Program.id]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._update_best_program]]
- [[AdaEvolveDatabase.get_global_pareto_front]]
