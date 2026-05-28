---
name: config._resolve_api_key_from_env
description: function in skydiscover/config.py (config)
metadata:
  type: project
---

# config._resolve_api_key_from_env

**File:** `skydiscover/config.py:77`  
**Kind:** function  
**Layer:** #config

## Source
````python
def _resolve_api_key_from_env(env_vars: Optional[List[str]] = None) -> Optional[str]:
    """Return the first API key found in *env_vars*, falling back to ``OPENAI_API_KEY``.

    *env_vars* typically comes from ``_parse_model_spec()``.
    """
    for var in env_vars or []:
        key = os.environ.get(var)
        if key:
            return key
    return os.environ.get("OPENAI_API_KEY")
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[LLMConfig.__post_init__]]
- [[config.apply_overrides]]
- [[config.load_config]]
