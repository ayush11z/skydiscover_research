---
name: OpenEvolveNativeDatabase._should_migrate
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._should_migrate

**File:** `skydiscover/search/openevolve_native/database.py:743`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _should_migrate(self) -> bool:
        if self.num_islands < 2:
            return False
        return (
            max(self.island_generations) - self.last_migration_generation
        ) >= self.migration_interval
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[OpenEvolveNativeDatabase.add]]
