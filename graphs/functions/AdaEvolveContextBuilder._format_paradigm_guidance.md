---
name: AdaEvolveContextBuilder._format_paradigm_guidance
description: staticmethod in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._format_paradigm_guidance

**File:** `skydiscover/context_builder/adaevolve/builder.py:311`  
**Kind:** staticmethod  
**Layer:** #context-builder

## Source
````python
    def _format_paradigm_guidance(paradigm: Dict[str, Any], language: str) -> str:
        """
        Format paradigm breakthrough guidance for the LLM.

        Uses different framing for prompt optimization vs code optimization.
        """
        is_prompt_opt = (language or "").lower() in ("text", "prompt")

        idea = paradigm.get("idea", "N/A")
        description = paradigm.get("description", "N/A")
        target = paradigm.get("what_to_optimize", "score")
        cautions = paradigm.get("cautions", "N/A")
        approach_type = paradigm.get("approach_type", "N/A")

        if is_prompt_opt:
            header = "## BREAKTHROUGH STRATEGY - APPLY THIS"
            intro = "The search has stagnated globally. You MUST apply this breakthrough prompt strategy:"
            fields = (
                f"**STRATEGY:** {idea}\n\n"
                f"**HOW TO APPLY:**\n{description}\n\n"
                f"**TARGET:** {target}\n\n"
                f"**CAUTIONS:** {cautions}\n\n"
                f"**APPROACH TYPE:** {approach_type}"
            )
            critical_bullets = (
                "- You MUST rewrite the prompt using this strategy\n"
                "- The strategy must be reflected in the actual prompt structure and content\n"
                "- Keep the prompt clear and well-structured\n"
                "- Do not add unnecessary verbosity — every sentence should serve a purpose\n"
                "- Ensure the prompt still addresses the core task"
            )
        else:
            header = "## BREAKTHROUGH IDEA - IMPLEMENT THIS"
            intro = "The search has stagnated globally. You MUST implement this breakthrough idea:"
            fields = (
                f"**IDEA:** {idea}\n\n"
                f"**HOW TO IMPLEMENT:**\n{description}\n\n"
                f"**TARGET METRIC:** {target}\n\n"
                f"**CAUTIONS:** {cautions}\n\n"
                f"**APPROACH TYPE:** {approach_type}"
            )
            critical_bullets = (
                "- You MUST implement the breakthrough idea\n"
                "- Ensure the paradigm is actually used in your implementation (not just mentioned in comments)\n"
                "- Correctness is essential - your implementation must be correct and functional\n"
                "- Verify output format matches evaluator requirements\n"
                "- Make purposeful changes that implement the idea\n"
                "- Test your implementation logic carefully"
            )

        return f"{header}\n\n{intro}\n\n{fields}\n\n**CRITICAL:**\n{critical_bullets}"
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[AdaEvolveContextBuilder._build_search_guidance]]
