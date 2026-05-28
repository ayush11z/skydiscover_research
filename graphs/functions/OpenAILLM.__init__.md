---
name: OpenAILLM.__init__
description: method in skydiscover/llm/openai.py (llm)
metadata:
  type: project
---

# OpenAILLM.__init__

**File:** `skydiscover/llm/openai.py:64`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    def __init__(self, model_cfg: Optional[LLMModelConfig] = None):
        self.model = model_cfg.name
        self.temperature = model_cfg.temperature
        self.top_p = model_cfg.top_p
        self.max_tokens = model_cfg.max_tokens
        self.timeout = model_cfg.timeout
        self.retries = model_cfg.retries
        self.retry_delay = model_cfg.retry_delay
        self.api_base = model_cfg.api_base
        self.api_key = model_cfg.api_key
        self.reasoning_effort = getattr(model_cfg, "reasoning_effort", None)

        max_retries = self.retries if self.retries is not None else 0
        is_azure = self.api_base and ".openai.azure.com" in self.api_base.lower()

        if is_azure:
            parsed_url = urlparse(self.api_base)
            azure_endpoint = f"{parsed_url.scheme}://{parsed_url.netloc}"
            query_params = parse_qs(parsed_url.query)
            api_version = query_params.get("api-version", ["2024-12-01-preview"])[0]

            self.client = openai.AzureOpenAI(
                azure_endpoint=azure_endpoint,
                api_key=self.api_key,
                api_version=api_version,
                timeout=self.timeout,
                max_retries=max_retries,
            )
        else:
            self.client = openai.OpenAI(
                api_key=self.api_key,
                base_url=self.api_base,
                timeout=self.timeout,
                max_retries=max_retries,
            )

        if not hasattr(logger, "_initialized_models"):
            logger._initialized_models = set()
        if self.model not in logger._initialized_models:
            api_base_str = (self.api_base or "").lower()
            if is_azure:
                provider = "AzureOpenAI"
            elif GOOGLE_AI_STUDIO_DOMAIN in api_base_str:
                provider = "Gemini"
            elif "api.anthropic.com" in api_base_str:
                provider = "Anthropic"
            elif "api.deepseek.com" in api_base_str:
                provider = "DeepSeek"
            elif "api.mistral.ai" in api_base_str:
                provider = "Mistral"
            else:
                provider = "OpenAI"
            logger.info(f"{provider} LLM: {self.model}")
            logger._initialized_models.add(self.model)
````

## → Calls
- [[BenchmarkConfig.name]]
- [[EvaluatorConfig.timeout]]
- [[LLMModelConfig.api_base]]
- [[LLMModelConfig.api_key]]
- [[LLMModelConfig.max_tokens]]
- [[LLMModelConfig.name]]
- [[LLMModelConfig.retries]]
- [[LLMModelConfig.retry_delay]]
- [[LLMModelConfig.temperature]]
- [[LLMModelConfig.timeout]]
- [[LLMModelConfig.top_p]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[config.LLMModelConfig]]

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
- [[LLMPool.__init__]]
- [[MultiDimensionalAdapter.add_dimension]]
- [[MultiDimensionalAdapter.from_dict]]
- [[OpenAILLM._call_api_via_responses]]
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
