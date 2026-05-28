---
name: GEPANativeDatabase.save
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase.save

**File:** `skydiscover/search/gepa_native/database.py:221`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def save(self, path: Optional[str] = None, iteration: int = 0) -> None:
        """Save base state plus GEPA-specific metadata."""
        super().save(path=path, iteration=iteration)

        save_path = path or self.config.db_path
        if not save_path:
            return

        metadata = {
            "elite_pool": self.elite_pool,
            "initial_program_id": self.initial_program_id,
            "metric_best": {k: list(v) for k, v in self.metric_best.items()},
            "program_at_metric_front": {
                k: list(v) for k, v in self.program_at_metric_front.items()
            },
            "rejection_history": [prog.to_dict() for prog in self.rejection_history],
        }
        os.makedirs(save_path, exist_ok=True)

        with open(os.path.join(save_path, "gepa_metadata.json"), "w") as f:
            json.dump(metadata, f, indent=2, cls=SafeJSONEncoder)
````

## → Calls
- [[AdaptiveState.to_dict]]
- [[Config.to_dict]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[DiscoveryControllerInput.config]]
- [[EvaluationResult.to_dict]]
- [[GEPANativeDatabase.__init__]]
- [[ParadigmTracker.to_dict]]
- [[Program.id]]
- [[Program.to_dict]]
- [[ProgramDatabase.save]]
- [[base_database.ProgramDatabase]]
- [[checkpoint_manager.SafeJSONEncoder]]

## ← Called by
_(entry point — nothing in this graph calls it)_
