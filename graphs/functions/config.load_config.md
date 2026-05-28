---
name: config.load_config
description: function in skydiscover/config.py (config)
metadata:
  type: project
---

# config.load_config

**File:** `skydiscover/config.py:817`  
**Kind:** function  
**Layer:** #config

## Source
````python
def load_config(config_path: Optional[Union[str, Path]] = None) -> Config:
    """Load configuration from a YAML file or use defaults"""
    if config_path:
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")
        config = Config.from_yaml(config_path)
    else:
        config = Config()

    # Update api_base from environment if provided — use overwrite=True
    # because __post_init__ already pushed the hardcoded default to all models.
    api_base = os.environ.get("OPENAI_API_BASE") or os.environ.get("OPENAI_BASE_URL")
    if api_base:
        config.llm.api_base = api_base
        config.llm.update_model_params({"api_base": api_base}, overwrite=True)

    # Determine which API key to use (provider-aware)
    if not config.llm.api_key:
        env_vars = None
        if config.llm.models:
            first_model_name = config.llm.models[0].name
            if first_model_name:
                _, _, _, env_vars = _parse_model_spec(first_model_name)
        api_key = _resolve_api_key_from_env(env_vars)
        if api_key:
            config.llm.api_key = api_key
            config.llm.update_model_params({"api_key": api_key})

    # Make the system message available to the individual models, in case it is not provided from the prompt sampler
    config.llm.update_model_params({"system_message": config.context_builder.system_message})

    # Bridge provider env vars so that downstream configs (e.g. evox search.yaml)
    # can resolve ${OPENAI_API_KEY} from the environment.
    bridge_provider_env(config)

    return config
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[Config.from_yaml]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMConfig.update_model_params]]
- [[LLMJudge.__init__]]
- [[LLMModelConfig.api_key]]
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
- [[config.Config]]
- [[config.ContextBuilderConfig]]
- [[config.LLMConfig]]
- [[config._parse_model_spec]]
- [[config._resolve_api_key_from_env]]
- [[config.bridge_provider_env]]

## ← Called by
- [[Runner.__init__]]
- [[api._run_discovery_async]]
- [[cli.main_async]]
- [[registry.setup_search]]
