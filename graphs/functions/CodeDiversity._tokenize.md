---
name: CodeDiversity._tokenize
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# CodeDiversity._tokenize

**File:** `skydiscover/search/adaevolve/archive/diversity.py:107`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _tokenize(self, code: str) -> set:
        """
        Extract meaningful tokens from code.

        Splits on whitespace and punctuation, filters short tokens.
        Captures identifiers, keywords, and significant patterns.
        """
        import re

        # Split on whitespace and common delimiters, keep meaningful tokens
        tokens = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*|[0-9]+\.?[0-9]*", code)
        # Filter very short tokens (likely noise) but keep keywords
        return set(t for t in tokens if len(t) >= 2)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[CodeDiversity.distance]]
