---
name: logging_utils._ConsoleFilter
description: class in skydiscover/search/utils/logging_utils.py (search-utils)
metadata:
  type: project
---

# logging_utils._ConsoleFilter

**File:** `skydiscover/search/utils/logging_utils.py:35`  
**Kind:** class  
**Layer:** #search-utils

## Source
````python
class _ConsoleFilter(logging.Filter):
    """Only pass skydiscover messages, suppressing noisy modules below WARNING."""

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[cli._configure_logging]]
- [[logging_utils.setup_search_logging]]
