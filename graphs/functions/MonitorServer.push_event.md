---
name: MonitorServer.push_event
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer.push_event

**File:** `skydiscover/extras/monitor/server.py:167`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def push_event(self, event: Dict[str, Any]) -> None:
        """Enqueue an event for broadcast to all connected WebSocket clients."""
        self._queue.put_nowait(event)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[Runner.run]]
- [[callback._push_program_event]]
- [[create_external_callback._callback]]
- [[monitor.stop_monitor]]
- [[viewer.main]]
