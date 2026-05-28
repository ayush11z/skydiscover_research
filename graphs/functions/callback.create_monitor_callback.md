---
name: callback.create_monitor_callback
description: function in skydiscover/extras/monitor/callback.py (monitor)
metadata:
  type: project
---

# callback.create_monitor_callback

**File:** `skydiscover/extras/monitor/callback.py:19`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def create_monitor_callback(
    server: MonitorServer,
    database: Any,
    start_time: float,
) -> Callable:
    """Create an iteration callback that pushes program data to the monitor server."""

    def _callback(program: Any, iteration: int, result: Any = None) -> None:
        """Push a new program event to the monitor. Never raises."""
        try:
            _push_program_event(server, database, program, iteration, result, start_time)
        except Exception:
            # Never crash discovery process due to monitor
            logger.debug("Monitor callback error", exc_info=True)

    return _callback
````

## → Calls
- [[create_monitor_callback._callback]]
- [[server.MonitorServer]]

## ← Called by
- [[Runner._start_monitor]]
