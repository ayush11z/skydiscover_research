---
name: logging_utils.setup_search_logging
description: function in skydiscover/search/utils/logging_utils.py (search-utils)
metadata:
  type: project
---

# logging_utils.setup_search_logging

**File:** `skydiscover/search/utils/logging_utils.py:46`  
**Kind:** function  
**Layer:** #search-utils

## Source
````python
def setup_search_logging(log_level: str, log_dir: str, name: str) -> None:
    """Configure root logger with a timestamped file handler and a console handler."""
    os.makedirs(log_dir, exist_ok=True)
    root = logging.getLogger()
    root.setLevel(getattr(logging, log_level))

    log_file = os.path.join(log_dir, f"{name}_{time.strftime('%Y%m%d_%H%M%S')}.log")
    fh = logging.FileHandler(log_file)
    fh.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    root.addHandler(fh)

    if not any(
        isinstance(h, logging.StreamHandler) and not isinstance(h, logging.FileHandler)
        for h in root.handlers
    ):
        ch = logging.StreamHandler()
        ch.setFormatter(_ConsoleFormatter())
        ch.addFilter(_ConsoleFilter())
        root.addHandler(ch)

    logging.getLogger(__name__).info(f"Logging to {log_file}")
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[logging_utils._ConsoleFilter]]
- [[logging_utils._ConsoleFormatter]]

## ← Called by
- [[Runner._setup_logging]]
