---
name: registry.register_controller
description: function in skydiscover/search/registry.py (search-core)
metadata:
  type: project
---

# registry.register_controller

**File:** `skydiscover/search/registry.py:44`  
**Kind:** function  
**Layer:** #search-core

## Source
````python
def register_controller(search_type: str, controller_class: Type[DiscoveryController]) -> None:
    """Register a discovery controller class for a search type."""
    _CONTROLLER_REGISTRY[search_type] = controller_class
    logger.debug(
        f"Registered controller class '{controller_class.__name__}' for search type '{search_type}'"
    )
````

## → Calls
- [[default_discovery_controller.DiscoveryController]]

## ← Called by
_(entry point — nothing in this graph calls it)_
