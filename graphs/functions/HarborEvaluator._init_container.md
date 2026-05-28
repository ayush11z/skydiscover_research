---
name: HarborEvaluator._init_container
description: method in skydiscover/evaluation/harbor_evaluator.py (evaluation)
metadata:
  type: project
---

# HarborEvaluator._init_container

**File:** `skydiscover/evaluation/harbor_evaluator.py:170`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _init_container(self):
        """Create log directories and upload test files into the container."""
        self._exec("mkdir -p /logs/verifier /logs/agent /logs/artifacts")

        # Upload the tests/ directory.
        tests_dir = os.path.join(self.task_dir, "tests")
        if os.path.isdir(tests_dir):
            self._exec("rm -rf /tests")
            subprocess.run(
                ["docker", "cp", tests_dir, f"{self.container_id}:/tests"],
                capture_output=True,
                check=True,
            )
            self._tests_uploaded = True
            logger.debug("Uploaded tests/ to container")
        else:
            raise RuntimeError(f"No tests/ directory found in {self.task_dir}")
````

## → Calls
- [[HarborEvaluator._exec]]
- [[Runner.run]]
- [[TaskPool.run]]
- [[container_evaluator.ContainerizedEvaluator]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
- [[HarborEvaluator.__init__]]
