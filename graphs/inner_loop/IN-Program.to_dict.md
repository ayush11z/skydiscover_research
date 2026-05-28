---
name: IN-Program.to_dict
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# Program.to_dict

**File:** `skydiscover/search/base_database.py:54`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return asdict(self)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IN-DiscoveryController._run_from_scratch_iteration]]
- [[IN-DiscoveryController._run_iteration]]
