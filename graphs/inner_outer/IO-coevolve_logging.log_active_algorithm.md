---
name: IO-coevolve_logging.log_active_algorithm
description: function in skydiscover/search/evox/utils/coevolve_logging.py (evox)
metadata:
  type: project
---

# coevolve_logging.log_active_algorithm

**File:** `skydiscover/search/evox/utils/coevolve_logging.py:255`  
**Kind:** function  
**Layer:** #evox

## Source
````python
async def log_active_algorithm(
    outputs_dir: str,
    active_search_code: str,
    iteration: int,
) -> None:
    """Log the active algorithm on the solution side (fallback if generation/validation failed)."""
    active_code = active_search_code or ""

    iteration_dir = os.path.join(outputs_dir, f"iteration_{iteration}")
    os.makedirs(iteration_dir, exist_ok=True)

    candidate_code_path = os.path.join(iteration_dir, "code.py")
    active_code_filename = "active_code.py" if os.path.exists(candidate_code_path) else "code.py"
    with open(os.path.join(iteration_dir, active_code_filename), "w") as f:
        f.write(active_code)

    metadata_path = os.path.join(iteration_dir, "metadata.json")
    if os.path.exists(metadata_path):
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
    else:
        metadata = {"iteration": iteration}

    metadata["is_fallback"] = True
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-coevolve_logging.handle_generation_failure]]
