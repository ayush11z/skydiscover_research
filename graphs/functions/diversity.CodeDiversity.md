---
name: diversity.CodeDiversity
description: class in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# diversity.CodeDiversity

**File:** `skydiscover/search/adaevolve/archive/diversity.py:55`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class CodeDiversity(DiversityStrategy):
    """
    Diversity based on code structure and content.

    Fast computation with no external dependencies. Uses multiple signals:
    - Token-based Jaccard distance (captures vocabulary differences)
    - Structural features (imports, functions, classes)
    - Normalized length difference

    Good for: General use, when code structure reflects behavior.
    """

````

## → Calls
- [[diversity.DiversityStrategy]]

## ← Called by
- [[UnifiedArchive.__init__]]
- [[diversity.create_diversity_strategy]]
