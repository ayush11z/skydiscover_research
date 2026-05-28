---
name: IO-DiscoveryController.request_shutdown
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController.request_shutdown

**File:** `skydiscover/search/default_discovery_controller.py:923`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    def request_shutdown(self) -> None:
        """Request graceful shutdown"""
        logger.info("Graceful shutdown requested...")
        self.shutdown_event.set()
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-_install_signal_handlers.on_signal]]
