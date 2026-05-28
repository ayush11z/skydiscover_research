---
name: gepa_backend._make_gepa_evaluator
description: function in skydiscover/extras/external/gepa_backend.py (external)
metadata:
  type: project
---

# gepa_backend._make_gepa_evaluator

**File:** `skydiscover/extras/external/gepa_backend.py:28`  
**Kind:** function  
**Layer:** #external

## Source
````python
def _make_gepa_evaluator(
    evaluator_path: str, monitor_callback=None, solution_prefix: str = "", solution_suffix: str = ""
):
    """
    Wrap a SkyDiscover-style evaluator (evaluate(program_path) -> dict)
    into a GEPA-style evaluator (evaluate(candidate_str) -> (score, side_info)).
    """
    spec = importlib.util.spec_from_file_location("_skydiscover_eval", evaluator_path)
    eval_module = importlib.util.module_from_spec(spec)

    eval_dir = os.path.dirname(os.path.abspath(evaluator_path))
    if eval_dir not in sys.path:
        sys.path.insert(0, eval_dir)

    spec.loader.exec_module(eval_module)
    user_evaluate = eval_module.evaluate
    eval_counter = [0]

    def gepa_evaluator(candidate: str, **kwargs) -> tuple[float, dict]:
        # Write candidate code to a temp file so the SkyDiscover evaluator can load it.
        # Reconstruct the full file if prefix/suffix exist (code outside EVOLVE block).
        full_solution = solution_prefix + candidate + solution_suffix
        tmp = tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            prefix="gepa_candidate_",
            delete=False,
        )
        try:
            tmp.write(full_solution)
            tmp.flush()
            tmp.close()

            metrics = user_evaluate(tmp.name)

            # Normalise to (score, side_info)
            if isinstance(metrics, (int, float)):
                score = float(metrics)
                metrics = {"combined_score": score}
            else:
                score = metrics.get("combined_score")
                if score is None:
                    nums = [
                        float(v)
                        for v in metrics.values()
                        if isinstance(v, (int, float)) and not isinstance(v, bool)
                    ]
                    score = sum(nums) / len(nums) if nums else 0.0

            eval_counter[0] += 1

            # Push to monitor if callback provided
            if monitor_callback and score > 0:
                try:
                    from skydiscover.search.base_database import Program

                    prog = Program(
                        id=str(uuid.uuid4()),
                        solution=candidate,
                        language="python",
                        metrics={
                            "combined_score": float(score),
                            **(metrics if isinstance(metrics, dict) else {}),
                        },
                        iteration_found=eval_counter[0],
                        generation=eval_counter[0],
                    )
                    monitor_callback(prog, eval_counter[0])
                except Exception:
                    logger.debug("Monitor callback error", exc_info=True)

            return float(score), metrics
        except Exception as e:
            logger.warning("GEPA evaluator error: %s", e)
            return 0.0, {"error": str(e)}
        finally:
            try:
                os.unlink(tmp.name)
            except OSError:
                pass

    return gepa_evaluator
````

## → Calls
- [[_make_gepa_evaluator.gepa_evaluator]]

## ← Called by
- [[gepa_backend.run]]
