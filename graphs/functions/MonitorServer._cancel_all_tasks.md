---
name: MonitorServer._cancel_all_tasks
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._cancel_all_tasks

**File:** `skydiscover/extras/monitor/server.py:158`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def _cancel_all_tasks(self) -> None:
        """Cancel every pending task on the server's event loop, then stop it."""
        loop = self._loop
        if loop is None or loop.is_closed():
            return
        for task in asyncio.all_tasks(loop):
            task.cancel()
        loop.stop()
````

## → Calls
- [[MonitorServer.__init__]]
- [[MonitorServer.stop]]

## ← Called by
- [[MonitorServer.stop]]
