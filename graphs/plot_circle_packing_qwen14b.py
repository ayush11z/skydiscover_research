import matplotlib.pyplot as plt

# qwen2.5-coder:14b run data
iterations = [1, 2, 8, 15, 18, 19, 23, 24, 26, 28, 29, 31, 36]
scores =     [1.2043, 1.3687, 1.3687, 0.4900, 1.0986, 0.3804, 0.0627, 1.1004, 1.0722, 0.0000, 1.1709, 1.2758, 0.0000]
new_bests =  [True, True, False, False, False, False, False, False, False, False, False, False, False]

running_best = []
current_best = 0.9598
for s in scores:
    current_best = max(current_best, s)
    running_best.append(current_best)

fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor('#0f1117')
ax.set_facecolor('#0f1117')

ax.scatter(iterations, scores, color='#4a9eff', alpha=0.5, s=35, zorder=3, label='Iteration score')
ax.step(iterations, running_best, where='post', color='#00ff88', linewidth=2.5, zorder=4, label='Best score so far')

best_iters = [iterations[i] for i, b in enumerate(new_bests) if b]
best_scores_vals = [scores[i] for i, b in enumerate(new_bests) if b]
ax.scatter(best_iters, best_scores_vals, color='#ffdd00', s=150, zorder=5, marker='*', label='New best found')

ax.axhline(y=2.635, color='#ff9944', linestyle=':', linewidth=1.5, alpha=0.8)
ax.text(1, 2.67, 'AlphaEvolve SOTA (2.635)', color='#ff9944', fontsize=8)

ax.annotate('Best: 1.3687\n(never improved)', xy=(2, 1.3687), xytext=(8, 1.6),
            color='#ffdd00', fontsize=8,
            arrowprops=dict(arrowstyle='->', color='#ffdd00', lw=1.2))

ax.annotate('Slow programs\n(eval: 185-1148s)', xy=(28, 0.0), xytext=(20, 0.2),
            color='#ff6b6b', fontsize=8,
            arrowprops=dict(arrowstyle='->', color='#ff6b6b', lw=1.2))

ax.set_xlabel('Iteration', color='#cccccc', fontsize=11)
ax.set_ylabel('Sum of Radii (combined_score)', color='#cccccc', fontsize=11)
ax.set_title('EvoX Circle Packing — 50 Iterations (qwen2.5-coder:14b local)\nStarting: 0.9598  ->  Best: 1.3687  (+42.6%)',
             color='white', fontsize=13, pad=15)

ax.tick_params(colors='#888888')
ax.spines['bottom'].set_color('#333333')
ax.spines['left'].set_color('#333333')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(-1, 51)
ax.set_ylim(-0.1, 2.9)
ax.grid(True, alpha=0.12, color='#ffffff')
ax.legend(loc='upper right', facecolor='#1a1d2e', edgecolor='#333333', labelcolor='white', fontsize=9)

plt.tight_layout()
plt.savefig('circle_packing_qwen14b.png', dpi=150, bbox_inches='tight', facecolor='#0f1117')
print("Saved to circle_packing_qwen14b.png")