"""Integration tests for Gemma3:12b via a live Ollama instance.

Run with:
    pytest -m integration tests/test_gemma_integration.py

All tests are automatically skipped if Ollama is not reachable at
http://127.0.0.1:11434 (enforced by the session-scoped `ollama_client`
fixture in conftest.py).
"""

import ast
import pathlib
import re
import textwrap

import numpy as np
import pytest

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPO_ROOT = pathlib.Path(__file__).parent.parent
MODEL = "gemma3:12b"

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
    "specific position, rather than an iterative search algorithm."
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
        for i in range(16):
            angle = 2 * np.pi * i / 16
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


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestGemmaIntegration:
    """Live integration tests against gemma3:12b through Ollama."""

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
