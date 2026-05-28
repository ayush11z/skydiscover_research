---
name: BeamSearchDatabase.sample
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase.sample

**File:** `skydiscover/search/beam_search/database.py:294`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def sample(
        self, num_context_programs: Optional[int] = 4, **kwargs
    ) -> Tuple[Program, List[Program]]:
        """
        Sample a parent program and context programs using beam search strategy.

        The parent is selected from the current beam using the configured
        selection strategy. context programs are drawn from top programs.

        Args:
            num_context_programs: Number of context programs to return

        Returns:
            Tuple of (parent, other_context_programs).
        """
        if not self.beam:
            # Fallback: use best program if beam is empty
            best = self.get_best_program()
            if best:
                self.beam.add(best.id)
            else:
                raise ValueError("Cannot sample: no programs in database")

        # Select parent based on strategy
        parent = self._select_parent()

        # Mark as expanded
        self.expanded.add(parent.id)
        self.stats["total_expansions"] += 1

        # Get context programs from top programs, excluding the parent
        n = num_context_programs or 4
        top_programs = self.get_top_programs(n + 1)
        other_context_programs = [p for p in top_programs if p.id != parent.id][:n]

        logger.info(
            f"Beam search: selected parent {parent.id} (depth={self.depth.get(parent.id, 0)}, "
            f"score={self._get_program_score(parent):.4f}), "
            f"beam_size={len(self.beam)}, other_context_programs={len(other_context_programs)}"
        )

        return parent, other_context_programs
````

## → Calls
- [[BeamSearchDatabase._get_program_score]]
- [[BeamSearchDatabase._select_parent]]
- [[LangFuseTracer.get]]
- [[Program.id]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.get_best_program]]
- [[ProgramDatabase.get_top_programs]]
- [[UnifiedArchive.get]]
- [[UnifiedArchive.get_top_programs]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
