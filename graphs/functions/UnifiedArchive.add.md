---
name: UnifiedArchive.add
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.add

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:112`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def add(self, program: Program) -> bool:
        """
        Add a program to the archive.

        Strategy:
        1. If under capacity, add directly
        2. Otherwise, find eviction candidate (most similar non-protected)
        3. Replace if new program has higher elite score

        Note: Genealogy is tracked ONLY after successful addition to prevent
        orphaned entries when programs are rejected.

        Args:
            program: Program to add

        Returns:
            True if program was added, False if rejected
        """
        if program.id in self._programs:
            logger.debug(f"Program {program.id[:8]} already in archive")
            return False

        # Case 1: Under capacity - add directly
        if len(self._programs) < self.config.max_size:
            self._insert(program)
            self._track_genealogy(program)
            logger.debug(f"Added {program.id[:8]} (under capacity)")
            return True

        # Case 2: At capacity - find eviction candidate
        self._ensure_cache_valid()
        candidate_id = self._find_eviction_candidate(program)

        if candidate_id is None:
            logger.debug(f"Rejected {program.id[:8]} (all protected)")
            return False

        # Compare elite scores
        new_score = self._compute_elite_score_for_new(program)
        old_score = self._elite_scores.get(candidate_id, 0.0)

        if new_score > old_score:
            self._evict(candidate_id)
            self._insert(program)
            self._track_genealogy(program)
            logger.debug(
                f"Replaced {candidate_id[:8]} with {program.id[:8]} "
                f"(score {old_score:.3f} → {new_score:.3f})"
            )
            return True

        logger.debug(f"Rejected {program.id[:8]} " f"(score {new_score:.3f} <= {old_score:.3f})")
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
- [[UnifiedArchive._track_genealogy]]
- [[base_database.Program]]

## ← Called by
- [[AgenticGenerator._tool_read_file]]
- [[ClaudeCodeController.run_discovery]]
- [[CoEvolutionController._migrate_to_db]]
- [[CoEvolutionController._restore_fallback_database]]
- [[CoEvolutionController._wrap_add_method]]
- [[DiscoveryController._process_iteration_result]]
- [[Runner._add_initial_program]]
- [[_wrap_add_method.wrapped_add]]
- [[search_strategy_evaluator.evaluate]]
