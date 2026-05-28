---
name: GEPANativeContextBuilder._format_rejection_history
description: staticmethod in skydiscover/context_builder/gepa_native/builder.py (context-builder)
metadata:
  type: project
---

# GEPANativeContextBuilder._format_rejection_history

**File:** `skydiscover/context_builder/gepa_native/builder.py:133`  
**Kind:** staticmethod  
**Layer:** #context-builder

## Source
````python
    def _format_rejection_history(
        rejected: List[Program],
        parent_scores: Dict[str, float],
    ) -> Optional[str]:
        """
        Format recently rejected programs for reflective prompting.

        Shows what mutations were tried and rejected (didn't improve on parent),
        including their scores, error messages, changes descriptions, and code
        snippets so the LLM can avoid repeating the same mistakes.
        """
        if not rejected:
            return None

        entries: List[str] = []

        for i, prog in enumerate(rejected, 1):
            prog_score = get_score(prog.metrics) if prog.metrics else 0.0

            parent_score_str = ""
            if prog.parent_id and prog.parent_id in parent_scores:
                parent_score_str = f", parent_score: {parent_scores[prog.parent_id]:.4f}"

            error_msg = ""
            if prog.metrics:
                error_msg = prog.metrics.get("error", "")
                if not error_msg:
                    error_msg = prog.metrics.get("error_message", "")

            changes = ""
            if prog.metadata:
                changes = prog.metadata.get("changes", "")

            entry_lines = [f"#### Attempt {i} (score: {prog_score:.4f}{parent_score_str})"]
            if changes:
                entry_lines.append(f"Changes: {changes}")
            if error_msg:
                entry_lines.append(f"Error: {error_msg}")

            # Code snippet so the LLM can see what was tried
            if prog.solution:
                code_lines = prog.solution.splitlines()
                if len(code_lines) > 30:
                    snippet = "\n".join(code_lines[:30]) + "\n... (truncated)"
                else:
                    snippet = prog.solution
                entry_lines.append(f"Code tried:\n```\n{snippet}\n```")

            entries.append("\n".join(entry_lines))

        lines = [
            "### Recent Rejected Attempts",
            "The following mutations were rejected because they did not "
            "improve on the parent. Avoid repeating these approaches:",
            *entries,
        ]
        return "\n\n".join(lines)
````

## → Calls
- [[base_database.Program]]
- [[metrics.get_score]]

## ← Called by
- [[GEPANativeContextBuilder._build_search_guidance]]
