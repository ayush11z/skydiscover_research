---
name: ParadigmGenerator._build_techniques_section
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_techniques_section

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:429`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_techniques_section(self) -> str:
        """Build the techniques guidance section."""
        if self._is_image_mode:
            return self._build_image_techniques_section()
        return """## Technique Guidance

**Note:** Standard scientific libraries (scipy, numpy, etc.) are available. PyTorch and TensorFlow are not available.

**For Continuous Optimization with Constraints:**
- scipy.optimize.minimize with constraint handling (SLSQP, trust-constr)
- Multiple initial guesses for global optimization
- Geometric approaches (Voronoi, convex hull)

**For Discrete/Combinatorial Problems:**
- Greedy heuristics with good ordering
- Local search (swaps, moves)
- scipy.optimize.linear_sum_assignment for assignment problems
- scipy.optimize.linprog for linear constraints

**For Graph/Network Problems:**
- NetworkX algorithms (shortest path, min spanning tree, flow)
- Spectral methods (eigenvalue-based ordering)

**For Repair/Reconstruction:**
- Heuristic-based detection and correction
- Structural constraint exploitation
- Averaging/interpolation for consistency

**For Robust Filtering/Noise Reduction:**
- scipy.signal (medfilt, savgol_filter, wiener) for direct filtering
- Use methods that handle outliers better than mean-based (median, percentile)
- Do NOT use scipy.optimize.minimize to tune filter parameters
- Use filtering functions directly, not multi-stage optimization

**General Principles:**
- Prefer single-function library calls over multi-stage pipelines
- Match algorithm to problem structure
- Simple approaches with good heuristics often beat complex methods

## ANTI-PATTERNS - Critical rules about what NOT to do

1. **Do NOT use multi-stage optimization**: Do NOT call one function then optimize its output. Deterministic setup code followed by a single optimization call is allowed.

2. **Do NOT use scipy.optimize.minimize for hyperparameter tuning**: Use minimize to solve the problem directly, NOT to tune parameters for another function.

3. **Do NOT use scipy.optimize.minimize for discrete problems**: Continuous optimizers cannot handle discrete constraint violations properly.

4. **Each idea MUST be a single-function library call**: Do NOT suggest multi-stage processing (e.g., "call A then call B").

**AVOID:** DEAP, genetic algorithm libraries, domain-specific complex libraries, custom research algorithms, or any library requiring additional `pip install`

**Learning from Success:**
When an approach succeeds, think: what principle made it work? Learn and think of better ideas, don't just add complexity. If breakthrough patterns are known, prioritize approaches that match them.

## DIVERSITY REQUIREMENTS

Before generating ideas, explicitly think:
- Idea 1: [Type A - e.g., algorithmic refinement or library-based approach]
- Idea 2: [Type B - e.g., structural change or processing pattern - DIFFERENT from A]
- Idea 3: [Type C - e.g., different technique or optimization method - DIFFERENT from A and B]

**Verify:** Are these DIFFERENT types? NOT variations of the same approach.

Each idea must:
- Use DIFFERENT libraries/techniques than failed attempts
- Target DIFFERENT metrics/aspects from the evaluator
- Be independently implementable
- Prefer clear implementations (different != more complex)

### Be Specific and Actionable

Not vague: "Try optimization"
Specific: "Use scipy.optimize.minimize with SLSQP method"

- Include exact library names, function names, methods, parameters
- Provide step-by-step implementation guide
- Focus on core logic that implements the idea correctly
- Handle edge cases and avoid errors/warnings
- For optimization: use multiple initializations, appropriate iteration counts and convergence criteria (evaluation timeout: {self.eval_timeout}s)"""
````

## → Calls
- [[ParadigmGenerator._build_image_techniques_section]]

## ← Called by
- [[ParadigmGenerator._build_prompt]]
