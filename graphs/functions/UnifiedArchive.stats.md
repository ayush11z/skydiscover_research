---
name: UnifiedArchive.stats
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.stats

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:892`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def stats(self) -> Dict[str, Any]:
        """Get archive statistics."""
        self._ensure_cache_valid()

        top_count = len(self.get_top_programs())
        pareto_front = self.get_pareto_front() if self.config.pareto_objectives else []
        return {
            "size": len(self._programs),
            "max_size": self.config.max_size,
            "top_count": top_count,
            "pareto_count": len(pareto_front) if pareto_front else top_count,
            "pareto_front_size": len(pareto_front),
            "protected_count": len(self._get_protected_ids()),
            "k_neighbors": self.config.k_neighbors,
        }
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[UnifiedArchive._ensure_cache_valid]]
- [[UnifiedArchive._get_protected_ids]]
- [[UnifiedArchive.get_pareto_front]]
- [[UnifiedArchive.get_top_programs]]

## ← Called by
- [[BeamSearchDatabase.add]]
- [[BeamSearchDatabase.get_search_stats]]
- [[BeamSearchDatabase.load]]
- [[BeamSearchDatabase.save]]
