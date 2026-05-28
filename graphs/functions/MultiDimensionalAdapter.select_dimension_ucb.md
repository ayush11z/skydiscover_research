---
name: MultiDimensionalAdapter.select_dimension_ucb
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# MultiDimensionalAdapter.select_dimension_ucb

**File:** `skydiscover/search/adaevolve/adaptation.py:403`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def select_dimension_ucb(self, total_iterations: int) -> int:
        """
        Select next dimension using UCB with decayed magnitude rewards.

        UCB formula: reward_avg + C * sqrt(ln(N) / visits)

        With decayed magnitude rewards:
        - Islands that find recent breakthroughs are prioritized
        - Old breakthroughs decay away, preventing stalling

        Args:
            total_iterations: Total iterations across all dimensions

        Returns:
            dim_idx: Index of selected dimension
        """
        n_dims = len(self.states)

        if n_dims == 0:
            raise ValueError("No dimensions available")

        # Ensure minimum visits for all dimensions
        # Randomize order to avoid always returning dimension 0 when multiple
        # dimensions are underexplored (fixes biased exploration issue)
        underexplored = [i for i in range(n_dims) if self.dimension_visits[i] < self.min_visits]
        if underexplored:
            import random

            return random.choice(underexplored)

        # UCB selection
        best_dim = 0
        best_ucb = float("-inf")

        for i in range(n_dims):
            raw_visits = self.dimension_visits[i]
            dec_visits = self.decayed_visits[i]

            # Recent reward average using DECAYED visits
            # This prevents reward_avg → 0 as raw visits grow
            # reward_avg = decayed_rewards / decayed_visits = recent reward per recent visit
            reward_avg = self.dimension_rewards[i] / dec_visits if dec_visits > 0 else 0.0

            # Exploration bonus uses RAW visits
            # We still want classic UCB exploration: visit underexplored islands
            # GUARD: Prevent division by zero if raw_visits is somehow 0
            # (shouldn't happen after min_visits check, but defensive programming)
            if raw_visits <= 0:
                exploration_bonus = float("inf")  # Force exploration of unvisited dimension
            else:
                exploration_bonus = self.ucb_exploration * math.sqrt(
                    math.log(total_iterations + 1) / raw_visits
                )

            ucb_score = reward_avg + exploration_bonus

            if ucb_score > best_ucb:
                best_ucb = ucb_score
                best_dim = i

        return best_dim
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.end_iteration]]
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[AdaEvolveDatabase.get_stats]]
- [[AdaEvolveDatabase.save]]
