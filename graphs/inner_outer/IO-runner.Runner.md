---
name: IO-runner.Runner
description: class in skydiscover/runner.py (runner)
metadata:
  type: project
---

# runner.Runner

**File:** `skydiscover/runner.py:25`  
**Kind:** class  
**Layer:** #runner

## Source
````python
class Runner:
    """Top-level entry point for a discovery run.

    Loads config, creates the database and discovery controller, runs the
    search loop, and saves checkpoints + best program.

    Args:
        initial_program_path: path to the starting solution file.
        evaluation_file: path to the user's evaluator script (must define evaluate()).
        config_path: optional YAML config file (ignored if config is provided).
        config: optional pre-built Config object (takes priority over config_path).
        output_dir: where to write logs, checkpoints, and best program.
            Auto-generated from search type + problem name if omitted.
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-Runner.__init__]]
- [[IO-Runner._setup_logging]]
- [[IO-Runner._start_monitor]]
