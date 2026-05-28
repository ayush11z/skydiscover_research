---
name: BenchmarkResolver.resolve
description: method in skydiscover/benchmarks/base.py (other)
metadata:
  type: project
---

# BenchmarkResolver.resolve

**File:** `skydiscover/benchmarks/base.py:32`  
**Kind:** method  
**Layer:** #other

## Source
````python
    def resolve(self, config: Dict[str, Any], output_dir: Path) -> BenchmarkResolution:
        """Resolve a benchmark problem to concrete file paths and evaluator config.

        Args:
            config: Benchmark configuration dictionary containing benchmark-specific
                   problem specifications and parameters.
                   The exact keys depend on the benchmark implementation.
            output_dir: Directory where generated files should be placed.

        Returns:
            BenchmarkResolution containing:
                - initial_program_path: Path to the generated initial program file
                - evaluator_path: Path to the evaluator (file or directory)
                - evaluator_env_vars: Per-run environment variables for the evaluator

        """
        pass
````

## → Calls
- [[resolution.BenchmarkResolution]]

## ← Called by
- [[resolution.resolve_benchmark_problem]]
