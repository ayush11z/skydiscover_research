---
name: EvoxContextBuilder.__init__
description: method in skydiscover/context_builder/evox/builder.py (context-builder)
metadata:
  type: project
---

# EvoxContextBuilder.__init__

**File:** `skydiscover/context_builder/evox/builder.py:42`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def __init__(
        self,
        config: Config,
        use_llm_stats_insight: bool = True,
    ):
        super().__init__(config)
        self.use_llm_stats_insight = use_llm_stats_insight
        self.template_manager = TemplateManager(_DEFAULT_TEMPLATES_DIR, _EVOX_TEMPLATES_DIR)

        summary_llm_config = config.llm.guide_models
        self.summary_llm: LLMPool = LLMPool(summary_llm_config)
        if summary_llm_config:
            logger.info(
                f"Initialized guide LLM inside EvoxContextBuilder: {summary_llm_config[0].name}"
            )

        self._problem_context_summary_cache: Dict[str, str] = {}
        self.output_dir: str = None

        evox_search_sys_prompt_path = (
            Path(__file__).parent.parent.parent
            / "search"
            / "evox"
            / "config"
            / "evox_search_sys_prompt.txt"
        )
        with open(evox_search_sys_prompt_path, "r") as f:
            self.relevant_task_description_message = f.read()

        batch_prompt = self.template_manager.get_template("batch_summary_prompt")
        self._batch_sections = self._parse_template_sections(batch_prompt)
````

## → Calls
- [[Config.llm]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[DefaultContextBuilder.__init__]]
- [[EvoxContextBuilder._parse_template_sections]]
- [[LLMPool.__init__]]
- [[TemplateManager.__init__]]
- [[TemplateManager.get_template]]
- [[config.Config]]
- [[llm_pool.LLMPool]]
- [[utils.TemplateManager]]

## ← Called by
_(entry point — nothing in this graph calls it)_
