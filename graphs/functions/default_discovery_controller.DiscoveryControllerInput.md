---
name: default_discovery_controller.DiscoveryControllerInput
description: class in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# default_discovery_controller.DiscoveryControllerInput

**File:** `skydiscover/search/default_discovery_controller.py:40`  
**Kind:** class  
**Layer:** #inner-loop

## Source
````python
class DiscoveryControllerInput:
    """Input to the discovery controller"""

    config: Config
    evaluation_file: str
    database: ProgramDatabase
    file_suffix: str = ".py"
    output_dir: Optional[str] = None
    evaluator_env_vars: Optional[Dict[str, str]] = None
````

## → Calls
- [[base_database.ProgramDatabase]]
- [[config.Config]]

## ← Called by
- [[AdaEvolveController.__init__]]
- [[ClaudeCodeController.__init__]]
- [[CoEvolutionController.__init__]]
- [[CoEvolutionController._init_output_dir]]
- [[DiscoveryController.__init__]]
- [[GEPANativeController.__init__]]
- [[Runner.run]]
- [[registry.setup_search]]
- [[route.get_discovery_controller]]
