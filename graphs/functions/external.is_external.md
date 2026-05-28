---
name: external.is_external
description: function in skydiscover/extras/external/__init__.py (external)
metadata:
  type: project
---

# external.is_external

**File:** `skydiscover/extras/external/__init__.py:40`  
**Kind:** function  
**Layer:** #external

## Source
````python
def is_external(search_type: str) -> bool:
    return search_type in _REGISTRY
````

## → Calls
- [[external._REGISTRY]]

## ← Called by
- [[api._run_discovery_async]]
- [[cli.main_async]]
