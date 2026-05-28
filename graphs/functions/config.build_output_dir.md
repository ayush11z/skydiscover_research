---
name: config.build_output_dir
description: function in skydiscover/config.py (config)
metadata:
  type: project
---

# config.build_output_dir

**File:** `skydiscover/config.py:885`  
**Kind:** function  
**Layer:** #config

## Source
````python
def build_output_dir(search_type: str, initial_program_path: str, base_dir: str = "outputs") -> str:
    """Build a standardized output directory: outputs/<search_type>/<problem_name>_<MMDD_HHMM>/"""
    from datetime import datetime

    problem_name = (
        os.path.basename(os.path.dirname(os.path.abspath(initial_program_path))) or "unknown"
    )
    timestamp = datetime.now().strftime("%m%d_%H%M")
    return os.path.join(base_dir, search_type, f"{problem_name}_{timestamp}")
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[Runner.__init__]]
- [[api._run_discovery_async]]
- [[cli.main_async]]
- [[registry.setup_search]]
