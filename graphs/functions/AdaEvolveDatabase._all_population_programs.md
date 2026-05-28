---
name: AdaEvolveDatabase._all_population_programs
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._all_population_programs

**File:** `skydiscover/search/adaevolve/database.py:1532`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _all_population_programs(self) -> List[Program]:
        """Return all currently active programs across islands."""
        if self.use_unified_archive and self.archives:
            programs = []
            for archive in self.archives:
                programs.extend(archive.get_all())
            return programs
        if self.islands:
            programs = []
            for island in self.islands:
                programs.extend(island)
            return programs
        return list(self.programs.values())
````

## → Calls
- [[AdaEvolveDatabase.__init__]]
- [[CheckpointManager.load]]
- [[UnifiedArchive.get_all]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._compute_global_pareto_front]]
- [[AdaEvolveDatabase._sample_global_top]]
- [[AdaEvolveDatabase.get_top_programs]]
