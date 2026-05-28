---
name: IO-EvoxContextBuilder._save_guide_prompt
description: method in skydiscover/context_builder/evox/builder.py (context-builder)
metadata:
  type: project
---

# EvoxContextBuilder._save_guide_prompt

**File:** `skydiscover/context_builder/evox/builder.py:93`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _save_guide_prompt(self, system_message: str, user_message: str) -> None:
        _guide_dir = Path("outputs/prompt_logs") / os.environ.get("SKYDISCOVER_RUN_NAME", "unknown_run") / "guide_llm"
        _guide_dir.mkdir(parents=True, exist_ok=True)
        _call_num = len(list(_guide_dir.glob("prompt_call_*.txt"))) + 1
        with open(_guide_dir / f"prompt_call_{_call_num:03d}.txt", "w") as _f:
            _f.write("--- SYSTEM ---\n")
            _f.write(system_message or "")
            _f.write("\n\n--- USER ---\n")
            _f.write(user_message or "")
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-EvoxContextBuilder._generate_batch_summaries_async]]
- [[IO-EvoxContextBuilder._generate_problem_context_summary_async]]
- [[IO-EvoxContextBuilder._generate_stats_insight_async]]
