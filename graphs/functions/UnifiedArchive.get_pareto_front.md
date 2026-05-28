---
name: UnifiedArchive.get_pareto_front
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.get_pareto_front

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:865`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_pareto_front(self) -> List[Program]:
        """Get non-dominated Pareto front when objectives configured, else top programs."""
        if self.config.pareto_objectives and self._pareto_ranks:
            self._ensure_cache_valid()
            return [
                self._programs[pid]
                for pid, rank in self._pareto_ranks.items()
                if rank == 0 and pid in self._programs
            ]
        return self.get_top_programs()
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._ensure_cache_valid]]
- [[UnifiedArchive.get_top_programs]]
- [[base_database.Program]]

## ← Called by
- [[UnifiedArchive.stats]]
