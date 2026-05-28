---
name: UnifiedArchive.sample_other_context_programs
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.sample_other_context_programs

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:677`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def sample_other_context_programs(
        self,
        parent: Program,
        n: int = 5,
        top_k_ratio: float = 0.5,
    ) -> List[Program]:
        """
        Sample context programs for LLM context.

        Strategy: Pick programs MOST DIFFERENT from parent, but only from
        top performers. This ensures other context programs are both diverse AND
        high-quality.

        Args:
            parent: The parent program (to be diverse from)
            n: Number of other context programs to sample
            top_k_ratio: Fraction of archive to consider as "top" (default 50%)

        Returns:
            List of context programs
        """
        if not self._programs or n <= 0:
            return []

        # First, get top performers by fitness
        all_programs = list(self._programs.values())
        all_programs.sort(key=lambda p: self._get_fitness(p), reverse=True)

        # Consider top 50% (or at least 2*n programs) as candidate pool
        top_k = max(2 * n, int(len(all_programs) * top_k_ratio))
        top_programs = all_programs[:top_k]

        # Now pick most diverse FROM the top performers
        candidates = []
        for p in top_programs:
            if p.id != parent.id:
                dist = self.diversity.distance(parent, p)
                candidates.append((p, dist))

        candidates.sort(key=lambda x: -x[1])

        return [p for p, _ in candidates[:n]]
````

## → Calls
- [[Program.id]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._get_fitness]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
