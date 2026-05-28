---
name: config._expand_env_vars
description: function in skydiscover/config.py (config)
metadata:
  type: project
---

# config._expand_env_vars

**File:** `skydiscover/config.py:89`  
**Kind:** function  
**Layer:** #config

## Source
````python
def _expand_env_vars(text: str) -> str:
    """Expand ${VAR} patterns in text with environment variable values."""

    def _replacer(match):
        return os.environ.get(match.group(1), match.group(0))

    return re.sub(r"\$\{(\w+)\}", _replacer, text)
````

## → Calls
- [[_expand_env_vars._replacer]]

## ← Called by
- [[Config.from_yaml]]
