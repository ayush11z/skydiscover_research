---
name: ContainerizedEvaluator._build_image
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator._build_image

**File:** `skydiscover/evaluation/container_evaluator.py:321`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _build_image(self) -> str:
        norm = os.path.normpath(self.benchmark_dir)
        name = os.path.basename(norm)
        # Include parent dir to avoid tag collisions when multiple benchmarks
        # share the same leaf directory name (e.g. "evaluator").
        parent = os.path.basename(os.path.dirname(norm))
        if parent and name == "evaluator":
            name = f"{parent}-{name}"
        tag = f"skydiscover-{name}:latest"

        logger.info(f"Building Docker image: {tag} (from {self.benchmark_dir})")
        result = subprocess.run(
            ["docker", "build", "-t", tag, self.benchmark_dir],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(f"Docker build failed for {self.benchmark_dir}:\n{result.stderr}")
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
- [[ContainerizedEvaluator.__init__]]
- [[ContainerizedEvaluator._start_container]]
