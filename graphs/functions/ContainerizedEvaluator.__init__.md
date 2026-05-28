---
name: ContainerizedEvaluator.__init__
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator.__init__

**File:** `skydiscover/evaluation/container_evaluator.py:71`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def __init__(
        self,
        benchmark_dir: str,
        config: EvaluatorConfig,
        max_concurrent: int = 4,
        env_vars: Optional[Dict[str, str]] = None,
    ):
        self.benchmark_dir = os.path.abspath(benchmark_dir)
        self.config = config
        self.program_suffix = config.file_suffix
        self.task_pool = TaskPool(max_concurrency=max_concurrent)
        self.llm_judge = None
        self.env_vars = dict(env_vars or {})
        if self.env_vars:
            logger.info(
                f"Passing {len(self.env_vars)} environment variables to container: {list(self.env_vars.keys())}"
            )
        self.image_tag = self._build_image()
        self.container_id = self._start_container()
        logger.info(f"ContainerizedEvaluator ready: container={self.container_id[:12]}")
````

## → Calls
- [[ContainerizedEvaluator._build_image]]
- [[ContainerizedEvaluator._start_container]]
- [[EvaluatorConfig.file_suffix]]
- [[TaskPool.__init__]]
- [[async_utils.TaskPool]]
- [[config.EvaluatorConfig]]

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
- [[HarborEvaluator.__init__]]
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
- [[evaluation.create_evaluator]]
- [[gepa_backend.run]]
- [[logging_utils.setup_search_logging]]
- [[openevolve_backend._to_skydiscover_program]]
- [[openevolve_backend.run]]
- [[registry.setup_search]]
- [[search_strategy_evaluator.evaluate]]
- [[shinkaevolve_backend._to_skydiscover_program]]
- [[shinkaevolve_backend.run]]
- [[variation_operator_generator.main]]
