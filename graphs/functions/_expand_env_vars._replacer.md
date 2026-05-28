---
name: _expand_env_vars._replacer
description: function in skydiscover/config.py (config)
metadata:
  type: project
---

# _expand_env_vars._replacer

**File:** `skydiscover/config.py:92`  
**Kind:** function  
**Layer:** #config

## Source
````python
    def _replacer(match):
        return os.environ.get(match.group(1), match.group(0))
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[config._expand_env_vars]]
