---
name: AdaEvolveContextBuilder._format_error_context
description: staticmethod in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._format_error_context

**File:** `skydiscover/context_builder/adaevolve/builder.py:487`  
**Kind:** staticmethod  
**Layer:** #context-builder

## Source
````python
    def _format_error_context(error_context: str) -> str:
        """Format retry error context."""
        return (
            "## RETRY CONTEXT\n"
            f"Previous attempt failed with error:\n```\n{error_context}\n```\n"
            "Please fix this issue in your response."
        )
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveContextBuilder._build_search_guidance]]
