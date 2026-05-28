---
name: AdaEvolveDatabase._spawn_island
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._spawn_island

**File:** `skydiscover/search/adaevolve/database.py:2043`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _spawn_island(self) -> int:
        """
        Spawn a new island and initialize it with top programs.

        Returns:
            Index of the newly created island
        """
        new_island_idx = self.num_islands

        # Select config for new island
        config_name, preset = self._select_spawn_config()

        # Create new archive with the selected preset
        higher_is_better = getattr(self.config, "higher_is_better", {})
        archive_config = ArchiveConfig(
            max_size=self.population_size,
            k_neighbors=getattr(self.config, "k_neighbors", 5),
            elite_ratio=preset["elite_ratio"],
            pareto_weight=preset["pareto_weight"],
            fitness_weight=preset["fitness_weight"],
            novelty_weight=preset["novelty_weight"],
            higher_is_better=higher_is_better,
            pareto_objectives=getattr(self.config, "pareto_objectives", []),
            pareto_objectives_weight=getattr(self.config, "pareto_objectives_weight", 0.0),
            fitness_key=getattr(self.config, "fitness_key", None),
        )

        # Create FRESH diversity strategy for new island
        # This is critical for stateful strategies like MetricDiversity
        # which maintain internal state that would be contaminated if shared
        diversity_strategy = create_diversity_strategy(
            self._diversity_strategy_type,
            higher_is_better=higher_is_better,
        )

        new_archive = UnifiedArchive(
            config=archive_config,
            diversity_strategy=diversity_strategy,
        )
        self.archives.append(new_archive)
        self.island_config_names.append(config_name)

        # Add new dimension to adapter
        state = AdaptiveState(
            decay=self.decay,
            intensity_min=self.intensity_min,
            intensity_max=self.intensity_max,
        )
        self.adapter.add_dimension(state)

        # Seed new island with top programs
        self._seed_new_island(new_island_idx)

        # Update count and record spawn
        self.num_islands += 1
        self.last_spawn_iteration = self._iteration_count

        logger.info(
            f"Spawned new island {new_island_idx} with config '{config_name}' "
            f"(total islands: {self.num_islands}/{self.max_islands})"
        )

        return new_island_idx
````

## → Calls
- [[AdaEvolveDatabase._seed_new_island]]
- [[AdaEvolveDatabase._select_spawn_config]]
- [[AdaEvolveDatabaseConfig.population_size]]
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[DiscoveryControllerInput.config]]
- [[Evaluator.__init__]]
- [[GEPANativeDatabaseConfig.population_size]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LangFuseTracer.get]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[MultiDimensionalAdapter.add_dimension]]
- [[MultiDimensionalAdapter.from_dict]]
- [[OpenAILLM.__init__]]
- [[OpenEvolveNativeDatabaseConfig.population_size]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[ProgramDatabase.get]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive.get]]
- [[_FinalResult.__init__]]
- [[adaptation.AdaptiveState]]
- [[base_database.ProgramDatabase]]
- [[diversity.create_diversity_strategy]]
- [[unified_archive.ArchiveConfig]]
- [[unified_archive.UnifiedArchive]]

## ← Called by
- [[AdaEvolveDatabase.end_iteration]]
