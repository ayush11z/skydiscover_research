---
name: BeamSearchDatabase.get_unexpanded_beam
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase.get_unexpanded_beam

**File:** `skydiscover/search/beam_search/database.py:467`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def get_unexpanded_beam(self) -> List[Program]:
        """
        Get beam programs that haven't been expanded yet.

        Useful for analysis or alternative expansion strategies.

        Returns:
            List of unexpanded beam programs
        """
        unexpanded = [
            self.programs[pid]
            for pid in self.beam
            if pid in self.programs and pid not in self.expanded
        ]
        return sorted(unexpanded, key=self._get_program_score, reverse=True)
````

## → Calls
- [[BeamSearchDatabase._get_program_score]]
- [[CheckpointManager.load]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
