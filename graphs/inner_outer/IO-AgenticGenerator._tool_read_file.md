---
name: IO-AgenticGenerator._tool_read_file
description: method in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# AgenticGenerator._tool_read_file

**File:** `skydiscover/llm/agentic_generator.py:285`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    def _tool_read_file(self, args: Dict[str, Any], files_read: set) -> Dict[str, Any]:
        path = args.get("path", "")
        if not path:
            return _err("'path' is required.")

        root = self.config.codebase_root
        if not root:
            return _err("codebase_root not configured.")
        full = os.path.join(root, path) if not os.path.isabs(path) else path

        ok, resolved, err = _validate_path(
            full, root, self.config.allowed_extensions, self.config.excluded_dirs
        )
        if not ok:
            return _err(err)

        if resolved not in files_read and len(files_read) >= self.config.max_files_read:
            return _err(f"Read limit ({self.config.max_files_read}). Output your solution.")

        try:
            with open(resolved, "r", encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
        except Exception as e:
            return _err(f"Cannot read: {e}")

        total = len(lines)
        start = max(1, int(args.get("line_start") or 1)) - 1
        end = min(total, int(args.get("line_end") or total))
        content = "".join(lines[start:end])

        if len(content) > self.config.max_file_chars:
            half = self.config.max_file_chars // 2
            content = (
                content[:half]
                + f"\n\n... ({len(content) - self.config.max_file_chars} chars truncated) ...\n\n"
                + content[-half:]
            )

        files_read.add(resolved)
        rel = os.path.relpath(resolved, root)
        numbered = [
            f"{i:4d} | {ln.rstrip(chr(10))}"
            for i, ln in enumerate(content.splitlines(True), start=start + 1)
        ]
        return {"content": f"{rel} (lines {start + 1}-{end} of {total})\n" + "\n".join(numbered)}
````

## → Calls
- [[IO-AgenticGenerator.__init__]]
- [[IO-agentic_generator._err]]
- [[IO-agentic_generator._validate_path]]

## ← Called by
- [[IO-AgenticGenerator._run_tool]]
