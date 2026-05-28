---
name: variation_operator_generator.get_available_packages
description: function in skydiscover/search/evox/utils/variation_operator_generator.py (evox)
metadata:
  type: project
---

# variation_operator_generator.get_available_packages

**File:** `skydiscover/search/evox/utils/variation_operator_generator.py:261`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def get_available_packages(problem_dir=None) -> list:
    """Get list of available packages from requirements.txt or pyproject.toml (direct dependencies only)."""
    from pathlib import Path

    repo_root = Path(__file__).resolve().parents[4]

    # Priority 1: requirements.txt in problem directory (or evaluator subdirectory)
    if problem_dir is not None:
        problem_dir = Path(problem_dir)
        candidates = [
            problem_dir / "requirements.txt",
            problem_dir / "evaluator" / "requirements.txt",
        ]
        for requirements_path in candidates:
            if requirements_path.exists():
                try:
                    with open(requirements_path, "r") as f:
                        lines = f.readlines()
                    packages = []
                    for line in lines:
                        line = line.strip()
                        if (
                            not line
                            or line.startswith("#")
                            or line.startswith("-e")
                            or line.startswith("--")
                        ):
                            continue
                        packages.append(line)
                    if packages:
                        logger.info(f"Read {len(packages)} packages from {requirements_path}")
                        return packages
                except Exception as e:
                    logger.warning(f"Could not read {requirements_path} ({e})")

    # Priority 2: requirements.txt at repo root
    requirements_path = repo_root / "requirements.txt"
    if requirements_path.exists():
        try:
            with open(requirements_path, "r") as f:
                lines = f.readlines()
            packages = []
            for line in lines:
                line = line.strip()
                if (
                    not line
                    or line.startswith("#")
                    or line.startswith("-e")
                    or line.startswith("--")
                ):
                    continue
                packages.append(line)
            if packages:
                logger.info(f"Read {len(packages)} packages from {requirements_path}")
                return packages
        except Exception as e:
            logger.warning(f"Could not read requirements.txt ({e}), trying pyproject.toml")

    # Priority 3: pyproject.toml
    try:
        try:
            import tomllib
        except ImportError:
            try:
                import tomli as tomllib
            except ImportError:
                raise ImportError("tomllib/tomli not available")

        pyproject_path = repo_root / "pyproject.toml"
        if not pyproject_path.exists():
            raise FileNotFoundError(f"pyproject.toml not found at {pyproject_path}")

        with open(pyproject_path, "rb") as f:
            data = tomllib.load(f)

        dependencies = data.get("project", {}).get("dependencies", [])
        return dependencies
    except (ImportError, FileNotFoundError, KeyError) as e:
        logger.warning(f"Could not read pyproject.toml ({e}), falling back to uv pip list")
        try:
            result = subprocess.run(
                ["uv", "pip", "list", "--format", "json"],
                capture_output=True,
                text=True,
                check=True,
                timeout=30,
            )
            packages = json.loads(result.stdout)
            return [f"{pkg['name']}=={pkg['version']}" for pkg in packages]
        except Exception as e2:
            logger.warning(f"Could not fetch package list: {e2}")
            return []
````

## → Calls
- [[CheckpointManager.load]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.load]]
- [[Runner.run]]
- [[TaskPool.run]]
- [[UnifiedArchive.get]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
- [[variation_operator_generator._build_operator_prompt]]
