---
name: AdaEvolveDatabase._sample_random
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._sample_random

**File:** `skydiscover/search/adaevolve/database.py:667`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _sample_random(self, population: List[Program]) -> Program:
        """Sample uniformly at random (exploration)."""
        return random.choice(population)
````

## → Calls
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._sample_legacy]]
