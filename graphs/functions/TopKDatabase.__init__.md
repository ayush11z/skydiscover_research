---
name: TopKDatabase.__init__
description: method in skydiscover/search/topk/database.py (topk)
metadata:
  type: project
---

# TopKDatabase.__init__

**File:** `skydiscover/search/topk/database.py:13`  
**Kind:** method  
**Layer:** #topk

## Source
````python
    def __init__(self, name: str, config: DatabaseConfig):
        super().__init__(name, config)
        self.initial_program = None
````

## → Calls
- [[ProgramDatabase.__init__]]
- [[config.DatabaseConfig]]

## ← Called by
_(entry point — nothing in this graph calls it)_
