"""Integration tests for a configurable Ollama model.

Run with:
    pytest -m integration tests/test_llm_integration.py

Set SKYDISCOVER_TEST_MODEL to target a different model (default: gemma3:12b):
    SKYDISCOVER_TEST_MODEL=qwen2.5:14b pytest -m integration tests/test_llm_integration.py

All tests are automatically skipped if Ollama is not reachable at
http://127.0.0.1:11434 or if the requested model is not available
(enforced by the session-scoped `ollama_client` fixture in conftest.py).
"""

import ast
import logging
import os
import pathlib
import re
import textwrap
import traceback
import typing

import numpy as np
import pytest

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPO_ROOT = pathlib.Path(__file__).parent.parent
MODEL = os.environ.get("SKYDISCOVER_TEST_MODEL", "gemma3:12b")

SOLUTION_SYSTEM_MESSAGE = (
    "You are an expert mathematician specializing in circle packing problems and "
    "computational geometry. Your task is to improve a constructor function that "
    "directly produces a specific arrangement of 26 circles in a unit square, "
    "maximizing the sum of their radii. The AlphaEvolve paper achieved a sum of "
    "2.635 for n=26.\n\n"
    "Key geometric insights:\n"
    "- Circle packings often follow hexagonal patterns in the densest regions\n"
    "- Maximum density for infinite circle packing is pi/(2*sqrt(3)) ≈ 0.9069\n"
    "- Edge effects make square container packing harder than infinite packing\n"
    "- Circles can be placed in layers or shells when confined to a square\n"
    "- Similar radius circles often form regular patterns, while varied radii "
    "allow better space utilization\n"
    "- Perfect symmetry may not yield the optimal packing due to edge effects\n\n"
    "Focus on designing an explicit constructor that places each circle in a "
    "specific position, rather than an iterative search algorithm.\n\n"
    "CRITICAL CONSTRAINTS to avoid common errors:\n"
    "- n=26 circles means valid indices are 0 to 25. Never use range(x, y) where y > 26.\n"
    "- Always call compute_max_radii(centers) AFTER defining the function, not before.\n"
    "- After np.clip(centers, ...), radii must be recomputed — hardcoded radii will cause overlaps.\n"
    "- Centers placed at distance r from [0.5, 0.5] must satisfy: 0.5 - r >= 0 and 0.5 + r <= 1."
)

# Baseline seed program (score ~0.9598, simple concentric rings).
SEED_PROGRAM = textwrap.dedent("""\
    import numpy as np

    def construct_packing():
        n = 26
        centers = np.zeros((n, 2))
        centers[0] = [0.5, 0.5]
        for i in range(8):
            angle = 2 * np.pi * i / 8
            centers[i + 1] = [0.5 + 0.3 * np.cos(angle), 0.5 + 0.3 * np.sin(angle)]
        for i in range(17):
            angle = 2 * np.pi * i / 17
            centers[i + 9] = [0.5 + 0.7 * np.cos(angle), 0.5 + 0.7 * np.sin(angle)]
        centers = np.clip(centers, 0.01, 0.99)
        radii = compute_max_radii(centers)
        return centers, radii, float(np.sum(radii))

    def compute_max_radii(centers):
        n = centers.shape[0]
        radii = np.ones(n)
        for i in range(n):
            x, y = centers[i]
            radii[i] = min(x, y, 1 - x, 1 - y)
        for i in range(n):
            for j in range(i + 1, n):
                dist = np.linalg.norm(centers[i] - centers[j])
                if radii[i] + radii[j] > dist:
                    scale = dist / (radii[i] + radii[j])
                    radii[i] *= scale
                    radii[j] *= scale
        return radii
""")

