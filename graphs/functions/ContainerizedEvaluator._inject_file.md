---
name: ContainerizedEvaluator._inject_file
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator._inject_file

**File:** `skydiscover/evaluation/container_evaluator.py:262`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _inject_file(self, content: str, suffix: str) -> str:
        """Write content to a unique temp file inside the container via stdin."""
        path = f"/tmp/{uuid.uuid4().hex}{suffix}"
        inject = subprocess.run(
            ["docker", "exec", "-i", self.container_id, "tee", path],
            input=content.encode(),
            capture_output=True,
        )
        if inject.returncode != 0:
            raise RuntimeError(f"Failed to inject file into container: {inject.stderr.decode()}")
        return path
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
