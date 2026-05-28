---
name: agentic_generator._safe_regex_search
description: function in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# agentic_generator._safe_regex_search

**File:** `skydiscover/llm/agentic_generator.py:496`  
**Kind:** function  
**Layer:** #llm

## Source
````python
def _safe_regex_search(
    compiled: "re.Pattern", text: str, timeout: float = 2.0
) -> Tuple[bool, List[str], str]:
    """Regex search with thread-based timeout."""

    def do_search():
        return [
            f"{i}: {line}"
            for i, line in enumerate(text.splitlines(), 1)
            if len(line) <= _MAX_SEARCH_LINE_LEN and compiled.search(line)
        ]

    fut = _REGEX_EXECUTOR.submit(do_search)
    try:
        result = fut.result(timeout=timeout)
        return True, result, ""
    except concurrent.futures.TimeoutError:
        return False, [], f"Regex timed out ({timeout}s). Simplify the pattern."
````

## → Calls
- [[_safe_regex_search.do_search]]

## ← Called by
- [[AgenticGenerator._tool_search]]
