---
name: DefaultContextBuilder.build_prompt
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder.build_prompt

**File:** `skydiscover/context_builder/default/builder.py:69`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def build_prompt(
        self,
        current_program: Union[Program, Dict[str, Program]],
        context: Dict[str, Any] = None,
        **kwargs: Any,
    ) -> Dict[str, str]:
        """
        Build a prompt dict with "system" and "user" keys.

        Args:
            current_program: Program or {info: Program} to evolve from.
            context: optional dict with program_metrics, other_context_programs,
                previous_programs, etc.

        Returns:
            {"system": str, "user": str} ready for LLM.generate().
        """
        context = context or {}

        # EXPERIENCES: information needed from the database
        program_metrics = context.get("program_metrics", {})
        other_context_programs = context.get("other_context_programs", {})
        previous_programs = context.get("previous_programs", [])

        # Information needed from the config
        language = self.config.language or "python"
        diff_based_generation = self.config.diff_based_generation

        # Format experiences
        metrics_str = self._format_metrics(program_metrics)
        previous_attempts_section = self._format_previous_attempts(previous_programs)
        other_context_section = self._format_other_context_programs(
            other_context_programs, language
        )
        current_program_section = self._format_current_program(current_program, language)
        has_current_program = bool(current_program_section)

        if isinstance(current_program, dict) and current_program:
            actual_program = list(current_program.values())[0]
            current_solution = prog_attr(actual_program, "solution")
        else:
            current_solution = prog_attr(current_program, "solution")

        improvement_areas = self._identify_improvement_areas(
            current_solution, program_metrics, previous_programs
        )

        if context.get("errors"):
            other_context_section += self._format_failed_attempts(context["errors"], language)

        evaluator_timeout = getattr(self.config.evaluator, "timeout", None)
        timeout_warning = (
            f"- Time limit: Programs should complete execution within {evaluator_timeout} seconds; otherwise, they will timeout."
            if evaluator_timeout
            else ""
        )

        user_template_key = self._select_template_key(
            language, diff_based_generation, has_current_program
        )
        user_template = self.template_manager.get_template(user_template_key)

        user_message = user_template.format(
            current_program=current_program_section,
            metrics=metrics_str,
            previous_attempts=previous_attempts_section,
            other_context_programs=other_context_section,
            improvement_areas=improvement_areas,
            language=language,
            timeout_warning=timeout_warning,
            **kwargs,
        )

        return {"system": self._get_system_message(), "user": user_message}
````

## → Calls
- [[DefaultContextBuilder._format_current_program]]
- [[DefaultContextBuilder._format_failed_attempts]]
- [[DefaultContextBuilder._format_metrics]]
- [[DefaultContextBuilder._format_other_context_programs]]
- [[DefaultContextBuilder._format_previous_attempts]]
- [[DefaultContextBuilder._get_system_message]]
- [[DefaultContextBuilder._identify_improvement_areas]]
- [[DefaultContextBuilder._select_template_key]]
- [[DiscoveryControllerInput.config]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[TemplateManager.get_template]]
- [[UnifiedArchive.get]]
- [[_ConsoleFormatter.format]]
- [[base.ContextBuilder]]
- [[base_database.Program]]
- [[utils.prog_attr]]

## ← Called by
- [[AdaEvolveContextBuilder.build_prompt]]
- [[DiscoveryController._build_prompt]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[GEPANativeContextBuilder.build_prompt]]
