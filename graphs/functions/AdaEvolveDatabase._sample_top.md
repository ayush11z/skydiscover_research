---
name: AdaEvolveDatabase._sample_top
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._sample_top

**File:** `skydiscover/search/adaevolve/database.py:671`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _sample_top(self, population: List[Program]) -> Program:
        """Sample from top performers (exploitation)."""
        sorted_pop = sorted(population, key=self._get_fitness, reverse=True)
        top_k = max(1, len(sorted_pop) // 4)
        return random.choice(sorted_pop[:top_k])
````

## → Calls
- [[AdaEvolveDatabase._get_fitness]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._sample_from_archive]]
- [[AdaEvolveDatabase._sample_legacy]]
- [[AdaEvolveDatabase._sample_pareto_front]]
