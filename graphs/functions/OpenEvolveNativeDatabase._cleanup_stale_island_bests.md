---
name: OpenEvolveNativeDatabase._cleanup_stale_island_bests
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._cleanup_stale_island_bests

**File:** `skydiscover/search/openevolve_native/database.py:725`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _cleanup_stale_island_bests(self) -> None:
        for i, best_id in enumerate(self.island_best_programs):
            if best_id is None:
                continue
            if best_id not in self.programs or best_id not in self.islands[i]:
                self.island_best_programs[i] = None
                # Recalculate
                progs = [self.programs[pid] for pid in self.islands[i] if pid in self.programs]
                if progs:
                    self.island_best_programs[i] = max(
                        progs,
                        key=lambda p: _get_fitness(p.metrics, self.feature_dimensions),
                    ).id
````

## → Calls
- [[CheckpointManager.load]]
- [[EvaluationResult.metrics]]
- [[LangFuseTracer.get]]
- [[Program.metrics]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[database._get_fitness]]

## ← Called by
- [[OpenEvolveNativeDatabase._enforce_population_limit]]
- [[OpenEvolveNativeDatabase._reconstruct_islands]]
