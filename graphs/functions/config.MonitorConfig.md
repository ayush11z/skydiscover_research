---
name: config.MonitorConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.MonitorConfig

**File:** `skydiscover/config.py:539`  
**Kind:** class  
**Layer:** #config

## Source
````python
class MonitorConfig:
    """Configuration for the live run monitor dashboard"""

    enabled: bool = False
    port: int = 8765
    host: str = "127.0.0.1"
    max_solution_length: int = 10000

    # AI summary settings
    summary_model: str = "gpt-5-mini"
    summary_api_key: Optional[str] = None  # Falls back to OPENAI_API_KEY
    summary_api_base: str = _PROVIDERS["openai"][0]
    summary_top_k: int = 3
    summary_interval: int = 0  # Auto-generate every N programs (0 = manual)
````

## → Calls
- [[config._PROVIDERS]]

## ← Called by
- [[Config.from_dict]]
- [[Config.to_dict]]
- [[config.Config]]
