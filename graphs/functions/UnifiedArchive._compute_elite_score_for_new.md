---
name: UnifiedArchive._compute_elite_score_for_new
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._compute_elite_score_for_new

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:317`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _compute_elite_score_for_new(self, program: Program) -> float:
        """
        Compute elite score for a new program (admission decision).

        Uses same formulas as cached programs for consistent comparison.
        """
        programs = list(self._programs.values())
        n = len(programs)
        use_pareto = bool(self.config.pareto_objectives and self._pareto_ranks)

        if n == 0:
            total_weight = self.config.fitness_weight + self.config.novelty_weight
            if use_pareto:
                total_weight += self.config.pareto_objectives_weight
            else:
                total_weight += self.config.pareto_weight
            return total_weight  # max score (all components = 1.0)

        # === Fitness percentile ===
        fitness = self._get_fitness(program)
        better_count = sum(1 for p in programs if self._get_fitness(p) > fitness)

        if n == 1:
            fitness_percentile = 1.0 if better_count == 0 else 0.0
        else:
            fitness_percentile = 1.0 - (better_count / (n - 1))
        fitness_percentile = max(0.0, min(1.0, fitness_percentile))

        # === Novelty percentile ===
        novelty = self._compute_novelty(program, programs)

        if self._cache_valid and self._novelty_scores:
            existing_novelties = [self._novelty_scores.get(p.id, 0.0) for p in programs]
        else:
            existing_novelties = [self._compute_novelty(p, programs) for p in programs]

        lower_count = sum(1 for n_val in existing_novelties if n_val < novelty)
        novelty_percentile = lower_count / n
        novelty_percentile = max(0.0, min(1.0, novelty_percentile))

        # === Pareto percentile ===
        if use_pareto:
            new_vec = self._get_objective_vector(program)
            dominated_by = sum(
                1 for p in programs if self._dominates(self._get_objective_vector(p), new_vec)
            )
            pareto_percentile = 1.0 - (dominated_by / max(n, 1))
            pareto_percentile = max(0.0, min(1.0, pareto_percentile))

            return (
                self.config.fitness_weight * fitness_percentile
                + self.config.novelty_weight * novelty_percentile
                + self.config.pareto_objectives_weight * pareto_percentile
            )

        # No Pareto objectives: redistribute pareto_weight to fitness
        effective_fitness_weight = self.config.fitness_weight + self.config.pareto_weight
        return (
            effective_fitness_weight * fitness_percentile
            + self.config.novelty_weight * novelty_percentile
        )
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._compute_novelty]]
- [[UnifiedArchive._dominates]]
- [[UnifiedArchive._get_fitness]]
- [[UnifiedArchive._get_objective_vector]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[UnifiedArchive.add]]
- [[UnifiedArchive.add_merged_program]]
