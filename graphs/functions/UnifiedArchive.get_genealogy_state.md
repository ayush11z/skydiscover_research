---
name: UnifiedArchive.get_genealogy_state
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.get_genealogy_state

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:918`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_genealogy_state(self) -> Dict[str, Any]:
        """
        Get genealogy state for checkpointing.

        Returns:
            Dict with parents and children mappings.
        """
        return {
            "parents": dict(self._parents),
            "children": {k: list(v) for k, v in self._children.items()},
        }
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.save]]
