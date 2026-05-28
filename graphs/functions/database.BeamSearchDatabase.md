---
name: database.BeamSearchDatabase
description: class in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# database.BeamSearchDatabase

**File:** `skydiscover/search/beam_search/database.py:28`  
**Kind:** class  
**Layer:** #beam-search

## Source
````python
class BeamSearchDatabase(ProgramDatabase):
    """
    Database implementing beam search for parent selection.

    Beam search maintains a fixed number of "active" candidates (the beam),
    expanding from the most promising programs while pruning others.

    Configuration options (via DatabaseConfig attributes):
        beam_width: Number of candidates to keep in beam (default: 5)
        beam_selection_strategy: How to pick parent from beam
            - "best": Always pick highest scoring
            - "stochastic": Weighted random by score
            - "round_robin": Cycle through beam members
            - "diversity_weighted": Balance score and diversity (default)
        beam_diversity_weight: Weight for diversity in selection (default: 0.3)
        beam_temperature: Temperature for stochastic selection (default: 1.0)
        beam_depth_penalty: Penalty factor for deep programs (default: 0.0)
    """

````

## → Calls
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
