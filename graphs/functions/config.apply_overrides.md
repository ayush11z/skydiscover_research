---
name: config.apply_overrides
description: function in skydiscover/config.py (config)
metadata:
  type: project
---

# config.apply_overrides

**File:** `skydiscover/config.py:901`  
**Kind:** function  
**Layer:** #config

## Source
````python
def apply_overrides(
    config: Config,
    *,
    model: Optional[str] = None,
    api_base: Optional[str] = None,
    agentic: bool = False,
    search: Optional[str] = None,
    system_prompt: Optional[str] = None,
) -> None:
    """Apply runtime overrides (model, api_base, etc.) to a loaded Config in place."""
    if model:
        # Parse the model string into a list of model specifications
        specs = [s.strip() for s in model.split(",")]
        models: List[LLMModelConfig] = []
        for spec in specs:
            provider, model_name, default_api_base, env_vars = _parse_model_spec(spec)
            effective_base = api_base or default_api_base
            if effective_base is None:
                raise ValueError(
                    f"Provider '{provider}' requires an explicit api_base.\n"
                    f"Example: model='{spec}', api_base='http://localhost:8000/v1'"
                )
            resolved_key = _resolve_api_key_from_env(env_vars)
            models.append(
                LLMModelConfig(
                    name=model_name,
                    api_base=effective_base,
                    api_key=resolved_key,
                )
            )

        config.llm.api_base = models[0].api_base
        if models[0].api_key:
            config.llm.api_key = models[0].api_key
        config.llm.models = models
        config.llm.evaluator_models = [
            LLMModelConfig(name=m.name, api_base=m.api_base, api_key=m.api_key) for m in models
        ]
        config.llm.guide_models = [
            LLMModelConfig(name=m.name, api_base=m.api_base, api_key=m.api_key) for m in models
        ]
    elif api_base:
        config.llm.api_base = api_base
        config.llm.update_model_params({"api_base": api_base}, overwrite=True)

    # API key (api_base-only; multi-model already resolved above)
    if not model and api_base:
        parsed_env_vars: Optional[List[str]] = None
        for _prefix, (base_url, env_list) in _PROVIDERS.items():
            if base_url and config.llm.api_base.startswith(base_url.rstrip("/")):
                parsed_env_vars = env_list
                break
        resolved_key = _resolve_api_key_from_env(parsed_env_vars)
        if resolved_key:
            config.llm.api_key = resolved_key
            config.llm.update_model_params({"api_key": resolved_key}, overwrite=True)

    # Propagate shared generation/request settings
    if model or api_base:
        config.llm.update_model_params(
            {
                "temperature": config.llm.temperature,
                "top_p": config.llm.top_p,
                "max_tokens": config.llm.max_tokens,
                "timeout": config.llm.timeout,
                "retries": config.llm.retries,
                "retry_delay": config.llm.retry_delay,
                "reasoning_effort": config.llm.reasoning_effort,
            },
            overwrite=True,
        )
        # Fill api_base/api_key only where a model doesn't already have them
        config.llm.update_model_params(
            {"api_base": config.llm.api_base, "api_key": config.llm.api_key},
            overwrite=False,
        )

    if agentic:
        config.agentic.enabled = True

    if search:
        if not hasattr(config, "search"):
            config.search = SearchConfig()
        config.search.type = search
        new_db_cls = _DB_CONFIG_BY_TYPE.get(search)
        if new_db_cls and not isinstance(config.search.database, new_db_cls):
            config.search.database = new_db_cls()

    if system_prompt:
        config.context_builder.system_message = system_prompt
        config.system_prompt_override = system_prompt
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[Config.llm]]
- [[Config.search]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
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
- [[config.LLMModelConfig]]
- [[config.SearchConfig]]
- [[config._DB_CONFIG_BY_TYPE]]
- [[config._PROVIDERS]]
- [[config._parse_model_spec]]
- [[config._resolve_api_key_from_env]]

## ← Called by
- [[api._run_discovery_async]]
- [[cli.main_async]]
