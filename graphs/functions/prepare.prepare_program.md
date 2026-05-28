---
name: prepare.prepare_program
description: function in skydiscover/utils/prepare.py (utils)
metadata:
  type: project
---

# prepare.prepare_program

**File:** `skydiscover/utils/prepare.py:20`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def prepare_program(
    initial_program: Union[str, Path, List[str]],
    temp_dir: Optional[str],
    temp_files: List[str],
) -> str:
    """Resolve initial_program to a file path, writing a temp file if needed."""
    if isinstance(initial_program, (str, Path)) and os.path.exists(str(initial_program)):
        return str(initial_program)

    solution = (
        "\n".join(initial_program) if isinstance(initial_program, list) else str(initial_program)
    )

    if "EVOLVE-BLOCK-START" not in solution:
        solution = f"# EVOLVE-BLOCK-START\n{solution}\n# EVOLVE-BLOCK-END"

    if temp_dir is None:
        temp_dir = tempfile.gettempdir()

    program_file = os.path.join(temp_dir, f"program_{uuid.uuid4().hex[:8]}.py")
    with open(program_file, "w") as fh:
        fh.write(solution)
    temp_files.append(program_file)
    return program_file
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[api._run_discovery_async]]
