---
name: IO-Runner.__init__
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner.__init__

**File:** `skydiscover/runner.py:40`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def __init__(
        self,
        evaluation_file: str,
        initial_program_path: Optional[str] = None,
        config_path: Optional[str] = None,
        config: Optional[Config] = None,
        output_dir: Optional[str] = None,
        evaluator_env_vars: Optional[dict[str, str]] = None,
    ):
        self.config = config if config is not None else load_config(config_path)
        self.name = self.config.search.type
        self.output_dir = output_dir or build_output_dir(
            self.name, initial_program_path or "scratch"
        )
        os.makedirs(self.output_dir, exist_ok=True)
        os.environ["SKYDISCOVER_RUN_NAME"] = os.path.basename(self.output_dir)
        self._setup_logging()

        # Load the initial program (can be optional)
        self.initial_program_path = initial_program_path
        self.initial_program_solution = (
            self._load_initial_program() if initial_program_path else None
        )
        if self.initial_program_solution and not self.config.language:
            self.config.language = extract_solution_language(self.initial_program_solution)
        if not self.config.language:
            self.config.language = "python"

        # Set the file extension
        ext = os.path.splitext(initial_program_path)[1] if initial_program_path else ".py"
        ext = ext or ".py"
        self.file_extension = ext if ext.startswith(".") else f".{ext}"
        if self.config.file_suffix == ".py":
            self.config.file_suffix = self.file_extension

        # Create the database
        self.database = create_database(self.config.search.type, self.config.search.database)
        self.database.language = self.config.language or "python"
        self.evaluation_file = evaluation_file
        self.evaluator_env_vars = dict(evaluator_env_vars or {})

        # Initialize the discovery controller
        self.discovery_controller: Optional[DiscoveryController] = None

        logger.info(f"Runner ready: search={self.name}, program={self.initial_program_path}")
````

## → Calls
- [[IO-DiscoveryControllerInput.config]]
- [[IO-DiscoveryControllerInput.output_dir]]
- [[IO-Runner._load_initial_program]]
- [[IO-Runner._setup_logging]]
- [[IO-code_utils.extract_solution_language]]
- [[IO-default_discovery_controller.DiscoveryController]]
- [[IO-runner.Runner]]

## ← Called by
- [[IO-Runner.run]]
