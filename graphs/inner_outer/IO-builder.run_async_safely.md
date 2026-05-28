---
name: IO-builder.run_async_safely
description: function in skydiscover/context_builder/evox/builder.py (context-builder)
metadata:
  type: project
---

# builder.run_async_safely

**File:** `skydiscover/context_builder/evox/builder.py:21`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def run_async_safely(coro):
    """Run an async coroutine, handling nested event loops."""
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(asyncio.run, coro)
            return future.result()
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-EvoxContextBuilder.build_prompt]]
