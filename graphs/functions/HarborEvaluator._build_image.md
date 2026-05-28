---
name: HarborEvaluator._build_image
description: method in skydiscover/evaluation/harbor_evaluator.py (evaluation)
metadata:
  type: project
---

# HarborEvaluator._build_image

**File:** `skydiscover/evaluation/harbor_evaluator.py:63`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _build_image(self) -> str:
        """Build from environment/Dockerfile."""
        name = os.path.basename(os.path.normpath(self.task_dir))
        tag = f"skydiscover-harbor-{name}:latest"
        dockerfile_dir = os.path.join(self.task_dir, "environment")

        logger.info(f"Building Harbor image: {tag} (from {dockerfile_dir})")
        result = subprocess.run(
            ["docker", "build", "-t", tag, dockerfile_dir],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(f"Docker build failed for {dockerfile_dir}:\n{result.stderr}")
        return tag
````

## → Calls
- [[Runner.run]]
- [[TaskPool.run]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
_(entry point — nothing in this graph calls it)_
