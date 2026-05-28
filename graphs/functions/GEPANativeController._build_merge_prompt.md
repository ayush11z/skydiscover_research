---
name: GEPANativeController._build_merge_prompt
description: method in skydiscover/search/gepa_native/controller.py (gepa)
metadata:
  type: project
---

# GEPANativeController._build_merge_prompt

**File:** `skydiscover/search/gepa_native/controller.py:417`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def _build_merge_prompt(self, prog_a: Program, prog_b: Program) -> Dict[str, str]:
        """Build a prompt asking the LLM to merge two programs.

        Includes both programs' code, per-metric strengths comparison,
        and evaluator diagnostics from each program's artifacts.
        """
        score_a = get_score(prog_a.metrics)
        score_b = get_score(prog_b.metrics)

        # Summarise per-metric strengths
        strengths_a: List[str] = []
        strengths_b: List[str] = []
        if prog_a.metrics and prog_b.metrics:
            for key in set(prog_a.metrics.keys()) | set(prog_b.metrics.keys()):
                va = prog_a.metrics.get(key)
                vb = prog_b.metrics.get(key)
                if not isinstance(va, (int, float)) or not isinstance(vb, (int, float)):
                    continue
                if va > vb:
                    strengths_a.append(f"{key}: {va}")
                elif vb > va:
                    strengths_b.append(f"{key}: {vb}")

        strengths_section = ""
        if strengths_a or strengths_b:
            strengths_section = "\n## Per-Metric Strengths\n"
            if strengths_a:
                strengths_section += f"Program A leads on: {', '.join(strengths_a)}\n"
            if strengths_b:
                strengths_section += f"Program B leads on: {', '.join(strengths_b)}\n"

        # Include evaluator diagnostics from parent artifacts
        diagnostics_section = ""
        for label, prog in [("A", prog_a), ("B", prog_b)]:
            if not prog.artifacts:
                continue
            diag_parts = []
            for key, value in prog.artifacts.items():
                if not isinstance(value, str) or not value.strip():
                    continue
                display = value if len(value) <= 500 else value[:500] + "... (truncated)"
                diag_parts.append(f"- {key}: {display}")
            if diag_parts:
                diagnostics_section += (
                    f"\n## Program {label} Diagnostics\n" + "\n".join(diag_parts) + "\n"
                )

        system = (
            "You are an expert programmer. Your task is to merge two programs into "
            "a single improved program that combines the strengths of both. "
            "Output only the complete merged program inside a code block."
        )

        user = (
            f"## Program A (score: {score_a:.4f})\n"
            f"```\n{prog_a.solution}\n```\n\n"
            f"## Program B (score: {score_b:.4f})\n"
            f"```\n{prog_b.solution}\n```\n"
            f"{strengths_section}"
            f"{diagnostics_section}\n"
            "## Instructions\n"
            "Combine the best ideas from both programs into a single solution. "
            "Preserve any approach that contributes to a higher score. "
            "Resolve conflicts by choosing the strategy that is more likely to "
            "generalise across all test cases. Output the complete merged program."
        )

        return {"system": system, "user": user}
````

## → Calls
- [[EvaluationResult.metrics]]
- [[Program.metrics]]
- [[Program.solution]]
- [[base_database.Program]]
- [[metrics.get_score]]

## ← Called by
- [[GEPANativeController._attempt_merge]]
