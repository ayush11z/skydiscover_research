---
name: LLMJudge.evaluate
description: method in skydiscover/evaluation/llm_judge.py (evaluation)
metadata:
  type: project
---

# LLMJudge.evaluate

**File:** `skydiscover/evaluation/llm_judge.py:36`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    async def evaluate(
        self, program_solution: str, program_id: str = ""
    ) -> Optional[EvaluationResult]:
        """Score a program via LLM. Returns None on failure."""
        try:
            tm = self.context_builder.template_manager
            eval_sys = self.context_builder.config.evaluator_system_message
            system_msg = tm.get_template(eval_sys) if eval_sys in tm.templates else eval_sys
            user_msg = tm.get_template("evaluator_user_message").format(
                current_program=program_solution
            )

            llm_responses = await self.llm_pool.generate_all(
                system_msg, [{"role": "user", "content": user_msg}]
            )
            response_texts = [r.text for r in llm_responses]

            if self.database and program_id:
                self.database.log_prompt(
                    program_id=program_id,
                    template_key="evaluator_user_message",
                    prompt={"system": system_msg, "user": user_msg},
                    responses=response_texts,
                )

            metrics: Dict[str, float] = {}
            artifacts: Dict[str, Any] = {}
            for i, response in enumerate(response_texts):
                parsed = self._parse_response(response)
                weight = self.llm_pool.weights[i] if self.llm_pool.weights else 1.0
                for key, value in parsed.items():
                    if isinstance(value, (int, float)):
                        metrics[key] = metrics.get(key, 0.0) + float(value) * weight
                    else:
                        artifacts[key] = value

            return EvaluationResult(metrics=metrics, artifacts=artifacts)
        except Exception as e:
            logger.warning(f"LLM judge failed: {e}")
            return None
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[DiscoveryControllerInput.config]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMJudge._parse_response]]
- [[LLMPool.__init__]]
- [[LLMPool.generate_all]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[ProgramDatabase.log_prompt]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[TemplateManager.get_template]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[evaluation_result.EvaluationResult]]

## ← Called by
- [[Evaluator.evaluate_program]]
