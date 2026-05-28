---
name: diversity.DiversityStrategy
description: class in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# diversity.DiversityStrategy

**File:** `skydiscover/search/adaevolve/archive/diversity.py:20`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class DiversityStrategy(ABC):
    """
    Abstract base for measuring how different two programs are.

    This is the SINGLE source of truth for distance/diversity/similarity.
    All archive operations use this abstraction.
    """

    @abstractmethod
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[HybridDiversity.__init__]]
- [[UnifiedArchive.__init__]]
- [[diversity.CodeDiversity]]
- [[diversity.HybridDiversity]]
- [[diversity.MetricDiversity]]
- [[diversity.create_diversity_strategy]]
