---
name: cli._configure_logging
description: function in skydiscover/cli.py (cli)
metadata:
  type: project
---

# cli._configure_logging

**File:** `skydiscover/cli.py:284`  
**Kind:** function  
**Layer:** #cli

## Source
````python
def _configure_logging(level_name: Optional[str]) -> None:
    """Set up the root logger with the SkyDiscover console format."""
    from skydiscover.search.utils.logging_utils import _ConsoleFilter, _ConsoleFormatter

    log_level = getattr(logging, level_name) if level_name else logging.WARNING
    root = logging.getLogger()
    root.setLevel(log_level)
    if not root.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(_ConsoleFormatter())
        handler.addFilter(_ConsoleFilter())
        root.addHandler(handler)
    logging.getLogger("skydiscover").setLevel(logging.INFO)
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
- [[cli.main_async]]
