---
name: server._ws_read_frame
description: function in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# server._ws_read_frame

**File:** `skydiscover/extras/monitor/server.py:51`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
async def _ws_read_frame(reader: asyncio.StreamReader) -> Optional[str]:
    """Read one WebSocket frame; return text payload or None on close/error."""
    try:
        header = await reader.readexactly(2)
    except Exception:
        return None
    opcode = header[0] & 0x0F
    masked = (header[1] & 0x80) != 0
    length = header[1] & 0x7F

    if opcode == 0x8:  # Close
        return None
    if opcode == 0x9:  # Ping — we could reply with pong but we ignore it here
        return None

    if length == 126:
        ext = await reader.readexactly(2)
        length = struct.unpack("!H", ext)[0]
    elif length == 127:
        ext = await reader.readexactly(8)
        length = struct.unpack("!Q", ext)[0]

    if masked:
        mask = await reader.readexactly(4)
        data = bytearray(await reader.readexactly(length))
        for i in range(length):
            data[i] ^= mask[i % 4]
        payload = bytes(data)
    else:
        payload = await reader.readexactly(length)

    if opcode == 0x1:  # Text
        return payload.decode("utf-8", errors="replace")
    return None  # Binary / continuation frames ignored
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[MonitorServer._handle_ws]]
