---
name: LLMPool.__init__
description: method in skydiscover/llm/llm_pool.py (llm)
metadata:
  type: project
---

# LLMPool.__init__

**File:** `skydiscover/llm/llm_pool.py:18`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    def __init__(self, models_cfg: List[LLMModelConfig]):
        if not models_cfg:
            raise ValueError("LLMPool requires at least one model config")

        self.models_cfg = models_cfg

        # Validate weights before creating clients to fail fast on bad config.
        self.weights = [m.weight for m in models_cfg]
        if any(w < 0 for w in self.weights):
            raise ValueError("LLMPool model weights must be non-negative")
        total = sum(self.weights)
        if total <= 0:
            raise ValueError("LLMPool model weights must sum to a positive value")
        self.weights = [w / total for w in self.weights]

        self.models = [
            model_cfg.init_client(model_cfg) if model_cfg.init_client else OpenAILLM(model_cfg)
            for model_cfg in models_cfg
        ]
        self.random_state = random.Random()

        # Logging
        if len(models_cfg) > 1:
            pool_key = tuple((c.name, w) for c, w in zip(models_cfg, self.weights))
            if not hasattr(logger, "_logged_pools"):
                logger._logged_pools = set()
            if pool_key not in logger._logged_pools:
                parts = ", ".join(f"{c.name}={w:.2f}" for c, w in zip(models_cfg, self.weights))
                logger.info(f"Pool weights: {parts}")
                logger._logged_pools.add(pool_key)
````

## → Calls
- [[LLMModelConfig.init_client]]
- [[LLMModelConfig.weight]]
- [[OpenAILLM.__init__]]
- [[config.LLMModelConfig]]
- [[openai.OpenAILLM]]

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
- [[CoEvolutionController._generate_variation_operators]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[Config.from_dict]]
- [[ContainerizedEvaluator._parse_output]]
- [[ContainerizedEvaluator._run_single_in_container]]
- [[ContainerizedEvaluator.evaluate_program]]
- [[DiscoveryController.__init__]]
- [[DiscoveryController._call_llm]]
- [[DiscoveryController._create_child_program]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
- [[EvaluationResult.from_dict]]
- [[Evaluator._cascade_evaluate]]
- [[Evaluator._normalize_result]]
- [[Evaluator.evaluate_program]]
- [[EvoxContextBuilder.__init__]]
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
