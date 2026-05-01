import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

log_path = "outputs/evox/circle_packing_0429_1508/logs/evox_20260429_150854.log"

with open(log_path, "r") as f:
    lines = f.readlines()

iter_scores = {}
stagnation_iters = []

for line in lines:
    m = re.search(r"Iteration (\d+): Program .+ completed in", line)
    if m:
        iter_num = int(m.group(1))
        # find score on next few lines
        continue
    
    m = re.search(r"Iteration (\d+): Program", line)
    if m:
        iter_num = int(m.group(1))

    m = re.search(r"combined_score=([0-9.]+), sum_radii", line)
    if m and "Metrics:" in line:
        score = float(m.group(1))
        iter_scores[iter_num] = score

    if "Stagnation detected" in line:
        m = re.search(r"solution_iter=(\d+)", line)
        if m:
            stagnation_iters.append(int(m.group(1)))

# Build best-so-far
all_iters = sorted(iter_scores.keys())
scores = [iter_scores[i] for i in all_iters]
best_so_far = []
best = 0
for s in scores:
    if s > best:
        best = s
    best_so_far.append(best)

# Plot
fig, ax = plt.subplots(figsize=(14, 6))

# Stagnation bands
for si in stagnation_iters:
    ax.axvline(x=si, color="#EF9F27", alpha=0.4, linewidth=8, label="_nolegend_")

# Scores
ax.scatter(all_iters, scores, color="#378ADD", zorder=3, s=50, label="Iteration score")

# Best so far
ax.step(all_iters, best_so_far, where="post", color="#1D9E75",
        linewidth=2, linestyle="--", label="Best so far")

# Target line
ax.axhline(y=2.635, color="#E24B4A", linewidth=1.5,
           linestyle=":", label="Target (2.635)")

ax.set_xlabel("Iteration", fontsize=12)
ax.set_ylabel("Sum of radii", fontsize=12)
ax.set_title("Circle packing — EvoX + gemma3:12b (run 0429_1508)", fontsize=13)
ax.set_ylim(0, 2.8)
ax.set_xlim(0, 52)
ax.grid(axis="y", alpha=0.2)

stag_patch = mpatches.Patch(color="#EF9F27", alpha=0.4, label="Stagnation triggered")
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles + [stag_patch], labels + ["Stagnation triggered"], fontsize=10)

plt.tight_layout()
plt.savefig("outputs/circle_packing_0429_1508_scores.png", dpi=150)
plt.show()
print("Saved to outputs/circle_packing_0429_1508_scores.png")