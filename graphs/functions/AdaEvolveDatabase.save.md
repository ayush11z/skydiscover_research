---
name: AdaEvolveDatabase.save
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.save

**File:** `skydiscover/search/adaevolve/database.py:1201`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def save(self, path: Optional[str] = None, iteration: int = 0) -> None:
        """
        Save database with AdaEvolve-specific state.

        This properly saves:
        1. All programs (via base class)
        2. Island membership (which programs in which island)
        3. Archive genealogy state (parent-child tracking)
        4. Adaptive state (UCB rewards, accumulated signals)
        5. Paradigm tracker state
        """
        save_path = path or self.config.db_path
        if not save_path:
            logger.warning("No database path specified, skipping save")
            return

        # Sync programs dict from archives/islands
        # CRITICAL: Preserve best program before rebuilding programs dict
        best_id = self.best_program_id
        best_program = self.programs.get(best_id) if best_id else None

        self.programs = {}
        if self.use_unified_archive and self.archives:
            for archive in self.archives:
                for p in archive.get_all():
                    self.programs[p.id] = p
        else:
            for island in self.islands:
                for p in island:
                    self.programs[p.id] = p

        # Restore best program if it was evicted (safety net)
        if best_program and best_id not in self.programs:
            self.programs[best_id] = best_program
            # Re-add to first archive to ensure it survives future save cycles
            if self.use_unified_archive and self.archives:
                self.archives[0].add(best_program)
            logger.warning(f"Restored evicted best program {best_id[:8]} during save")

        # Save base state (programs, prompts, artifacts)
        super().save(save_path, iteration)

        # Build AdaEvolve metadata
        metadata = {
            "num_islands": self.num_islands,
            "current_island": self.current_island,
            "iteration_count": self._iteration_count,
            "global_best_score": self._global_best_score,
            "decay": self.decay,
            "intensity_min": self.intensity_min,
            "intensity_max": self.intensity_max,
            "migration_interval": self.migration_interval,
            "diversity_strategy_type": self._diversity_strategy_type,
            "use_unified_archive": self.use_unified_archive,
            # Ablation flags
            "use_adaptive_search": self.use_adaptive_search,
            "use_ucb_selection": self.use_ucb_selection,
            "fixed_intensity": self.fixed_intensity,
            # Adapter state (UCB rewards, accumulated signals, etc.)
            "adapter": self.adapter.to_dict(),
            # Island config names for dynamic spawning
            "island_config_names": self.island_config_names,
        }

        # Island membership and genealogy depend on mode
        if self.use_unified_archive and self.archives:
            metadata["islands"] = [[p.id for p in archive.get_all()] for archive in self.archives]
            metadata["archive_genealogies"] = [
                archive.get_genealogy_state() for archive in self.archives
            ]
        else:
            metadata["islands"] = [[p.id for p in island] for island in self.islands]
            metadata["children_map"] = self.children_map

        # Save dynamic island state if enabled
        if self.use_dynamic_islands:
            metadata["use_dynamic_islands"] = True
            metadata["max_islands"] = self.max_islands
            metadata["last_spawn_iteration"] = self.last_spawn_iteration

        # Save paradigm tracker state if enabled
        if self.use_paradigm_breakthrough and self.paradigm_tracker is not None:
            metadata["use_paradigm_breakthrough"] = True
            metadata["paradigm_tracker"] = self.paradigm_tracker.to_dict()

        os.makedirs(save_path, exist_ok=True)
        metadata_path = os.path.join(save_path, "adaevolve_metadata.json")
        with open(metadata_path, "w") as f:
            from skydiscover.search.utils.checkpoint_manager import SafeJSONEncoder

            json.dump(metadata, f, indent=2, cls=SafeJSONEncoder)

        logger.info(f"Saved AdaEvolve state to {save_path}")
````

## → Calls
- [[AdaEvolveDatabase.__init__]]
- [[AdaptiveState.to_dict]]
- [[CheckpointManager.load]]
- [[Config.to_dict]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[DiscoveryControllerInput.config]]
- [[EvaluationResult.to_dict]]
- [[LangFuseTracer.get]]
- [[MultiDimensionalAdapter.select_dimension_ucb]]
- [[ParadigmTracker.to_dict]]
- [[Program.to_dict]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.save]]
- [[UnifiedArchive.get]]
- [[UnifiedArchive.get_all]]
- [[UnifiedArchive.get_genealogy_state]]
- [[base_database.ProgramDatabase]]
- [[checkpoint_manager.SafeJSONEncoder]]

## ← Called by
_(entry point — nothing in this graph calls it)_
