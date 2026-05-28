---
name: ParadigmGenerator._build_previously_tried_section
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_previously_tried_section

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:404`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_previously_tried_section(self, previously_tried: List[str]) -> str:
        """Build the previously tried ideas section."""
        if not previously_tried:
            return """## Previously Tried Ideas

No previous paradigms have been tried yet. You have freedom to explore any approach."""

        formatted = "\n".join(f"- {idea}" for idea in previously_tried)
        return f"""## Previously Tried Ideas - CHECK THIS FIRST

**CRITICAL:** Review what was already tried. Do NOT suggest ideas that use
the same libraries, functions, or approaches as FAILED attempts.

{formatted}

**STRICT PROHIBITION:** Do NOT keep suggesting approaches that have already failed.
If an approach failed, understand WHY before suggesting similar techniques.
Prioritize approaches that are fundamentally different from failed attempts.

**Learning from Failures - Understand Root Causes:**
When a technique fails badly (score decreased significantly), understand WHY before suggesting alternatives:
- **Fundamental mismatch:** Wrong problem type (e.g., continuous optimizer on discrete problem) -> avoid that entire class of approaches
- **Structural mismatch:** Wrong approach for problem structure (e.g., linear proxy for non-linear objective) -> use approaches that match the actual structure
- **Implementation issues:** If the same library failed multiple times or very badly (>10% decrease), it likely indicates a fundamental mismatch - suggest a different class of approaches"""
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[ParadigmGenerator._build_prompt]]
