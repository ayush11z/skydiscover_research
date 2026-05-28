---
name: MonitorServer.configure_summary
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer.configure_summary

**File:** `skydiscover/extras/monitor/server.py:179`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def configure_summary(
        self,
        model: str = "gpt-5-mini",
        api_key: str = "",
        api_base: str = "https://api.openai.com/v1",
        top_k: int = 3,
        interval: int = 0,
    ) -> None:
        """Configure the AI summary generator.

        Args:
            model: OpenAI model name (default gpt-5-mini).
            api_key: API key. Falls back to OPENAI_API_KEY env var.
            api_base: API base URL.
            top_k: Number of top programs to include in summary prompt.
            interval: Auto-generate every N new programs (0 = manual only).
        """
        self._summary_model = model
        self._summary_api_key = api_key or os.environ.get("OPENAI_API_KEY", "")
        self._summary_api_base = api_base
        self._summary_top_k = top_k
        self._summary_interval = interval
        self._summary_executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="summary")
        logger.info(
            f"AI summary configured: model={model}, top_k={top_k}, "
            f"interval={interval or 'manual'}, api_key={'set' if self._summary_api_key else 'MISSING'}"
        )
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[Runner._setup_monitor_summary]]
- [[monitor.start_monitor]]
- [[viewer.main]]
