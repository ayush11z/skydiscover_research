---
name: HarborEvaluator._extract_path_from_solve_sh
description: method in skydiscover/evaluation/harbor_evaluator.py (evaluation)
metadata:
  type: project
---

# HarborEvaluator._extract_path_from_solve_sh

**File:** `skydiscover/evaluation/harbor_evaluator.py:267`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _extract_path_from_solve_sh(self) -> str:
        """Extract the solution target path from ``solution/solve.sh``.

        Looks for shell redirect patterns like ``cat > /app/solver.py``
        or ``> /workspace/solution.py``.  If the path is relative, resolves
        it against the last ``cd`` target found before the redirect.
        """
        solve_sh = os.path.join(self.task_dir, "solution", "solve.sh")
        if not os.path.exists(solve_sh):
            return ""

        try:
            with open(solve_sh) as f:
                text = f.read()
        except Exception:
            return ""

        _CODE_EXTS = r"\.(?:py|sh|js|ts|cpp|c|rs|go|java|rb)"

        # First try: absolute path redirects.
        for pattern in [
            rf"cat\s+>\s*(/\S+{_CODE_EXTS})",
            rf">\s*(/\S+{_CODE_EXTS})",
        ]:
            match = re.search(pattern, text)
            if match:
                return match.group(1)

        # Second try: relative path redirect (e.g. crustbench writes to
        # src/interfaces/base122.rs after cd-ing into a project directory).
        redirect_pattern = rf"cat\s+>\s*(\S+{_CODE_EXTS})"
        redirect_match = re.search(redirect_pattern, text)
        if redirect_match:
            rel_path = redirect_match.group(1)

            # Resolve the base directory.  Strategy:
            # 1. Look for concrete absolute paths in cd commands.
            # 2. Look for absolute paths assigned to shell variables (the
            #    variable may be used with cd later — e.g. RBENCH_DIR).
            # 3. Fall back to the Dockerfile WORKDIR.
            candidates = re.findall(r'cd\s+"?(/[^"$\s]+)"?\s*$', text, re.MULTILINE)
            if not candidates:
                # Variable assignments like RBENCH_DIR="/workspace/rbench_reference"
                candidates = re.findall(r'[A-Z_]+=\s*"?(/[^"$\s]+)"?\s*$', text, re.MULTILINE)

            if candidates:
                base = candidates[0].rstrip('"')
            else:
                # Dockerfile WORKDIR fallback.
                base = "/workspace"
                dockerfile = os.path.join(self.task_dir, "environment", "Dockerfile")
                if os.path.exists(dockerfile):
                    try:
                        with open(dockerfile) as f:
                            for line in f:
                                m = re.match(r"WORKDIR\s+(/\S+)", line)
                                if m:
                                    base = m.group(1)
                    except Exception:
                        pass

            return os.path.join(base, rel_path)

        return ""
````

## → Calls
- [[Config.search]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[HarborEvaluator._extract_solution_path]]
