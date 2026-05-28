---
name: GEPANativeController.__init__
description: method in skydiscover/search/gepa_native/controller.py (gepa)
metadata:
  type: project
---

# GEPANativeController.__init__

**File:** `skydiscover/search/gepa_native/controller.py:54`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def __init__(self, controller_input: DiscoveryControllerInput):
        super().__init__(controller_input)

        # Override context builder with GEPA-specific one
        self.context_builder = GEPANativeContextBuilder(self.config)

        db_config = self.config.search.database
        self.acceptance_gating: bool = getattr(db_config, "acceptance_gating", True)
        self.use_merge: bool = getattr(db_config, "use_merge", True)
        self.merge_after_stagnation: int = getattr(db_config, "merge_after_stagnation", 15)
        self.max_recent_failures: int = getattr(db_config, "max_recent_failures", 5)
        self.max_merge_attempts: int = getattr(db_config, "max_merge_attempts", 10)

        # Stagnation tracking
        self._best_score_seen: float = -float("inf")
        self._iterations_without_improvement: int = 0

        # Merge state
        self._merge_due: bool = False
        self._merge_attempts_used: int = 0
        self._merge_pairs_tried: Set[Tuple[str, str]] = set()

        logger.info(
            f"GEPANativeController initialized: "
            f"acceptance_gating={self.acceptance_gating}, "
            f"use_merge={self.use_merge}, "
            f"merge_after_stagnation={self.merge_after_stagnation}, "
            f"max_merge_attempts={self.max_merge_attempts}"
        )
````

## → Calls
- [[DiscoveryController.__init__]]
- [[DiscoveryControllerInput.config]]
- [[builder.GEPANativeContextBuilder]]
- [[default_discovery_controller.DiscoveryController]]
- [[default_discovery_controller.DiscoveryControllerInput]]

## ← Called by
- [[GEPANativeController._build_prompt]]
