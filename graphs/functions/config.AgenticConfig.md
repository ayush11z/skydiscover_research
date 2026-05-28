---
name: config.AgenticConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.AgenticConfig

**File:** `skydiscover/config.py:239`  
**Kind:** class  
**Layer:** #config

## Source
````python
class AgenticConfig:
    """Configuration for agentic solution generation.

    When enabled, replaces the single-shot LLM call with a multi-turn
    tool-calling agent loop that can read files and search the codebase
    before outputting the discovered solution.
    """

    enabled: bool = False
    codebase_root: Optional[str] = None

    # Agent loop limits
    max_steps: int = 5

    # Timeouts (seconds)
    per_step_timeout: float = 60.0
    overall_timeout: float = 300.0

    # Context management
    max_context_chars: int = 400_000
    max_file_chars: int = 50_000
    max_search_results: int = 50
    max_files_read: int = 20

    # Regex safety
    regex_timeout: float = 2.0
    max_regex_length: int = 200

    # Repo map — a depth-limited directory tree injected into the agent's first
    # message so it knows what files are available to read_file/search.
    repo_map_max_depth: int = 4
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[Config.from_dict]]
- [[Config.to_dict]]
- [[config.Config]]
