---
name: BeamSearchDatabase.log_status
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase.log_status

**File:** `skydiscover/search/beam_search/database.py:504`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def log_status(self) -> None:
        """Log the status of the beam search database."""
        stats = self.get_search_stats()
        logger.info(
            f"BeamSearchDatabase status: {stats['total_programs']} programs, "
            f"beam_size={stats['beam_size']}, max_depth={stats['max_depth_reached']}, "
            f"expansions={stats['total_expansions']}"
        )

        # Log beam contents
        if self.beam:
            beam_progs = self.get_beam_programs()
            logger.info("Current beam:")
            for i, prog in enumerate(beam_progs[:5]):  # Show top 5
                logger.info(
                    f"  {i+1}. {prog.id}: score={self._get_program_score(prog):.4f}, "
                    f"depth={self.depth.get(prog.id, 0)}"
                )
````

## → Calls
- [[BeamSearchDatabase._get_program_score]]
- [[BeamSearchDatabase.get_beam_programs]]
- [[BeamSearchDatabase.get_search_stats]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[BeamSearchDatabase.load]]
