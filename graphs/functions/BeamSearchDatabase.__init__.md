---
name: BeamSearchDatabase.__init__
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase.__init__

**File:** `skydiscover/search/beam_search/database.py:47`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def __init__(self, name: str, config: DatabaseConfig):
        # Initialize beam-specific attributes BEFORE super().__init__()
        # because super().__init__() may call load() which needs these
        self.beam_width = getattr(config, "beam_width", 5)
        self.selection_strategy = getattr(config, "beam_selection_strategy", "diversity_weighted")
        self.diversity_weight = getattr(config, "beam_diversity_weight", 0.3)
        self.temperature = getattr(config, "beam_temperature", 1.0)
        self.depth_penalty = getattr(config, "beam_depth_penalty", 0.0)

        # Track program depths in search tree
        self.depth: Dict[str, int] = {}

        # Current beam (set of program IDs)
        self.beam: Set[str] = set()

        # Track which programs have been expanded (had children generated)
        self.expanded: Set[str] = set()

        # Round-robin state
        self._rr_index = 0

        # Statistics for analysis
        self.stats: Dict[str, Any] = {
            "total_expansions": 0,
            "max_depth_reached": 0,
            "beam_updates": 0,
            "diversity_scores": [],
        }

        # Now call super().__init__() which may trigger load()
        super().__init__(name, config)

        logger.info(
            f"BeamSearchDatabase initialized: width={self.beam_width}, "
            f"strategy={self.selection_strategy}, diversity_weight={self.diversity_weight}"
        )
````

## → Calls
- [[ProgramDatabase.__init__]]
- [[config.DatabaseConfig]]

## ← Called by
- [[BeamSearchDatabase.load]]
