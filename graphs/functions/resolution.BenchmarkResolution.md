---
name: resolution.BenchmarkResolution
description: class in skydiscover/benchmarks/resolution.py (other)
metadata:
  type: project
---

# resolution.BenchmarkResolution

**File:** `skydiscover/benchmarks/resolution.py:13`  
**Kind:** class  
**Layer:** #other

## Source
````python
class BenchmarkResolution:
    """Resolved benchmark assets and evaluator-scoped configuration."""

    initial_program_path: str
    evaluator_path: str
    evaluator_env_vars: Dict[str, str] = field(default_factory=dict)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[BenchmarkResolver.resolve]]
- [[resolution.resolve_benchmark_problem]]
