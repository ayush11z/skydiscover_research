---
name: OpenEvolveNativeDatabase._sample_exploration_parent
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._sample_exploration_parent

**File:** `skydiscover/search/openevolve_native/database.py:297`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _sample_exploration_parent(self) -> Program:
        """Random program from current island (diverse sampling)."""
        island_programs = self.islands[self.current_island]

        if not island_programs:
            return self._seed_empty_island(self.current_island)

        valid = [pid for pid in island_programs if pid in self.programs]
        # Remove stale refs
        if len(valid) < len(island_programs):
            for stale in island_programs - set(valid):
                self.islands[self.current_island].discard(stale)

        if not valid:
            return self._seed_empty_island(self.current_island)

        return self.programs[random.choice(valid)]
````

## → Calls
- [[CheckpointManager.load]]
- [[OpenEvolveNativeDatabase._seed_empty_island]]
- [[base_database.Program]]

## ← Called by
- [[OpenEvolveNativeDatabase._sample_exploitation_parent]]
- [[OpenEvolveNativeDatabase._sample_parent]]
