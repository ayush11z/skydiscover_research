---
name: MonitorServer._ws_send
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._ws_send

**File:** `skydiscover/extras/monitor/server.py:601`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    async def _ws_send(self, writer: asyncio.StreamWriter, text: str) -> None:
        writer.write(_ws_encode_text(text))
        await writer.drain()
````

## → Calls
- [[server._ws_encode_text]]

## ← Called by
- [[MonitorServer._broadcast]]
- [[MonitorServer._generate_program_summary]]
- [[MonitorServer._handle_client_msg]]
- [[MonitorServer._handle_ws]]
