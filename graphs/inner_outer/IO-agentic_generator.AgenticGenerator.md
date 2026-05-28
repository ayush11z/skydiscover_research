---
name: IO-agentic_generator.AgenticGenerator
description: class in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# agentic_generator.AgenticGenerator

**File:** `skydiscover/llm/agentic_generator.py:49`  
**Kind:** class  
**Layer:** #llm

## Source
````python
class AgenticGenerator:
    """
    V0 [simple version]: Multi-turn tool-calling agent that explores a codebase before generating code.

    Tools: read_file, search. When it stops calling tools, its text output
    is the final answer. Returns None if no output is produced (caller falls
    back to direct generation).
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-DiscoveryController.__init__]]
- [[IO-DiscoveryController._call_llm]]
