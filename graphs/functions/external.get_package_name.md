---
name: external.get_package_name
description: function in skydiscover/extras/external/__init__.py (external)
metadata:
  type: project
---

# external.get_package_name

**File:** `skydiscover/extras/external/__init__.py:28`  
**Kind:** function  
**Layer:** #external

## Source
````python
def get_package_name(search_type: str) -> str:
    """Return the pip-installable package name for a search type."""
    return _PACKAGE_NAMES.get(search_type, search_type)
````

## → Calls
- [[external._PACKAGE_NAMES]]

## ← Called by
- [[api._run_discovery_async]]
- [[cli.main_async]]
