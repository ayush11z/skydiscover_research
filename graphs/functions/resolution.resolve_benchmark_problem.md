---
name: resolution.resolve_benchmark_problem
description: function in skydiscover/benchmarks/resolution.py (other)
metadata:
  type: project
---

# resolution.resolve_benchmark_problem

**File:** `skydiscover/benchmarks/resolution.py:21`  
**Kind:** function  
**Layer:** #other

## Source
````python
def resolve_benchmark_problem(benchmark_config: Any) -> BenchmarkResolution:
    """Load benchmark problem from external dataset using the configured resolver."""
    resolver_path = getattr(benchmark_config, "resolver", None)
    if not resolver_path:
        raise ValueError("BenchmarkConfig.resolver must be set to use benchmark loading")

    cwd = os.getcwd()
    if cwd not in sys.path:
        sys.path.insert(0, cwd)

    resolver_module = importlib.import_module(resolver_path)
    resolver = resolver_module.resolver

    benchmark_name = getattr(benchmark_config, "name", None) or "benchmark"
    output_dir = Path(tempfile.mkdtemp(prefix=f"skydiscover_{benchmark_name}_"))

    params = getattr(benchmark_config, "params", {})
    return resolver.resolve(config=params, output_dir=output_dir)
````

## → Calls
- [[BenchmarkConfig.resolver]]
- [[BenchmarkResolver.resolve]]
- [[resolution.BenchmarkResolution]]

## ← Called by
- [[api._run_discovery_async]]
- [[cli.main_async]]
