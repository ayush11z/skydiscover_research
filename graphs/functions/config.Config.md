---
name: config.Config
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.Config

**File:** `skydiscover/config.py:586`  
**Kind:** class  
**Layer:** #config

## Source
````python
class Config:
    """Master configuration for SkyDiscover"""

    # General settings
    max_iterations: int = 100
    checkpoint_interval: int = 10
    log_level: str = "INFO"
    log_dir: Optional[str] = None
    language: Optional[str] = None
    file_suffix: str = ".py"

    # Component configurations
    llm: LLMConfig = field(default_factory=LLMConfig)
    context_builder: ContextBuilderConfig = field(default_factory=ContextBuilderConfig)
    search: SearchConfig = field(default_factory=SearchConfig)
    evaluator: EvaluatorConfig = field(default_factory=EvaluatorConfig)
    agentic: AgenticConfig = field(default_factory=AgenticConfig)
    benchmark: BenchmarkConfig = field(default_factory=BenchmarkConfig)

    # Live monitor dashboard
    monitor: MonitorConfig = field(default_factory=MonitorConfig)

    # Human feedback settings
    human_feedback_enabled: bool = False
    human_feedback_file: Optional[str] = None
    human_feedback_mode: str = "append"  # "append" or "replace"

    # Generation settings
    diff_based_generation: bool = True
    max_solution_length: int = 60000

````

## → Calls
- [[config.AgenticConfig]]
- [[config.BenchmarkConfig]]
- [[config.ContextBuilderConfig]]
- [[config.EvaluatorConfig]]
- [[config.LLMConfig]]
- [[config.MonitorConfig]]
- [[config.SearchConfig]]

## ← Called by
- [[AdaEvolveContextBuilder.__init__]]
- [[ContextBuilder.__init__]]
- [[DefaultContextBuilder.__init__]]
- [[EvoxContextBuilder.__init__]]
- [[GEPANativeContextBuilder.__init__]]
- [[Runner.__init__]]
- [[api._run_discovery_async]]
- [[api.run_discovery]]
- [[config.apply_overrides]]
- [[config.bridge_provider_env]]
- [[config.load_config]]
- [[default_discovery_controller.DiscoveryControllerInput]]
- [[gepa_backend._build_gepa_config]]
- [[gepa_backend._ensure_litellm_api_key]]
- [[gepa_backend.run]]
- [[openevolve_backend._map_config]]
- [[openevolve_backend.run]]
- [[registry.get_program]]
- [[shinkaevolve_backend._map_config]]
- [[shinkaevolve_backend.run]]
