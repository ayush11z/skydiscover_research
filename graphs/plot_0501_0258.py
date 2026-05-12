import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Iteration scores from log
iter_scores = {
    1: 1.2219, 4: 1.1548, 5: 1.6013, 6: 1.1976, 7: 1.6589,
    8: 0.9791, 9: 1.4345, 10: 1.6013, 11: 1.7079, 12: 1.5449,
    13: 1.6457, 14: 1.3380, 15: 1.7545, 16: 0.8662, 17: 1.0035,
    18: 1.5449, 19: 1.4958, 20: 1.2219, 21: 1.3284, 22: 1.4958,
    23: 1.1875, 24: 1.7447, 28: 1.6517, 29: 1.6231, 33: 1.7533,
    34: 0.9925, 35: 1.4291, 37: 1.6734, 38: 1.7184, 39: 1.4506,
    40: 0.7483, 41: 1.0942, 42: 1.6915, 43: 1.5366, 44: 1.5048,
    45: 1.4295, 46: 1.5255, 47: 1.4485, 48: 1.4410, 49: 1.6481,
    55: 1.4729, 56: 1.4577, 57: 1.0635, 58: 1.7545, 59: 1.0699,
    60: 1.2127, 61: 1.3581, 65: 1.3240, 66: 1.7250, 67: 1.6924,
    69: 1.7369, 70: 1.7366, 71: 1.7310, 72: 1.6229, 73: 1.4771,
    74: 1.7111, 76: 1.2824, 77: 1.7001, 78: 1.6765, 80: 1.7154,
    81: 1.4741, 83: 1.6224, 84: 1.6334, 85: 1.7604, 87: 1.4361,
    89: 1.4120, 90: 0.8662, 91: 1.6909, 92: 1.7680, 93: 1.5876,
    94: 1.7761, 95: 1.5366, 96: 1.2858, 97: 1.4798, 98: 0.6297,
    99: 1.7386
}

stagnation_iters = [25, 40, 52, 66, 78, 92]
new_strategy_iters = [52, 66, 78, 92]  # iterations where new search algo was generated

all_iters = sorted(iter_scores.keys())
scores = [iter_scores[i] for i in all_iters]

best = 0.9598
best_so_far = []
for s in scores:
    if s > best:
        best = s
    best_so_far.append(best)

fig, ax = plt.subplots(figsize=(16, 6))

# Stagnation bands
for si in stagnation_iters:
    color = "#1D9E75" if si in new_strategy_iters else "#EF9F27"
    ax.axvline(x=si, color=color, alpha=0.35, linewidth=8)

ax.scatter(all_iters, scores, color="#378ADD", zorder=3, s=45, label="Iteration score")
ax.step(all_iters, best_so_far, where="post", color="#E24B4A",
        linewidth=2.5, linestyle="--", label="Best so far")
ax.axhline(y=2.635, color="#888780", linewidth=1.5, linestyle=":", label="Target (2.635)")
ax.axhline(y=0.9598, color="#BBBBBB", linewidth=1, linestyle=":", alpha=0.6, label="Baseline (0.960)")

ax.set_xlabel("Iteration", fontsize=12)
ax.set_ylabel("Sum of radii", fontsize=12)
ax.set_title("Circle packing — EvoX + gemma3:12b (run 0501_0258) — with meta-evolution fixes", fontsize=13)
ax.set_ylim(0, 2.8)
ax.set_xlim(0, 102)
ax.grid(axis="y", alpha=0.2)

stag_fail = mpatches.Patch(color="#EF9F27", alpha=0.4, label="Stagnation (failed)")
stag_success = mpatches.Patch(color="#1D9E75", alpha=0.4, label="Stagnation (new strategy generated ✓)")
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles + [stag_fail, stag_success], labels + ["Stagnation (failed)", "New strategy generated ✓"], fontsize=9)

ax.annotate(f"Best: 1.776\n(iter 94)", xy=(94, 1.7761), xytext=(80, 2.2),
            arrowprops=dict(arrowstyle="->", color="gray"), fontsize=9, color="#E24B4A")

plt.tight_layout()
plt.savefig("outputs/circle_packing_0501_0258_scores.png", dpi=150)
print("Saved.")
