---
name: prepare.prepare_evaluator
description: function in skydiscover/utils/prepare.py (utils)
metadata:
  type: project
---

# prepare.prepare_evaluator

**File:** `skydiscover/utils/prepare.py:46`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def prepare_evaluator(
    evaluator: Union[str, Path, Callable],
    temp_dir: Optional[str],
    temp_files: List[str],
    caller_module_name: str = "skydiscover.api",
) -> str:
    """Resolve evaluator to a file path, writing a temp file if needed.

    When *evaluator* is a callable, it is registered in the caller module's
    globals so the generated wrapper script can import it at runtime.
    ``caller_module_name`` must match the module whose globals hold the callable.
    """
    if isinstance(evaluator, (str, Path)) and os.path.exists(str(evaluator)):
        return str(evaluator)

    if callable(evaluator):
        import sys

        caller_module = sys.modules.get(caller_module_name)
        evaluator_id = f"_skydiscover_evaluator_{uuid.uuid4().hex[:8]}"
        if caller_module is not None:
            setattr(caller_module, evaluator_id, evaluator)
        evaluator_code = (
            f"import {caller_module_name} as _api\n\n"
            f"def evaluate(program_path):\n"
            f"    return getattr(_api, '{evaluator_id}')(program_path)\n"
        )
    else:
        evaluator_code = str(evaluator)
        if "def evaluate" not in evaluator_code:
            raise ValueError("Evaluator code must contain a 'def evaluate(program_path)' function")

    if temp_dir is None:
        temp_dir = tempfile.gettempdir()

    eval_file = os.path.join(temp_dir, f"evaluator_{uuid.uuid4().hex[:8]}.py")
    with open(eval_file, "w") as fh:
        fh.write(evaluator_code)
    temp_files.append(eval_file)
    return eval_file
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[api._run_discovery_async]]
