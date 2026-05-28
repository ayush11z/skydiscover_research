---
name: discovery_utils.load_database_from_file
description: function in skydiscover/search/utils/discovery_utils.py (search-utils)
metadata:
  type: project
---

# discovery_utils.load_database_from_file

**File:** `skydiscover/search/utils/discovery_utils.py:76`  
**Kind:** function  
**Layer:** #search-utils

## Source
````python
def load_database_from_file(
    file_path: str,
    database_class_name: str = "EvolvedProgramDatabase",
    program_class_name: str = "EvolvedProgram",
) -> Tuple[Type[ProgramDatabase], Type[Program]]:
    """Dynamically load database and program classes from a Python file."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Database file not found: {file_path}")

    import hashlib

    module_name = f"custom_database_{hashlib.md5(file_path.encode()).hexdigest()[:16]}"

    if module_name not in sys.modules:
        spec = importlib.util.spec_from_file_location(module_name, file_path)

        if spec is None or spec.loader is None:
            raise ValueError(f"Could not load module from: {file_path}")

        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module

        try:
            spec.loader.exec_module(module)
        except Exception as e:
            del sys.modules[module_name]
            raise ValueError(f"Error executing {file_path}: {e}") from e

    module = sys.modules[module_name]
    database_class = getattr(module, database_class_name, None)
    program_class = getattr(module, program_class_name, None)

    if database_class is None or program_class is None:
        raise AttributeError(
            f"Expected {database_class_name} and {program_class_name} in {file_path}"
        )

    if not issubclass(database_class, ProgramDatabase) or not issubclass(program_class, Program):
        raise TypeError(
            f"{database_class_name} must extend ProgramDatabase, {program_class_name} must extend Program"
        )

    return database_class, program_class
````

## → Calls
- [[base_database.Program]]
- [[base_database.ProgramDatabase]]

## ← Called by
- [[CoEvolutionController._restore_fallback_database]]
- [[CoEvolutionController._switch_to_new_search_algorithm]]
- [[registry.create_database]]
- [[registry.get_program]]
- [[search_strategy_evaluator.evaluate]]
