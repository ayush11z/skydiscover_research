---
name: BeamSearchDatabase.get_beam_programs
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase.get_beam_programs

**File:** `skydiscover/search/beam_search/database.py:457`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def get_beam_programs(self) -> List[Program]:
        """
        Get all programs currently in the beam.

        Returns:
            List of programs in the beam, sorted by score (descending)
        """
        beam_programs = [self.programs[pid] for pid in self.beam if pid in self.programs]
        return sorted(beam_programs, key=self._get_program_score, reverse=True)
````

## → Calls
- [[BeamSearchDatabase._get_program_score]]
- [[CheckpointManager.load]]
- [[base_database.Program]]

## ← Called by
- [[BeamSearchDatabase.log_status]]
