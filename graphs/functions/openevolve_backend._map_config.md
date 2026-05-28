---
name: openevolve_backend._map_config
description: function in skydiscover/extras/external/openevolve_backend.py (external)
metadata:
  type: project
---

# openevolve_backend._map_config

**File:** `skydiscover/extras/external/openevolve_backend.py:24`  
**Kind:** function  
**Layer:** #external

## Source
````python
def _map_config(config: Config, iterations: Optional[int], output_dir: str):
    """Convert SkyDiscover Config to an OpenEvolve Config, mapping shared fields."""
    from openevolve.config import Config as OEConfig

    # Power-user escape hatch: if they attached an OpenEvolve config, use it.
    ext = getattr(config, "external_config", None)
    if isinstance(ext, OEConfig):
        if iterations is not None:
            ext.max_iterations = iterations
        return ext

    oe = OEConfig()

    # Apply tuned backend defaults (population_size, prompt, evaluator, etc.)
    from skydiscover.extras.external.defaults import apply_defaults, load_defaults

    apply_defaults(oe, load_defaults("openevolve_default.yaml"))

    # CLI overrides
    oe.max_iterations = iterations or config.max_iterations

    # LLM models (from --model / -c config)
    if config.llm.models:
        from openevolve.config import LLMModelConfig as OEModel

        # Resolve the correct api_base for OpenEvolve models.
        # The openai library ignores OPENAI_BASE_URL when base_url is
        # explicitly passed, so we must resolve the env var here and pass it
        # through.  Priority: env var > SkyDiscover config value.
        resolved_api_base = (
            os.environ.get("OPENAI_API_BASE")
            or os.environ.get("OPENAI_BASE_URL")
            or getattr(config.llm, "api_base", None)
            or "https://api.openai.com/v1"
        )
        oe.llm.api_base = resolved_api_base
        oe.llm.models = [
            OEModel(
                name=m.name,
                weight=getattr(m, "weight", 1.0),
                temperature=getattr(m, "temperature", oe.llm.temperature),
                api_key=getattr(m, "api_key", None),
                api_base=resolved_api_base,
            )
            for m in config.llm.models
        ]
        # Sync evaluator models (OE's __post_init__ ran before we set models)
        oe.llm.evaluator_models = oe.llm.models.copy()
        # Propagate OE shared config (max_tokens, timeout, etc.) to new models
        oe.llm.update_model_params(
            {
                "max_tokens": oe.llm.max_tokens,
                "timeout": oe.llm.timeout,
                "retries": oe.llm.retries,
                "retry_delay": oe.llm.retry_delay,
                "top_p": oe.llm.top_p,
                "reasoning_effort": oe.llm.reasoning_effort,
            }
        )

    # LLM timeout
    if config.llm.timeout:
        oe.llm.timeout = config.llm.timeout

    # System prompt — propagate to OpenEvolve's prompt config and models
    sys_prompt = config.system_prompt_override
    if sys_prompt is None and hasattr(config, "context_builder"):
        sp = config.context_builder.system_message
        if sp and sp not in ("system_message", "evaluator_system_message"):
            sys_prompt = sp
    if sys_prompt:
        if hasattr(oe, "prompt"):
            oe.prompt.system_message = sys_prompt
        for m in oe.llm.models:
            m.system_message = sys_prompt

    # Evaluator settings
    if hasattr(config, "evaluator"):
        if hasattr(config.evaluator, "timeout") and config.evaluator.timeout:
            oe.evaluator.timeout = config.evaluator.timeout
        if hasattr(config.evaluator, "max_retries") and config.evaluator.max_retries:
            oe.evaluator.max_retries = config.evaluator.max_retries
        if hasattr(config.evaluator, "cascade_evaluation"):
            oe.evaluator.cascade_evaluation = config.evaluator.cascade_evaluation

    oe.diff_based_generation = config.diff_based_generation

    return oe
````

## → Calls
- [[BenchmarkConfig.name]]
- [[Config.context_builder]]
- [[Config.diff_based_generation]]
- [[Config.evaluator]]
- [[Config.llm]]
- [[Config.max_iterations]]
- [[Config.system_prompt_override]]
- [[LLMModelConfig.name]]
- [[config.Config]]
- [[config.LLMModelConfig]]
- [[defaults.apply_defaults]]
- [[defaults.load_defaults]]

## ← Called by
- [[openevolve_backend.run]]
- [[openevolve_backend.run._poll_programs]]
