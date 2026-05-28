---
name: AgenticGenerator._tool_search
description: method in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# AgenticGenerator._tool_search

**File:** `skydiscover/llm/agentic_generator.py:331`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    def _tool_search(self, args: Dict[str, Any]) -> Dict[str, Any]:
        pattern = args.get("pattern", "")
        glob_pat = args.get("file_glob", "*.py")

        if not pattern:
            return _err("'pattern' is required.")
        if len(pattern) > self.config.max_regex_length:
            return _err(f"Pattern too long ({len(pattern)} > {self.config.max_regex_length}).")

        safety_err = _check_regex_safety(pattern)
        if safety_err:
            return _err(safety_err)

        try:
            compiled = re.compile(pattern)
        except re.error as e:
            return _err(f"Invalid regex: {e}")

        root = self.config.codebase_root
        if not root:
            return _err("codebase_root not configured.")
        excluded = set(self.config.excluded_dirs)
        allowed = set(self.config.allowed_extensions)
        matches: List[str] = []
        n_files = 0
        max_results = self.config.max_search_results

        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if not d.startswith(".") and d not in excluded]
            for fname in filenames:
                if not fnmatch.fnmatch(fname, glob_pat):
                    continue
                if os.path.splitext(fname)[1].lower() not in allowed:
                    continue
                fpath = os.path.join(dirpath, fname)
                try:
                    if os.path.getsize(fpath) > self.config.max_file_chars:
                        continue
                    with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                        text = f.read()
                except Exception:
                    continue

                n_files += 1
                ok, hits, err = _safe_regex_search(compiled, text, self.config.regex_timeout)
                if not ok:
                    return _err(err)

                rel = os.path.relpath(fpath, root)
                for hit in hits:
                    matches.append(f"{rel}:{hit}")
                    if len(matches) >= max_results:
                        break
                if len(matches) >= max_results:
                    break
            if len(matches) >= max_results:
                break

        if not matches:
            return {"content": f"No matches for '{pattern}' in {n_files} files."}

        suffix = f"\n(capped at {max_results} results)" if len(matches) >= max_results else ""
        return {"content": "\n".join(matches) + suffix}
````

## → Calls
- [[AgenticConfig.allowed_extensions]]
- [[AgenticConfig.codebase_root]]
- [[AgenticConfig.excluded_dirs]]
- [[AgenticConfig.max_file_chars]]
- [[AgenticConfig.max_regex_length]]
- [[AgenticConfig.max_search_results]]
- [[AgenticConfig.regex_timeout]]
- [[AgenticGenerator.__init__]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[SerializableResult.error]]
- [[UnifiedArchive.get]]
- [[agentic_generator._check_regex_safety]]
- [[agentic_generator._err]]
- [[agentic_generator._safe_regex_search]]
- [[build_repo_map.walk]]

## ← Called by
- [[AgenticGenerator._run_tool]]
