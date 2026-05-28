---
name: monitor.stop_monitor
description: function in skydiscover/extras/monitor/__init__.py (monitor)
metadata:
  type: project
---

# monitor.stop_monitor

**File:** `skydiscover/extras/monitor/__init__.py:80`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def stop_monitor(monitor_server: Optional[MonitorServer]) -> None:
    """Gracefully shut down the monitor server."""
    if monitor_server is None:
        return
    try:
        monitor_server.push_event({"type": "discovery_complete"})
        time.sleep(0.5)
        monitor_server.stop()
    except Exception:
        logger.debug("Failed to stop monitor server", exc_info=True)
````

## → Calls
- [[MonitorServer.push_event]]
- [[MonitorServer.stop]]
- [[server.MonitorServer]]

## ← Called by
- [[api._run_discovery_async]]
- [[cli.main_async]]
