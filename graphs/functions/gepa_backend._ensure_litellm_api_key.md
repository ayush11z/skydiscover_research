---
name: gepa_backend._ensure_litellm_api_key
description: function in skydiscover/extras/external/gepa_backend.py (external)
metadata:
  type: project
---

# gepa_backend._ensure_litellm_api_key

**File:** `skydiscover/extras/external/gepa_backend.py:117`  
**Kind:** function  
**Layer:** #external

## Source
````python
def _ensure_litellm_api_key(config: Config):
    """Warn early if the provider-specific env var that litellm expects is missing."""
    if not config.llm.models:
        return
    model_name = config.llm.models[0].name or ""
    provider, _, _, env_vars = _parse_model_spec(model_name)
    if provider == "openai" or not env_vars:
        return  # OPENAI_API_KEY already set via bridge_provider_env
    if not any(os.environ.get(v) for v in env_vars):
        logger.warning(
            "GEPA backend with model '%s' (provider=%s) requires one of %s. "
            "Export it before running: export %s=<your-key>",
            model_name,
            provider,
            env_vars,
            env_vars[0],
        )
````

## → Calls
- [[Config.llm]]
- [[config.Config]]
- [[config._parse_model_spec]]

## ← Called by
- [[gepa_backend.run]]
