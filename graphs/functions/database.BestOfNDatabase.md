---
name: database.BestOfNDatabase
description: class in skydiscover/search/best_of_n/database.py (best-of-n)
metadata:
  type: project
---

# database.BestOfNDatabase

**File:** `skydiscover/search/best_of_n/database.py:11`  
**Kind:** class  
**Layer:** #best-of-n

## Source
````python
class BestOfNDatabase(ProgramDatabase):
    """
    Database implementing "best of N" strategy.

    Reuses the same parent for N consecutive iterations before sampling a new parent.
    This allows exploring multiple variations from the same starting point.

    Configuration options (via DatabaseConfig attributes):
        best_of_n: Number of iterations to reuse the same parent (default: 5)
    """

````

## → Calls
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
