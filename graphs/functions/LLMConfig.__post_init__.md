---
name: LLMConfig.__post_init__
description: method in skydiscover/config.py (config)
metadata:
  type: project
---

# LLMConfig.__post_init__

**File:** `skydiscover/config.py:181`  
**Kind:** method  
**Layer:** #config

## Source
````python
    def __post_init__(self):
        """Post-initialization to set up model configurations"""
        # If no evaluator models are defined, use the same models as for solution discovery
        if not self.evaluator_models:
            self.evaluator_models = self.models.copy()

        # If no guide models are defined, use the same models as for solution discovery
        if not self.guide_models:
            self.guide_models = self.models.copy()

        # Resolve per-model api_base, api_key, and bare name from provider prefix
        # Check if user explicitly set api_base at the LLMConfig level
        # (i.e. it differs from the hardcoded default).  When a custom api_base
        # is provided, we should NOT override it with the provider default so
        # that update_model_params() below can propagate the user's value.
        user_set_api_base = self.api_base.rstrip("/") != _PROVIDERS["openai"][0].rstrip("/")
        for model in self.models + self.evaluator_models + self.guide_models:
            if model.name and model.api_base is None:
                provider, bare_name, provider_base, env_vars = _parse_model_spec(model.name)
                # Skip provider URL only for unrecognized bare names that fell
                # through to the OpenAI default — never for an explicitly-prefixed
                # provider (e.g. "anthropic/claude-3-sonnet") or a known bare prefix.
                is_fallback = provider == "openai" and not (
                    model.name.startswith("openai/")
                    or any(model.name.startswith(p) for p in _BARE_PREFIX_MAP)
                )
                if provider_base and not (user_set_api_base and is_fallback):
                    model.api_base = provider_base
                if model.api_key is None:
                    model.api_key = _resolve_api_key_from_env(env_vars)
                # Strip provider prefix so the API receives the bare model name
                if "/" in model.name and provider != "openai":
                    model.name = bare_name

        # Update models with shared configuration values
        shared_config = {
            "api_base": self.api_base,
            "api_key": self.api_key,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "max_tokens": self.max_tokens,
            "timeout": self.timeout,
            "retries": self.retries,
            "retry_delay": self.retry_delay,
            "reasoning_effort": self.reasoning_effort,
        }
        self.update_model_params(shared_config)
````

## → Calls
- [[LLMConfig.api_base]]
- [[LLMConfig.update_model_params]]
- [[LLMModelConfig.api_key]]
- [[config.LLMModelConfig]]
- [[config._BARE_PREFIX_MAP]]
- [[config._PROVIDERS]]
- [[config._parse_model_spec]]
- [[config._resolve_api_key_from_env]]

## ← Called by
_(entry point — nothing in this graph calls it)_
