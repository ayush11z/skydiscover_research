---
name: IO-Runner._load_initial_program
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._load_initial_program

**File:** `skydiscover/runner.py:392`  
**Kind:** method  
**Layer:** #runner

## What it does
Reads the initial program source code from disk (path set in config). Called once during startup before the search loop begins.

## Source
````python
    def _load_initial_program(self) -> str:
        with open(self.initial_program_path, "r") as f:
            return f.read()
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-Runner.__init__]]
