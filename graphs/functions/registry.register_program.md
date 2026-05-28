---
name: registry.register_program
description: function in skydiscover/search/registry.py (search-core)
metadata:
  type: project
---

# registry.register_program

**File:** `skydiscover/search/registry.py:28`  
**Kind:** function  
**Layer:** #search-core

## Source
````python
def register_program(search_type: str, program_class: Type[Program]) -> None:
    """Register a program class for a search type."""
    _PROGRAM_REGISTRY[search_type] = program_class
    logger.debug(
        f"Registered program class '{program_class.__name__}' for search type '{search_type}'"
    )
````

## → Calls
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
