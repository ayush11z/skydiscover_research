---
name: OpenEvolveNativeDatabase._sample_parent
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._sample_parent

**File:** `skydiscover/search/openevolve_native/database.py:288`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _sample_parent(self) -> Program:
        rand_val = random.random()
        if rand_val < self.exploration_ratio:
            return self._sample_exploration_parent()
        elif rand_val < self.exploration_ratio + self.exploitation_ratio:
            return self._sample_exploitation_parent()
        else:
            return self._sample_random_parent()
````

## → Calls
- [[OpenEvolveNativeDatabase._sample_exploitation_parent]]
- [[OpenEvolveNativeDatabase._sample_exploration_parent]]
- [[OpenEvolveNativeDatabase._sample_random_parent]]
- [[base_database.Program]]

## ← Called by
- [[OpenEvolveNativeDatabase.sample]]
