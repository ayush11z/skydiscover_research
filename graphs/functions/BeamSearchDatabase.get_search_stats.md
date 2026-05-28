---
name: BeamSearchDatabase.get_search_stats
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase.get_search_stats

**File:** `skydiscover/search/beam_search/database.py:483`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def get_search_stats(self) -> Dict:
        """
        Get statistics about the beam search progress.

        Returns:
            Dictionary with search statistics
        """
        return {
            "beam_size": len(self.beam),
            "total_programs": len(self.programs),
            "total_expansions": self.stats["total_expansions"],
            "max_depth_reached": self.stats["max_depth_reached"],
            "beam_updates": self.stats["beam_updates"],
            "unexpanded_in_beam": len(self.beam - self.expanded),
            "avg_beam_depth": (
                sum(self.depth.get(pid, 0) for pid in self.beam) / len(self.beam)
                if self.beam
                else 0
            ),
        }
````

## → Calls
- [[CheckpointManager.load]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[UnifiedArchive.stats]]

## ← Called by
- [[BeamSearchDatabase.log_status]]
