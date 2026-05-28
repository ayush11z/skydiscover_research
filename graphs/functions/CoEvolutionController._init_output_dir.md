---
name: CoEvolutionController._init_output_dir
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._init_output_dir

**File:** `skydiscover/search/evox/controller.py:95`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _init_output_dir(self, controller_input: DiscoveryControllerInput) -> None:
        base_dir = controller_input.output_dir or os.path.join(
            os.path.dirname(controller_input.evaluation_file),
            "outputs",
            self.config.search.type,
        )
        self.search_outputs_dir = os.path.join(base_dir, "search")
        os.makedirs(self.search_outputs_dir, exist_ok=True)
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.evaluation_file]]
- [[DiscoveryControllerInput.output_dir]]
- [[DiscoveryResult.output_dir]]
- [[EvaluatorConfig.evaluation_file]]
- [[EvoxDatabaseConfig.evaluation_file]]
- [[SearchConfig.output_dir]]
- [[default_discovery_controller.DiscoveryController]]
- [[default_discovery_controller.DiscoveryControllerInput]]

## ← Called by
- [[CoEvolutionController.__init__]]
