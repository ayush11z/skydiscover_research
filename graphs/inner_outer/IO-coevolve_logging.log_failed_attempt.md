---
name: IO-coevolve_logging.log_failed_attempt
description: function in skydiscover/search/evox/utils/coevolve_logging.py (evox)
metadata:
  type: project
---

# coevolve_logging.log_failed_attempt

**File:** `skydiscover/search/evox/utils/coevolve_logging.py:198`  
**Kind:** function  
**Layer:** #evox

## Source
````python
async def log_failed_attempt(
    outputs_dir: str,
    iteration: int,
    result: Optional[SerializableResult],
    error: str,
    stage: str,
    solution_iter: Optional[int] = None,
) -> None:
    """Log a single failed attempt."""
    iteration_dir = os.path.join(outputs_dir, f"iteration_{iteration}")
    os.makedirs(iteration_dir, exist_ok=True)

    child_dict = (result.child_program_dict or {}) if result else {}
    prompt = (result.prompt or {}) if result else {}
    llm_response = (result.llm_response or "") if result else ""

    failed_file = os.path.join(iteration_dir, "failed_attempts.json")
    failed_attempts: List[Dict[str, Any]] = []
    if os.path.exists(failed_file):
        with open(failed_file, "r") as f:
            failed_attempts = json.load(f).get("failed_attempts", [])

    attempt_number = len(failed_attempts) + 1
    attempt_data: Dict[str, Any] = {
        "attempt_number": attempt_number,
        "solution_iter": solution_iter,
        "error": error,
        "stage": stage,
        "solution": child_dict.get("solution", ""),
        "program_id": child_dict.get("id", "unknown"),
    }

    if llm_response:
        llm_filename = f"failed_attempt_{attempt_number}_llm_response.txt"
        with open(os.path.join(iteration_dir, llm_filename), "w") as f:
            f.write(llm_response)
        attempt_data["llm_response_file"] = llm_filename
        attempt_data["llm_response_preview"] = llm_response[:2000]

    if isinstance(prompt, dict) and (prompt.get("system") or prompt.get("user")):
        prompt_filename = f"failed_attempt_{attempt_number}_prompt.json"
        with open(os.path.join(iteration_dir, prompt_filename), "w") as f:
            json.dump(
                {"system": prompt.get("system", ""), "user": prompt.get("user", "")}, f, indent=2
            )
        attempt_data["prompt_file"] = prompt_filename

    failed_attempts.append(attempt_data)
    with open(failed_file, "w") as f:
        json.dump({"iteration": iteration, "failed_attempts": failed_attempts}, f, indent=2)

    if attempt_data["solution"]:
        code_file = os.path.join(iteration_dir, f"failed_attempt_{attempt_number}.py")
        with open(code_file, "w") as f:
            f.write(attempt_data["solution"])
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-coevolve_logging.handle_generation_failure]]
