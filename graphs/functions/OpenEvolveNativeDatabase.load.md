---
name: OpenEvolveNativeDatabase.load
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase.load

**File:** `skydiscover/search/openevolve_native/database.py:838`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def load(self, path: str) -> None:
        super().load(path)

        meta_path = os.path.join(path, "openevolve_native_metadata.json")
        if not os.path.exists(meta_path):
            logger.warning(
                "No openevolve_native_metadata.json found; distributing " "programs round-robin"
            )
            self._distribute_programs_to_islands()
            return

        with open(meta_path, "r") as f:
            meta = json.load(f)

        self.island_feature_maps = meta.get(
            "island_feature_maps", [{} for _ in range(self.num_islands)]
        )
        saved_islands = meta.get("islands", [])
        self.archive = set(meta.get("archive", []))
        self.island_best_programs = meta.get("island_best_programs", [None] * self.num_islands)
        self.current_island = meta.get("current_island", 0)
        self.island_generations = meta.get("island_generations", [0] * self.num_islands)
        self.last_migration_generation = meta.get("last_migration_generation", 0)
        self.feature_stats = self._deserialize_feature_stats(meta.get("feature_stats", {}))

        self._reconstruct_islands(saved_islands)
        self._log_island_status()
````

## → Calls
- [[CheckpointManager.load]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[LangFuseTracer.get]]
- [[OpenEvolveNativeDatabase._deserialize_feature_stats]]
- [[OpenEvolveNativeDatabase._distribute_programs_to_islands]]
- [[OpenEvolveNativeDatabase._log_island_status]]
- [[OpenEvolveNativeDatabase._reconstruct_islands]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.load]]
- [[UnifiedArchive.get]]

## ← Called by
_(entry point — nothing in this graph calls it)_
