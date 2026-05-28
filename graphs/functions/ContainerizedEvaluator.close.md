---
name: ContainerizedEvaluator.close
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator.close

**File:** `skydiscover/evaluation/container_evaluator.py:92`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def close(self):
        """Stop and remove the persistent container."""
        cid = getattr(self, "container_id", None)
        if cid:
            try:
                logger.info(f"Stopping container {cid[:12]}...")
                subprocess.run(
                    ["docker", "stop", cid],
                    capture_output=True,
                    timeout=30,
                    check=True,
                )
            except subprocess.TimeoutExpired:
                logger.warning(f"Timed out stopping container {cid[:12]}, killing...")
                try:
                    subprocess.run(["docker", "kill", cid], capture_output=True, timeout=10)
                except Exception:
                    logger.warning(f"Failed to kill container {cid[:12]}", exc_info=True)
            except Exception:
                logger.warning(f"Failed to stop container {cid[:12]}", exc_info=True)
            finally:
                self.container_id = None
````

## → Calls
- [[Runner.run]]
- [[TaskPool.run]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
- [[ContainerizedEvaluator.__del__]]
- [[ContainerizedEvaluator.__exit__]]
- [[DiscoveryController.close]]
- [[MonitorServer._handle_connection]]
- [[MonitorServer._run_loop]]
- [[Runner.run]]
- [[_make_gepa_evaluator.gepa_evaluator]]
- [[gepa_backend.run]]
