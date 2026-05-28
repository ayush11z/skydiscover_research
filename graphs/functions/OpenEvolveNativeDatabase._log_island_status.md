---
name: OpenEvolveNativeDatabase._log_island_status
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._log_island_status

**File:** `skydiscover/search/openevolve_native/database.py:944`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _log_island_status(self) -> None:
        for i, island in enumerate(self.islands):
            progs = [self.programs[pid] for pid in island if pid in self.programs]
            if progs:
                scores = [_get_fitness(p.metrics, self.feature_dimensions) for p in progs]
                best, avg = max(scores), sum(scores) / len(scores)
            else:
                best = avg = 0.0
            cells = len(self.island_feature_maps[i]) if i < len(self.island_feature_maps) else 0
            gen = self.island_generations[i] if i < len(self.island_generations) else 0
            logger.info(
                "Island %d: %d programs, %d cells, gen=%d, best=%.4f, avg=%.4f%s",
                i,
                len(progs),
                cells,
                gen,
                best,
                avg,
                " [current]" if i == self.current_island else "",
            )
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
- [[OpenEvolveNativeDatabase.load]]
