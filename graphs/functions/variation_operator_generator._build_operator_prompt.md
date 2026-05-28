---
name: variation_operator_generator._build_operator_prompt
description: function in skydiscover/search/evox/utils/variation_operator_generator.py (evox)
metadata:
  type: project
---

# variation_operator_generator._build_operator_prompt

**File:** `skydiscover/search/evox/utils/variation_operator_generator.py:423`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def _build_operator_prompt(
    system_message: str,
    evaluator_code: str,
    problem_dir: Optional[str] = None,
    initial_program_solution: Optional[str] = None,
) -> str:
    """Build the user prompt for variation operator generation."""
    available_packages = get_available_packages(problem_dir=problem_dir)
    packages_list = "\n".join(available_packages) if available_packages else "No packages found"

    initial_program_section = ""
    if initial_program_solution:
        initial_program_section = f"""

## Initial Program (Reference Implementation)
The following is a very simple reference implementation program that will be evolved:
```python
{initial_program_solution}
```
This shows the current approach and structure. Use this to understand what exists but do not over-rely on the structure of the reference implementation."""

    context = f"""## Problem Description:
```
{system_message}
```

## Available Packages in Environment
The following packages are available in the current uv environment:
```
{packages_list}
```

## Evaluator Code:
```python
{evaluator_code}
```{initial_program_section}"""

    return f"""Please analyze this problem and generate BOTH guidance blocks.

{context}

Generate BOTH the EXPLORATION (different approaches) and EXPLOITATION (refinement/intensification) guidance blocks now.

For EXPLORATION guidance block, focus on DIFFERENT algorithmic approaches and structural changes.
For EXPLOITATION guidance block, focus on INTENSIFYING within existing approaches - e.g., computational budget (e.g., increase max iterations), better seeds, tighter tolerances, local polish stages.
"""
````

## → Calls
- [[variation_operator_generator.get_available_packages]]

## ← Called by
- [[variation_operator_generator.generate_variation_operators]]
