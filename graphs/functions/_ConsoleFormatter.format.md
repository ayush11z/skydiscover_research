---
name: _ConsoleFormatter.format
description: method in skydiscover/search/utils/logging_utils.py (search-utils)
metadata:
  type: project
---

# _ConsoleFormatter.format

**File:** `skydiscover/search/utils/logging_utils.py:18`  
**Kind:** method  
**Layer:** #search-utils

## Source
````python
    def format(self, record):
        ts = self.formatTime(record, "%H:%M:%S")
        name = (
            record.name[len("skydiscover.") :]
            if record.name.startswith("skydiscover.")
            else record.name
        )
        parts = name.split(".")
        short = f"search.{parts[1]}" if parts[0] == "search" and len(parts) >= 3 else parts[-1]
        fmt = (
            f"{ts} {record.levelname} [{short}] "
            if record.levelno >= logging.WARNING
            else f"{ts} [{short}] "
        )
        return fmt + record.getMessage()
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[BenchmarkConfig.name]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMModelConfig.name]]
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

## ← Called by
- [[AdaEvolveContextBuilder._format_previous_attempts]]
- [[DefaultContextBuilder._format_previous_attempts]]
- [[DefaultContextBuilder.build_prompt]]
- [[EvoxContextBuilder.build_prompt]]
