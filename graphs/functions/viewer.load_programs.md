---
name: viewer.load_programs
description: function in skydiscover/extras/monitor/viewer.py (monitor)
metadata:
  type: project
---

# viewer.load_programs

**File:** `skydiscover/extras/monitor/viewer.py:85`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def load_programs(ckpt_dir: str) -> Tuple[List[Dict], Optional[str], int]:
    """Load programs from a checkpoint directory.

    Returns:
        (programs_list_sorted_by_iteration, best_program_id, last_iteration)
    """
    p = Path(ckpt_dir)
    programs: Dict[str, Dict] = {}
    best_program_id: Optional[str] = None
    last_iteration = 0

    # Metadata
    meta_path = p / "metadata.json"
    if meta_path.exists():
        with open(meta_path) as f:
            meta = json.load(f)
        best_program_id = meta.get("best_program_id")
        last_iteration = meta.get("last_iteration", 0)

    # Programs from programs/ subdir
    programs_dir = p / "programs"
    if programs_dir.is_dir():
        for jf in programs_dir.glob("*.json"):
            try:
                with open(jf) as f:
                    data = json.load(f)
                programs[data["id"]] = data
            except Exception as e:
                logger.warning(f"Skipping {jf.name}: {e}")
    else:
        # Flat directory
        for jf in p.glob("*.json"):
            if jf.name == "metadata.json":
                continue
            try:
                with open(jf) as f:
                    data = json.load(f)
                if "id" in data:
                    programs[data["id"]] = data
            except Exception:
                logger.debug("Failed to load program from %s", jf, exc_info=True)

    # Infer best if not in metadata
    if not best_program_id and programs:
        best_score = -float("inf")
        for pid, prog in programs.items():
            s = (prog.get("metrics") or {}).get("combined_score", 0)
            if isinstance(s, (int, float)) and s > best_score:
                best_score = s
                best_program_id = pid

    prog_list = sorted(programs.values(), key=lambda x: x.get("iteration_found", 0))
    return prog_list, best_program_id, last_iteration
````

## → Calls
- [[BenchmarkConfig.name]]
- [[CheckpointManager.load]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[LLMModelConfig.name]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.load]]
- [[UnifiedArchive.get]]

## ← Called by
- [[viewer.main]]
