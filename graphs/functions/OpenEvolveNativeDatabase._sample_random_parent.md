---
name: OpenEvolveNativeDatabase._sample_random_parent
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._sample_random_parent

**File:** `skydiscover/search/openevolve_native/database.py:340`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _sample_random_parent(self) -> Program:
        """Uniformly random program from entire population."""
        return self.programs[random.choice(list(self.programs.keys()))]
````

## → Calls
- [[CheckpointManager.load]]
- [[base_database.Program]]

## ← Called by
- [[OpenEvolveNativeDatabase._sample_parent]]
