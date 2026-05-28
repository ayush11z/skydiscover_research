---
name: HarborEvaluator._extract_path_from_instruction
description: method in skydiscover/evaluation/harbor_evaluator.py (evaluation)
metadata:
  type: project
---

# HarborEvaluator._extract_path_from_instruction

**File:** `skydiscover/evaluation/harbor_evaluator.py:332`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _extract_path_from_instruction(self) -> str:
        """Extract the solution file path from ``instruction.md``."""
        instruction_path = os.path.join(self.task_dir, "instruction.md")
        if not os.path.exists(instruction_path):
            return ""

        try:
            with open(instruction_path) as f:
                text = f.read()
        except Exception:
            return ""

        patterns = [
            r'[`"\'](/\S+\.(?:py|sh|js|ts|cpp|c|rs|go|java))[`"\']',
            r"(?:in|at|to|into)\s+(/\S+\.(?:py|sh|js|ts|cpp|c|rs|go|java))",
        ]
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(1)

        return ""
````

## → Calls
- [[Config.search]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[HarborEvaluator._extract_solution_path]]
