---
name: variation_operator_generator.main
description: function in skydiscover/search/evox/utils/variation_operator_generator.py (evox)
metadata:
  type: project
---

# variation_operator_generator.main

**File:** `skydiscover/search/evox/utils/variation_operator_generator.py:521`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def main():
    parser = argparse.ArgumentParser(
        description="Generate problem-specific variation operators (e.g. structural variation operator and local refinement operator)"
    )
    parser.add_argument(
        "problem_dir",
        type=str,
        help="Path to the problem directory containing config.yaml and evaluator.py",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file path (e.g. variation_operators.txt)",
    )
    parser.add_argument(
        "--provide-initial",
        action="store_true",
        default=False,
        help="Include initial_program.py as additional context for variation operator generation",
    )
    args = parser.parse_args()

    # Build paths
    config_path = os.path.join(args.problem_dir, "config.yaml")
    evaluator_path = os.path.join(args.problem_dir, "evaluator.py")

    # Validate
    if not os.path.exists(config_path):
        print(f"Error: Config file not found: {config_path}")
        return 1
    if not os.path.exists(evaluator_path):
        print(f"Error: Evaluator file not found: {evaluator_path}")
        return 1

    # Load config and evaluator
    print(f"Loading config from: {config_path}")
    config_content = load_config(config_path)
    system_message = config_content.get("prompt", {}).get("system_message", "")

    print(f"Loading evaluator from: {evaluator_path}")
    evaluator_code = load_evaluator(evaluator_path)

    # Optionally load initial program
    initial_program_solution = None
    if args.provide_initial:
        initial_program_path = os.path.join(args.problem_dir, "initial_program.py")
        if os.path.exists(initial_program_path):
            print(f"Loading initial program from: {initial_program_path}")
            initial_program_solution = load_initial_program(initial_program_path)
        else:
            print(f"Warning: --provide-initial set but {initial_program_path} not found, skipping")

    # Build LLMPool for CLI usage
    from skydiscover.config import LLMModelConfig
    from skydiscover.llm.llm_pool import LLMPool

    model_cfg = LLMModelConfig(
        name=DEFAULT_CLI_MODEL,
        api_base=os.environ.get("OPENAI_API_BASE") or os.environ.get("OPENAI_BASE_URL") or "https://api.openai.com/v1",
        api_key=os.environ.get("OPENAI_API_KEY", ""),
        max_tokens=DEFAULT_CLI_MAX_TOKENS,
        timeout=DEFAULT_CLI_TIMEOUT,
        retries=3,
        retry_delay=5,
    )
    llm = LLMPool([model_cfg])

    # Generate variation operator labels
    print(f"Generating variation operators with model={DEFAULT_CLI_MODEL}...")
    diverge_operator, refine_operator = asyncio.run(
        generate_variation_operators(
            system_message=system_message,
            evaluator_code=evaluator_code,
            problem_dir=args.problem_dir,
            initial_program_solution=initial_program_solution,
            llm_pool=llm,
        )
    )

    # Output
    output_text = f"### STRUCTURAL VARIATION OPERATOR \n{diverge_operator}\n\n### LOCAL REFINEMENT OPERATOR \n{refine_operator}"
    if args.output:
        with open(args.output, "w") as f:
            f.write(output_text)
        print(f"Saved variation operators to: {args.output}")
    else:
        print("\n" + "=" * 80)
        print(output_text)
        print("=" * 80)

    return 0
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LangFuseTracer.get]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[ProgramDatabase.get]]
- [[Runner.__init__]]
- [[Runner.run]]
- [[TaskPool.__init__]]
- [[TaskPool.run]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive.get]]
- [[_FinalResult.__init__]]
- [[cli.parse_args]]
- [[config.LLMModelConfig]]
- [[gepa_backend.run]]
- [[llm_pool.LLMPool]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[variation_operator_generator.generate_variation_operators]]
- [[variation_operator_generator.load_config]]
- [[variation_operator_generator.load_evaluator]]
- [[variation_operator_generator.load_initial_program]]
- [[wrapper.run]]

## ← Called by
_(entry point — nothing in this graph calls it)_
