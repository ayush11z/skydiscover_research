---
name: IO-agentic_generator._err
description: function in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# agentic_generator._err

**File:** `skydiscover/llm/agentic_generator.py:401`  
**Kind:** function  
**Layer:** #llm

## Source
````python
def _err(msg: str) -> Dict[str, Any]:
    return {"content": msg, "_error": True}
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-AgenticGenerator._run_tool]]
- [[IO-AgenticGenerator._tool_read_file]]
- [[IO-AgenticGenerator._tool_search]]
