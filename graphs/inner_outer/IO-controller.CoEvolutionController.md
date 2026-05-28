---
name: IO-controller.CoEvolutionController
description: class in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# controller.CoEvolutionController

**File:** `skydiscover/search/evox/controller.py:34`  
**Kind:** class  
**Layer:** #outer-loop

## Source
````python
class CoEvolutionController(DiscoveryController):
    """
    Co-evolves solution programs alongside search algorithms.

    The solution database uses an evolving search algorithm for sampling,
    while the search algorithm itself is scored based on solution improvements.
    """

    # Adaptive mode defaults
    DEFAULT_SWITCH_RATIO = 0.10  # Evolve search after 10% of total iterations stagnate
    DEFAULT_IMPROVEMENT_THRESHOLD = 0.01

````

## → Calls
- [[IO-default_discovery_controller.DiscoveryController]]

## ← Called by
_(entry point — nothing in this graph calls it)_
