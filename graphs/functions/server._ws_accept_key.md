---
name: server._ws_accept_key
description: function in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# server._ws_accept_key

**File:** `skydiscover/extras/monitor/server.py:33`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def _ws_accept_key(client_key: str) -> str:
    digest = hashlib.sha1((client_key + WS_GUID).encode()).digest()
    return base64.b64encode(digest).decode()
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[MonitorServer._handle_ws]]
