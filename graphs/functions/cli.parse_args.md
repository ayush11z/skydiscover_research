---
name: cli.parse_args
description: function in skydiscover/cli.py (cli)
metadata:
  type: project
---

# cli.parse_args

**File:** `skydiscover/cli.py:38`  
**Kind:** function  
**Layer:** #cli

## Source
````python
def parse_args() -> argparse.Namespace:
    """Build and parse the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="SkyDiscover - AI-Driven Scientific and Algorithmic Discovery",
    )

    parser.add_argument(
        "initial_program",
        nargs="?",
        default=None,
        help="Path to the initial program file (can be optional)",
    )
    parser.add_argument(
        "evaluation_file",
        help=(
            "Evaluator: path to a Python file (must define evaluate()) "
            "or a benchmark directory containing Dockerfile + evaluate.sh"
        ),
    )
    parser.add_argument("--config", "-c", help="Path to configuration file (YAML)", default=None)
    parser.add_argument("--output", "-o", help="Output directory for results", default=None)
    parser.add_argument(
        "--iterations", "-i", type=int, default=None, help="Maximum number of iterations"
    )
    parser.add_argument(
        "--log-level",
        "-l",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default=None,
        help="Logging level",
    )
    parser.add_argument(
        "--checkpoint",
        default=None,
        help="Path to a checkpoint directory to resume from",
    )
    parser.add_argument("--api-base", default=None, help="Base URL for the LLM API")
    parser.add_argument(
        "--agentic",
        action="store_true",
        default=False,
        help="Enable agentic mode (codebase root derived from initial program location)",
    )
    parser.add_argument(
        "--model",
        "-m",
        default=None,
        help="LLM model(s) for solution generation, comma-separated (e.g. 'gpt-5', 'gpt-5,gemini/gemini-3-pro')",
    )
    parser.add_argument(
        "--search",
        "-s",
        choices=_SEARCH_CHOICES,
        default=None,
        help="Search algorithm to use",
    )

    return parser.parse_args()
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[cli.main_async]]
- [[variation_operator_generator.main]]
- [[viewer.main]]
