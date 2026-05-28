---
name: UnifiedArchive._get_protected_ids
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._get_protected_ids

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:599`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _get_protected_ids(self) -> Set[str]:
        """Get IDs of protected programs (top by elite_score + best by fitness + Pareto front)."""
        protected = set()

        # Protect top programs by elite score
        if self._elite_scores:
            elite_count = max(1, int(len(self._programs) * self.config.elite_ratio))
            sorted_ids = sorted(
                self._elite_scores.keys(), key=lambda pid: self._elite_scores[pid], reverse=True
            )
            protected.update(sorted_ids[:elite_count])

        # CRITICAL: Always protect the best program by fitness
        if self._programs:
            best_fitness_id = max(
                self._programs.keys(), key=lambda pid: self._get_fitness(self._programs[pid])
            )
            protected.add(best_fitness_id)

        # Protect Pareto front members (rank 0) when objectives are configured
        if self._pareto_ranks and self.config.pareto_objectives:
            for pid, rank in self._pareto_ranks.items():
                if rank == 0:
                    protected.add(pid)

        return protected
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._get_fitness]]

## ← Called by
- [[UnifiedArchive._find_eviction_candidate]]
- [[UnifiedArchive.stats]]
