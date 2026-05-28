---
name: unified_archive.UnifiedArchive
description: class in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# unified_archive.UnifiedArchive

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:58`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class UnifiedArchive:
    """
    Flat-list archive with unified elite scoring.

    Elite Score = fitness_weight * fitness_percentile + novelty_weight * novelty_percentile

    Where:
    - fitness_percentile: position when sorted by primary metric / n
    - novelty_percentile: position when sorted by k-NN distance / n

    Programs with high elite_score are protected from eviction.
    Replacement uses deterministic crowding (compete with most similar).
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._init_archives]]
- [[AdaEvolveDatabase._spawn_island]]