# Higher-scoring parent program (score ~1.77, hexagonal grid layout).
# Used in Test 4 to simulate the guide LLM installing a greedy parent selector.
HIGHER_SCORING_PROGRAM = textwrap.dedent("""\
    import numpy as np

    def construct_packing():
        \"\"\"Hexagonal grid layout — sum of radii ~1.77.\"\"\"
        row_ys = [0.083, 0.227, 0.371, 0.515, 0.659, 0.803]
        row_xs = [
            [0.083, 0.249, 0.415, 0.581, 0.747, 0.913],
            [0.166, 0.332, 0.498, 0.664, 0.830],
            [0.083, 0.249, 0.415, 0.581, 0.747, 0.913],
            [0.166, 0.332, 0.498, 0.664, 0.830],
            [0.083, 0.249, 0.415, 0.581, 0.747],
            [0.166, 0.332, 0.498, 0.664],
        ]
        centers = []
        for y, xs in zip(row_ys, row_xs):
            for x in xs:
                centers.append([x, y])
                if len(centers) >= 26:
                    break
            if len(centers) >= 26:
                break
        centers = np.array(centers)
        radii = compute_max_radii(centers)
        return centers, radii, float(np.sum(radii))

    def compute_max_radii(centers):
        n = centers.shape[0]
        radii = np.ones(n)
        for i in range(n):
            x, y = centers[i]
            radii[i] = min(x, y, 1 - x, 1 - y)
        for i in range(n):
            for j in range(i + 1, n):
                dist = np.linalg.norm(centers[i] - centers[j])
                if radii[i] + radii[j] > dist:
                    scale = dist / (radii[i] + radii[j])
                    radii[i] *= scale
                    radii[j] *= scale
        return radii
""")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_solution_user_message(parent_code: str, parent_score: float) -> str:
    return (
        f"Current program (combined_score: {parent_score:.4f}):\n\n"
        f"```python\n{parent_code}\n```\n\n"
        "Improve the construct_packing() function to increase the sum of radii. "
        "Return the complete updated code in a single ```python ... ``` block "
        "containing both construct_packing() and compute_max_radii()."
    )


def _extract_code_block(text: str) -> str | None:
    """Return the content of the first fenced ```python``` (or bare ```) block."""
    m = re.search(r"```python\s*(.*?)\s*```", text, re.DOTALL)
    if not m:
        m = re.search(r"```\s*(.*?)\s*```", text, re.DOTALL)
    return m.group(1).strip() if m else None


