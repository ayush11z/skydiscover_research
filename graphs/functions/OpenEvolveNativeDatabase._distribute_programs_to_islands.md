---
name: OpenEvolveNativeDatabase._distribute_programs_to_islands
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._distribute_programs_to_islands

**File:** `skydiscover/search/openevolve_native/database.py:903`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _distribute_programs_to_islands(self) -> None:
        for i, pid in enumerate(self.programs):
            idx = i % self.num_islands
            self.islands[idx].add(pid)
            self.programs[pid].metadata["island"] = idx
````

## → Calls
- [[CheckpointManager.load]]

## ← Called by
- [[OpenEvolveNativeDatabase._reconstruct_islands]]
- [[OpenEvolveNativeDatabase.load]]
