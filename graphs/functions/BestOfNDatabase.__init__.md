---
name: BestOfNDatabase.__init__
description: method in skydiscover/search/best_of_n/database.py (best-of-n)
metadata:
  type: project
---

# BestOfNDatabase.__init__

**File:** `skydiscover/search/best_of_n/database.py:22`  
**Kind:** method  
**Layer:** #best-of-n

## Source
````python
    def __init__(self, name: str, config: DatabaseConfig):
        super().__init__(name, config)

        # Get N parameter from config, default to 5
        self.n = getattr(config, "best_of_n", 5)

        # Track current parent and iteration count
        self.current_parent_id: Optional[str] = None
        self.parent_iteration_count: int = 0

        logger.info(f"BestOfNDatabase initialized: N={self.n}")
````

## → Calls
- [[ProgramDatabase.__init__]]
- [[config.DatabaseConfig]]

## ← Called by
_(entry point — nothing in this graph calls it)_
