---
name: MonitorServer.__init__
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer.__init__

**File:** `skydiscover/extras/monitor/server.py:96`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def __init__(self, host: str = "127.0.0.1", port: int = 8765, max_solution_length: int = 10000):
        self.host = host
        self.port = port
        self.max_solution_length = max_solution_length

        self._queue: queue.Queue = queue.Queue()

        # In-memory state for reconnecting clients
        self._programs: List[Dict[str, Any]] = []
        self._program_solutions: Dict[str, str] = {}
        self._parent_solutions: Dict[str, str] = {}
        self._best_program_id: Optional[str] = None
        self._best_score: float = -float("inf")
        self._stats: Dict[str, Any] = {}
        self._config_summary: str = ""

        # Per-program summary cache
        self._program_summary_cache: Dict[str, str] = {}

        # Human feedback reader (set via set_feedback_reader)
        self._feedback_reader: Optional[Any] = None

        # AI summary state
        self._summary_model: str = ""
        self._summary_api_key: str = ""
        self._summary_api_base: str = "https://api.openai.com/v1"
        self._summary_top_k: int = 3
        self._summary_interval: int = 0  # 0 = manual only
        self._summary_text: str = ""
        self._summary_generating: bool = False
        self._summary_last_program_count: int = 0
        self._summary_executor: Optional[ThreadPoolExecutor] = None

        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._thread: Optional[threading.Thread] = None
        self._clients: Set[asyncio.StreamWriter] = set()
        self._stop_event = threading.Event()
        self._ready_event = threading.Event()  # set when TCP port is bound
        self._dashboard_html: Optional[bytes] = None
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveController._ensure_all_islands_seeded]]
- [[AdaEvolveController._execute_generation]]
- [[AdaEvolveController._generate_child]]
- [[AdaEvolveController._process_result]]
- [[AdaEvolveController._run_normal_step]]
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._migrate_archives]]
- [[AdaEvolveDatabase._migrate_legacy]]
- [[AdaEvolveDatabase._seed_new_island]]
- [[AdaEvolveDatabase._spawn_island]]
- [[AdaEvolveDatabase.seed_all_islands]]
- [[AdaptiveState.from_dict]]
- [[ClaudeCodeController.run_discovery]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[Config.from_dict]]
- [[ContainerizedEvaluator._parse_output]]
- [[ContainerizedEvaluator._run_single_in_container]]
- [[ContainerizedEvaluator.evaluate_program]]
- [[DiscoveryController._call_llm]]
- [[DiscoveryController._create_child_program]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
- [[EvaluationResult.from_dict]]
- [[Evaluator._cascade_evaluate]]
- [[Evaluator._normalize_result]]
- [[Evaluator.evaluate_program]]
- [[GEPANativeController._attempt_merge]]
- [[HarborEvaluator._read_reward]]
- [[HarborEvaluator._run_container]]
- [[LLMJudge.evaluate]]
- [[MonitorServer._build_summary_prompt]]
- [[MonitorServer._cancel_all_tasks]]
- [[MonitorServer._compute_solution_discovery_analysis]]
- [[MonitorServer._consume_queue]]
- [[MonitorServer._generate_program_summary]]
- [[MonitorServer._get_top_k_programs]]
- [[MonitorServer._handle_client_msg]]
- [[MonitorServer.stop]]
- [[MultiDimensionalAdapter.add_dimension]]
- [[MultiDimensionalAdapter.from_dict]]
- [[OpenAILLM._generate_with_image]]
- [[OpenAILLM.generate]]
- [[OpenEvolveNativeDatabase._migrate_programs]]
- [[OpenEvolveNativeDatabase._seed_empty_island]]
- [[ParadigmTracker.from_dict]]
- [[Program.from_dict]]
- [[Runner.run]]
- [[UnifiedArchive.__init__]]
- [[_ConsoleFormatter.format]]
- [[_make_gepa_evaluator.gepa_evaluator]]
- [[api._run_discovery_async]]
- [[cli._configure_logging]]
- [[config.apply_overrides]]
- [[config.load_config]]
- [[gepa_backend.run]]
- [[logging_utils.setup_search_logging]]
- [[monitor.start_monitor]]
- [[openevolve_backend._to_skydiscover_program]]
- [[openevolve_backend.run]]
- [[registry.setup_search]]
- [[search_strategy_evaluator.evaluate]]
- [[shinkaevolve_backend._to_skydiscover_program]]
- [[shinkaevolve_backend.run]]
- [[variation_operator_generator.main]]
- [[viewer.main]]
