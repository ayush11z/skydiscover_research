---
name: create_monitor_callback._callback
description: function in skydiscover/extras/monitor/callback.py (monitor)
metadata:
  type: project
---

# create_monitor_callback._callback

**File:** `skydiscover/extras/monitor/callback.py:26`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
    def _callback(program: Any, iteration: int, result: Any = None) -> None:
        """Push a new program event to the monitor. Never raises."""
        try:
            _push_program_event(server, database, program, iteration, result, start_time)
        except Exception:
            # Never crash discovery process due to monitor
            logger.debug("Monitor callback error", exc_info=True)
````

## → Calls
- [[callback._push_program_event]]

## ← Called by
- [[callback.create_monitor_callback]]
