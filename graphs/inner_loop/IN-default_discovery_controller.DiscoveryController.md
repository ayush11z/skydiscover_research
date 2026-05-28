---
name: IN-default_discovery_controller.DiscoveryController
description: class in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# default_discovery_controller.DiscoveryController

**File:** `skydiscover/search/default_discovery_controller.py:51`  
**Kind:** class  
**Layer:** #inner-loop

## Source
````python
class DiscoveryController:
    """
    Discovery controller with a default sequential execution strategy.

    Handles the full generate-evaluate cycle: prompt building, LLM calls,
    response parsing, evaluation, and result processing.

    The default ``run_discovery`` runs iterations sequentially.  Subclasses
    (e.g. CoEvolutionController) can override it for different orchestration
    while reusing the shared iteration primitives.
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
_(entry point — nothing in this graph calls it)_
