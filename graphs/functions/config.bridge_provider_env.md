---
name: config.bridge_provider_env
description: function in skydiscover/config.py (config)
metadata:
  type: project
---

# config.bridge_provider_env

**File:** `skydiscover/config.py:855`  
**Kind:** function  
**Layer:** #config

## Source
````python
def bridge_provider_env(config: Config) -> None:
    """
    Set provider-specific env vars from resolved config.

    External backends read credentials from environment variables directly.
    """
    if not config.llm.models:
        return
    model = config.llm.models[0]
    if not model.api_key:
        return

    # Use _parse_model_spec to get the right env vars for this model
    _, _, _, env_vars = _parse_model_spec(model.name or "")
    for var in env_vars:
        os.environ.setdefault(var, model.api_key)

    # Always ensure OPENAI_API_KEY is set — many tools (ShinkaEvolve, etc.) expect it
    os.environ.setdefault("OPENAI_API_KEY", model.api_key)

    # Set OPENAI_API_BASE only for non-default endpoints.  The default OpenAI
    # URL is already known to every OpenAI-compatible backend, so publishing
    # it here would silently override inner configs (e.g. search.yaml) that
    # use a different endpoint (e.g. a local Ollama server) when their own
    # load_config() call reads OPENAI_API_BASE from the environment.
    _openai_default = _PROVIDERS["openai"][0].rstrip("/")
    if model.api_base and model.api_base.rstrip("/") != _openai_default:
        os.environ.setdefault("OPENAI_API_BASE", model.api_base)
````

## → Calls
- [[Config.llm]]
- [[config.Config]]
- [[config._PROVIDERS]]
- [[config._parse_model_spec]]

## ← Called by
- [[config.load_config]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
