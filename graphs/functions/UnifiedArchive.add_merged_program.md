---
name: UnifiedArchive.add_merged_program
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.add_merged_program

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:784`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def add_merged_program(self, program: Program, parent_ids: List[str]) -> bool:
        """
        Add a program created by merging multiple parents.

        Note: Genealogy is tracked ONLY after successful addition to prevent
        orphaned entries when programs are rejected.

        Args:
            program: The merged program
            parent_ids: List of parent program IDs

        Returns:
            True if added, False if rejected
        """
        if program.id in self._programs:
            return False

        # Case 1: Under capacity - add directly
        if len(self._programs) < self.config.max_size:
            self._insert(program)
            self._track_merged_genealogy(program, parent_ids)
            return True

        # Case 2: At capacity - find eviction candidate
        self._ensure_cache_valid()
        candidate_id = self._find_eviction_candidate(program)

        if candidate_id is None:
            return False

        new_score = self._compute_elite_score_for_new(program)
        old_score = self._elite_scores.get(candidate_id, 0.0)

        if new_score > old_score:
            self._evict(candidate_id)
            self._insert(program)
            self._track_merged_genealogy(program, parent_ids)
            return True

        return False
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[Program.id]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._compute_elite_score_for_new]]
- [[UnifiedArchive._ensure_cache_valid]]
- [[UnifiedArchive._evict]]
- [[UnifiedArchive._find_eviction_candidate]]
- [[UnifiedArchive._insert]]
- [[UnifiedArchive._track_merged_genealogy]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
