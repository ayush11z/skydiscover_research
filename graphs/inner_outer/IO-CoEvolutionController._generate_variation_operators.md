---
name: IO-CoEvolutionController._generate_variation_operators
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._generate_variation_operators

**File:** `skydiscover/search/evox/controller.py:295`  
**Kind:** method  
**Layer:** #outer-loop

## What it does
Called once at startup. Uses the outer LLM to generate two short text labels — `DIVERGE_LABEL` and `REFINE_LABEL` — that get attached to the database. These labels guide whether the inner-loop LLM should explore new ideas or refine existing ones.

## Source
````python
    async def _generate_variation_operators(self) -> None:
        """Generate diverge/refine labels once and assign to the current database."""
        if self._diverge_label and self._refine_label:
            self._assign_labels_to_db(self.database)
            return

        db_cfg = self.config.search.database
        if not getattr(db_cfg, "auto_generate_variation_operators", True):
            from skydiscover.search.evox.utils.template import (
                DEFAULT_DIVERGE_TEMPLATE,
                DEFAULT_REFINE_TEMPLATE,
            )

            self._diverge_label = DEFAULT_DIVERGE_TEMPLATE
            self._refine_label = DEFAULT_REFINE_TEMPLATE
            logger.info(
                "Using default variation operators (auto_generate_variation_operators=false)"
            )
            self._assign_labels_to_db(self.database)
            return

        system_message = self.config.context_builder.system_message or ""
        from skydiscover.search.utils.discovery_utils import load_evaluator_code

        evaluator_code = load_evaluator_code(self.evaluation_file)

        try:
            problem_dir = Path(self.evaluation_file).parent if self.evaluation_file else None
            label_llms = self.search_controller.guide_llms
            model_names = ", ".join(m.name for m in label_llms.models_cfg)
            logger.info(f"Label generation: using guide_model = [{model_names}]")
            self._diverge_label, self._refine_label = await generate_variation_operators(
                system_message,
                evaluator_code,
                problem_dir=problem_dir,
                llm_pool=label_llms,
            )
            logger.info(
                f"Generated variation operator labels ({len(self._diverge_label)}/{len(self._refine_label)} chars)"
            )
        except Exception as e:
            self._diverge_label = ""
            self._refine_label = ""
            logger.error(f"Label generation failed: {e}, setting labels to empty strings")

        self._assign_labels_to_db(self.database)
````

## → Calls
- [[IO-CoEvolutionController._assign_labels_to_db]]
- [[IO-DiscoveryControllerInput.config]]
- [[IO-DiscoveryControllerInput.database]]
- [[IO-DiscoveryControllerInput.evaluation_file]]
- [[IO-LLMPool.__init__]]
- [[IO-default_discovery_controller.DiscoveryController]]
- [[IO-llm_pool.LLMPool]]
- [[IO-template.DEFAULT_DIVERGE_TEMPLATE]]
- [[IO-template.DEFAULT_REFINE_TEMPLATE]]
- [[IO-variation_operator_generator.generate_variation_operators]]

## ← Called by
- [[IO-CoEvolutionController.run_discovery]]
