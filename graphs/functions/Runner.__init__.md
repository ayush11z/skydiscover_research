---
name: Runner.__init__
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner.__init__

**File:** `skydiscover/runner.py:40`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def __init__(
        self,
        evaluation_file: str,
        initial_program_path: Optional[str] = None,
        config_path: Optional[str] = None,
        config: Optional[Config] = None,
        output_dir: Optional[str] = None,
        evaluator_env_vars: Optional[dict[str, str]] = None,
    ):
        self.config = config if config is not None else load_config(config_path)
        self.name = self.config.search.type
        self.output_dir = output_dir or build_output_dir(
            self.name, initial_program_path or "scratch"
        )
        os.makedirs(self.output_dir, exist_ok=True)
        os.environ["SKYDISCOVER_RUN_NAME"] = os.path.basename(self.output_dir)
        self._setup_logging()

        # Load the initial program (can be optional)
        self.initial_program_path = initial_program_path
        self.initial_program_solution = (
            self._load_initial_program() if initial_program_path else None
        )
        if self.initial_program_solution and not self.config.language:
            self.config.language = extract_solution_language(self.initial_program_solution)
        if not self.config.language:
            self.config.language = "python"

        # Set the file extension
        ext = os.path.splitext(initial_program_path)[1] if initial_program_path else ".py"
        ext = ext or ".py"
        self.file_extension = ext if ext.startswith(".") else f".{ext}"
        if self.config.file_suffix == ".py":
            self.config.file_suffix = self.file_extension

        # Create the database
        self.database = create_database(self.config.search.type, self.config.search.database)
        self.database.language = self.config.language or "python"
        self.evaluation_file = evaluation_file
        self.evaluator_env_vars = dict(evaluator_env_vars or {})

        # Initialize the discovery controller
        self.discovery_controller: Optional[DiscoveryController] = None

        logger.info(f"Runner ready: search={self.name}, program={self.initial_program_path}")
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.output_dir]]
- [[DiscoveryResult.output_dir]]
- [[Runner._load_initial_program]]
- [[Runner._setup_logging]]
- [[SearchConfig.output_dir]]
- [[code_utils.extract_solution_language]]
- [[config.Config]]
- [[config.build_output_dir]]
- [[config.load_config]]
- [[default_discovery_controller.DiscoveryController]]
- [[registry.create_database]]
- [[runner.Runner]]

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
