---
name: MonitorServer._broadcast
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._broadcast

**File:** `skydiscover/extras/monitor/server.py:590`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    async def _broadcast(self, message: str) -> None:
        if not self._clients:
            return
        dead = set()
        for writer in list(self._clients):
            try:
                await self._ws_send(writer, message)
            except Exception:
                dead.add(writer)
        self._clients -= dead
````

## → Calls
- [[MonitorServer._ws_send]]

## ← Called by
- [[MonitorServer._consume_queue]]
- [[MonitorServer._handle_client_msg]]
- [[MonitorServer._heartbeat]]
- [[MonitorServer._trigger_summary]]
