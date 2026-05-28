---
name: build_prompt.gather_llm_calls
description: function in skydiscover/context_builder/evox/builder.py (context-builder)
metadata:
  type: project
---

# build_prompt.gather_llm_calls

**File:** `skydiscover/context_builder/evox/builder.py:236`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
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
````

## → Calls
- [[EvoxContextBuilder._generate_batch_summaries_async]]
- [[EvoxContextBuilder._generate_problem_context_summary_async]]
- [[EvoxContextBuilder._generate_stats_insight_async]]
- [[TaskPool.gather]]
- [[formatters.format_evaluator_context]]
- [[formatters.format_population_state]]
- [[formatters.format_problem_description]]

## ← Called by
- [[EvoxContextBuilder.build_prompt]]
