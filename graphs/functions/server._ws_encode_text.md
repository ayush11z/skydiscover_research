---
name: server._ws_encode_text
description: function in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# server._ws_encode_text

**File:** `skydiscover/extras/monitor/server.py:38`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def _ws_encode_text(text: str) -> bytes:
    """Encode a text frame (server→client, unmasked)."""
    payload = text.encode("utf-8")
    length = len(payload)
    if length < 126:
        header = struct.pack("BB", 0x81, length)
    elif length < 65536:
        header = struct.pack("!BBH", 0x81, 126, length)
    else:
        header = struct.pack("!BBQ", 0x81, 127, length)
    return header + payload
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[MonitorServer._ws_send]]
