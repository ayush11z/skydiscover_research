---
name: UnifiedArchive._compute_novelty
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._compute_novelty

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:392`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _compute_novelty(self, program: Program, all_programs: List[Program]) -> float:
        """
        Compute novelty as average distance to k nearest neighbors.

        Higher novelty = more different from neighbors.
        """
        others = [p for p in all_programs if p.id != program.id]

        if not others:
            return 1.0  # Max novelty if alone

        # Compute distances to all other programs
        distances = [self.diversity.distance(program, other) for other in others]

        # Sort and take k nearest
        distances.sort()
        k = min(self.config.k_neighbors, len(distances))
        k_nearest = distances[:k]

        if not k_nearest:
            return 1.0

        return sum(k_nearest) / len(k_nearest)
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[Program.id]]
- [[UnifiedArchive.__init__]]
- [[base_database.Program]]

## ← Called by
- [[UnifiedArchive._compute_elite_score_for_new]]
- [[UnifiedArchive._ensure_cache_valid]]
