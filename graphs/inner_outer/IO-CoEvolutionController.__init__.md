---
name: IO-CoEvolutionController.__init__
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController.__init__

**File:** `skydiscover/search/evox/controller.py:46`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def __init__(self, controller_input: DiscoveryControllerInput):
        super().__init__(controller_input)

        self._init_search_evolution_controller()
        self._init_output_dir(controller_input)
````

## → Calls
- [[IO-CoEvolutionController._init_output_dir]]
- [[IO-CoEvolutionController._init_search_evolution_controller]]
- [[IO-DiscoveryController.__init__]]
- [[IO-default_discovery_controller.DiscoveryControllerInput]]

## ← Called by
_(entry point — nothing in this graph calls it)_
