---
name: AdaEvolveDatabase._get_mode_labels
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._get_mode_labels

**File:** `skydiscover/search/adaevolve/database.py:368`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _get_mode_labels(self) -> Tuple[str, str]:
        """Return (explore_label, exploit_label) appropriate for the language."""
        if self.language.lower() in ("text", "prompt"):
            return EXPLORE_LABEL_PROMPT_OPT, EXPLOIT_LABEL_PROMPT_OPT
        return EXPLORE_LABEL, EXPLOIT_LABEL
````

## → Calls
- [[AdaEvolveDatabase.__init__]]

## ← Called by
- [[AdaEvolveDatabase._sample_from_archive]]
- [[AdaEvolveDatabase._sample_legacy]]
