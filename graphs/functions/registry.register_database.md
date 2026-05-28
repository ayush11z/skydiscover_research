---
name: registry.register_database
description: function in skydiscover/search/registry.py (search-core)
metadata:
  type: project
---

# registry.register_database

**File:** `skydiscover/search/registry.py:36`  
**Kind:** function  
**Layer:** #search-core

## Source
````python
def register_database(search_type: str, database_class: Type[ProgramDatabase]) -> None:
    """Register a database class for a search type."""
    _DATABASE_REGISTRY[search_type] = database_class
    logger.debug(
        f"Registered database class '{database_class.__name__}' for search type '{search_type}'"
    )
````

## → Calls
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
