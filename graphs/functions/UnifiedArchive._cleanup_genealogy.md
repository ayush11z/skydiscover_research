---
name: UnifiedArchive._cleanup_genealogy
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._cleanup_genealogy

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:203`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _cleanup_genealogy(self, program_id: str) -> None:
        """
        Remove all genealogy references for a program being evicted.

        This is O(n) in the number of parent entries, but eviction is already
        O(n) for finding candidates, so this doesn't change complexity.
        """
        # 1. Remove program's parent tracking
        if program_id in self._parents:
            del self._parents[program_id]

        # 2. Remove program from its parent's children list
        parents_to_clean = []
        for parent_id, children in self._children.items():
            if program_id in children:
                children.remove(program_id)
                if not children:
                    parents_to_clean.append(parent_id)

        # 3. Remove empty children lists to prevent memory bloat
        for parent_id in parents_to_clean:
            del self._children[parent_id]

        # 4. Remove program's children list
        if program_id in self._children:
            del self._children[program_id]
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[UnifiedArchive._evict]]
