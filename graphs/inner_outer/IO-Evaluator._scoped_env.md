---
name: IO-Evaluator._scoped_env
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator._scoped_env

**File:** `skydiscover/evaluation/evaluator.py:217`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _scoped_env(self):
        if not self.env_vars:
            yield
            return

        with _EVALUATOR_ENV_LOCK:
            old_values = {k: os.environ.get(k) for k in self.env_vars}
            try:
                os.environ.update(self.env_vars)
                yield
            finally:
                for key, old_value in old_values.items():
                    if old_value is None:
                        os.environ.pop(key, None)
                    else:
                        os.environ[key] = old_value
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-Evaluator._call_with_env]]