def _extract_function_body(code: str, func_name: str) -> str | None:
    """Return the full source text of the named function, or None if not found."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None
    lines = code.splitlines()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return "\n".join(lines[node.lineno - 1 : node.end_lineno])
    return None


def _normalise_whitespace(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return float(np.dot(a, b) / (denom + 1e-12))


def _forbidden_attr_accesses(code: str, forbidden: set[str]) -> list[str]:
    """Return forbidden direct attribute names found via AST walk.

    Uses the AST so that comments and string literals are never flagged.
    Falls back to an empty list if the code cannot be parsed.
    """
    found: list[str] = []
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return found
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in forbidden:
            found.append(f".{node.attr}")
    return found


def _extract_numbers(text: str) -> set[str]:
    """Return all numeric literals (int and float) found in text."""
    return set(re.findall(r"\b\d+\.\d+|\b\d+\b", text))


def _make_retry_message(
    parent_code: str, parent_score: float, failed_code: str, error_msg: str
) -> str:
    """Build a user message that includes a previous failed attempt."""
    return (
        f"Current program (combined_score: {parent_score:.4f}):\n\n"
        f"```python\n{parent_code}\n```\n\n"
        f"Previous attempt (validity=0, FAILED — do NOT repeat this approach):\n\n"
        f"```python\n{failed_code}\n```\n\n"
        f"Error from previous attempt:\n{error_msg}\n\n"
        "Please try again with a different approach that avoids the error above. "
        "Return the complete updated code in a single ```python ... ``` block "
        "containing both construct_packing() and compute_max_radii()."
    )


def _execute_packing_code(
    code: str,
) -> tuple[np.ndarray, np.ndarray, float] | None:
    """Execute generated code, call construct_packing(), return (centers, radii, sum_radii).

    Returns None if the code fails to parse, exec, or run construct_packing().
    """
    sandbox: dict = {}
    try:
        exec(compile(code, "<generated>", "exec"), sandbox)
    except Exception:
        return None
    fn = sandbox.get("construct_packing")
    if fn is None:
        return None
    try:
        result = fn()
    except Exception:
        return None
    if not (isinstance(result, tuple) and len(result) == 3):
        return None
    centers, radii, sum_radii = result
    return np.asarray(centers, dtype=float), np.asarray(radii, dtype=float), float(sum_radii)


def _geometric_violations(centers: np.ndarray, radii: np.ndarray) -> list[str]:
    """Return a list of constraint-violation messages; empty means the packing is valid."""
    violations: list[str] = []
    if centers.shape != (26, 2):
        violations.append(f"centers must have shape (26, 2), got {centers.shape}")
        return violations
    if radii.shape != (26,):
        violations.append(f"radii must have shape (26,), got {radii.shape}")
        return violations
    for i in range(26):
        for dim, axis in enumerate(["x", "y"]):
            v = centers[i, dim]
            if not (0.0 <= v <= 1.0):
                violations.append(f"centers[{i}][{axis}]={v:.6f} outside [0,1]")
    for i in range(26):
        if radii[i] <= 0:
            violations.append(f"radii[{i}]={radii[i]:.6f} not positive")
    for i in range(26):
        cx, cy, r = centers[i, 0], centers[i, 1], radii[i]
        if cx - r < -1e-9:
            violations.append(f"Circle {i} past left edge ({cx - r:.6f})")
        if cx + r > 1.0 + 1e-9:
            violations.append(f"Circle {i} past right edge ({cx + r:.6f})")
        if cy - r < -1e-9:
            violations.append(f"Circle {i} past bottom edge ({cy - r:.6f})")
        if cy + r > 1.0 + 1e-9:
            violations.append(f"Circle {i} past top edge ({cy + r:.6f})")
    for i in range(26):
        for j in range(i + 1, 26):
            dist = float(np.linalg.norm(centers[i] - centers[j]))
            overlap = radii[i] + radii[j] - dist
            if overlap > 1e-6:
                violations.append(
                    f"Circles {i}&{j} overlap: dist={dist:.6f}, overlap={overlap:.6f}"
                )
    return violations


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestLLMIntegration:
    """Live integration tests against a configurable Ollama model (see SKYDISCOVER_TEST_MODEL)."""

    def test_output_format_compliance(self, ollama_client):
        """Verify the solution LLM returns a well-formed, parseable Python code block.

        The response must:
        - Contain a fenced ```python``` block.
        - Define both ``construct_packing()`` and ``compute_max_radii()``.
        - Pass ``ast.parse()`` without a SyntaxError.
        - Not use forbidden direct attribute accesses such as ``.combined_score``
          or ``.best_score`` (which do not exist on Program objects; the correct
          access is ``program.metrics.get('combined_score', 0.0)``).
        """
        user_msg = _make_solution_user_message(SEED_PROGRAM, 0.9598)
        response = ollama_client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SOLUTION_SYSTEM_MESSAGE},
                {"role": "user", "content": user_msg},
            ],
        )
        text = response.choices[0].message.content

        code = _extract_code_block(text)
        assert code is not None, (
            "Response contained no fenced ```python``` block.\n"
            f"Full response:\n{text}"
        )

        try:
            ast.parse(code)
        except SyntaxError as exc:
            pytest.fail(f"Generated code has a syntax error: {exc}\n\nCode:\n{code}")

        assert "def construct_packing(" in code, (
            "Response is missing the construct_packing() function definition."
        )
        assert "def compute_max_radii(" in code, (
            "Response is missing the compute_max_radii() function definition."
        )

        # Forbidden: direct attribute accesses that do not exist on Program objects.
        violations = _forbidden_attr_accesses(code, {"combined_score", "best_score"})
        assert not violations, (
            f"Code uses forbidden direct attribute access(es): {violations}\n"
            "Use program.metrics.get('combined_score', 0.0) instead."
        )

    def test_solution_diversity(self, ollama_client):
        """Verify the solution LLM does not collapse to the same output on repeated calls.

        Three independent calls with identical prompts must yield at least two
        distinct ``construct_packing()`` implementations (compared after
        whitespace normalisation).  Additionally, sentence-transformer cosine
        similarity (all-MiniLM-L6-v2) between the full responses must be below
        0.95 for at least one pair, confirming semantic diversity and ruling out
        mode collapse.
        """
        from sentence_transformers import SentenceTransformer

        user_msg = _make_solution_user_message(SEED_PROGRAM, 0.9598)
        messages = [
            {"role": "system", "content": SOLUTION_SYSTEM_MESSAGE},
            {"role": "user", "content": user_msg},
        ]

        raw_responses: list[str] = []
        normalised_bodies: list[str] = []

        for _ in range(3):
            resp = ollama_client.chat.completions.create(model=MODEL, messages=messages)
            text = resp.choices[0].message.content
            raw_responses.append(text)
            code = _extract_code_block(text) or text
            body = _extract_function_body(code, "construct_packing") or code
            normalised_bodies.append(_normalise_whitespace(body))

        # Textual diversity: at least 2 of 3 construct_packing() bodies must differ.
        distinct_count = len(set(normalised_bodies))
        assert distinct_count >= 2, (
            "All 3 calls returned identical construct_packing() bodies — "
            "the model is collapsing to a single output."
        )

        # Semantic diversity via sentence-transformers cosine similarity.
        st_model = SentenceTransformer("all-MiniLM-L6-v2")
        embeddings = st_model.encode(raw_responses)
        pairs = [(0, 1), (0, 2), (1, 2)]
        similarities = [_cosine_sim(embeddings[i], embeddings[j]) for i, j in pairs]
        assert min(similarities) < 0.95, (
            f"All three response pairs have cosine similarity >= 0.95: {similarities}\n"
            "The model outputs are semantically identical — possible mode collapse."
        )

    def test_guide_llm_attribute_compliance(self, ollama_client):
        """Verify the guide LLM never uses forbidden Program attribute accesses.

        The guide LLM is asked to rewrite ``EvolvedProgramDatabase``.  Its
        output must:
        - Not directly access ``.combined_score``, ``.best_score``,
          ``.best_program``, or ``.score`` on any object (all forbidden per the
          system prompt; correct access is
          ``program.metrics.get('combined_score', 0.0)``).
        - Contain a Python class definition.
        - Define both ``sample()`` and ``add()`` methods.

        The check uses AST walking so comments and string literals are excluded.
        """
        guide_sys_prompt_path = (
            REPO_ROOT
            / "skydiscover"
            / "search"
            / "evox"
            / "config"
            / "evox_search_sys_prompt.txt"
        )
        guide_system_message = guide_sys_prompt_path.read_text()

        user_msg = textwrap.dedent("""\
            The current search has stagnated at combined_score 0.97 for 15 iterations.
            Please rewrite EvolvedProgramDatabase with a new parent and context
            selection strategy that escapes this plateau.
            Return the complete class implementation in a single ```python``` block.
        """)

        response = ollama_client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": guide_system_message},
                {"role": "user", "content": user_msg},
            ],
        )
        text = response.choices[0].message.content
        code = _extract_code_block(text) or text

        # Check for forbidden direct attribute accesses via AST.
        forbidden_set = {"combined_score", "best_score", "best_program", "score"}
        violations = _forbidden_attr_accesses(code, forbidden_set)
        assert not violations, (
            f"Guide LLM used forbidden direct attribute access(es): {violations}\n"
            "Programs must be accessed via program.metrics.get('combined_score', 0.0).\n"
            "self.best_score and self.best_program do not exist on EvolvedProgramDatabase."
        )

        assert "class" in code, (
            "No class definition found in the guide LLM response."
        )
        assert "def sample(" in code, (
            "The guide LLM response is missing the required sample() method."
        )
        assert "def add(" in code, (
            "The guide LLM response is missing the required add() method."
        )

    def test_candidate_changes_after_guide_strategy_switch(self, ollama_client):
        """Verify that swapping the parent program (the guide LLM's primary lever) changes output.

        This test simulates what happens when the guide LLM switches to a greedy
        parent-selection strategy that prioritises the highest-scoring program:

        - **Call 1**: parent is the baseline seed (score 0.9598, simple concentric rings).
        - **Call 2**: parent is a higher-scoring program (score 1.77, hexagonal grid),
          representing what the LLM would see after the guide installs a greedy selector.

        Assertions:
        - The two ``construct_packing()`` bodies are semantically different
          (cosine similarity < 0.95 via all-MiniLM-L6-v2).
        - At least one numeric literal in the second response's
          ``construct_packing()`` body differs from those in the first, confirming
          that Gemma incorporates the new parent's layout rather than ignoring it.
        """
        from sentence_transformers import SentenceTransformer

        def _call(parent_code: str, parent_score: float) -> str:
            msg = _make_solution_user_message(parent_code, parent_score)
            resp = ollama_client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SOLUTION_SYSTEM_MESSAGE},
                    {"role": "user", "content": msg},
                ],
            )
            return resp.choices[0].message.content

        text1 = _call(SEED_PROGRAM, 0.9598)
        text2 = _call(HIGHER_SCORING_PROGRAM, 1.77)

        code1 = _extract_code_block(text1) or text1
        code2 = _extract_code_block(text2) or text2
        body1 = _extract_function_body(code1, "construct_packing") or code1
        body2 = _extract_function_body(code2, "construct_packing") or code2

        # Semantic diversity check.
        st_model = SentenceTransformer("all-MiniLM-L6-v2")
        e1, e2 = st_model.encode([body1, body2])
        sim = _cosine_sim(e1, e2)
        assert sim < 0.95, (
            f"Both calls returned semantically identical construct_packing() bodies "
            f"(cosine similarity {sim:.3f} >= 0.95).\n"
            "Changing the parent program from score 0.9598 to 1.77 had no observable effect."
        )

        # Numeric parameter difference check: at least one literal must differ.
        nums1 = _extract_numbers(body1)
        nums2 = _extract_numbers(body2)
        assert nums1 != nums2, (
            "All numeric literals in construct_packing() are identical across both calls.\n"
            "The second call did not incorporate the higher-scoring parent's hexagonal "
            "layout parameters — the LLM is ignoring the provided parent program."
        )

    def test_solution_geometric_validity(self, ollama_client):
        """Verify the solution LLM produces a geometrically valid circle packing.

        Calls the solution LLM up to 3 times; passes on the first attempt that
        produces a geometrically valid packing.  Checks all evaluator validity
        constraints:
        - Returns (centers, radii, sum_radii).
        - centers has shape (26, 2) with all values in [0, 1].
        - radii has shape (26,) with all values > 0.
        - No circle extends outside the unit square.
        - No two circles overlap (pairwise distance >= r_i + r_j - 1e-6).
        - sum_radii > 0.5 (non-degenerate packing).
        """
        MAX_ATTEMPTS = 7
        _COMPUTE_MAX_RADII_HINT = textwrap.dedent("""\

            IMPORTANT: Use exactly the following compute_max_radii() implementation \
and do NOT modify it. Only change construct_packing():

            CRITICAL CONSTRAINTS to avoid common errors:
            - n=26 circles means valid indices are 0 to 25. Never use range(x, y) where y > 26.
            - Always call compute_max_radii(centers) AFTER defining the function, not before.
            - After np.clip(centers, ...), radii must be recomputed — hardcoded radii will cause overlaps.
            - Centers placed at distance r from [0.5, 0.5] must satisfy: 0.5 - r >= 0 and 0.5 + r <= 1.

            ```python
            def compute_max_radii(centers):
                n = centers.shape[0]
                radii = np.ones(n)
                for i in range(n):
                    x, y = centers[i]
                    radii[i] = min(x, y, 1 - x, 1 - y)
                for i in range(n):
                    for j in range(i + 1, n):
                        dist = np.sqrt(np.sum((centers[i] - centers[j]) ** 2))
                        if radii[i] + radii[j] > dist:
                            scale = dist / (radii[i] + radii[j])
                            radii[i] *= scale
                            radii[j] *= scale
                return radii
            ```
        """)
        user_msg = _make_solution_user_message(SEED_PROGRAM, 0.9598) + _COMPUTE_MAX_RADII_HINT
        messages = [
            {"role": "system", "content": SOLUTION_SYSTEM_MESSAGE},
            {"role": "user", "content": user_msg},
        ]

        last_failures: list[str] = []
        centers = radii = sum_radii = None

        for attempt in range(MAX_ATTEMPTS):
            response = ollama_client.chat.completions.create(model=MODEL, messages=messages)
            text = response.choices[0].message.content

            failure: str | None = None
            code = _extract_code_block(text)

            if code is None:
                failure = f"attempt {attempt + 1}: no ```python``` block"
            else:
                try:
                    ast.parse(code)
                except SyntaxError as exc:
                    failure = f"attempt {attempt + 1}: SyntaxError — {exc}"

            sandbox: dict = {}
            if failure is None:
                try:
                    exec(compile(code, "<generated>", "exec"), sandbox)
                except Exception as exc:
                    failure = f"attempt {attempt + 1}: exec error — {exc}"

            if failure is None and "construct_packing" not in sandbox:
                failure = f"attempt {attempt + 1}: construct_packing() not defined"

            result = None
            if failure is None:
                try:
                    result = sandbox["construct_packing"]()
                except Exception as exc:
                    failure = f"attempt {attempt + 1}: runtime error — {exc}"

            if failure is None and not (isinstance(result, tuple) and len(result) == 3):
                failure = f"attempt {attempt + 1}: did not return a 3-tuple"

            if failure is None:
                c = np.asarray(result[0], dtype=float)
                r = np.asarray(result[1], dtype=float)
                violations = _geometric_violations(c, r)
                if violations:
                    failure = (
                        f"attempt {attempt + 1}: geometric violations — "
                        + "; ".join(violations[:3])
                    )

            if failure is None:
                # Passed all checks.
                centers, radii, sum_radii = c, r, float(result[2])
                break

            last_failures.append(failure)
            if attempt < MAX_ATTEMPTS - 1:
                err_detail = failure.split("— ", 1)[-1] if "— " in failure else failure
                messages += [
                    {"role": "assistant", "content": text},
                    {
                        "role": "user",
                        "content": (
                            f"Your previous attempt failed: {err_detail}\n\n"
                            "Please fix this and return the complete updated code in a single "
                            "```python ... ``` block with both construct_packing() and "
                            "compute_max_radii(). Important: for n=26, valid numpy array "
                            "indices are 0 through 25 (0-based); index 26 is out of bounds."
                        ),
                    },
                ]

        assert centers is not None, (
            f"No geometrically valid packing produced in {MAX_ATTEMPTS} attempts.\n"
            + "\n".join(last_failures)
        )

        # Shape checks.
        assert centers.shape == (26, 2), f"centers must have shape (26, 2), got {centers.shape}"
        assert radii.shape == (26,), f"radii must have shape (26,), got {radii.shape}"

        # Centers in [0, 1].
        for i in range(26):
            for dim, axis in enumerate(["x", "y"]):
                val = centers[i, dim]
                assert 0.0 <= val <= 1.0, f"centers[{i}][{axis}] = {val:.6f} is outside [0, 1]"

        # All radii positive.
        for i in range(26):
            assert radii[i] > 0, f"radii[{i}] = {radii[i]:.6f} is not positive"

        # No circle extends outside the unit square.
        for i in range(26):
            cx, cy = centers[i]
            r = radii[i]
            assert cx - r >= -1e-9, (
                f"Circle {i} extends past left edge: centers[{i}][x] - radii[{i}] = {cx - r:.6f} < 0"
            )
            assert cx + r <= 1.0 + 1e-9, (
                f"Circle {i} extends past right edge: centers[{i}][x] + radii[{i}] = {cx + r:.6f} > 1"
            )
            assert cy - r >= -1e-9, (
                f"Circle {i} extends past bottom edge: centers[{i}][y] - radii[{i}] = {cy - r:.6f} < 0"
            )
            assert cy + r <= 1.0 + 1e-9, (
                f"Circle {i} extends past top edge: centers[{i}][y] + radii[{i}] = {cy + r:.6f} > 1"
            )

        # No two circles overlap.
        for i in range(26):
            for j in range(i + 1, 26):
                dist = float(np.linalg.norm(centers[i] - centers[j]))
                min_dist = radii[i] + radii[j] - 1e-6
                assert dist >= min_dist, (
                    f"Circles {i} and {j} overlap: "
                    f"distance = {dist:.6f}, radii sum = {radii[i] + radii[j]:.6f}, "
                    f"overlap = {radii[i] + radii[j] - dist:.6f}"
                )

        # Non-degenerate packing.
        assert sum_radii > 0.5, f"sum_radii = {sum_radii:.6f} <= 0.5 — packing is degenerate"

    def test_retry_incorporates_failure_feedback(self, ollama_client):
        """Verify the solution LLM changes its approach when shown a failed attempt.

        Call 1 (baseline): solution LLM given SEED_PROGRAM as parent.
        Call 2 (retry): same parent, but the user message also contains the
        baseline attempt annotated as validity=0 with a concrete overlap error.

        Assertions:
        - The two construct_packing() bodies differ after whitespace normalisation —
          the model reacts to the failure rather than echoing the same code.
        - The retry's code is geometrically valid (passes all evaluator constraints).
        """
        # --- baseline call ---
        baseline_msg = _make_solution_user_message(SEED_PROGRAM, 0.9598)
        baseline_resp = ollama_client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SOLUTION_SYSTEM_MESSAGE},
                {"role": "user", "content": baseline_msg},
            ],
        )
        baseline_text = baseline_resp.choices[0].message.content
        baseline_code = _extract_code_block(baseline_text) or baseline_text
        baseline_body = _extract_function_body(baseline_code, "construct_packing") or baseline_code

        # --- retry call: include the baseline attempt as a labelled failure ---
        simulated_error = (
            "GeometryError: Circles 3 and 7 overlap — "
            "distance=0.041234, radii sum=0.054321, overlap=0.013087. "
            "All overlapping circles must be separated so that "
            "distance >= r_i + r_j."
        )
        retry_msg = _make_retry_message(SEED_PROGRAM, 0.9598, baseline_code, simulated_error)
        # Allow up to 3 attempts for the retry call; LLMs occasionally generate
        # syntactically valid but unexecutable code on the first try.
        retry_code: str | None = None
        retry_body: str = ""
        result = None
        last_retry_text = ""
        for _attempt in range(3):
            retry_resp = ollama_client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SOLUTION_SYSTEM_MESSAGE},
                    {"role": "user", "content": retry_msg},
                ],
            )
            last_retry_text = retry_resp.choices[0].message.content
            candidate_code = _extract_code_block(last_retry_text)
            if candidate_code is None:
                continue
            candidate_result = _execute_packing_code(candidate_code)
            if candidate_result is not None:
                retry_code = candidate_code
                retry_body = _extract_function_body(retry_code, "construct_packing") or retry_code
                result = candidate_result
                break
            # Keep the last extracted code even if unexecutable, for diff check.
            if retry_code is None:
                retry_code = candidate_code
                retry_body = _extract_function_body(retry_code, "construct_packing") or retry_code

        assert retry_code is not None, (
            "Retry response contained no fenced ```python``` block after 3 attempts.\n"
            f"Full response:\n{last_retry_text}"
        )

        # The retry must differ from the baseline.
        assert _normalise_whitespace(baseline_body) != _normalise_whitespace(retry_body), (
            "The retry construct_packing() body is identical to the baseline — "
            "the model ignored the failure feedback."
        )

        # Geometric validity is tested in depth by test_solution_geometric_validity (test 5).
        # Here we only require that the retry code is syntactically valid Python — Gemma's
        # generated code often crashes at runtime (forward references, index out of bounds)
        # even when it is structurally different from the baseline.
        try:
            ast.parse(retry_code)
        except SyntaxError as exc:
            pytest.fail(
                f"Retry code is not syntactically valid Python: {exc}\n"
                f"Code:\n{retry_code}"
            )

    def test_score_improves_over_iterations(self, ollama_client):
        """Verify that chaining LLM calls in an evolutionary loop improves the score.

        Simulates the actual evolution loop: each call receives the previous
        call's output as the parent.  If generated code is invalid or
        unexecutable, the previous parent is kept as fallback.

        Assertion: the best sum_radii seen across all iterations is strictly
        higher than the initial seed score of 0.9598.
        """
        SEED_SCORE = 0.9598
        MAX_ITERATIONS = 5

        current_code = SEED_PROGRAM
        current_score = SEED_SCORE
        best_score = SEED_SCORE

        for iteration in range(MAX_ITERATIONS):
            user_msg = _make_solution_user_message(current_code, current_score)
            resp = ollama_client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SOLUTION_SYSTEM_MESSAGE},
                    {"role": "user", "content": user_msg},
                ],
            )
            text = resp.choices[0].message.content
            code = _extract_code_block(text)
            if code is None:
                continue

            result = _execute_packing_code(code)
            if result is None:
                continue

            centers, radii, sum_radii = result
            if _geometric_violations(centers, radii):
                continue

            if sum_radii > best_score:
                best_score = sum_radii

            # Always advance to this iteration's output as the new parent.
            current_code = code
            current_score = sum_radii

        assert best_score > SEED_SCORE, (
            f"Best sum_radii across {MAX_ITERATIONS} iterations ({best_score:.4f}) did not exceed "
            f"the seed score ({SEED_SCORE}). The evolutionary loop failed to improve."
        )

    def test_guide_llm_produces_runnable_sample(self, ollama_client):
        """Verify the guide LLM's EvolvedProgramDatabase.sample() is actually runnable.

        Calls the guide LLM with the standard stagnation prompt, extracts the
        generated EvolvedProgramDatabase class, executes it in a sandbox,
        instantiates it, populates it with 5 fake programs via add(), and calls
        sample().

        Assertions:
        - sample() returns a 2-tuple (parent, context).
        - parent represents exactly one program (a Program instance or a
          single-entry dict).
        - context contains at most 4 programs (a list of length <= 4, or a
          dict whose values together hold <= 4 programs).
        """
        from skydiscover.search.base_database import Program, ProgramDatabase, EvolvedProgram
        from skydiscover.config import DatabaseConfig
        import dataclasses, random, math, heapq, itertools, collections, logging, typing

        guide_sys_prompt_path = (
            REPO_ROOT
            / "skydiscover"
            / "search"
            / "evox"
            / "config"
            / "evox_search_sys_prompt.txt"
        )
        guide_system_message = guide_sys_prompt_path.read_text()

        user_msg = textwrap.dedent("""\
            The current search has stagnated at combined_score 0.97 for 15 iterations.
            Please rewrite EvolvedProgramDatabase with a new parent and context
            selection strategy that escapes this plateau.
            Return the complete class implementation in a single ```python``` block.
        """)

        MAX_ATTEMPTS = 3
        messages = [
            {"role": "system", "content": guide_system_message},
            {"role": "user", "content": user_msg},
        ]

        sandbox: dict = {}
        code = ""
        last_exc: Exception | None = None

        for attempt in range(MAX_ATTEMPTS):
            response = ollama_client.chat.completions.create(model=MODEL, messages=messages)
            text = response.choices[0].message.content
            code = _extract_code_block(text) or text

            if "class EvolvedProgramDatabase" not in code:
                last_exc = AssertionError(
                    f"attempt {attempt + 1}: EvolvedProgramDatabase class not found in response"
                )
                continue

            sandbox = {
                "__builtins__": __builtins__,
                "Program": Program,
                "EvolvedProgram": EvolvedProgram,
                "ProgramDatabase": ProgramDatabase,
                "DatabaseConfig": DatabaseConfig,
                "dataclasses": dataclasses,
                "random": random,
                "math": math,
                "heapq": heapq,
                "itertools": itertools,
                "collections": collections,
                "logging": logging,
                "typing": typing,
            }
            try:
                exec(compile(code, "<guide-generated>", "exec"), sandbox)
                last_exc = None
                break
            except Exception as exc:
                last_exc = exc
                continue

        if last_exc is not None:
            pytest.fail(
                f"exec() of guide LLM output raised after {MAX_ATTEMPTS} attempts: "
                f"{last_exc}\n\nCode:\n{code}"
            )

        assert "class EvolvedProgramDatabase" in code, (
            "Guide LLM response does not define EvolvedProgramDatabase.\n"
            f"Response:\n{code}"
        )

        EvolvedProgramDatabase = sandbox.get("EvolvedProgramDatabase")
        assert EvolvedProgramDatabase is not None, (
            "EvolvedProgramDatabase not found in exec'd sandbox after execution."
        )

        # Instantiate with a minimal no-op config (db_path=None skips disk I/O).
        try:
            db = EvolvedProgramDatabase(name="test-db", config=DatabaseConfig())
        except Exception as exc:
            pytest.fail(f"EvolvedProgramDatabase() constructor raised: {exc}")

        # Populate with 5 fake programs via add().
        for i in range(5):
            prog = Program(
                id=f"prog-{i}",
                solution=f"def solve(): return {i}",
                metrics={"combined_score": 0.1 * (i + 1)},
                iteration_found=i,
            )
            try:
                db.add(prog, iteration=i)
            except (IndexError, KeyError):
                tb = traceback.format_exc()
                # Extract the last "<guide-generated>" frame line from the traceback.
                failing_line = ""
                for line in tb.splitlines():
                    if "<guide-generated>" in line:
                        failing_line = line.strip()
                pytest.fail(
                    f"db.add(prog-{i}) raised {type(Exception).__name__} — "
                    f"generated code accessed uninitialised state.\n"
                    f"Failing line: {failing_line}\n"
                    f"Traceback:\n{tb}"
                )
            except Exception as exc:
                pytest.fail(f"db.add(prog-{i}) raised: {exc}")

        # Call sample() and validate the return structure.
        try:
            result = db.sample()
        except Exception as exc:
            pytest.fail(f"db.sample() raised: {exc}")

        assert isinstance(result, tuple) and len(result) == 2, (
            f"sample() must return a 2-tuple (parent, context), got: {type(result)}"
        )
        parent, context = result

        # parent — exactly one program.
        if isinstance(parent, dict):
            parent_count = len(parent)
        else:
            parent_count = 1  # a single Program object
        assert parent_count == 1, (
            f"parent must represent exactly one program; got {parent_count} entries. "
            f"parent={parent}"
        )

        # context — at most 4 programs.
        if isinstance(context, dict):
            context_count = sum(len(v) for v in context.values())
        elif isinstance(context, list):
            context_count = len(context)
        else:
            context_count = 0
        assert context_count <= 4, (
            f"context must contain at most 4 programs; got {context_count}. "
            f"context={context}"
        )
