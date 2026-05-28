---
name: HarborEvaluator._apply_task_toml_timeout
description: method in skydiscover/evaluation/harbor_evaluator.py (evaluation)
metadata:
  type: project
---

# HarborEvaluator._apply_task_toml_timeout

**File:** `skydiscover/evaluation/harbor_evaluator.py:155`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _apply_task_toml_timeout(self, config) -> None:
        """Read verifier.timeout_sec from task.toml and apply it to config."""
        toml_path = os.path.join(self.task_dir, "task.toml")
        if not os.path.exists(toml_path):
            return
        try:
            with open(toml_path) as f:
                text = f.read()
            match = re.search(r"timeout_sec\s*=\s*(\d+)", text)
            if match:
                config.timeout = int(match.group(1))
                logger.info(f"Harbor task.toml: set evaluator timeout to {config.timeout}s")
        except Exception as e:
            logger.warning(f"Failed to read task.toml: {e}")
````

## → Calls
- [[Config.search]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[EvaluatorConfig.timeout]]
- [[LLMModelConfig.timeout]]

## ← Called by
- [[HarborEvaluator.__init__]]
