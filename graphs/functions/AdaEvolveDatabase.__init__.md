---
name: AdaEvolveDatabase.__init__
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.__init__

**File:** `skydiscover/search/adaevolve/database.py:164`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def __init__(self, name: str, config: DatabaseConfig):
        super().__init__(name, config)

        # Language-aware label selection (set by Runner after creation)
        # Default to "python"; overridden to "text" for prompt optimization
        self.language: str = "python"

        # Configuration
        self.num_islands = getattr(config, "num_islands", 4)
        self.current_island = 0
        self.migration_interval = getattr(config, "migration_interval", 50)
        self.migration_count = getattr(config, "migration_count", 3)
        self._iteration_count = 0
        self.population_size = config.population_size
        self.higher_is_better = getattr(config, "higher_is_better", {}) or {}
        self.fitness_key = getattr(config, "fitness_key", None)
        self.pareto_objectives = list(getattr(config, "pareto_objectives", []) or [])

        # Unified archive flag (can be disabled for ablation studies)
        self.use_unified_archive = getattr(config, "use_unified_archive", True)

        # Adaptive configuration
        self.decay = getattr(config, "decay", 0.9)
        self.intensity_min = getattr(config, "intensity_min", 0.1)
        self.intensity_max = getattr(config, "intensity_max", 0.7)

        # Ablation flags for adaptive mechanisms
        # use_adaptive_search: When False, use fixed exploration ratio instead of G-based intensity
        # use_ucb_selection: When False, use round-robin island selection instead of UCB
        # use_migration: When False, disable inter-island migration
        self.use_adaptive_search = getattr(config, "use_adaptive_search", True)
        self.use_ucb_selection = getattr(config, "use_ucb_selection", True)
        self.use_migration = getattr(config, "use_migration", True)
        self.fixed_intensity = getattr(config, "fixed_intensity", 0.4)

        # Validate intensity bounds
        if self.intensity_min > self.intensity_max:
            logger.warning(
                f"intensity_min ({self.intensity_min}) > intensity_max ({self.intensity_max}). "
                f"This inverts the exploration/exploitation logic! Swapping values."
            )
            self.intensity_min, self.intensity_max = self.intensity_max, self.intensity_min

        if not (0.0 <= self.decay <= 1.0):
            logger.warning(f"decay ({self.decay}) should be in [0, 1]. Clamping.")
            self.decay = max(0.0, min(1.0, self.decay))

        # other context program mix (local vs global)
        self.local_context_program_ratio = getattr(config, "local_context_program_ratio", 0.6)

        # Dynamic island spawning configuration
        self.use_dynamic_islands = getattr(config, "use_dynamic_islands", False)
        self.max_islands = getattr(config, "max_islands", 8)
        self.spawn_productivity_threshold = getattr(config, "spawn_productivity_threshold", 0.02)
        self.spawn_cooldown = getattr(config, "spawn_cooldown_iterations", 50)
        self.last_spawn_iteration = -self.spawn_cooldown
        self.island_config_names: List[str] = ["balanced"] * self.num_islands

        if self.use_dynamic_islands and not self.use_unified_archive:
            logger.warning(
                "use_dynamic_islands=true requires use_unified_archive=true. "
                "Dynamic island spawning will be disabled."
            )

        # Paradigm breakthrough configuration
        self.use_paradigm_breakthrough = getattr(config, "use_paradigm_breakthrough", False)
        if self.use_paradigm_breakthrough:
            self.paradigm_tracker = ParadigmTracker(
                window_size=getattr(config, "paradigm_window_size", 30),
                improvement_threshold=getattr(config, "paradigm_improvement_threshold", 0.05),
                max_paradigm_uses=getattr(config, "paradigm_max_uses", 5),
                max_tried_paradigms=getattr(config, "paradigm_max_tried", 10),
                num_paradigms_to_generate=getattr(config, "paradigm_num_to_generate", 3),
            )
        else:
            self.paradigm_tracker = None

        # Multi-dimensional adapter handles ALL per-island adaptive state
        self.adapter = MultiDimensionalAdapter(decay=self.decay)
        for i in range(self.num_islands):
            state = AdaptiveState(
                decay=self.decay,
                intensity_min=self.intensity_min,
                intensity_max=self.intensity_max,
            )
            self.adapter.add_dimension(state)

        # Per-island storage: UnifiedArchive (default) or legacy list
        if self.use_unified_archive:
            self.archives: List[UnifiedArchive] = []
            self._init_archives(config)
            self.islands = None  # Not used in archive mode
            self.children_map = None  # Archive handles genealogy
        else:
            self.archives = None  # Not used in legacy mode
            self.islands: List[List[Program]] = [[] for _ in range(self.num_islands)]
            self.children_map: List[Dict[str, List[str]]] = [{} for _ in range(self.num_islands)]
            self._diversity_strategy_type = getattr(config, "diversity_strategy", "code")

        # Global best tracking
        self._global_best_score = float("-inf")

        # Cached global Pareto front (lazy, invalidated on population changes)
        self._global_pareto_cache: Optional[List[Program]] = None
        self._global_pareto_cache_valid: bool = False

        # Last sampling mode (stashed by sample() for the controller to read)
        self._last_sampling_mode: Optional[str] = None

        logger.info(
            f"AdaEvolveDatabase initialized: "
            f"num_islands={self.num_islands}, "
            f"decay={self.decay}, "
            f"intensity=[{self.intensity_min}, {self.intensity_max}], "
            f"migration={self.use_migration} (interval={self.migration_interval}), "
            f"unified_archive={self.use_unified_archive}, "
            f"adaptive_search={self.use_adaptive_search}, "
            f"ucb_selection={self.use_ucb_selection}, "
            f"dynamic_islands={self.use_dynamic_islands}, "
            f"paradigm_breakthrough={self.use_paradigm_breakthrough}, "
            f"multiobjective={self.is_multiobjective_enabled()}"
        )
````

## → Calls
- [[AdaEvolveDatabase._init_archives]]
- [[AdaEvolveDatabase.is_multiobjective_enabled]]
- [[AdaEvolveDatabaseConfig.population_size]]
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[GEPANativeDatabaseConfig.population_size]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[MultiDimensionalAdapter.add_dimension]]
- [[OpenAILLM.__init__]]
- [[OpenEvolveNativeDatabaseConfig.population_size]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[adaptation.AdaptiveState]]
- [[adaptation.MultiDimensionalAdapter]]
- [[base_database.Program]]
- [[config.DatabaseConfig]]
- [[tracker.ParadigmTracker]]
- [[unified_archive.UnifiedArchive]]

## ← Called by
- [[AdaEvolveDatabase._all_population_programs]]
- [[AdaEvolveDatabase._get_archive_crowding_distance]]
- [[AdaEvolveDatabase._get_archive_elite_score]]
- [[AdaEvolveDatabase._get_mode_labels]]
- [[AdaEvolveDatabase._init_archives]]
- [[AdaEvolveDatabase.active_programs]]
- [[AdaEvolveDatabase.add]]
- [[AdaEvolveDatabase.get_best_program]]
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[AdaEvolveDatabase.save]]
