---
name: OpenEvolveNativeDatabase._update_island_best_program
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._update_island_best_program

**File:** `skydiscover/search/openevolve_native/database.py:673`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _update_island_best_program(self, program: Program, island_idx: int) -> None:
        if island_idx >= len(self.island_best_programs):
            return
        cur_id = self.island_best_programs[island_idx]
        if cur_id is None or cur_id not in self.programs:
            self.island_best_programs[island_idx] = program.id
            return
        if self._is_better(program, self.programs[cur_id]):
            self.island_best_programs[island_idx] = program.id
````

## → Calls
- [[CheckpointManager.load]]
- [[LangFuseTracer.get]]
- [[OpenEvolveNativeDatabase._is_better]]
- [[Program.id]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[OpenEvolveNativeDatabase.add]]
