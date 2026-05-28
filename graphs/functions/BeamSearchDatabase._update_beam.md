---
name: BeamSearchDatabase._update_beam
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._update_beam

**File:** `skydiscover/search/beam_search/database.py:133`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _update_beam(self, new_program: Program) -> None:
        """
        Update the beam to include the new program if it's good enough.

        The beam always contains the best beam_width programs based on
        fitness score, with optional diversity consideration.
        """
        # Add to beam candidates
        self.beam.add(new_program.id)

        # If beam exceeds width, prune to best beam_width
        if len(self.beam) > self.beam_width:
            self._prune_beam()
            self.stats["beam_updates"] += 1
````

## → Calls
- [[BeamSearchDatabase._prune_beam]]
- [[Program.id]]
- [[base_database.Program]]

## ← Called by
- [[BeamSearchDatabase.add]]
