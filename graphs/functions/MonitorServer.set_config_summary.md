---
name: MonitorServer.set_config_summary
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer.set_config_summary

**File:** `skydiscover/extras/monitor/server.py:171`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def set_config_summary(self, summary: str) -> None:
        """Set a human-readable config summary sent to new dashboard clients."""
        self._config_summary = summary
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[Runner._start_monitor]]
