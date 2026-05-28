---
name: ContainerizedEvaluator._start_container
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator._start_container

**File:** `skydiscover/evaluation/container_evaluator.py:305`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _start_container(self) -> str:
        """Start a persistent container and return its ID."""
        # Build docker run command with environment variables
        cmd = ["docker", "run", "-d", "--rm"]
        for key, value in self.env_vars.items():
            cmd.extend(["-e", f"{key}={value}"])
        cmd.extend(["--entrypoint", "sleep", self.image_tag, "infinity"])

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
````

## → Calls
- [[ContainerizedEvaluator._build_image]]
- [[Runner.run]]
- [[TaskPool.run]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
- [[ContainerizedEvaluator.__init__]]
