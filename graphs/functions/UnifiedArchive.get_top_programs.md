---
name: UnifiedArchive.get_top_programs
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.get_top_programs

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:841`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_top_programs(self, n: Optional[int] = None) -> List[Program]:
        """
        Get top programs by fitness.

        Args:
            n: Number of programs to return. If None, returns top ~20%
               (at least 1, at most 10).

        Returns:
            List of top programs sorted by fitness (best first)
        """
        programs = list(self._programs.values())
        if not programs:
            return []

        programs.sort(key=lambda p: self._get_fitness(p), reverse=True)

        if n is not None:
            return programs[:n]

        # Default: top ~20% (at least 1, at most 10)
        top_count = max(1, min(10, len(programs) // 5))
        return programs[:top_count]
````

## → Calls
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._get_fitness]]
- [[base_database.Program]]

## ← Called by
- [[BeamSearchDatabase._validate_and_reconstruct_beam]]
- [[BeamSearchDatabase.sample]]
- [[BestOfNDatabase.sample]]
- [[TopKDatabase.sample]]
- [[UnifiedArchive.find_merge_candidates]]
- [[UnifiedArchive.get_pareto_front]]
- [[UnifiedArchive.sample_parent]]
- [[UnifiedArchive.stats]]
