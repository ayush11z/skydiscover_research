---
name: HarborEvaluator._extract_solution_path
description: method in skydiscover/evaluation/harbor_evaluator.py (evaluation)
metadata:
  type: project
---

# HarborEvaluator._extract_solution_path

**File:** `skydiscover/evaluation/harbor_evaluator.py:238`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _extract_solution_path(self) -> str:
        """Extract the expected solution file path for this Harbor task.

        Uses a three-tier strategy (most reliable first):

        1. **Parse ``solution/solve.sh``** — the authoritative reference solution
           script almost always contains a ``cat > /path/to/file`` redirect that
           reveals the exact injection path.
        2. **Parse ``instruction.md``** — look for explicit absolute paths in
           backticks or after prepositions like "in", "at", "to".
        3. **Default to ``/app/solution.py``** — the most common path across
           Harbor benchmarks (evoeval, livecodebench, usaco, etc.).
        """
        # Tier 1: parse solution/solve.sh (most reliable).
        path = self._extract_path_from_solve_sh()
        if path:
            logger.info(f"Extracted solution path from solve.sh: {path}")
            return path

        # Tier 2: parse instruction.md.
        path = self._extract_path_from_instruction()
        if path:
            logger.info(f"Extracted solution path from instruction.md: {path}")
            return path

        # Tier 3: default.
        logger.warning(f"Could not extract solution path, using default: {_DEFAULT_SOLUTION_PATH}")
        return _DEFAULT_SOLUTION_PATH
````

## → Calls
- [[HarborEvaluator._extract_path_from_instruction]]
- [[HarborEvaluator._extract_path_from_solve_sh]]

## ← Called by
- [[HarborEvaluator.__init__]]
- [[HarborEvaluator._run_container]]
