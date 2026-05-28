---
name: AdaEvolveDatabase._sample_weighted
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._sample_weighted

**File:** `skydiscover/search/adaevolve/database.py:701`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _sample_weighted(self, population: List[Program]) -> Program:
        """Sample weighted by fitness (balanced)."""
        weights = []
        for prog in population:
            fitness = self._get_fitness(prog)
            weights.append(max(fitness, 0.001))  # Avoid zero weights

        total = sum(weights)
        weights = [w / total for w in weights]

        return random.choices(population, weights=weights, k=1)[0]
````

## → Calls
- [[AdaEvolveDatabase._get_fitness]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._sample_legacy]]
