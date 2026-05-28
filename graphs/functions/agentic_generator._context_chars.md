---
name: agentic_generator._context_chars
description: function in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# agentic_generator._context_chars

**File:** `skydiscover/llm/agentic_generator.py:405`  
**Kind:** function  
**Layer:** #llm

## Source
````python
def _context_chars(system: str, conversation: List[Dict[str, Any]]) -> int:
    n = len(system)
    for msg in conversation:
        n += len(msg.get("content", ""))
        for tc in msg.get("tool_calls", []):
            n += len(tc.get("function", {}).get("arguments", ""))
    return n
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[AgenticGenerator.generate]]
