---
name: MonitorServer._heartbeat
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._heartbeat

**File:** `skydiscover/extras/monitor/server.py:605`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    async def _heartbeat(self) -> None:
        while not self._stop_event.is_set():
            await asyncio.sleep(5)
            if self._clients:
                await self._broadcast(json.dumps({"type": "heartbeat", "timestamp": time.time()}))
````

## → Calls
- [[MonitorServer._broadcast]]

## ← Called by
- [[MonitorServer._serve]]
