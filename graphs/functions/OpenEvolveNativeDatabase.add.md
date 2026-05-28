---
name: OpenEvolveNativeDatabase.add
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase.add

**File:** `skydiscover/search/openevolve_native/database.py:204`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def add(
        self,
        program: Program,
        iteration: Optional[int] = None,
        **kwargs: Any,
    ) -> str:
        target_island: Optional[int] = kwargs.get("target_island")
        is_migration: bool = kwargs.get("_is_migration", False)

        if iteration is not None:
            program.iteration_found = iteration
            self.last_iteration = max(self.last_iteration, iteration)

        self.programs[program.id] = program

        # Feature coordinates for MAP-Elites
        feature_coords = self._calculate_feature_coords(program)

        # --- Determine target island ---
        if target_island is not None:
            island_idx = target_island
        elif program.parent_id:
            parent = self.programs.get(program.parent_id)
            if parent and "island" in parent.metadata:
                island_idx = parent.metadata["island"]
            else:
                island_idx = self.current_island
        else:
            island_idx = self.current_island
        island_idx = island_idx % self.num_islands

        # --- MAP-Elites: insert into island feature map if better ---
        feature_key = self._feature_coords_to_key(feature_coords)
        island_feature_map = self.island_feature_maps[island_idx]

        should_replace = feature_key not in island_feature_map
        if not should_replace:
            existing_id = island_feature_map[feature_key]
            if existing_id not in self.programs:
                should_replace = True  # stale reference
            else:
                should_replace = self._is_better(program, self.programs[existing_id])

        if should_replace:
            if feature_key in island_feature_map:
                existing_id = island_feature_map[feature_key]
                if existing_id in self.programs:
                    # Swap archive membership
                    if existing_id in self.archive:
                        self.archive.discard(existing_id)
                        self.archive.add(program.id)
                # Remove replaced program from island set
                self.islands[island_idx].discard(existing_id)
            island_feature_map[feature_key] = program.id

        # Add to island
        self.islands[island_idx].add(program.id)
        program.metadata["island"] = island_idx

        # Archive, population limit, best-program tracking
        self._update_archive(program)
        self._enforce_population_limit(exclude_program_id=program.id)
        self._update_best_program(program)
        self._update_island_best_program(program, island_idx)

        # Save to disk
        if self.config.db_path:
            self._save_program(program)

        # --- Post-add: generation increment + migration ---
        # (OpenEvolve's controller calls these separately; we fold them
        # into add() because DiscoveryController doesn't.)
        if not is_migration:
            self.island_generations[island_idx] += 1
            if self._should_migrate():
                self._migrate_programs()

        logger.debug("Added program %s to island %d", program.id, island_idx)
        return program.id
````

## → Calls
- [[CheckpointManager._save_program]]
- [[CheckpointManager.load]]
- [[DiscoveryControllerInput.config]]
- [[OpenEvolveNativeDatabase._calculate_feature_coords]]
- [[OpenEvolveNativeDatabase._enforce_population_limit]]
- [[OpenEvolveNativeDatabase._feature_coords_to_key]]
- [[OpenEvolveNativeDatabase._is_better]]
- [[OpenEvolveNativeDatabase._migrate_programs]]
- [[OpenEvolveNativeDatabase._should_migrate]]
- [[OpenEvolveNativeDatabase._update_archive]]
- [[OpenEvolveNativeDatabase._update_best_program]]
- [[OpenEvolveNativeDatabase._update_island_best_program]]
- [[Program.id]]
- [[Program.metadata]]
- [[Program.parent_id]]
- [[ProgramDatabase._save_program]]
- [[ProgramDatabase.load]]
- [[SerializableResult.parent_id]]
- [[base_database.Program]]
- [[base_database.ProgramDatabase]]

## ← Called by
- [[OpenEvolveNativeDatabase._migrate_programs]]
