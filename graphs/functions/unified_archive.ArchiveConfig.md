---
name: unified_archive.ArchiveConfig
description: class in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# unified_archive.ArchiveConfig

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:29`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class ArchiveConfig:
    """Configuration for UnifiedArchive."""

    # Maximum number of programs in archive
    max_size: int = 100

    # Number of neighbors for k-NN novelty computation
    k_neighbors: int = 5

    # Fraction of archive protected as elite (top by elite_score)
    elite_ratio: float = 0.2

    # Weights for elite score components (should sum to ~1.0)
    # NOTE: pareto_weight is deprecated and redistributed to fitness_weight
    pareto_weight: float = 0.0  # Deprecated - added to fitness_weight
    fitness_weight: float = 0.7  # Weight for fitness rank
    novelty_weight: float = 0.3  # Weight for novelty rank

    # Primary metric key for fitness (None = auto-detect from common names)
    fitness_key: Optional[str] = None

    # Higher is better for each metric (default True for all)
    higher_is_better: Dict[str, bool] = field(default_factory=dict)

    # Pareto multi-objective selection (opt-in: empty list = disabled)
    pareto_objectives: List[str] = field(default_factory=list)
    pareto_objectives_weight: float = 0.0
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._init_archives]]
- [[AdaEvolveDatabase._spawn_island]]
- [[UnifiedArchive.__init__]]
