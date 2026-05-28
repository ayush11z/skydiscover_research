---
name: DiscoveryController._finalize_discovery
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._finalize_discovery

**File:** `skydiscover/search/default_discovery_controller.py:376`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    def _finalize_discovery(self) -> Optional[Program]:
        if self.shutdown_event.is_set():
            logger.info(
                f"✅ Discovery process completed "
                f"(search strategy = {self.database.name}) - Shutdown requested"
            )
        else:
            logger.info(
                f"✅ Discovery process completed "
                f"(search strategy = {self.database.name}) - Maximum iterations reached"
            )
        return self.database.get_best_program()
````

## → Calls
- [[BenchmarkConfig.name]]
- [[LLMModelConfig.name]]
- [[ProgramDatabase.get_best_program]]
- [[base_database.Program]]

## ← Called by
- [[DiscoveryController._run_discovery_parallel]]
- [[DiscoveryController._run_discovery_sequential]]
