---
name: UnifiedArchive._find_common_ancestor
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._find_common_ancestor

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:758`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _find_common_ancestor(self, id_a: str, id_b: str) -> Optional[str]:
        """Find most recent common ancestor of two programs."""
        # Get all ancestors of a
        ancestors_a: Set[str] = set()
        queue = [id_a]
        while queue:
            current = queue.pop()
            for parent in self._parents.get(current, []):
                if parent not in ancestors_a:
                    ancestors_a.add(parent)
                    queue.append(parent)

        # Walk up from b and find first intersection
        queue = [id_b]
        visited: Set[str] = set()
        while queue:
            current = queue.pop()
            if current in ancestors_a:
                return current
            visited.add(current)
            for parent in self._parents.get(current, []):
                if parent not in visited:
                    queue.append(parent)

        return None
````

## → Calls
- [[UnifiedArchive.__init__]]

## ← Called by
- [[UnifiedArchive.find_merge_candidates]]
