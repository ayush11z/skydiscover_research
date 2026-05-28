---
name: OpenEvolveNativeDatabase._fast_code_diversity
description: staticmethod in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._fast_code_diversity

**File:** `skydiscover/search/openevolve_native/database.py:536`  
**Kind:** staticmethod  
**Layer:** #openevolve

## Source
````python
    def _fast_code_diversity(code1: str, code2: str) -> float:
        if code1 == code2:
            return 0.0
        length_diff = abs(len(code1) - len(code2))
        line_diff = abs(code1.count("\n") - code2.count("\n"))
        char_diff = len(set(code1).symmetric_difference(set(code2)))
        return length_diff * 0.1 + line_diff * 10 + char_diff * 0.5
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[OpenEvolveNativeDatabase._get_cached_diversity]]
- [[OpenEvolveNativeDatabase._update_diversity_reference_set]]
