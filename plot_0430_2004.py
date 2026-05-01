import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

log_path = "outputs/evox/circle_packing_0430_2004/logs/evox_20260430_200429.log"

with open(log_path, "r") as f:
    lines = f.readlines()

iter_scores = {}
stagnation_iters = []
last_iter = None

for line in lines:
    m = re.search(r"Iteration (\d+): Program .+ completed in", line)
    if m:
        last_iter = int(m.group(1))

    m = re.search(r"Metrics: combined_score=([0-9.]+)", line)
    if m and last_iter is not None:
        iter_scores[last_iter] = float(m.group(1))
        last_iter = None

    if "Stagnation detected" in line:
        m = re.search(r"solution_iter=(\d+)", line)
        if m:
            stagnation_iters.append(int(m.group(1)))

all_iters = sorted(iter_scores.keys())
scores = [iter_scores[i] for i in all_iters]

best = 0.9598
best_so_far = []
for s in scores:
    if s > best:
        best = s
    best_so_far.append(best)

fig, ax = plt.subplots(figsize=(14, 6))

for si in stagnation_iters:
    ax.axvline(x=si, color="#EF9F27", alpha=0.35, linewidth=10)

ax.scatter(all_iters, scores, color="#378ADD", zorder=3, s=55, label="Iteration score")
ax.step(all_iters, best_so_far, where="post", color="#1D9E75",
        linewidth=2, linestyle="--", label="Best so far")
ax.axhline(y=2.635, color="#E24B4A", linewidth=1.5, linestyle=":", label="Target (2.635)")
ax.axhline(y=0.9598, color="#888780", linewidth=1, linestyle=":", alpha=0.6, label="Baseline (0.960)")

ax.set_xlabel("Iteration", fontsize=12)
ax.set_ylabel("Sum of radii", fontsize=12)
ax.set_title("Circle packing — EvoX + gemma3:12b (run 0430_2004)", fontsize=13)
ax.set_ylim(0, 2.8)
ax.set_xlim(0, 52)
ax.grid(axis="y", alpha=0.2)

stag_patch = mpatches.Patch(color="#EF9F27", alpha=0.4, label="Stagnation triggered")
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles + [stag_patch], labels + ["Stagnation triggered"], fontsize=10)

# Annotate final best
ax.annotate(f"Final best: 1.632", xy=(50, 1.6324), xytext=(42, 1.9),
            arrowprops=dict(arrowstyle="->", color="gray"), fontsize=10, color="#1D9E75")

plt.tight_layout()
plt.savefig("outputs/circle_packing_0430_2004_scores.png", dpi=150)
print("Saved.")
