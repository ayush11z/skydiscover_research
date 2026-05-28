---
name: IO-AgenticGenerator.__init__
description: method in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# AgenticGenerator.__init__

**File:** `skydiscover/llm/agentic_generator.py:58`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    def __init__(self, llm_pool, config):
        self.llm_pool = llm_pool
        self.config = config
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-AgenticGenerator._call_llm]]
- [[IO-AgenticGenerator._tool_read_file]]
- [[IO-AgenticGenerator._tool_search]]
- [[IO-AgenticGenerator.generate]]
- [[IO-DiscoveryController.__init__]]
