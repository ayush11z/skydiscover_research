---
name: HarborEvaluator._exec
description: method in skydiscover/evaluation/harbor_evaluator.py (evaluation)
metadata:
  type: project
---

# HarborEvaluator._exec

**File:** `skydiscover/evaluation/harbor_evaluator.py:355`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _exec(self, cmd: str) -> subprocess.CompletedProcess:
        """Run a shell command inside the container."""
        return subprocess.run(
            ["docker", "exec", self.container_id, "/bin/sh", "-c", cmd],
            capture_output=True,
            text=True,
        )
````

## → Calls
- [[Runner.run]]
- [[TaskPool.run]]
- [[container_evaluator.ContainerizedEvaluator]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
- [[HarborEvaluator._init_container]]
- [[HarborEvaluator._run_container]]
