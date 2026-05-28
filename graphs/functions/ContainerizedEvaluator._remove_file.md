---
name: ContainerizedEvaluator._remove_file
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator._remove_file

**File:** `skydiscover/evaluation/container_evaluator.py:274`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _remove_file(self, path: str) -> None:
        """Remove a file inside the container."""
        subprocess.run(
            ["docker", "exec", self.container_id, "rm", "-f", path],
            capture_output=True,
        )
````

## → Calls
- [[Runner.run]]
- [[TaskPool.run]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
- [[ContainerizedEvaluator._run_container]]
