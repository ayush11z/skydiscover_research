---
name: UnifiedArchive.__init__
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.__init__

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:72`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def __init__(
        self,
        config: Optional[ArchiveConfig] = None,
        diversity_strategy: Optional[DiversityStrategy] = None,
    ):
        """
        Args:
            config: Archive configuration
            diversity_strategy: Strategy for computing program distance.
                               Defaults to CodeDiversity.
        """
        self.config = config or ArchiveConfig()
        self.diversity = diversity_strategy or CodeDiversity()

        # Core storage
        self._programs: Dict[str, Program] = {}

        # Genealogy tracking
        self._parents: Dict[str, List[str]] = {}
        self._children: Dict[str, List[str]] = defaultdict(list)

        # Caches (invalidated on changes)
        self._elite_scores: Dict[str, float] = {}
        self._novelty_scores: Dict[str, float] = {}
        self._fitness_ranks: Dict[str, int] = {}
        self._dominated_flags: Dict[str, bool] = {}
        self._pareto_ranks: Dict[str, int] = {}
        self._crowding_distances: Dict[str, float] = {}
        self._pareto_percentiles: Dict[str, float] = {}
        self._cache_valid: bool = False

        logger.debug(
            f"UnifiedArchive initialized: max_size={self.config.max_size}, "
            f"k={self.config.k_neighbors}, elite_ratio={self.config.elite_ratio}"
        )
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[DiscoveryControllerInput.config]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[_FinalResult.__init__]]
- [[base_database.Program]]
- [[diversity.CodeDiversity]]
- [[diversity.DiversityStrategy]]
- [[unified_archive.ArchiveConfig]]

## ← Called by
- [[AdaEvolveController._ensure_all_islands_seeded]]
- [[AdaEvolveController._execute_generation]]
- [[AdaEvolveController._generate_child]]
- [[AdaEvolveController._process_result]]
- [[AdaEvolveController._run_normal_step]]
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._migrate_archives]]
- [[AdaEvolveDatabase._migrate_legacy]]
- [[AdaEvolveDatabase._seed_new_island]]
- [[AdaEvolveDatabase._spawn_island]]
- [[AdaEvolveDatabase.seed_all_islands]]
- [[AdaptiveState.from_dict]]
- [[ClaudeCodeController.run_discovery]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[Config.from_dict]]
- [[ContainerizedEvaluator._parse_output]]
- [[ContainerizedEvaluator._run_single_in_container]]
- [[ContainerizedEvaluator.evaluate_program]]
- [[DiscoveryController._call_llm]]
- [[DiscoveryController._create_child_program]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
- [[EvaluationResult.from_dict]]
- [[Evaluator._cascade_evaluate]]
- [[Evaluator._normalize_result]]
- [[Evaluator.evaluate_program]]
- [[GEPANativeController._attempt_merge]]
- [[HarborEvaluator._read_reward]]
- [[HarborEvaluator._run_container]]
- [[LLMJudge.evaluate]]
- [[MultiDimensionalAdapter.add_dimension]]
- [[MultiDimensionalAdapter.from_dict]]
- [[OpenAILLM._generate_with_image]]
- [[OpenAILLM.generate]]
- [[OpenEvolveNativeDatabase._migrate_programs]]
- [[OpenEvolveNativeDatabase._seed_empty_island]]
- [[ParadigmTracker.from_dict]]
- [[Program.from_dict]]
- [[Runner.run]]
- [[UnifiedArchive._compute_elite_score_for_new]]
- [[UnifiedArchive._compute_novelty]]
- [[UnifiedArchive._ensure_cache_valid]]
- [[UnifiedArchive._find_common_ancestor]]
- [[UnifiedArchive._find_eviction_candidate]]
- [[UnifiedArchive._get_objective_vector]]
- [[UnifiedArchive._get_protected_ids]]
- [[UnifiedArchive.add]]
- [[UnifiedArchive.add_merged_program]]
- [[UnifiedArchive.get]]
- [[UnifiedArchive.get_all]]
- [[UnifiedArchive.get_best]]
- [[UnifiedArchive.get_parents]]
- [[UnifiedArchive.get_pareto_front]]
- [[UnifiedArchive.get_top_programs]]
- [[UnifiedArchive.sample_other_context_programs]]
- [[UnifiedArchive.sample_parent]]
- [[_ConsoleFormatter.format]]
- [[_make_gepa_evaluator.gepa_evaluator]]
- [[api._run_discovery_async]]
- [[cli._configure_logging]]
- [[config.apply_overrides]]
- [[config.load_config]]
- [[gepa_backend.run]]
- [[logging_utils.setup_search_logging]]
- [[openevolve_backend._to_skydiscover_program]]
- [[openevolve_backend.run]]
- [[registry.setup_search]]
- [[search_strategy_evaluator.evaluate]]
- [[shinkaevolve_backend._to_skydiscover_program]]
- [[shinkaevolve_backend.run]]
- [[variation_operator_generator.main]]
