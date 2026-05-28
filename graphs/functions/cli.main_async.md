---
name: cli.main_async
description: function in skydiscover/cli.py (cli)
metadata:
  type: project
---

# cli.main_async

**File:** `skydiscover/cli.py:103`  
**Kind:** function  
**Layer:** #cli

## Source
````python
async def main_async() -> int:
    """Async entry point for the CLI. Returns exit code."""
    args = parse_args()
    _configure_logging(args.log_level)

    if args.initial_program and not os.path.exists(args.initial_program):
        print(f"Error: Initial program file '{args.initial_program}' not found", file=sys.stderr)
        return 1
    if not os.path.exists(args.evaluation_file):
        print(f"Error: Evaluation file '{args.evaluation_file}' not found", file=sys.stderr)
        return 1

    has_overrides = any((args.api_base, args.model, args.agentic, args.search))
    config = None
    evaluator_env_vars: Optional[dict[str, str]] = None

    # Load the configuration
    if args.config or has_overrides:
        config = load_config(args.config)

        evaluator_env_vars = None

        try:
            apply_overrides(
                config,
                model=args.model,
                api_base=args.api_base,
                agentic=args.agentic,
                search=args.search,
            )
        except ValueError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1

        # Resolve benchmark problem if configured and no initial_program provided
        if args.initial_program is None and config.benchmark and config.benchmark.enabled:
            try:
                resolution = resolve_benchmark_problem(config.benchmark)
                args.initial_program = resolution.initial_program_path
                args.evaluation_file = resolution.evaluator_path
                evaluator_env_vars = resolution.evaluator_env_vars
                print(
                    f"[Benchmark Loader] Benchmark: {config.benchmark.name}, Initial program: {args.initial_program}, Evaluator: {args.evaluation_file}"
                )
            except Exception as exc:
                print(f"Error: Failed to load benchmark problem: {exc}", file=sys.stderr)
                traceback.print_exc()
                return 1

        if args.model:
            print("Active models:")
            for i, m in enumerate(config.llm.models):
                provider, *_ = _parse_model_spec(m.name)
                print(f"  {i + 1}. {m.name} (provider: {provider}, weight: {m.weight})")
        if args.api_base:
            print(f"Using API base: {config.llm.api_base}")
        if args.agentic:
            if not config.agentic.codebase_root and args.initial_program:
                config.agentic.codebase_root = os.path.dirname(
                    os.path.abspath(args.initial_program)
                )
            print(f"Agentic mode enabled (codebase: {config.agentic.codebase_root})")
        if args.search:
            print(f"Using search algorithm: {args.search}")

    # Run the discovery
    try:
        search_type = config.search.type if config and hasattr(config, "search") else None

        if search_type:
            from skydiscover.extras.external import (
                KNOWN_EXTERNAL,
                get_package_name,
                get_runner,
                is_external,
            )

            # External backends (openevolve, shinkaevolve, gepa)
            if is_external(search_type):
                if evaluator_env_vars:
                    env_var_names = ", ".join(sorted(evaluator_env_vars))
                    print(
                        "Error: Passing evaluator environment variables to external backends "
                        "is not yet supported. "
                        f"External backend '{search_type}' cannot be used with evaluator env vars: "
                        f"{env_var_names}",
                        file=sys.stderr,
                    )
                    return 1

                from skydiscover.config import build_output_dir

                output_dir = args.output or build_output_dir(
                    search_type, args.initial_program or "scratch"
                )
                os.makedirs(output_dir, exist_ok=True)

                from skydiscover.extras.monitor import start_monitor, stop_monitor

                # Start monitor for external backends as well
                monitor_server, monitor_callback, feedback_reader = start_monitor(
                    config, output_dir
                )
                try:
                    result = await get_runner(search_type)(
                        program_path=args.initial_program,
                        evaluator_path=args.evaluation_file,
                        config_obj=config,
                        iterations=args.iterations or config.max_iterations,
                        output_dir=output_dir,
                        monitor_callback=monitor_callback,
                        feedback_reader=feedback_reader,
                    )
                except ModuleNotFoundError as exc:
                    pkg = get_package_name(search_type)
                    print(f"Error: {exc}", file=sys.stderr)
                    print(f"\nThe '{search_type}' backend requires its package.", file=sys.stderr)
                    print(f"Install with:  pip install {pkg}", file=sys.stderr)
                    return 1
                finally:
                    stop_monitor(monitor_server)

                print(f"\nDiscovery complete! Best score: {result.best_score:.4f}")
                return 0

            if search_type in KNOWN_EXTERNAL:
                pkg = get_package_name(search_type)
                print(
                    f"Error: Search type '{search_type}' requires the '{pkg}' package. "
                    f"Install with: pip install {pkg}",
                    file=sys.stderr,
                )
                return 1

        # Initialize the runner
        runner = Runner(
            initial_program_path=args.initial_program,
            evaluation_file=args.evaluation_file,
            config=config,
            config_path=args.config if config is None else None,
            output_dir=args.output,
            evaluator_env_vars=evaluator_env_vars,
        )

        # Load the checkpoint if provided
        if args.checkpoint:
            if not os.path.exists(args.checkpoint):
                print(f"Error: Checkpoint directory '{args.checkpoint}' not found", file=sys.stderr)
                return 1
            print(f"Will resume from checkpoint: {args.checkpoint}")

        # Run the discovery
        best_program = await runner.run(
            iterations=args.iterations,
            checkpoint_path=args.checkpoint,
        )

        checkpoint_dir = os.path.join(runner.output_dir, "checkpoints")
        latest_checkpoint = _find_latest_checkpoint(checkpoint_dir)

        print("\nDiscovery complete!")
        if best_program is None:
            print("No valid programs were found.")
        else:
            print("Best program metrics:")
            for name, value in best_program.metrics.items():
                formatted = f"{value:.4f}" if isinstance(value, (int, float)) else str(value)
                print(f"  {name}: {formatted}")

        if latest_checkpoint:
            print(f"\nLatest checkpoint: {latest_checkpoint}")
            print(f"To resume: --checkpoint {latest_checkpoint}")

        return 0

    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        traceback.print_exc()
        return 1
````

## → Calls
- [[BenchmarkResolution.evaluator_env_vars]]
- [[BenchmarkResolution.evaluator_path]]
- [[BenchmarkResolution.initial_program_path]]
- [[Config.agentic]]
- [[Config.benchmark]]
- [[Config.llm]]
- [[Config.log_level]]
- [[Config.max_iterations]]
- [[Config.search]]
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.evaluation_file]]
- [[DiscoveryControllerInput.evaluator_env_vars]]
- [[DiscoveryControllerInput.output_dir]]
- [[DiscoveryResult.output_dir]]
- [[EvaluatorConfig.evaluation_file]]
- [[EvoxDatabaseConfig.evaluation_file]]
- [[LLMModelConfig.api_base]]
- [[Runner.run]]
- [[SearchConfig.output_dir]]
- [[cli._configure_logging]]
- [[cli._find_latest_checkpoint]]
- [[cli.parse_args]]
- [[config._parse_model_spec]]
- [[config.apply_overrides]]
- [[config.build_output_dir]]
- [[config.load_config]]
- [[external.KNOWN_EXTERNAL]]
- [[external.get_package_name]]
- [[external.get_runner]]
- [[external.is_external]]
- [[monitor.start_monitor]]
- [[monitor.stop_monitor]]
- [[resolution.resolve_benchmark_problem]]
- [[runner.Runner]]

## ← Called by
- [[cli.main]]
