---
name: BeamSearchDatabase._prune_beam
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._prune_beam

**File:** `skydiscover/search/beam_search/database.py:148`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _prune_beam(self) -> None:
        """
        Prune beam to beam_width, keeping the best candidates.

        Uses a combination of fitness score and diversity to select
        which programs to keep.
        """
        if len(self.beam) <= self.beam_width:
            return

        # Get all beam programs with their scores
        beam_programs = []
        for pid in self.beam:
            prog = self.programs.get(pid)
            if prog:
                score = self._get_program_score(prog)
                beam_programs.append((pid, prog, score))

        if self.diversity_weight > 0:
            # Use diversity-aware selection
            selected = self._diverse_selection(beam_programs, self.beam_width)
        else:
            # Pure fitness-based selection
            beam_programs.sort(key=lambda x: x[2], reverse=True)
            selected = [bp[0] for bp in beam_programs[: self.beam_width]]

        self.beam = set(selected)
````

## → Calls
- [[BeamSearchDatabase._diverse_selection]]
- [[BeamSearchDatabase._get_program_score]]
- [[CheckpointManager.load]]

## ← Called by
- [[BeamSearchDatabase._update_beam]]
