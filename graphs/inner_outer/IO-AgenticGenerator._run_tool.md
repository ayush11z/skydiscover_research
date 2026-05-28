---
name: IO-AgenticGenerator._run_tool
description: method in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# AgenticGenerator._run_tool

**File:** `skydiscover/llm/agentic_generator.py:275`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    def _run_tool(self, name: str, args: Dict[str, Any], files_read: set) -> Dict[str, Any]:
        try:
            if name == "read_file":
                return self._tool_read_file(args, files_read)
            elif name == "search":
                return self._tool_search(args)
            return _err(f"Unknown tool '{name}'. Available: read_file, search.")
        except Exception as e:
            return _err(f"Tool '{name}' error: {e}")
````

## → Calls
- [[IO-AgenticGenerator._tool_read_file]]
- [[IO-AgenticGenerator._tool_search]]
- [[IO-agentic_generator._err]]

## ← Called by
- [[IO-AgenticGenerator.generate]]
