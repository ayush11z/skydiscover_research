---
name: ProgramDatabase.__init__
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.__init__

**File:** `skydiscover/search/base_database.py:87`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def __init__(self, name: str, config: DatabaseConfig, **kwargs: Any):
        self.name = name
        self.config = config

        # In-memory program storage
        self.programs: Dict[str, Program] = {}

        # Track the last iteration number (for resuming)
        self.last_iteration: int = 0

        # Optionally track initial program info (set by controller on first add)
        self.initial_program_id: Optional[str] = None
        self.initial_program_score: Optional[float] = None

        # Best program tracking
        self.best_program_id: Optional[str] = None

        # Prompt log
        self.prompts_by_program: Optional[Dict[str, Dict[str, Dict[str, str]]]] = None

        # Initialize checkpoint manager (imported here to avoid circular imports)
        from skydiscover.search.utils.checkpoint_manager import CheckpointManager

        self.checkpoint_manager = CheckpointManager(self.config)

        # Load database from disk if path is provided
        if config.db_path and os.path.exists(config.db_path):
            self.load(config.db_path)
````

## → Calls
- [[CheckpointManager.__init__]]
- [[DatabaseConfig.db_path]]
- [[ProgramDatabase.load]]
- [[base_database.Program]]
- [[checkpoint_manager.CheckpointManager]]
- [[config.DatabaseConfig]]

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
- [[BeamSearchDatabase.__init__]]
- [[BestOfNDatabase.__init__]]
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
- [[EvolvedProgramDatabase.__init__]]
- [[GEPANativeController._attempt_merge]]
- [[GEPANativeDatabase.__init__]]
- [[HarborEvaluator._read_reward]]
- [[HarborEvaluator._run_container]]
- [[LLMJudge.evaluate]]
- [[MultiDimensionalAdapter.add_dimension]]
- [[MultiDimensionalAdapter.from_dict]]
- [[OpenAILLM._generate_with_image]]
- [[OpenAILLM.generate]]
- [[OpenEvolveNativeDatabase.__init__]]
- [[OpenEvolveNativeDatabase._migrate_programs]]
- [[OpenEvolveNativeDatabase._seed_empty_island]]
- [[ParadigmTracker.from_dict]]
- [[Program.from_dict]]
- [[ProgramDatabase.log_prompt]]
- [[Runner.run]]
- [[SearchStrategyDatabase.__init__]]
- [[TopKDatabase.__init__]]
- [[UnifiedArchive.__init__]]
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
