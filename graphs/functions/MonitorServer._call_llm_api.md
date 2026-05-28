---
name: MonitorServer._call_llm_api
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._call_llm_api

**File:** `skydiscover/extras/monitor/server.py:1010`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def _call_llm_api(
        self, prompt_data: Dict[str, str], max_tokens: int = 8192, timeout: int = 180
    ) -> str:
        """Call OpenAI-compatible API (blocking, runs in executor thread)."""
        url = f"{self._summary_api_base}/chat/completions"
        body = json.dumps(
            {
                "model": self._summary_model,
                "messages": [
                    {"role": "system", "content": prompt_data["system"]},
                    {"role": "user", "content": prompt_data["user"]},
                ],
                "max_completion_tokens": max_tokens,
            }
        ).encode("utf-8")

        req = urllib.request.Request(
            url,
            data=body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._summary_api_key}",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"].strip()
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8", errors="replace")[:500]
            raise RuntimeError(f"API error {e.code}: {error_body}") from e
        except Exception as e:
            raise RuntimeError(f"API call failed: {e}") from e
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[MonitorServer._call_program_summary_api]]
- [[MonitorServer._trigger_summary]]
