---
name: AdaEvolveDatabase.find_merge_candidates
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.find_merge_candidates

**File:** `skydiscover/search/adaevolve/database.py:1941`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def find_merge_candidates(
        self, island_idx: Optional[int] = None
    ) -> Optional[Tuple[Program, Program, Program]]:
        """Find merge candidates on an island."""
        idx = island_idx if island_idx is not None else self.current_island
        if 0 <= idx < self.num_islands:
            if (
                self.use_unified_archive
                and self.archives
                and hasattr(self.archives[idx], "find_merge_candidates")
            ):
                return self.archives[idx].find_merge_candidates()
        # Legacy mode doesn't support merging
        return None
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
