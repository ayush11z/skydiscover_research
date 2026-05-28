---
name: AdaEvolveDatabase.load
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.load

**File:** `skydiscover/search/adaevolve/database.py:1295`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def load(self, path: str) -> None:
        """
        Load database with AdaEvolve-specific state.

        Restores:
        1. All programs (via base class)
        2. Island membership (programs to correct archives/islands)
        3. Archive genealogy state (or children_map for legacy)
        4. Adaptive state (UCB rewards, accumulated signals)
        5. Paradigm tracker state
        """
        # Load base state (programs dict, best_program_id, last_iteration)
        super().load(path)

        # Load AdaEvolve metadata
        metadata_path = os.path.join(path, "adaevolve_metadata.json")
        if not os.path.exists(metadata_path):
            logger.warning(
                f"No AdaEvolve metadata found at {path}, distributing programs to islands"
            )
            self._distribute_programs_to_islands()
            return

        with open(metadata_path, "r") as f:
            metadata = json.load(f)

        # Restore scalar state
        saved_num_islands = metadata.get("num_islands", self.num_islands)
        self.current_island = metadata.get("current_island", 0)
        self._iteration_count = metadata.get("iteration_count", 0)
        self._global_best_score = metadata.get("global_best_score", float("-inf"))
        self._diversity_strategy_type = metadata.get("diversity_strategy_type", "code")

        # NOTE: Ablation flags are NOT restored from checkpoint.
        # The current config's ablation settings take precedence.
        # This allows running ablation experiments from existing checkpoints.
        # (e.g., load a baseline checkpoint and run no_adaptive_search ablation)
        #
        # The adaptive STATE (G, UCB rewards, visits) IS restored from checkpoint,
        # only the FLAGS are kept from current config.

        # Handle dynamic island count - may need to expand
        if saved_num_islands > self.num_islands:
            logger.info(
                f"Checkpoint has {saved_num_islands} islands, " f"expanding from {self.num_islands}"
            )
            self._expand_to_island_count(saved_num_islands, metadata)

        self.num_islands = saved_num_islands

        # Load adapter state
        if "adapter" in metadata:
            self.adapter = MultiDimensionalAdapter.from_dict(metadata["adapter"])

        # Restore island config names
        self.island_config_names = metadata.get(
            "island_config_names", ["balanced"] * self.num_islands
        )

        # Restore dynamic island state
        if metadata.get("use_dynamic_islands", False):
            self.use_dynamic_islands = True
            self.max_islands = metadata.get("max_islands", self.max_islands)
            self.last_spawn_iteration = metadata.get("last_spawn_iteration", 0)

        # Restore paradigm tracker state IF current config has it enabled
        # We respect the current config's flag, not the checkpoint's flag
        # This allows ablation: load checkpoint with paradigm, run without it
        if self.use_paradigm_breakthrough and "paradigm_tracker" in metadata:
            # Current config wants paradigm - restore state from checkpoint
            self.paradigm_tracker = ParadigmTracker.from_dict(metadata["paradigm_tracker"])

        # Restore island membership based on mode
        island_ids = metadata.get("islands", [])

        if self.use_unified_archive:
            # Reinitialize archives to ensure clean state before restoring
            self.archives = []
            self._init_archives(self.config)
            genealogies = metadata.get("archive_genealogies", [])

            for island_idx, program_ids in enumerate(island_ids):
                if island_idx >= len(self.archives):
                    break

                archive = self.archives[island_idx]

                # Restore genealogy state first (for parent-child tracking)
                if island_idx < len(genealogies):
                    archive.set_genealogy_state(genealogies[island_idx])

                # Add programs to archive
                for pid in program_ids:
                    if pid in self.programs:
                        archive.add(self.programs[pid])
        else:
            # Legacy mode: restore to island lists
            self.islands = [[] for _ in range(self.num_islands)]
            self.children_map = metadata.get("children_map", [{} for _ in range(self.num_islands)])

            for island_idx, program_ids in enumerate(island_ids):
                if island_idx >= self.num_islands:
                    break

                for pid in program_ids:
                    if pid in self.programs:
                        self.islands[island_idx].append(self.programs[pid])

        self._invalidate_global_pareto_cache()
        logger.info(
            f"Loaded AdaEvolve state from {path}: "
            f"{self.num_islands} islands, {len(self.programs)} programs, "
            f"unified_archive={self.use_unified_archive}"
        )
````

## → Calls
- [[AdaEvolveDatabase._distribute_programs_to_islands]]
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._init_archives]]
- [[AdaEvolveDatabase._invalidate_global_pareto_cache]]
- [[CheckpointManager.load]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[DiscoveryControllerInput.config]]
- [[LangFuseTracer.get]]
- [[MultiDimensionalAdapter.from_dict]]
- [[ParadigmTracker.from_dict]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.load]]
- [[UnifiedArchive.get]]
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
