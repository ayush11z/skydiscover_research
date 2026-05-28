---
name: MonitorServer._build_summary_prompt
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._build_summary_prompt

**File:** `skydiscover/extras/monitor/server.py:947`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def _build_summary_prompt(self, top_programs: List[Dict[str, Any]]) -> Dict[str, str]:
        """Build the system + user prompt for the summary LLM call."""
        system = (
            "You are an expert analyst monitoring a solution discovery process. "
            "You will be given run statistics, evolution progress data, and the source code "
            "of the top-performing programs from the current run.\n\n"
            "Respond using EXACTLY this markdown structure:\n\n"
            "## Status\n"
            "One sentence: is the search improving, stagnating, or plateauing? "
            "Cite the score trend numbers.\n\n"
            "## Key Techniques\n"
            "Bullet list of the main algorithmic ideas found in the top programs' code. "
            "Be specific — name the techniques (e.g. 'Kalman filter with adaptive Q', "
            "'hexagonal lattice packing', 'exponential moving average').\n\n"
            "## Diversity\n"
            "Are the top programs converging on one approach or exploring different strategies? "
            "One sentence.\n\n"
            "## Recommendation\n"
            "One specific, actionable suggestion grounded in the code. "
            "For example: **try wavelet denoising** — the top programs all use simple "
            "moving averages which limits frequency response.\n\n"
            "Rules:\n"
            "- Use markdown: **bold** for key terms, `- ` for bullets, `##` for sections\n"
            "- Be concise — max 250 words total\n"
            "- Every claim must reference what you see in the actual code"
        )

        # Build user message with stats + solution discovery analysis + top-k programs
        parts = []
        if self._stats:
            parts.append(
                f"Run: {self._config_summary}\n"
                f"Total programs: {self._stats.get('total_programs', len(self._programs))}\n"
                f"Current iteration: {self._stats.get('current_iteration', '?')}\n"
                f"Best score: {self._stats.get('best_score', '?')}\n"
                f"Programs/min: {self._stats.get('programs_per_min', '?')}\n"
                f"Elapsed: {self._stats.get('elapsed_seconds', '?')}s\n"
                f"Iterations since improvement: {self._stats.get('iterations_since_improvement', '?')}"
            )

        # Add solution discovery analysis
        solution_discovery_analysis = self._compute_solution_discovery_analysis()
        if solution_discovery_analysis:
            parts.append(f"\n{solution_discovery_analysis}")

        for i, p in enumerate(top_programs, 1):
            pid = p.get("id", "?")
            code = self._program_solutions.get(pid, p.get("solution_snippet", ""))
            # Truncate code to keep prompt reasonable
            if len(code) > 2000:
                code = code[:2000] + "\n... (truncated)"
            island_str = f", island={p.get('island')}" if p.get("island") is not None else ""
            parts.append(
                f"\n--- Top Program #{i} ---\n"
                f"ID: {pid}\n"
                f"Score: {p.get('score', '?')}\n"
                f"Iteration: {p.get('iteration', '?')}{island_str}\n"
                f"Metrics: {json.dumps(p.get('metrics', {}))}\n"
                f"Code:\n{code}"
            )

        return {"system": system, "user": "\n".join(parts)}
````

## → Calls
- [[LangFuseTracer.get]]
- [[MonitorServer.__init__]]
- [[MonitorServer._compute_solution_discovery_analysis]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[MonitorServer._trigger_summary]]
