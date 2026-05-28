---
name: LangFuseTracer.__init__
description: method in skydiscover/llm/langfuse_tracer.py (observability)
metadata:
  type: project
---

# LangFuseTracer.__init__

**File:** `skydiscover/llm/langfuse_tracer.py:87`  
**Kind:** method  
**Layer:** #observability

## Source
````python
    def __init__(self) -> None:
        public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
        secret_key = os.getenv("LANGFUSE_SECRET_KEY")
        host = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

        if not public_key or not secret_key:
            logger.info(
                "LangFuse tracing disabled — "
                "set LANGFUSE_PUBLIC_KEY + LANGFUSE_SECRET_KEY to enable"
            )
            return

        try:
            from langfuse import Langfuse  # type: ignore[import-untyped]

            self._client = Langfuse(
                public_key=public_key,
                secret_key=secret_key,
                host=host,
            )
            atexit.register(self._flush_on_exit)
            logger.info(f"LangFuse tracing enabled → {host}")
        except ImportError:
            logger.warning(
                "langfuse package not found — tracing disabled. "
                "Install with: pip install langfuse"
            )
````

## → Calls
- [[LangFuseTracer._flush_on_exit]]

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
- [[LangFuseTracer.get]]
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
