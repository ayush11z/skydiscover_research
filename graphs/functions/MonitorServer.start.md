---
name: MonitorServer.start
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer.start

**File:** `skydiscover/extras/monitor/server.py:136`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def start(self) -> None:
        """Load the dashboard and start the server in a daemon thread."""
        self._load_dashboard()
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()
        # Wait until TCP port is actually bound (up to 5s)
        self._ready_event.wait(timeout=5)
        logger.info(f"Monitor server started → http://localhost:{self.port}/")
````

## → Calls
- [[MonitorServer._load_dashboard]]
- [[MonitorServer._run_loop]]
- [[search_strategy_evaluator.start]]

## ← Called by
- [[Runner._start_monitor]]
- [[code_utils._extract_def_info]]
- [[monitor.start_monitor]]
- [[viewer.main]]
