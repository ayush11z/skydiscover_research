---
name: wrapper.run
description: function in skydiscover/evaluation/wrapper.py (evaluation)
metadata:
  type: project
---

# wrapper.run

**File:** `skydiscover/evaluation/wrapper.py:19`  
**Kind:** function  
**Layer:** #evaluation

## Source
````python
def run(evaluate_fn):
    """Call *evaluate_fn*, format the result as container-protocol JSON on stdout.

    * Reads ``sys.argv[1]`` as the program path.
    * Redirects stdout → stderr while *evaluate_fn* runs so that debug prints
      don't contaminate the JSON output.
    * Separates numeric metrics from non-numeric artifacts.
    * Guarantees ``combined_score`` is always present in metrics.
    """
    if len(sys.argv) < 2:
        print("Usage: evaluator.py <program_path>", file=sys.stderr)
        sys.exit(1)

    program_path = sys.argv[1]

    # Redirect stdout → stderr during evaluation so debug prints from
    # the evaluator don't contaminate the JSON output on stdout.
    real_stdout = sys.stdout
    sys.stdout = sys.stderr
    try:
        result = evaluate_fn(program_path)
    except Exception as e:
        sys.stdout = real_stdout
        print(
            json.dumps(
                {
                    "status": "error",
                    "combined_score": 0.0,
                    "metrics": {"combined_score": 0.0},
                    "artifacts": {
                        "error": str(e),
                        "traceback": traceback.format_exc(),
                    },
                }
            )
        )
        return
    sys.stdout = real_stdout

    if not isinstance(result, dict):
        print(
            json.dumps(
                {
                    "status": "error",
                    "combined_score": 0.0,
                    "metrics": {"combined_score": 0.0},
                    "artifacts": {
                        "error": f"evaluate() returned {type(result).__name__}, expected dict"
                    },
                }
            )
        )
        return

    # Separate numeric metrics from non-numeric artifacts.
    metrics = {}
    artifacts = {}
    for k, v in result.items():
        if isinstance(v, bool):
            metrics[k] = float(v)
        elif isinstance(v, (int, float)):
            metrics[k] = float(v)
        elif isinstance(v, str):
            artifacts[k] = v
        elif isinstance(v, (list, dict)):
            artifacts[k] = json.dumps(v)

    if "combined_score" not in metrics:
        metrics["combined_score"] = 0.0

    status = "error" if "error" in artifacts else "success"
    output = {
        "status": status,
        "combined_score": metrics["combined_score"],
        "metrics": metrics,
    }
    if artifacts:
        output["artifacts"] = artifacts

    print(json.dumps(output))
````

## → Calls
- [[SearchConfig.type]]

## ← Called by
- [[ClaudeCodeController._ensure_image_built]]
- [[ClaudeCodeController._save_evaluator_image]]
- [[ClaudeCodeController.run_discovery]]
- [[ContainerizedEvaluator._build_image]]
- [[ContainerizedEvaluator._inject_file]]
- [[ContainerizedEvaluator._remove_file]]
- [[ContainerizedEvaluator._run_single_in_container]]
- [[ContainerizedEvaluator._start_container]]
- [[ContainerizedEvaluator.close]]
- [[HarborEvaluator._build_image]]
- [[HarborEvaluator._exec]]
- [[HarborEvaluator._init_container]]
- [[HarborEvaluator._read_reward]]
- [[HarborEvaluator._run_container]]
- [[api.run_discovery]]
- [[builder.run_async_safely]]
- [[cli.main]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[variation_operator_generator.get_available_packages]]
- [[variation_operator_generator.main]]
