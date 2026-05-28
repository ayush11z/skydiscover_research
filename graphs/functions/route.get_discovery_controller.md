---
name: route.get_discovery_controller
description: function in skydiscover/search/route.py (search-core)
metadata:
  type: project
---

# route.get_discovery_controller

**File:** `skydiscover/search/route.py:41`  
**Kind:** function  
**Layer:** #search-core

## Source
````python
def get_discovery_controller(controller_input: DiscoveryControllerInput) -> DiscoveryController:
    """
    Get the discovery controller for a given search type.

    Returns the registered controller class, or the default DiscoveryController
    if none is registered.
    """
    search_type = controller_input.config.search.type
    controller_class = _CONTROLLER_REGISTRY.get(search_type, DiscoveryController)
    logger.debug(f"Using controller {controller_class.__name__} for search type '{search_type}'")
    return controller_class(controller_input)
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[default_discovery_controller.DiscoveryController]]
- [[default_discovery_controller.DiscoveryControllerInput]]
- [[registry._CONTROLLER_REGISTRY]]

## ← Called by
- [[Runner.run]]
