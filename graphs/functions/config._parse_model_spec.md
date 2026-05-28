---
name: config._parse_model_spec
description: function in skydiscover/config.py (config)
metadata:
  type: project
---

# config._parse_model_spec

**File:** `skydiscover/config.py:53`  
**Kind:** function  
**Layer:** #config

## Source
````python
def _parse_model_spec(model_str: str) -> tuple:
    """Parse a model string into ``(provider, model_name, default_api_base, env_vars)``.

    Supports:
      - ``provider/model``  (e.g. ``gemini/gemini-3-pro``)
      - bare names with known prefix (e.g. ``gemini-3-pro`` → gemini)
      - unknown bare names default to ``openai``
    """
    if "/" in model_str:
        provider, _, model_name = model_str.partition("/")
        provider_lower = provider.lower()
        if provider_lower in _PROVIDERS:
            api_base, env_vars = _PROVIDERS[provider_lower]
            return provider_lower, model_name, api_base, env_vars

    for prefix, provider in _BARE_PREFIX_MAP.items():
        if model_str.startswith(prefix):
            api_base, env_vars = _PROVIDERS[provider]
            return provider, model_str, api_base, env_vars

    api_base, env_vars = _PROVIDERS["openai"]
    return "openai", model_str, api_base, env_vars
````

## → Calls
- [[config._BARE_PREFIX_MAP]]
- [[config._PROVIDERS]]

## ← Called by
- [[LLMConfig.__post_init__]]
- [[cli.main_async]]
- [[config.apply_overrides]]
- [[config.bridge_provider_env]]
- [[config.load_config]]
- [[gepa_backend._build_gepa_config]]
- [[gepa_backend._ensure_litellm_api_key]]
