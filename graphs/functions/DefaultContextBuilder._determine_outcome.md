---
name: DefaultContextBuilder._determine_outcome
description: staticmethod in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder._determine_outcome

**File:** `skydiscover/context_builder/default/builder.py:429`  
**Kind:** staticmethod  
**Layer:** #context-builder

## Source
````python
    def _determine_outcome(program_metrics: Dict[str, Any], parent_metrics: Dict[str, Any]) -> str:
        """Compare combined_score to parent: 'Improvement', 'Regression', or 'No change'."""
        prog_value = program_metrics.get("combined_score")
        parent_value = parent_metrics.get("combined_score", 0)
        if isinstance(prog_value, (int, float)) and isinstance(parent_value, (int, float)):
            if prog_value > parent_value:
                return "Improvement in combined_score"
            elif prog_value < parent_value:
                return "Regression in combined_score"
        return "No change in combined_score"
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[AdaEvolveContextBuilder._determine_outcome]]
- [[DefaultContextBuilder._format_previous_attempts]]
