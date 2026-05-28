---
name: IO-Evaluator._load_evaluation_function
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator._load_evaluation_function

**File:** `skydiscover/evaluation/evaluator.py:59`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _load_evaluation_function(self) -> None:
        if not os.path.exists(self.evaluation_file):
            raise ValueError(f"Evaluation file not found: {self.evaluation_file}")

        eval_dir = os.path.dirname(os.path.abspath(self.evaluation_file))
        if eval_dir not in sys.path:
            sys.path.insert(0, eval_dir)

        self._module_name = f"_skydiscover_eval_{uuid.uuid4().hex}"
        spec = importlib.util.spec_from_file_location(self._module_name, self.evaluation_file)
        if spec is None or spec.loader is None:
            raise ImportError(f"Cannot load module from {self.evaluation_file}")

        module = importlib.util.module_from_spec(spec)
        sys.modules[self._module_name] = module
        spec.loader.exec_module(module)

        if not hasattr(module, "evaluate"):
            raise AttributeError(f"No evaluate() function in {self.evaluation_file}")

        self.evaluate_function = module.evaluate
        self._eval_module = module
        self._validate_cascade_configuration(module)
````

## → Calls
- [[IO-Evaluator._validate_cascade_configuration]]

## ← Called by
- [[IO-Evaluator.__init__]]
