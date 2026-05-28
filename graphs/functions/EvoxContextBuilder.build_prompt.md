---
name: EvoxContextBuilder.build_prompt
description: method in skydiscover/context_builder/evox/builder.py (context-builder)
metadata:
  type: project
---

# EvoxContextBuilder.build_prompt

**File:** `skydiscover/context_builder/evox/builder.py:151`  
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
        """Build prompt for search algorithm discovery.

        Args:
            current_program: Program or {label: Program} to evolve from.
            context: optional dict with program_metrics, other_context_programs,
                previous_programs, db_stats, search_stats, etc.

        Returns:
            {"system": str, "user": str} ready for LLM.generate().
        """
        context = context or {}

        program_metrics = context.get("program_metrics", {})
        other_context_programs = context.get("other_context_programs", {})
        previous_programs = context.get("previous_programs", [])
        language = self.config.language or "python"

        user_template_key = self.user_template_override or "search_evolution_user_message"
        user_template = self.template_manager.get_template(user_template_key)
        system_message = self._get_system_message()

        search_window_context = fmt.format_search_window_context(context)

        db_stats = context.get("db_stats", {})

        actual_program = (
            list(current_program.values())[0]
            if isinstance(current_program, dict) and current_program
            else current_program
        )
        horizon = 0
        if actual_program:
            metrics = prog_attr(actual_program, "metrics", {})
            horizon = int(metrics.get("search_window_horizon") or 0)

        if horizon > 0 and db_stats:
            db_stats = fmt.filter_db_stats_by_horizon(db_stats, horizon)

        search_stats = context.get("search_stats") or {}

        stats_insight_data = None
        population_state = ""
        if self.use_llm_stats_insight and db_stats:
            stats_text = fmt.format_population_state(db_stats)
            if stats_text:
                stats_insight_data = stats_text
        else:
            population_state = fmt.format_population_state(db_stats) if db_stats else ""

        problem_description = fmt.format_problem_description(
            search_stats.get("problem_description")
        )
        evaluator_context = fmt.format_evaluator_context(search_stats.get("evaluator_context"))

        problem_context_data = self.template_manager.get_template("problem_template").format(
            problem_description=problem_description,
            evaluator_context=evaluator_context,
        )

        all_programs_data = fmt.prepare_search_algorithms_data(other_context_programs)
        batch_summary_data = None
        if all_programs_data:
            per_program_tpl = self._batch_sections["PER_PROGRAM"]
            combined_content_parts = []
            for prog in all_programs_data:
                part = (
                    f"=== PROGRAM {prog['program_num']} (score={prog['combined_score']:.4f}, improvement={prog['improvement']:.4f}) ===\n"
                    + per_program_tpl.format(
                        task_description=self.relevant_task_description_message,
                        solution=prog["solution"],
                        db_stats_text=prog["db_stats_text"],
                    )
                )
                combined_content_parts.append(part)
            batch_summary_data = self._batch_sections["INSTRUCTIONS"].format(
                num_programs=len(all_programs_data),
                combined_content="\n".join(combined_content_parts),
            )

        async def gather_llm_calls():
            tasks = []

            if stats_insight_data:
                tasks.append(
                    ("stats_insight", self._generate_stats_insight_async(stats_insight_data))
                )

            has_meaningful_data = (
                problem_description
                and problem_description.strip()
                and evaluator_context
                and evaluator_context.strip()
                and not (
                    problem_description.startswith("(No ") and evaluator_context.startswith("(No ")
                )
            )
            if has_meaningful_data:
                tasks.append(
                    (
                        "problem_context",
                        self._generate_problem_context_summary_async(
                            problem_description, evaluator_context
                        ),
                    )
                )

            if batch_summary_data:
                tasks.append(
                    ("batch_summaries", self._generate_batch_summaries_async(batch_summary_data))
                )

            if not tasks:
                return {}

            results = await asyncio.gather(*[task for _, task in tasks], return_exceptions=True)

            result_dict = {}
            for (name, _), result in zip(tasks, results):
                if isinstance(result, Exception):
                    result_dict[name] = ""
                else:
                    result_dict[name] = result

            return result_dict

        llm_results = run_async_safely(gather_llm_calls())

        if self.use_llm_stats_insight:
            population_state = llm_results.get("stats_insight", population_state)

        problem_context_summary = llm_results.get("problem_context", "")
        problem_template = (
            problem_context_summary.strip()
            if problem_context_summary
            else (problem_context_data or "")
        )

        summaries_by_num = fmt.parse_batch_summaries(
            llm_results.get("batch_summaries", ""), all_programs_data
        )

        simplification_threshold = self.context_config.suggest_simplification_after_chars
        improvement_areas = fmt.identify_search_improvement_areas(
            actual_program, program_metrics, previous_programs, simplification_threshold
        )
        other_context_program_section = fmt.format_search_algorithms(
            other_context_programs, language, summaries_by_num=summaries_by_num
        )

        current_program_section = fmt.format_current_program(
            current_program,
            language,
            improvement_areas=improvement_areas,
        )

        user_message = user_template.format(
            current_program=current_program_section,
            other_context_programs=other_context_program_section,
            language=language,
            search_window_context=search_window_context,
            population_state=population_state,
            problem_template=problem_template,
            **kwargs,
        )

        return {
            "system": system_message,
            "user": user_message,
        }
````

## → Calls
- [[Config.context_builder]]
- [[DefaultContextBuilder._get_system_message]]
- [[DiscoveryControllerInput.config]]
- [[EvoxContextBuilder._parse_template_sections]]
- [[LangFuseTracer.get]]
- [[ParadigmGenerator._get_system_message]]
- [[ProgramDatabase.get]]
- [[TemplateManager.get_template]]
- [[UnifiedArchive.get]]
- [[_ConsoleFormatter.format]]
- [[base.ContextBuilder]]
- [[base_database.Program]]
- [[build_prompt.gather_llm_calls]]
- [[builder.DefaultContextBuilder]]
- [[builder.run_async_safely]]
- [[formatters.filter_db_stats_by_horizon]]
- [[formatters.format_current_program]]
- [[formatters.format_evaluator_context]]
- [[formatters.format_population_state]]
- [[formatters.format_problem_description]]
- [[formatters.format_search_algorithms]]
- [[formatters.format_search_window_context]]
- [[formatters.identify_search_improvement_areas]]
- [[formatters.parse_batch_summaries]]
- [[formatters.prepare_search_algorithms_data]]
- [[utils.prog_attr]]

## ← Called by
_(entry point — nothing in this graph calls it)_
