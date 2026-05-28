---
name: IN-DiscoveryController._save_solution_prompt
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._save_solution_prompt

**File:** `skydiscover/search/default_discovery_controller.py:165`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    def _save_solution_prompt(self, system_message: str, user_message: str, iteration: int) -> None:
        run_name = os.path.basename(self.output_dir) if self.output_dir else "default"
        self._solution_prompt_counter += 1
        prompt_dir = Path(f"outputs/prompt_logs/{run_name}/solution_llm")
        prompt_dir.mkdir(parents=True, exist_ok=True)
        prompt_file = prompt_dir / f"prompt_call_{self._solution_prompt_counter:03d}_iter{iteration}.txt"
        user_msg_str = user_message if isinstance(user_message, str) else str(user_message)
        with open(prompt_file, "w") as f:
            f.write("--- SYSTEM ---\n")
            f.write(system_message)
            f.write("\n\n--- USER ---\n")
            f.write(user_msg_str)
````

## → Calls
- [[IN-DiscoveryControllerInput.output_dir]]

## ← Called by
- [[IN-DiscoveryController._run_from_scratch_iteration]]
- [[IN-DiscoveryController._run_iteration]]
