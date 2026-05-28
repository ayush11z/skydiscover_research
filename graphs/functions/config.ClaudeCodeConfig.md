---
name: config.ClaudeCodeConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.ClaudeCodeConfig

**File:** `skydiscover/config.py:471`  
**Kind:** class  
**Layer:** #config

## Source
````python
class ClaudeCodeConfig(DatabaseConfig):
    """Configuration for the Claude Code baseline.

    Claude Code runs autonomously inside a Docker container, iterating on
    the solution using the evaluator directly.  max_turns maps to the
    --max-turns flag passed to the claude CLI.
    """

    max_turns: int = 50
    docker_image: str = "skydiscover-claude-code:latest"
````

## → Calls
- [[config.DatabaseConfig]]

## ← Called by
_(entry point — nothing in this graph calls it)_
