---
name: TaskPool.semaphore
description: method in skydiscover/utils/async_utils.py (utils)
metadata:
  type: project
---

# TaskPool.semaphore

**File:** `skydiscover/utils/async_utils.py:23`  
**Kind:** method  
**Layer:** #utils

## Source
````python
    def semaphore(self) -> asyncio.Semaphore:
        """Lazy-initialize the semaphore when first needed."""
        if self._semaphore is None:
            self._semaphore = asyncio.Semaphore(self.max_concurrency)
        return self._semaphore
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[TaskPool.run]]
