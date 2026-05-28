---
name: OpenEvolveNativeDatabase.save
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase.save

**File:** `skydiscover/search/openevolve_native/database.py:817`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def save(self, path: Optional[str] = None, iteration: int = 0) -> None:
        super().save(path=path, iteration=iteration)

        save_path = path or getattr(self.config, "db_path", None)
        if not save_path:
            return

        meta = {
            "island_feature_maps": self.island_feature_maps,
            "islands": [list(s) for s in self.islands],
            "archive": list(self.archive),
            "island_best_programs": self.island_best_programs,
            "current_island": self.current_island,
            "island_generations": self.island_generations,
            "last_migration_generation": self.last_migration_generation,
            "feature_stats": self._serialize_feature_stats(),
        }
        os.makedirs(save_path, exist_ok=True)
        with open(os.path.join(save_path, "openevolve_native_metadata.json"), "w") as f:
            json.dump(meta, f)
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[DiscoveryControllerInput.config]]
- [[LangFuseTracer.get]]
- [[OpenEvolveNativeDatabase._serialize_feature_stats]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.save]]
- [[UnifiedArchive.get]]
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
