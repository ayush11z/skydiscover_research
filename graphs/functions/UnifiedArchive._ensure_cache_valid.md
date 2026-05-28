---
name: UnifiedArchive._ensure_cache_valid
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._ensure_cache_valid

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:234`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _ensure_cache_valid(self) -> None:
        """Recompute caches if invalid."""
        if self._cache_valid:
            return

        programs = list(self._programs.values())
        n = len(programs)

        if n == 0:
            self._cache_valid = True
            return

        # Update diversity strategy bounds
        self.diversity.update(programs)

        # Compute fitness ranks (higher fitness = higher rank)
        fitness_sorted = sorted(programs, key=lambda p: self._get_fitness(p), reverse=True)
        self._fitness_ranks = {p.id: i for i, p in enumerate(fitness_sorted)}

        # Compute Pareto ranking on explicit objectives (no-op when unconfigured)
        self._compute_pareto_ranking(programs)
        if self._pareto_ranks:
            entries = [
                (pid, self._pareto_ranks[pid], self._crowding_distances.get(pid, 0.0))
                for pid in self._pareto_ranks
            ]
            entries.sort(key=lambda x: (x[1], -x[2]))
            n_entries = max(len(entries) - 1, 1)
            self._pareto_percentiles = {
                pid: 1.0 - (i / n_entries) for i, (pid, _, _) in enumerate(entries)
            }
        else:
            self._pareto_percentiles = {}
        self._dominated_flags = {}

        # Compute novelty scores (O(n²) but used for diversity-based sampling)
        self._novelty_scores = {p.id: self._compute_novelty(p, programs) for p in programs}

        # Compute elite scores
        self._elite_scores = {}
        for p in programs:
            self._elite_scores[p.id] = self._compute_elite_score(p, n)

        self._cache_valid = True
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._compute_elite_score]]
- [[UnifiedArchive._compute_novelty]]
- [[UnifiedArchive._compute_pareto_ranking]]
- [[UnifiedArchive._get_fitness]]
- [[UnifiedArchive.get]]

## ← Called by
- [[AdaEvolveDatabase._get_archive_crowding_distance]]
- [[AdaEvolveDatabase._get_archive_elite_score]]
- [[AdaEvolveDatabase._sample_pareto_front]]
- [[UnifiedArchive.add]]
- [[UnifiedArchive.add_merged_program]]
- [[UnifiedArchive.get_pareto_front]]
- [[UnifiedArchive.sample_parent]]
- [[UnifiedArchive.stats]]
