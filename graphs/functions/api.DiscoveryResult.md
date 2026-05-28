---
name: api.DiscoveryResult
description: class in skydiscover/api.py (api)
metadata:
  type: project
---

# api.DiscoveryResult

**File:** `skydiscover/api.py:43`  
**Kind:** class  
**Layer:** #api

## Source
````python
class DiscoveryResult:
    """Result of a single discovery run."""

    best_program: Optional[Program]
    best_score: float
    best_solution: str
    metrics: Dict[str, Any]
    output_dir: Optional[str]
    initial_score: Optional[float] = None

````

## → Calls
- [[base_database.Program]]

## ← Called by
- [[api._run_discovery_async]]
- [[api.discover_solution]]
- [[api.run_discovery]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
