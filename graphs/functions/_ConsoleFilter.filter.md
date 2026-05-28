---
name: _ConsoleFilter.filter
description: method in skydiscover/search/utils/logging_utils.py (search-utils)
metadata:
  type: project
---

# _ConsoleFilter.filter

**File:** `skydiscover/search/utils/logging_utils.py:38`  
**Kind:** method  
**Layer:** #search-utils

## Source
````python
    def filter(self, record):
        if record.levelno >= logging.WARNING:
            return True
        if not record.name.startswith("skydiscover") or record.name.split(".")[-1] in _QUIET:
            return False
        return True
````

## → Calls
- [[BenchmarkConfig.name]]
- [[LLMModelConfig.name]]
- [[logging_utils._QUIET]]

## ← Called by
_(entry point — nothing in this graph calls it)_
