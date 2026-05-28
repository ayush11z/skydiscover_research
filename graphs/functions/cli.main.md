---
name: cli.main
description: function in skydiscover/cli.py (cli)
metadata:
  type: project
---

# cli.main

**File:** `skydiscover/cli.py:98`  
**Kind:** function  
**Layer:** #cli

## Source
````python
def main() -> int:
    """Synchronous entry point for the skydiscover console script."""
    return asyncio.run(main_async())
````

## → Calls
- [[Runner.run]]
- [[TaskPool.run]]
- [[cli.main_async]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
_(entry point — nothing in this graph calls it)_
