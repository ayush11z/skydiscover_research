---
name: external.get_runner
description: function in skydiscover/extras/external/__init__.py (external)
metadata:
  type: project
---

# external.get_runner

**File:** `skydiscover/extras/external/__init__.py:44`  
**Kind:** function  
**Layer:** #external

## Source
````python
def get_runner(search_type: str):
    return _REGISTRY[search_type]
````

## → Calls
- [[external._REGISTRY]]

## ← Called by
- [[api._run_discovery_async]]
- [[cli.main_async]]
