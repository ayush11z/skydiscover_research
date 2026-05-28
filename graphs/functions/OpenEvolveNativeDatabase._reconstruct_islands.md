---
name: OpenEvolveNativeDatabase._reconstruct_islands
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._reconstruct_islands

**File:** `skydiscover/search/openevolve_native/database.py:870`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _reconstruct_islands(self, saved_islands: List[List[str]]) -> None:
        num_islands = max(len(saved_islands), self.num_islands)
        self.islands = [set() for _ in range(num_islands)]

        for island_idx, program_ids in enumerate(saved_islands):
            if island_idx >= len(self.islands):
                continue
            for pid in program_ids:
                if pid in self.programs:
                    self.islands[island_idx].add(pid)
                    self.programs[pid].metadata["island"] = island_idx

        # Clean stale refs from archive and feature maps
        self.archive = {pid for pid in self.archive if pid in self.programs}
        for imap in self.island_feature_maps:
            for k in [k for k, pid in imap.items() if pid not in self.programs]:
                del imap[k]

        self._cleanup_stale_island_bests()

        if self.best_program_id and self.best_program_id not in self.programs:
            self.best_program_id = None

        # If no island assignments recovered, distribute round-robin
        if self.programs and sum(len(s) for s in self.islands) == 0:
            self._distribute_programs_to_islands()

        # Ensure list lengths match
        while len(self.island_generations) < len(self.islands):
            self.island_generations.append(0)
        while len(self.island_best_programs) < len(self.islands):
            self.island_best_programs.append(None)
````

## → Calls
- [[CheckpointManager.load]]
- [[LangFuseTracer.get]]
- [[OpenEvolveNativeDatabase._cleanup_stale_island_bests]]
- [[OpenEvolveNativeDatabase._distribute_programs_to_islands]]
- [[Program.id]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[OpenEvolveNativeDatabase.load]]
