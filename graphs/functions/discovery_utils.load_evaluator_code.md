---
name: discovery_utils.load_evaluator_code
description: function in skydiscover/search/utils/discovery_utils.py (search-utils)
metadata:
  type: project
---

# discovery_utils.load_evaluator_code

**File:** `skydiscover/search/utils/discovery_utils.py:14`  
**Kind:** function  
**Layer:** #search-utils

## Source
````python
def load_evaluator_code(evaluation_file: Optional[str]) -> str:
    """Return evaluator source as a string for LLM context.

    For a plain Python file, returns its contents.
    For a containerized benchmark directory, returns all text files except
    infrastructure files (Dockerfile, requirements.txt) and data files (.json).
    """
    if not evaluation_file:
        return ""
    try:
        p = Path(evaluation_file)
        if not p.exists():
            return ""
        if p.is_dir():
            # Harbor task: prioritize instruction.md — it contains the full
            # problem description, reference implementation, and constraints.
            instruction = p / "instruction.md"
            if instruction.exists():
                return instruction.read_text()

            _SKIP = {"Dockerfile", "requirements.txt"}
            _MAX_FILES = 10
            _MAX_BYTES = 50_000
            parts = []
            for f in sorted(p.iterdir()):
                if len(parts) >= _MAX_FILES:
                    break
                if not f.is_file():
                    continue
                if f.name in _SKIP or f.suffix == ".json":
                    continue
                if f.stat().st_size > _MAX_BYTES:
                    continue
                try:
                    parts.append(f"# {f.name}\n{f.read_text()}")
                except Exception:
                    pass  # skip binary or unreadable files
            return "\n\n".join(parts)
        return p.read_text()
    except Exception as e:
        logger.warning(f"Could not load evaluator code from {evaluation_file}: {e}")
        return ""
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveController._load_evaluator_code]]
- [[CoEvolutionController._generate_variation_operators]]
- [[DiscoveryController._inject_evaluator_context]]
