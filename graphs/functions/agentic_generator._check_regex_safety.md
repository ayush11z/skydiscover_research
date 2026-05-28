---
name: agentic_generator._check_regex_safety
description: function in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# agentic_generator._check_regex_safety

**File:** `skydiscover/llm/agentic_generator.py:486`  
**Kind:** function  
**Layer:** #llm

## Source
````python
def _check_regex_safety(pattern: str) -> Optional[str]:
    """Reject patterns with nested quantifiers that cause catastrophic backtracking."""
    if _NESTED_QUANTIFIER_RE.search(pattern):
        return "Nested quantifiers detected (e.g. '(a+)+'). Use a simpler pattern."
    return None
````

## → Calls
- [[Config.search]]

## ← Called by
- [[AgenticGenerator._tool_search]]
