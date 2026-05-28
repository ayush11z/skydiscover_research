---
name: AdaEvolveContextBuilder._format_sibling_context
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._format_sibling_context

**File:** `skydiscover/context_builder/adaevolve/builder.py:363`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _format_sibling_context(
        self, siblings: List[Program], parent_program: Program
    ) -> Optional[str]:
        """
        Format sibling context showing previous mutations of the parent.

        Shows what mutations have been tried before, whether they improved
        or regressed, so the LLM can avoid repeating failed approaches.
        """
        if not siblings:
            return None

        parent_fitness = self._get_progress_score(getattr(parent_program, "metrics", {}))
        missing = self._PROGRESS_SCORE_MISSING

        improved, regressed, unchanged = 0, 0, 0
        entries: List[str] = []

        for i, child in enumerate(siblings, 1):
            child_fitness = self._get_progress_score(getattr(child, "metrics", {}))

            if parent_fitness == missing or child_fitness == missing:
                entries.append(f"  {i}. (metrics unavailable) [UNKNOWN]")
                unchanged += 1
                continue

            delta = child_fitness - parent_fitness

            if delta > 0.001:
                status = "IMPROVED"
                improved += 1
            elif delta < -0.001:
                status = "REGRESSED"
                regressed += 1
            else:
                status = "NO CHANGE"
                unchanged += 1

            entries.append(
                f"  {i}. {parent_fitness:.4f} -> {child_fitness:.4f} " f"({delta:+.4f}) [{status}]"
            )

        lines = [
            "## PREVIOUS ATTEMPTS ON THIS PARENT",
            f"Summary: {improved} improved, {unchanged} unchanged, {regressed} regressed",
            *entries,
            "Avoid repeating approaches that didn't work.",
        ]
        return "\n".join(lines)
````

## → Calls
- [[AdaEvolveContextBuilder._get_progress_score]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveContextBuilder._build_search_guidance]]
