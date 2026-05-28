---
name: HybridDiversity.update
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# HybridDiversity.update

**File:** `skydiscover/search/adaevolve/archive/diversity.py:335`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def update(self, programs: List[Program]) -> None:
        """Update all sub-strategies."""
        for strategy in self.strategies:
            strategy.update(programs)
````

## → Calls
- [[DiversityStrategy.update]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
