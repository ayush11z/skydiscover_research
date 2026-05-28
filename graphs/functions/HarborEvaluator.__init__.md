---
name: HarborEvaluator.__init__
description: method in skydiscover/evaluation/harbor_evaluator.py (evaluation)
metadata:
  type: project
---

# HarborEvaluator.__init__

**File:** `skydiscover/evaluation/harbor_evaluator.py:51`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def __init__(self, benchmark_dir, config, max_concurrent=4, env_vars=None):
        self.task_dir = os.path.abspath(benchmark_dir)
        self.solution_path = self._extract_solution_path()
        self._tests_uploaded = False
        self._apply_task_toml_timeout(config)
        super().__init__(benchmark_dir, config, max_concurrent, env_vars=env_vars)
        self._init_container()
````

## → Calls
- [[ContainerizedEvaluator.__init__]]
- [[HarborEvaluator._apply_task_toml_timeout]]
- [[HarborEvaluator._extract_solution_path]]
- [[HarborEvaluator._init_container]]

## ← Called by
_(entry point — nothing in this graph calls it)_
