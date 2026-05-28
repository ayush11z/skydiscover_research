---
name: GEPANativeDatabase.load
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase.load

**File:** `skydiscover/search/gepa_native/database.py:243`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def load(self, path: str) -> None:
        """Load base state plus GEPA-specific metadata."""
        super().load(path)

        metadata_path = os.path.join(path, "gepa_metadata.json")
        if not os.path.exists(metadata_path):
            # Legacy checkpoint — rebuild from programs
            self._rebuild_elite_pool()
            return

        with open(metadata_path, "r") as f:
            metadata = json.load(f)

        # Restore elite pool (filter out IDs no longer in programs)
        self.elite_pool = [pid for pid in metadata.get("elite_pool", []) if pid in self.programs]

        # Restore initial program
        self.initial_program_id = metadata.get("initial_program_id")

        # Restore per-metric best
        for k, v in metadata.get("metric_best", {}).items():
            pid, score = v[0], v[1]
            if pid in self.programs:
                self.metric_best[k] = (pid, score)

        # Restore metric Pareto front
        self.program_at_metric_front = {
            k: {pid for pid in v if pid in self.programs}
            for k, v in metadata.get("program_at_metric_front", {}).items()
        }

        # Restore rejection history
        self.rejection_history.clear()
        for prog_dict in metadata.get("rejection_history", []):
            try:
                self.rejection_history.append(Program.from_dict(prog_dict))
            except Exception as e:
                logger.warning(f"Failed to load rejected program from history: {e}")
````

## → Calls
- [[CheckpointManager.load]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[GEPANativeDatabase._rebuild_elite_pool]]
- [[LangFuseTracer.get]]
- [[Program.from_dict]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.load]]
- [[UnifiedArchive.get]]

## ← Called by
_(entry point — nothing in this graph calls it)_
