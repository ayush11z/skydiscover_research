---
name: AdaEvolveDatabase.sample
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.sample

**File:** `skydiscover/search/adaevolve/database.py:496`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def sample(
        self,
        num_context_programs: Optional[int] = 4,
        force_exploration: bool = False,
        **kwargs,
    ) -> Tuple[Dict[str, Program], Dict[str, List[Program]]]:
        """
        Sample parent and other context programs using adaptive search intensity.

        The search intensity determines sampling mode:
        - High intensity → exploration mode (sample by novelty)
        - Low intensity → exploitation mode (sample by fitness)

        UnifiedArchive maintains diversity even during exploitation via
        elite_score which combines fitness, novelty, and Pareto status.

        Returns the standard framework format:
        - parent_dict: Dict mapping a label string to one parent Program.
          The label is EXPLORE_LABEL, EXPLOIT_LABEL, or "" (balanced).
        - context_programs_dict: Dict mapping "" to a list of context programs.

        The sampling mode is also stored on self._last_sampling_mode for
        the controller to read (for logging, paradigm, sibling context).

        Args:
            num_context_programs: Number of context programs
            force_exploration: Force exploration mode

        Returns:
            Tuple of (parent_dict, context_programs_dict)
        """
        island_idx = self.current_island

        if self.use_unified_archive and self.archives:
            return self._sample_from_archive(island_idx, num_context_programs, force_exploration)
        else:
            return self._sample_legacy(island_idx, num_context_programs, force_exploration)
````

## → Calls
- [[AdaEvolveDatabase._sample_from_archive]]
- [[AdaEvolveDatabase._sample_legacy]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
