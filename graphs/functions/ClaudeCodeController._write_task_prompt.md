---
name: ClaudeCodeController._write_task_prompt
description: method in skydiscover/search/claude_code/controller.py (claude-code)
metadata:
  type: project
---

# ClaudeCodeController._write_task_prompt

**File:** `skydiscover/search/claude_code/controller.py:122`  
**Kind:** method  
**Layer:** #claude-code

## Source
````python
    def _write_task_prompt(self, workspace: Path, suffix: str, max_turns: int) -> str:
        """Write TASK.md and return its content for piping to the CLI."""
        system_msg = getattr(self.config.context_builder, "system_message", "") or ""
        eval_timeout = self.config.evaluator.timeout
        content = (
            "# SkyDiscover: Optimization Task\n\n"
            "You are an AI assistant iteratively improving a program to maximize "
            f"its evaluation score. You have **{max_turns} turns** total.\n\n"
            "## Current solution\n\n"
            f"`/workspace/solution{suffix}` -- read it, understand it, modify it freely.\n\n"
            "## How to evaluate\n\n"
            "```bash\n"
            f"bash /workspace/run_eval.sh /workspace/solution{suffix}\n"
            "```\n\n"
            "Output is JSON. The `combined_score` field is what you want to maximize "
            f"(higher is better). The evaluator has a **{eval_timeout}s timeout**.\n\n"
            "## Task description\n\n"
            f"{system_msg}\n\n"
            "## Instructions\n\n"
            "- Run the evaluator once to confirm the baseline score, then start improving.\n"
            "- After each change, evaluate and decide whether to keep or revert.\n"
            f"- Always keep `/workspace/solution{suffix}` set to your best solution.\n"
            "- Aim to try several distinct approaches within your turn budget.\n"
        )
        (workspace / "TASK.md").write_text(content)
        return content
````

## → Calls
- [[Config.context_builder]]
- [[Config.evaluator]]

## ← Called by
- [[ClaudeCodeController.run_discovery]]
