---
name: AdaEvolveController.__init__
description: method in skydiscover/search/adaevolve/controller.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveController.__init__

**File:** `skydiscover/search/adaevolve/controller.py:62`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def __init__(self, controller_input: DiscoveryControllerInput):
        super().__init__(controller_input)

        # Configuration
        db_config = self.config.search.database
        self.enable_retry = getattr(db_config, "enable_error_retry", True)
        self.max_retries = getattr(db_config, "max_error_retries", 2)
        self.num_context_programs = self.config.search.num_context_programs

        # Components
        self.llms = LLMPool(self.config.llm.models)
        self.context_builder = AdaEvolveContextBuilder(self.config)

        # Paradigm generator (if paradigm breakthrough is enabled)
        # Note: We check database.use_paradigm_breakthrough at runtime, not this init-time flag
        # This ensures correct behavior after checkpoint load
        if self.database.use_paradigm_breakthrough:
            model_names = ", ".join(m.name for m in self.guide_llms.models_cfg)
            logger.info(f"Paradigm LLM: using guide_models [{model_names}]")

            self.paradigm_generator = ParadigmGenerator(
                llm_pool=self.guide_llms,
                system_message=self.config.context_builder.system_message or "",
                evaluator_code=self._load_evaluator_code(),
                num_paradigms=self.database.get_paradigm_num_to_generate(),
                eval_timeout=self.config.evaluator.timeout,
                language=self.config.language or "python",
                objective_names=getattr(db_config, "pareto_objectives", []),
                higher_is_better=getattr(db_config, "higher_is_better", {}),
                fitness_key=getattr(db_config, "fitness_key", None),
            )
        else:
            self.paradigm_generator = None

        # JSON logging for comprehensive AdaEvolve stats
        self._iteration_stats_log_path: Optional[str] = None
        self._iteration_stats_file = None
        self._last_sampling_mode: Optional[str] = None
        self._last_sampling_intensity: Optional[float] = None

        logger.info(
            f"AdaEvolveController initialized "
            f"(language={self.config.language}, "
            f"paradigm_breakthrough={self.database.use_paradigm_breakthrough})"
        )
````

## → Calls
- [[AdaEvolveController._load_evaluator_code]]
- [[BenchmarkConfig.name]]
- [[DiscoveryController.__init__]]
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.database]]
- [[LLMModelConfig.name]]
- [[LLMPool.__init__]]
- [[SearchConfig.database]]
- [[builder.AdaEvolveContextBuilder]]
- [[default_discovery_controller.DiscoveryController]]
- [[default_discovery_controller.DiscoveryControllerInput]]
- [[generator.ParadigmGenerator]]
- [[llm_pool.LLMPool]]

## ← Called by
- [[AdaEvolveController._generate_paradigms_if_needed]]
