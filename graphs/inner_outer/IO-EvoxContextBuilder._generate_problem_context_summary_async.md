---
name: IO-EvoxContextBuilder._generate_problem_context_summary_async
description: method in skydiscover/context_builder/evox/builder.py (context-builder)
metadata:
  type: project
---

# EvoxContextBuilder._generate_problem_context_summary_async

**File:** `skydiscover/context_builder/evox/builder.py:116`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    async def _generate_problem_context_summary_async(
        self, problem_description: str, evaluator_context: str
    ) -> str:
        """Generate problem context summary via LLM (cached)."""
        cache_key = hashlib.sha256(
            f"{problem_description}|||{evaluator_context}".encode("utf-8")
        ).hexdigest()

        if cache_key in self._problem_context_summary_cache:
            return self._problem_context_summary_cache[cache_key]

        problem_context_input = self.template_manager.get_template("problem_template").format(
            problem_description=problem_description,
            evaluator_context=evaluator_context,
        )

        system_msg = self.template_manager.get_template("problem_context_summary_system_message")
        self._save_guide_prompt(system_msg, problem_context_input)
        result = await self.summary_llm.generate(
            system_message=system_msg,
            messages=[{"role": "user", "content": problem_context_input}],
        )

        self._problem_context_summary_cache[cache_key] = result.text
        return result.text
````

## → Calls
- [[IO-EvoxContextBuilder._save_guide_prompt]]
- [[IO-LLMPool.generate]]
- [[IO-TemplateManager.get_template]]

## ← Called by
- [[IO-build_prompt.gather_llm_calls]]
