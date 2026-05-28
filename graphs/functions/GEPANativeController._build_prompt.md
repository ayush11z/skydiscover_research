---
name: GEPANativeController._build_prompt
description: method in skydiscover/search/gepa_native/controller.py (gepa)
metadata:
  type: project
---

# GEPANativeController._build_prompt

**File:** `skydiscover/search/gepa_native/controller.py:189`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def _build_prompt(
        self,
        current_program: Dict[str, Program],
        context_programs: Union[List, Dict[str, list]],
        failed_attempts: list,
    ) -> Dict[str, str]:
        """Build prompt with GEPA reflective context.

        Gathers rejection history from the database and passes it through
        the context dict so GEPANativeContextBuilder can format it into
        the {search_guidance} template placeholder.
        """
        parent = (
            list(current_program.values())[0]
            if isinstance(current_program, dict)
            else current_program
        )
        db_stats = self._prompt_context.get("db_stats") or self.database.get_statistics()

        # Gather rejection history for reflective prompting
        rejected = self.database.get_rejection_history(limit=self.max_recent_failures)

        # Pre-compute parent scores for rejected programs
        rejection_parent_scores: Dict[str, float] = {}
        for prog in rejected:
            if prog.parent_id and prog.parent_id in self.database.programs:
                p = self.database.programs[prog.parent_id]
                rejection_parent_scores[prog.parent_id] = get_score(p.metrics)

        context: Dict[str, Any] = {
            "program_metrics": parent.metrics,
            "other_context_programs": context_programs,
            "previous_programs": db_stats.get("previous_programs", []),
            "db_stats": db_stats,
            # GEPA-specific keys (consumed by GEPANativeContextBuilder)
            "rejection_history": rejected,
            "rejection_parent_scores": rejection_parent_scores,
        }
        for k, v in self._prompt_context.items():
            if k not in context:
                context[k] = v

        if failed_attempts:
            context["errors"] = failed_attempts

        return self.context_builder.build_prompt(current_program=current_program, context=context)
````

## → Calls
- [[DiscoveryControllerInput.database]]
- [[GEPANativeContextBuilder.build_prompt]]
- [[GEPANativeController.__init__]]
- [[Program.parent_id]]
- [[SearchConfig.database]]
- [[SerializableResult.parent_id]]
- [[base_database.Program]]
- [[default_discovery_controller.DiscoveryController]]
- [[metrics.get_score]]

## ← Called by
_(entry point — nothing in this graph calls it)_
