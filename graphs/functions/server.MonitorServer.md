---
name: server.MonitorServer
description: class in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# server.MonitorServer

**File:** `skydiscover/extras/monitor/server.py:87`  
**Kind:** class  
**Layer:** #monitor

## Source
````python
class MonitorServer:
    """
    Single-port HTTP+WebSocket server for live solution discovery monitoring.

    - GET /  →  dashboard.html
    - WS upgrade  →  event broadcast
    Runs in a daemon thread with its own asyncio event loop.
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[Runner._start_monitor]]
- [[callback._push_program_event]]
- [[callback.create_external_callback]]
- [[callback.create_monitor_callback]]
- [[monitor.start_monitor]]
- [[monitor.stop_monitor]]
- [[viewer.main]]
