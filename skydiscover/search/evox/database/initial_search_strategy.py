# EVOLVE-BLOCK-START
import logging
import random
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from skydiscover.config import DatabaseConfig
from skydiscover.search.base_database import Program, ProgramDatabase

logger = logging.getLogger(__name__)


@dataclass
class EvolvedProgram(Program):
    """Program for the evolved database."""


class EvolvedProgramDatabase(ProgramDatabase):
    """Initial search strategy database.

    Demonstrates the full label mechanism so evolved strategies can build on it:
    - Tracks per-iteration improvement in add() so sample() can read state.
    - Uses DIVERGE_LABEL when the population stagnates at a low score.
    - Uses REFINE_LABEL when a high-scoring program has stalled recently.
    - Falls back to empty "" (no label) when the search is making steady progress.
    """

    def __init__(self, name: str, config: DatabaseConfig, **kwargs: Any):
        super().__init__(name, config, **kwargs)
        self.initial_program = None
        # State tracked in add() — read in sample()
        self._best_score_history: List[float] = []   # one entry per iteration
        self._stagnant_count: int = 0
        self._last_best: Optional[float] = None

    def add(self, program: EvolvedProgram, iteration: Optional[int] = None, **kwargs) -> str:
        """Add program and update stagnation tracking."""
        if iteration == 0 or program.iteration_found == 0:
            self.initial_program = program

        self.programs[program.id] = program

        if iteration is not None:
            self.last_iteration = max(self.last_iteration, iteration)

        if self.config.db_path:
            self._save_program(program)

        self._update_best_program(program)

        # Track best score per add() call so sample() can detect stagnation.
        current_best = max(
            (p.metrics.get("combined_score", 0.0)
             for p in self.programs.values()
             if isinstance(p.metrics.get("combined_score"), (int, float))),
            default=0.0,
        )
        self._best_score_history.append(current_best)
        if self._last_best is not None:
            improved = current_best - self._last_best > 0.01
            self._stagnant_count = 0 if improved else self._stagnant_count + 1
        self._last_best = current_best

        logger.debug(f"Added program {program.id}  best={current_best:.4f}  stagnant={self._stagnant_count}")
        return program.id

    def sample(
        self, num_context_programs: Optional[int] = 4, **kwargs
    ) -> Tuple[Dict[str, EvolvedProgram], Dict[str, List[EvolvedProgram]]]:
        """Select parent and context, injecting a label when the search needs guidance.

        Label logic:
          stagnant >= 4 AND best < 0.35  → DIVERGE  (stuck at low score, need new ideas)
          stagnant >= 3 AND best >= 0.35 → REFINE   (promising area, polish it)
          otherwise                       → ""       (making progress, no label needed)
        """
        candidates = list(self.programs.values())
        if not candidates:
            raise ValueError("No candidates available for sampling")

        current_best = self._last_best or 0.0

        # Choose label based on stagnation state
        if self._stagnant_count >= 4 and current_best < 0.35:
            label = self.DIVERGE_LABEL   # tell LLM to try something fundamentally different
        elif self._stagnant_count >= 3 and current_best >= 0.35:
            label = self.REFINE_LABEL    # tell LLM to polish the current best approach
        else:
            label = ""                   # no label — let parent/context selection do the work

        # Pick parent: best program when refining, random otherwise to avoid fixation
        if label == self.REFINE_LABEL:
            scored = [p for p in candidates
                      if isinstance(p.metrics.get("combined_score"), (int, float))]
            parent = max(scored, key=lambda p: p.metrics["combined_score"]) if scored else random.choice(candidates)
        else:
            parent = random.choice(candidates)

        # Context: pick diverse programs excluding the parent
        sample_size = min(num_context_programs + 1, len(candidates))
        examples = random.sample(candidates, sample_size)
        examples = [p for p in examples if p.id != parent.id][:num_context_programs]

        parent_dict = {label: parent}
        context_programs_dict = {"": examples}

        return parent_dict, context_programs_dict


# EVOLVE-BLOCK-END
