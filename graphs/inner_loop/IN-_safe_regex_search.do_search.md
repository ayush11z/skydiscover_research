---
name: IN-_safe_regex_search.do_search
description: function in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# _safe_regex_search.do_search

**File:** `skydiscover/llm/agentic_generator.py:501`  
**Kind:** function  
**Layer:** #llm

## Source
````python
    def do_search():
        return [
            f"{i}: {line}"
            for i, line in enumerate(text.splitlines(), 1)
            if len(line) <= _MAX_SEARCH_LINE_LEN and compiled.search(line)
        ]
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IN-agentic_generator._safe_regex_search]]
