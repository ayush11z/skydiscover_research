---
name: DefaultContextBuilder._format_failed_attempts
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder._format_failed_attempts

**File:** `skydiscover/context_builder/default/builder.py:343`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _format_failed_attempts(self, errors: list, language: str) -> str:
        """Format failed retry attempts for the prompt."""
        lines = ["\n## ❌ Previous Failed Attempts (this retry):\n"]
        lines.append("The following attempts failed. Avoid these errors:\n\n")
        for attempt in errors:
            err_msg = attempt.get("metadata", {}).get("error", "Unknown error")
            attempt_num = attempt.get("metadata", {}).get("attempt_number", "?")
            lines.append(f"### Attempt {attempt_num}:\n")
            lines.append(f"**Error:** {err_msg}\n")

            failed_solution = attempt.get("solution", "")
            llm_response = attempt.get("llm_response", "")

            if "SEARCH" in err_msg and llm_response:
                if len(llm_response) > 1500:
                    llm_response = llm_response[:1500] + "\n... (truncated)"
                lines.append(f"**Your response that failed:**\n```\n{llm_response}\n```\n\n")
            elif failed_solution:
                if len(failed_solution) > 1500:
                    failed_solution = failed_solution[:1500] + "\n... (truncated)"
                lines.append(
                    f"**Generated solution that failed:**\n```{language}\n{failed_solution}\n```\n"
                )

                traceback_str = attempt.get("metadata", {}).get("traceback", "")
                if traceback_str:
                    if len(traceback_str) > 800:
                        traceback_str = "... (truncated)\n" + traceback_str[-800:]
                    lines.append(f"**Traceback:**\n```\n{traceback_str}\n```\n\n")
                else:
                    lines.append("\n")
        return "".join(lines)
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[DefaultContextBuilder.build_prompt]]
