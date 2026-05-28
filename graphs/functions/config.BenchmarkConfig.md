---
name: config.BenchmarkConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.BenchmarkConfig

**File:** `skydiscover/config.py:561`  
**Kind:** class  
**Layer:** #config

## Source
````python
class BenchmarkConfig:
    """Configuration for loading problems from external benchmark datasets.

    When enabled, allows SkyDiscover to fetch problems from external
    benchmark datasets (e.g., KernelBench, Frontier-CS) without requiring
    explicit initial_program paths.

    Benchmark specification and evaluation parameters (e.g., target problem)
    are stored in a `params` dictionary.
    """

    enabled: bool = False
    name: Optional[str] = None
    resolver: Optional[str] = (
        None  # Python import path to resolver module (e.g., 'benchmarks.kernelbench.resolver')
    )
    params: Dict[str, Any] = field(default_factory=dict)  # Benchmark-specific parameters
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[Config.from_dict]]
- [[config.Config]]
