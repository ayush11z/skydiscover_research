---
name: AdaEvolveContextBuilder._diversity_note_text
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._diversity_note_text

**File:** `skydiscover/context_builder/adaevolve/builder.py:109`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _diversity_note_text(self) -> str:
        if not self._is_multiobjective_enabled():
            return "Different solutions with similar combined_score but different features are valuable."
        return "Different solutions with similar overall trade-offs but different objective balances are valuable."
````

## → Calls
- [[AdaEvolveContextBuilder._is_multiobjective_enabled]]

## ← Called by
- [[AdaEvolveContextBuilder.build_prompt]]
