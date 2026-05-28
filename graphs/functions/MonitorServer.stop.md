---
name: MonitorServer.stop
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer.stop

**File:** `skydiscover/extras/monitor/server.py:145`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def stop(self) -> None:
        """Signal the server to stop and wait for the thread to finish."""
        self._stop_event.set()
        loop = self._loop
        if loop is not None and not loop.is_closed():
            # Schedule cancellation of all tasks, then stop the loop
            try:
                loop.call_soon_threadsafe(self._cancel_all_tasks)
            except RuntimeError:
                pass  # Loop already closed
        if self._thread:
            self._thread.join(timeout=5)
````

## → Calls
- [[MonitorServer.__init__]]
- [[MonitorServer._cancel_all_tasks]]

## ← Called by
- [[MonitorServer._cancel_all_tasks]]
- [[Runner.run]]
- [[monitor.stop_monitor]]
- [[viewer.main]]
