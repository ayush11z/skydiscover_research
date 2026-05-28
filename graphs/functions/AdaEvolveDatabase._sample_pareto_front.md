---
name: AdaEvolveDatabase._sample_pareto_front
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._sample_pareto_front

**File:** `skydiscover/search/adaevolve/database.py:677`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _sample_pareto_front(self, archive, population: List[Program]) -> Program:
        """Sample from Pareto front weighted by crowding distance.

        Falls back to _sample_top if front is too small.
        """
        archive._ensure_cache_valid()
        front_programs = [
            archive.get(pid)
            for pid, rank in archive._pareto_ranks.items()
            if rank == 0 and archive.get(pid) is not None
        ]

        if len(front_programs) < 2:
            return self._sample_top(population)

        weights = []
        for p in front_programs:
            cd = archive._crowding_distances.get(p.id, 0.0)
            if cd == float("inf"):
                cd = 1e6
            weights.append(max(cd, 0.001))

        return random.choices(front_programs, weights=weights, k=1)[0]
````

## → Calls
- [[AdaEvolveDatabase._sample_top]]
- [[LangFuseTracer.get]]
- [[Program.id]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive._ensure_cache_valid]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._sample_from_archive]]
