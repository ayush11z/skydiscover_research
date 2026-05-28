---
name: CoEvolutionController._init_search_tracking
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._init_search_tracking

**File:** `skydiscover/search/evox/controller.py:79`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _init_search_tracking(self) -> None:
        """Initialize search evolution tracking state."""
        self._pending_search_result: Optional[SerializableResult] = None
        self._best_search_score: Optional[float] = None
        self._num_search_evolutions = 0

        self._switch_interval = getattr(self.config.search, "switch_interval", None)
        self._stagnant_count = 0
        self._last_tracked_best_score: Optional[float] = None

        self._diverge_label = ""
        self._refine_label = ""

        self._fallback_database = None
        self._fallback_search_code = None
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[default_discovery_controller.DiscoveryController]]
- [[discovery_utils.SerializableResult]]

## ← Called by
- [[CoEvolutionController._init_search_evolution_controller]]
