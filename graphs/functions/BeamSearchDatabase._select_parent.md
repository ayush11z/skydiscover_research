---
name: BeamSearchDatabase._select_parent
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._select_parent

**File:** `skydiscover/search/beam_search/database.py:337`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _select_parent(self) -> Program:
        """
        Select a parent program from the beam using the configured strategy.

        Returns:
            Selected parent program
        """
        beam_list = [self.programs[pid] for pid in self.beam if pid in self.programs]

        if not beam_list:
            raise ValueError("Beam is empty, cannot select parent")

        if self.selection_strategy == "best":
            return self._select_best(beam_list)
        elif self.selection_strategy == "stochastic":
            return self._select_stochastic(beam_list)
        elif self.selection_strategy == "round_robin":
            return self._select_round_robin(beam_list)
        elif self.selection_strategy == "diversity_weighted":
            return self._select_diversity_weighted(beam_list)
        else:
            logger.warning(f"Unknown strategy {self.selection_strategy}, using best")
            return self._select_best(beam_list)
````

## → Calls
- [[BeamSearchDatabase._select_best]]
- [[BeamSearchDatabase._select_diversity_weighted]]
- [[BeamSearchDatabase._select_round_robin]]
- [[BeamSearchDatabase._select_stochastic]]
- [[CheckpointManager.load]]
- [[base_database.Program]]

## ← Called by
- [[BeamSearchDatabase.sample]]
