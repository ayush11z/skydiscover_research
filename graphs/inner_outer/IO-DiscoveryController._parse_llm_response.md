---
name: IO-DiscoveryController._parse_llm_response
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._parse_llm_response

**File:** `skydiscover/search/default_discovery_controller.py:800`  
**Kind:** method  
**Layer:** #inner-loop

## What it does
Extracts the child program from the raw LLM text. Two modes depending on config:
- **diff mode** (`diff_based_generation=True`) — finds `SEARCH/REPLACE` blocks, applies them to the parent
- **full rewrite mode** — extracts a complete code block from the response

If nothing valid is found, returns `(None, None, error_message)` so the caller can retry.

## Source
````python
    def _parse_llm_response(
        self,
        llm_response: str,
        parent_solution: str,
        iteration: int,
        attempt: int,
        retry_times: int,
    ) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """
        Parse LLM response to extract child solution.

        Returns:
            Tuple of (child_solution, changes_summary, parse_error)
        """
        if self.config.diff_based_generation:
            diff_blocks = extract_diffs(llm_response)
            if not diff_blocks:
                preview = llm_response[:2000] + (
                    "\n... (truncated) ..." if len(llm_response) > 2000 else ""
                )
                logger.warning(
                    "No valid diffs found in LLM response (iteration=%s, attempt %s/%s). "
                    "Expected SEARCH/REPLACE blocks. Preview:\n%s",
                    iteration,
                    attempt,
                    retry_times,
                    preview,
                )
                return None, None, "No valid diffs found in response"

            child_solution = apply_diff(parent_solution, llm_response)
            changes_summary = format_diff_summary(diff_blocks)

            if child_solution == parent_solution:
                logger.warning(
                    "Diff blocks found but none matched parent solution (iteration=%s, attempt %s/%s).",
                    iteration,
                    attempt,
                    retry_times,
                )
                return (
                    None,
                    None,
                    "Diff SEARCH blocks did not match parent solution - no changes applied",
                )

            return child_solution, changes_summary, None
        else:
            new_solution = parse_full_rewrite(llm_response, self.config.language)
            if not new_solution:
                logger.warning(
                    "No valid solution found in LLM response (iteration=%s, attempt %s/%s).",
                    iteration,
                    attempt,
                    retry_times,
                )
                return None, None, "No valid solution found in response"
            return new_solution, "Full rewrite", None
````

## → Calls
- [[IO-Program.language]]
- [[IO-code_utils.apply_diff]]
- [[IO-code_utils.extract_diffs]]
- [[IO-code_utils.format_diff_summary]]
- [[IO-code_utils.parse_full_rewrite]]

## ← Called by
- [[IO-DiscoveryController._run_iteration]]
