---
name: base.BenchmarkResolver
description: class in skydiscover/benchmarks/base.py (other)
metadata:
  type: project
---

# base.BenchmarkResolver

**File:** `skydiscover/benchmarks/base.py:15`  
**Kind:** class  
**Layer:** #other

## Source
````python
class BenchmarkResolver(ABC):
    """Base class for benchmark-specific problem resolvers.

    Resolvers are responsible for:
    1. Fetching problem specifications from external sources
    2. Generating initial_program files with appropriate structure
    3. Configuring evaluators (via environment variables or generated files)

    Example usage:
        resolver = KernelBenchResolver()
        initial_program, evaluator = resolver.resolve(
            config={'level': 1, 'problem_id': 3},
            output_dir=Path('/tmp/skydiscover_kernelbench_123')
        )
    """

    @abstractmethod
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
_(entry point — nothing in this graph calls it)_
