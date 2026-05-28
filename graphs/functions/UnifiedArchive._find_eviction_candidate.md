---
name: UnifiedArchive._find_eviction_candidate
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._find_eviction_candidate

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:573`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _find_eviction_candidate(self, new_program: Program) -> Optional[str]:
        """
        Find program to potentially evict.

        Uses deterministic crowding: find most similar NON-PROTECTED program.

        Protected programs:
        - Top elite_ratio by elite_score
        """
        protected = self._get_protected_ids()

        # Find most similar non-protected program
        best_id = None
        best_dist = float("inf")

        for pid, p in self._programs.items():
            if pid in protected:
                continue

            dist = self.diversity.distance(new_program, p)
            if dist < best_dist:
                best_dist = dist
                best_id = pid

        return best_id
````

## → Calls
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._get_protected_ids]]
- [[base_database.Program]]

## ← Called by
- [[UnifiedArchive.add]]
- [[UnifiedArchive.add_merged_program]]
