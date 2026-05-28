---
name: container_evaluator.ContainerizedEvaluator
description: class in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# container_evaluator.ContainerizedEvaluator

**File:** `skydiscover/evaluation/container_evaluator.py:20`  
**Kind:** class  
**Layer:** #evaluation

## Source
````python
class ContainerizedEvaluator:
    """Evaluates programs by running them inside a persistent Docker container.

    The benchmark directory must contain:
      - Dockerfile
      - evaluate.sh  (called as: evaluate.sh <solution_path> <mode>)

    Any data files or other resources needed by evaluate.sh, such as a
    requirements.txt or data files, are the benchmark's own concern — the
    framework imposes no structure on them.

    evaluate.sh receives two arguments:
      1. ``<solution_path>`` — absolute path to the candidate program inside
         the container (e.g. ``/tmp/candidate_abc123.py``).
      2. ``<mode>`` — either ``"train"`` or ``"test"``.

         - **train**: called during the optimization loop in the process
           of iterating towards a single solution. This may be called multiple
           times per program, thus should be relatively fast.
         - **test**: called at publish time (e.g. end-of-run best program).
           Should be the authoritative, full evaluation, which will be used
           for reporting and leaderboard ranking.

         Evaluators that don't need the distinction can ignore the mode.

    evaluate.sh writes a single JSON object to stdout::

        {
          "status": "success" | "error" | "timeout",
          "combined_score": <float>,
          "metrics": {<str>: <float>},
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[HarborEvaluator._exec]]
- [[HarborEvaluator._init_container]]
- [[HarborEvaluator._read_reward]]
- [[HarborEvaluator._run_container]]
- [[evaluation.create_evaluator]]
- [[harbor_evaluator.HarborEvaluator]]
