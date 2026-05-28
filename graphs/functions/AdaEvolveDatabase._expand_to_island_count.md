---
name: AdaEvolveDatabase._expand_to_island_count
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._expand_to_island_count

**File:** `skydiscover/search/adaevolve/database.py:1436`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _expand_to_island_count(self, target_count: int, metadata: Dict[str, Any]) -> None:
        """
        Expand archives/islands to accommodate more islands from checkpoint.

        Args:
            target_count: Target number of islands
            metadata: Checkpoint metadata for config restoration
        """
        # Legacy mode: just expand island lists
        if not self.use_unified_archive:
            while len(self.islands) < target_count:
                self.islands.append([])
                self.children_map.append({})
                self.island_config_names.append("balanced")
                # Add adaptive state dimension
                state = AdaptiveState(
                    decay=self.decay,
                    intensity_min=self.intensity_min,
                    intensity_max=self.intensity_max,
                )
                self.adapter.add_dimension(state)
            return

        higher_is_better = getattr(self.config, "higher_is_better", {})
        saved_config_names = metadata.get("island_config_names", [])

        while len(self.archives) < target_count:
            new_idx = len(self.archives)

            # Get config name from saved state or default to "balanced"
            config_name = (
                saved_config_names[new_idx] if new_idx < len(saved_config_names) else "balanced"
            )
            preset = get_island_config_preset(config_name)

            archive_config = ArchiveConfig(
                max_size=self.population_size,
                k_neighbors=getattr(self.config, "k_neighbors", 5),
                elite_ratio=preset["elite_ratio"],
                pareto_weight=preset["pareto_weight"],
                fitness_weight=preset["fitness_weight"],
                novelty_weight=preset["novelty_weight"],
                higher_is_better=higher_is_better,
            )

            # Create fresh diversity strategy
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

            # Add adaptive state dimension
            state = AdaptiveState(
                decay=self.decay,
                intensity_min=self.intensity_min,
                intensity_max=self.intensity_max,
            )
            self.adapter.add_dimension(state)
````

## → Calls
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
- [[database.get_island_config_preset]]
- [[diversity.create_diversity_strategy]]
- [[unified_archive.ArchiveConfig]]
- [[unified_archive.UnifiedArchive]]

## ← Called by
- [[AdaEvolveDatabase.load]]
