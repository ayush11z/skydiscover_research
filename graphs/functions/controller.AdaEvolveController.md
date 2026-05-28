---
name: controller.AdaEvolveController
description: class in skydiscover/search/adaevolve/controller.py (adaevolve)
metadata:
  type: project
---

# controller.AdaEvolveController

**File:** `skydiscover/search/adaevolve/controller.py:46`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class AdaEvolveController(DiscoveryController):
    """
    AdaEvolve evolution controller with adaptive search intensity.

    Key Features:
    1. Adaptive sampling: Search intensity per island determines exploration/exploitation
    2. Mode-aware prompting: Different guidance for exploration vs exploitation
    3. Sibling context: Shows previous mutations for learning
    4. Error retry: Retries failed generations with error context
    5. Island rotation: UCB-based selection via database.end_iteration()
    6. Paradigm breakthrough: High-level strategy shifts when globally stuck

    No explicit stagnation tracking - search intensity handles exploration
    automatically based on accumulated improvement signal.
    """

````

## → Calls
- [[default_discovery_controller.DiscoveryController]]

## ← Called by
_(entry point — nothing in this graph calls it)_
