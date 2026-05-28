---
name: Program.from_dict
description: classmethod in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# Program.from_dict

**File:** `skydiscover/search/base_database.py:59`  
**Kind:** classmethod  
**Layer:** #database

## Source
````python
    def from_dict(cls, data: Dict[str, Any]) -> Program:
        """Create from dictionary representation"""
        # Get the valid field names for the Program dataclass
        valid_fields = {f.name for f in fields(cls)}

        # Filter the data to only include valid fields
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}

        # Log if we're filtering out any fields
        if len(filtered_data) != len(data):
            filtered_out = set(data.keys()) - set(filtered_data.keys())
            logger.debug(f"Filtered out unsupported fields when loading Program: {filtered_out}")

        return cls(**filtered_data)
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
- [[BeamSearchDatabase.load]]
- [[CheckpointManager.load]]
- [[GEPANativeController._acceptance_gate]]
- [[GEPANativeDatabase.load]]
