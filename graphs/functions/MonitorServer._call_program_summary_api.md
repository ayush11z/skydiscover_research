---
name: MonitorServer._call_program_summary_api
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._call_program_summary_api

**File:** `skydiscover/extras/monitor/server.py:737`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def _call_program_summary_api(self, prompt_data: Dict[str, str]) -> str:
        """Call LLM for per-program summary (blocking, runs in executor)."""
        return self._call_llm_api(prompt_data, max_tokens=2048, timeout=120)
````

## → Calls
- [[MonitorServer._call_llm_api]]

## ← Called by
- [[MonitorServer._generate_program_summary]]
