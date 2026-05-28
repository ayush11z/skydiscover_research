---
name: DiscoveryController.__init__
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController.__init__

**File:** `skydiscover/search/default_discovery_controller.py:63`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    def __init__(self, controller_input: DiscoveryControllerInput):
        self.config = controller_input.config
        self.evaluation_file = controller_input.evaluation_file
        self.database = controller_input.database
        self.file_suffix = controller_input.file_suffix
        self.output_dir = controller_input.output_dir
        self.evaluator_env_vars = controller_input.evaluator_env_vars

        self.shutdown_event = mp.Event()
        self.early_stopping_triggered = False

        self.llms = LLMPool(self.config.llm.models)
        self.evaluator_llms = LLMPool(self.config.llm.evaluator_models)
        self.guide_llms = LLMPool(self.config.llm.guide_models)

        self._init_context_builder()

        self.config.evaluator.evaluation_file = self.evaluation_file
        self.config.evaluator.file_suffix = self.file_suffix
        self.config.evaluator.is_image_mode = self.config.language == "image"

        llm_judge = None
        if self.config.evaluator.llm_as_judge:
            ctx = DefaultContextBuilder(self.config)
            ctx.set_templates("evaluator_system_message")
            llm_judge = LLMJudge(self.evaluator_llms, ctx, self.database)

        self.evaluator = create_evaluator(
            self.config.evaluator,
            llm_judge=llm_judge,
            max_concurrent=max(self.config.max_parallel_iterations, 4),
            env_vars=controller_input.evaluator_env_vars,
        )

        self.agentic_generator = None
        if self.config.agentic.enabled:
            from skydiscover.llm.agentic_generator import AgenticGenerator

            self.agentic_generator = AgenticGenerator(self.llms, self.config.agentic)
            logger.info(f"Agentic mode enabled (codebase: {self.config.agentic.codebase_root})")

        self.num_context_programs = controller_input.config.search.num_context_programs

        self.monitor_callback: Optional[Callable] = None
        self.feedback_reader: Optional[Any] = None
        self._prompt_context: Dict[str, Any] = {}
        self._solution_prompt_counter = 0

        # Load evaluator/task description and inject into system message so
        # the LLM knows what problem to solve (especially for from-scratch).
        self._inject_evaluator_context()

        logger.info(
            f"DiscoveryController initialized: num_context_programs={self.num_context_programs}"
        )
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[BenchmarkResolution.evaluator_env_vars]]
- [[Config.agentic]]
- [[Config.evaluator]]
- [[Config.language]]
- [[Config.llm]]
- [[Config.max_parallel_iterations]]
- [[DefaultContextBuilder.set_templates]]
- [[DiscoveryController._init_context_builder]]
- [[DiscoveryController._inject_evaluator_context]]
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.database]]
- [[DiscoveryControllerInput.evaluation_file]]
- [[DiscoveryControllerInput.evaluator_env_vars]]
- [[DiscoveryControllerInput.output_dir]]
- [[DiscoveryResult.output_dir]]
- [[EvaluatorConfig.evaluation_file]]
- [[EvaluatorConfig.file_suffix]]
- [[EvoxDatabaseConfig.evaluation_file]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[Program.language]]
- [[SearchConfig.database]]
- [[SearchConfig.output_dir]]
- [[agentic_generator.AgenticGenerator]]
- [[builder.DefaultContextBuilder]]
- [[default_discovery_controller.DiscoveryControllerInput]]
- [[evaluation.create_evaluator]]
- [[llm_judge.LLMJudge]]
- [[llm_pool.LLMPool]]

## ← Called by
- [[AdaEvolveController.__init__]]
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
- [[CoEvolutionController.__init__]]
- [[CoEvolutionController._init_search_evolution_controller]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[Config.from_dict]]
- [[ContainerizedEvaluator._parse_output]]
- [[ContainerizedEvaluator._run_single_in_container]]
- [[ContainerizedEvaluator.evaluate_program]]
- [[DiscoveryController._build_prompt]]
- [[DiscoveryController._call_llm]]
- [[DiscoveryController._create_child_program]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
- [[EvaluationResult.from_dict]]
- [[Evaluator._cascade_evaluate]]
- [[Evaluator._normalize_result]]
- [[Evaluator.evaluate_program]]
- [[GEPANativeController.__init__]]
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
