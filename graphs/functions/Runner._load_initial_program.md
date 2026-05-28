---
name: Runner._load_initial_program
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
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[Runner.__init__]]
