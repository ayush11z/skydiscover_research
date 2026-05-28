---
name: DiversityStrategy.update
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# DiversityStrategy.update

**File:** `skydiscover/search/adaevolve/archive/diversity.py:42`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def update(self, programs: List[Program]) -> None:
        """
        Update internal state based on current archive.

        Called after archive changes. Override for strategies that need
        normalization bounds or other population-dependent state.

        Args:
            programs: All programs currently in the archive
        """
        pass
````

## → Calls
- [[base_database.Program]]

## ← Called by
- [[HybridDiversity.update]]
