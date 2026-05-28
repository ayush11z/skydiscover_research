---
name: MonitorServer._load_dashboard
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._load_dashboard

**File:** `skydiscover/extras/monitor/server.py:244`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def _load_dashboard(self) -> None:
        try:
            raw = DASHBOARD_PATH.read_text(encoding="utf-8")
        except FileNotFoundError:
            logger.warning(f"Dashboard HTML not found at {DASHBOARD_PATH}")
            raw = "<html><body><h1>Dashboard not found</h1></body></html>"
        # No port injection needed — WS connects to the same host:port
        self._dashboard_html = raw.encode("utf-8")
````

## → Calls
- [[server.DASHBOARD_PATH]]

## ← Called by
- [[MonitorServer.start]]
