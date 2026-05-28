---
name: ParadigmGenerator._build_current_program_analysis
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_current_program_analysis

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:253`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_current_program_analysis(self, best_score: float) -> str:
        """Build the current program analysis directive."""
        return f"""**CRITICAL: ANALYZE THE CURRENT PROGRAM FIRST**
Before suggesting new ideas, carefully analyze the Current Program above:
- What algorithm/approach does it use? (This is what's WORKING - {self._score_label()} {best_score:.6f})
- What are its strengths? (Why does it achieve this {self._score_label()}?)
- What are its weaknesses? (What limits further improvement?)
- How can you improve it? (How to beat it?)

**IMPORTANT:** The program above is the CURRENT program that needs to be improved. Start by understanding what works, then suggest breakthrough ideas that build on or improve it."""
````

## → Calls
- [[ParadigmGenerator._score_label]]

## ← Called by
- [[ParadigmGenerator._build_prompt]]
