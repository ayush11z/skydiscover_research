---
name: Config.to_dict
description: method in skydiscover/config.py (config)
metadata:
  type: project
---

# Config.to_dict

**File:** `skydiscover/config.py:734`  
**Kind:** method  
**Layer:** #config

## Source
````python
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to a dictionary"""
        return {
            # General settings
            "max_iterations": self.max_iterations,
            "checkpoint_interval": self.checkpoint_interval,
            "log_level": self.log_level,
            "log_dir": self.log_dir,
            # Component configurations
            "llm": {
                "models": self.llm.models,
                "evaluator_models": self.llm.evaluator_models,
                "api_base": self.llm.api_base,
                "temperature": self.llm.temperature,
                "top_p": self.llm.top_p,
                "max_tokens": self.llm.max_tokens,
                "timeout": self.llm.timeout,
                "retries": self.llm.retries,
                "retry_delay": self.llm.retry_delay,
            },
            "prompt": {
                "template": self.context_builder.template,
                "template_dir": self.context_builder.template_dir,
                "system_message": self.context_builder.system_message,
                "evaluator_system_message": self.context_builder.evaluator_system_message,
            },
            "search": {
                "type": self.search.type,
                "num_context_programs": self.search.num_context_programs,
                "database": {
                    f.name: getattr(self.search.database, f.name)
                    for f in fields(self.search.database)
                },
            },
            "evaluator": {
                "evaluation_file": self.evaluator.evaluation_file,
                "file_suffix": self.evaluator.file_suffix,
                "is_image_mode": self.evaluator.is_image_mode,
                "timeout": self.evaluator.timeout,
                "max_retries": self.evaluator.max_retries,
                "cascade_evaluation": self.evaluator.cascade_evaluation,
                "cascade_thresholds": self.evaluator.cascade_thresholds,
                "inject_evaluator_context": self.evaluator.inject_evaluator_context,
                "llm_as_judge": self.evaluator.llm_as_judge,
            },
            # Agentic generation
            "agentic": {
                "enabled": self.agentic.enabled,
                "codebase_root": self.agentic.codebase_root,
                "max_steps": self.agentic.max_steps,
                "per_step_timeout": self.agentic.per_step_timeout,
                "overall_timeout": self.agentic.overall_timeout,
                "max_context_chars": self.agentic.max_context_chars,
                "max_file_chars": self.agentic.max_file_chars,
                "max_search_results": self.agentic.max_search_results,
                "max_files_read": self.agentic.max_files_read,
                "regex_timeout": self.agentic.regex_timeout,
                "max_regex_length": self.agentic.max_regex_length,
                "repo_map_max_depth": self.agentic.repo_map_max_depth,
                "allowed_extensions": list(self.agentic.allowed_extensions),
                "excluded_dirs": list(self.agentic.excluded_dirs),
            },
            # Live monitor
            "monitor": {
                "enabled": self.monitor.enabled,
                "port": self.monitor.port,
                "host": self.monitor.host,
                "max_solution_length": self.monitor.max_solution_length,
                "summary_model": self.monitor.summary_model,
                "summary_top_k": self.monitor.summary_top_k,
                "summary_interval": self.monitor.summary_interval,
            },
            # Human-in-the-loop
            "human_feedback_enabled": self.human_feedback_enabled,
            "human_feedback_file": self.human_feedback_file,
            # Generation settings
            "diff_based_generation": self.diff_based_generation,
            "max_solution_length": self.max_solution_length,
            # Parallelism
            "max_parallel_iterations": self.max_parallel_iterations,
        }
````

## → Calls
- [[BenchmarkConfig.name]]
- [[LLMConfig.api_base]]
- [[LLMModelConfig.name]]
- [[config.AgenticConfig]]
- [[config.ContextBuilderConfig]]
- [[config.EvaluatorConfig]]
- [[config.LLMConfig]]
- [[config.LLMModelConfig]]
- [[config.MonitorConfig]]
- [[config.SearchConfig]]

## ← Called by
- [[AdaEvolveDatabase.save]]
- [[CheckpointManager._save_program]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[Config.to_yaml]]
- [[DiscoveryController._run_iteration]]
- [[GEPANativeDatabase.save]]
- [[MultiDimensionalAdapter.to_dict]]
- [[coevolve_logging.make_json_serializable]]
