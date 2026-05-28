---
name: UnifiedArchive._compute_elite_score
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._compute_elite_score

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:283`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _compute_elite_score(self, program: Program, n: int) -> float:
        """
        Compute unified elite score.

        When pareto_objectives configured:
            elite_score = fitness_weight * fitness_pct
                        + novelty_weight * novelty_pct
                        + pareto_objectives_weight * pareto_pct

        Otherwise (backward compatible):
            elite_score = (fitness_weight + pareto_weight) * fitness_pct
                        + novelty_weight * novelty_pct
        """
        fitness_rank = self._fitness_ranks.get(program.id, n - 1)
        fitness_percentile = 1.0 - (fitness_rank / max(n - 1, 1))

        novelty = self._novelty_scores.get(program.id, 0.0)
        novelty_percentile = self._novelty_to_percentile(novelty)

        if self._pareto_percentiles and self.config.pareto_objectives:
            pareto_percentile = self._pareto_percentiles.get(program.id, 0.0)
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
- [[Program.id]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive._novelty_to_percentile]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[UnifiedArchive._ensure_cache_valid]]
