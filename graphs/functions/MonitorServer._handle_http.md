---
name: MonitorServer._handle_http
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._handle_http

**File:** `skydiscover/extras/monitor/server.py:339`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    async def _handle_http(self, writer: asyncio.StreamWriter) -> None:
        """Serve the dashboard HTML over a plain HTTP GET."""
        html = self._dashboard_html or b""
        resp = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(html)}\r\n"
            "Connection: close\r\n"
            "\r\n"
        ).encode() + html
        writer.write(resp)
        await writer.drain()
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[MonitorServer._handle_connection]]
