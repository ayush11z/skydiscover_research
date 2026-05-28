---
name: config.SearchConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.SearchConfig

**File:** `skydiscover/config.py:518`  
**Kind:** class  
**Layer:** #config

## Source
````python
class SearchConfig:
    """General Configuration for All Search Algorithms"""

    type: str = "topk"
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    num_context_programs: int = 4
    output_dir: Optional[str] = None
    switch_interval: Optional[int] = (
        None  # EvoX: stagnation iters before strategy switch. Auto-calculated if None.
    )
    share_llm: bool = (
        False  # EvoX: if True, meta-level search evolution uses the same LLM as the main discovery process.
    )
````

## → Calls
- [[config.DatabaseConfig]]

## ← Called by
- [[Config.from_dict]]
- [[Config.to_dict]]
- [[config.Config]]
- [[config.apply_overrides]]
