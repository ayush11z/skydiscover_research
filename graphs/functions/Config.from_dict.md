---
name: Config.from_dict
description: classmethod in skydiscover/config.py (config)
metadata:
  type: project
---

# Config.from_dict

**File:** `skydiscover/config.py:660`  
**Kind:** classmethod  
**Layer:** #config

## Source
````python
    def from_dict(cls, config_dict: Dict[str, Any]) -> Config:
        """Create configuration from a dictionary"""
        # Handle nested configurations
        config = Config()

        # Update top-level fields
        for key, value in config_dict.items():
            if key not in [
                "llm",
                "prompt",
                "database",
                "search",
                "evaluator",
                "agentic",
                "benchmark",
                "monitor",
            ] and hasattr(config, key):
                setattr(config, key, value)

        # Update nested configs
        if "llm" in config_dict:
            llm_dict = config_dict["llm"]
            if "models" in llm_dict:
                llm_dict["models"] = [LLMModelConfig(**m) for m in llm_dict["models"]]
            if "evaluator_models" in llm_dict:
                llm_dict["evaluator_models"] = [
                    LLMModelConfig(**m) for m in llm_dict["evaluator_models"]
                ]
            if "guide_models" in llm_dict:
                llm_dict["guide_models"] = [LLMModelConfig(**m) for m in llm_dict["guide_models"]]
            config.llm = LLMConfig(**llm_dict)
        if "prompt" in config_dict:
            config.context_builder = ContextBuilderConfig(**config_dict["prompt"])

        if "search" in config_dict:
            search_dict = config_dict["search"]
            search_type = search_dict.get("type", "topk")
            db_config_cls = _DB_CONFIG_BY_TYPE.get(search_type, DatabaseConfig)
            if "database" in search_dict:
                db_dict = search_dict["database"]
                # Separate known fields from algorithm-specific extras
                # (e.g., adaevolve's decay, intensity_min, use_adaptive_search, etc.)
                known_fields = {f.name for f in fields(db_config_cls)}
                db_known = {k: v for k, v in db_dict.items() if k in known_fields}
                db_extras = {k: v for k, v in db_dict.items() if k not in known_fields}
                db_config = db_config_cls(**db_known)
                for k, v in db_extras.items():
                    setattr(db_config, k, v)
                search_dict["database"] = db_config
            else:
                search_dict["database"] = db_config_cls()
            config.search = SearchConfig(**search_dict)

        if "evaluator" in config_dict:
            config.evaluator = EvaluatorConfig(**config_dict["evaluator"])
        if "agentic" in config_dict:
            agentic_dict = dict(config_dict["agentic"])  # copy to avoid mutating input
            # Convert list fields to tuples for the dataclass
            for tuple_field in ("allowed_extensions", "excluded_dirs"):
                if tuple_field in agentic_dict and isinstance(agentic_dict[tuple_field], list):
                    agentic_dict[tuple_field] = tuple(agentic_dict[tuple_field])
            config.agentic = AgenticConfig(**agentic_dict)
        if "benchmark" in config_dict:
            benchmark_dict = config_dict["benchmark"]
            # Separate known dataclass fields from benchmark-specific parameters
            known_fields = {f.name for f in fields(BenchmarkConfig) if f.name != "params"}
            benchmark_known = {k: v for k, v in benchmark_dict.items() if k in known_fields}
            benchmark_params = {k: v for k, v in benchmark_dict.items() if k not in known_fields}
            config.benchmark = BenchmarkConfig(**benchmark_known, params=benchmark_params)
        if "monitor" in config_dict:
            config.monitor = MonitorConfig(**config_dict["monitor"])

        return config
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[BenchmarkConfig.name]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMModelConfig.name]]
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
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[config.AgenticConfig]]
- [[config.BenchmarkConfig]]
- [[config.ContextBuilderConfig]]
- [[config.DatabaseConfig]]
- [[config.EvaluatorConfig]]
- [[config.LLMConfig]]
- [[config.LLMModelConfig]]
- [[config.MonitorConfig]]
- [[config.SearchConfig]]
- [[config._DB_CONFIG_BY_TYPE]]

## ← Called by
- [[Config.from_yaml]]
