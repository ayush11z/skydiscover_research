---
name: UnifiedArchive.find_merge_candidates
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.find_merge_candidates

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:734`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def find_merge_candidates(self) -> Optional[Tuple[Program, Program, Program]]:
        """
        Find two programs suitable for merging.

        Looks for two top programs that share a common ancestor.

        Returns:
            Tuple of (program_a, program_b, common_ancestor) or None
        """
        # Get top programs by fitness
        top_progs = self.get_top_programs()

        if len(top_progs) < 2:
            return None

        # Try to find a pair with common ancestor
        for i, pa in enumerate(top_progs[:-1]):
            for pb in top_progs[i + 1 :]:
                ancestor_id = self._find_common_ancestor(pa.id, pb.id)
                if ancestor_id and ancestor_id in self._programs:
                    return (pa, pb, self._programs[ancestor_id])

        return None
````

## → Calls
- [[UnifiedArchive._find_common_ancestor]]
- [[UnifiedArchive.get_top_programs]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
