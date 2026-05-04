"""Session-scoped fixtures shared across the test suite."""

import urllib.request
import urllib.error

import pytest

OLLAMA_BASE = "http://127.0.0.1:11434/v1"
_OLLAMA_TAGS_URL = "http://127.0.0.1:11434/api/tags"


def _is_ollama_running() -> bool:
    try:
        with urllib.request.urlopen(_OLLAMA_TAGS_URL, timeout=3) as resp:
            return resp.status == 200
    except Exception:
        return False


@pytest.fixture(scope="session")
def ollama_client():
    """Return an OpenAI client pointed at the local Ollama instance.

    Skips the entire session if Ollama is not reachable.
    """
    if not _is_ollama_running():
        pytest.skip(
            "Ollama is not reachable at http://127.0.0.1:11434 — "
            "skipping all integration tests"
        )
    from openai import OpenAI

    return OpenAI(base_url=OLLAMA_BASE, api_key="ollama")
