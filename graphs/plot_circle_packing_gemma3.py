import matplotlib.pyplot as plt

# Gemma3:12b run data
iterations = [1, 3, 5, 6, 11, 12, 18, 22, 24, 27, 29, 37, 42, 43, 44, 45, 46, 48]
scores =     [0.8849, 0.8848, 0.7729, 0.8398, 1.2398, 0.8425, 0.8364, 1.1140, 1.2543, 1.1127, 0.9714, 0.8248, 1.8278, 1.4861, 1.3510, 1.0592, 1.4862, 1.7079]
new_bests =  [False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False]

# Running best
running_best = []
current_best = 0.9598
for s in scores:
    current_best = max(current_best, s)
    running_best.append(current_best)

fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor('#0f1117')
ax.set_facecolor('#0f1117')

# Individual scores
ax.scatter(iterations, scores, color='#4a9eff', alpha=0.5, s=35, zorder=3, label='Iteration score')

# Running best
ax.step(iterations, running_best, where='post', color='#00ff88', linewidth=2.5, zorder=4, label='Best score so far')

# New best stars
best_iters = [iterations[i] for i, b in enumerate(new_bests) if b]
best_scores_vals = [scores[i] for i, b in enumerate(new_bests) if b]
ax.scatter(best_iters, best_scores_vals, color='#ffdd00', s=150, zorder=5, marker='*', label='New best found')

# AlphaEvolve SOTA
ax.axhline(y=2.635, color='#ff9944', linestyle=':', linewidth=1.5, alpha=0.8)
ax.text(1, 2.67, 'AlphaEvolve SOTA (2.635)', color='#ff9944', fontsize=8)

# Annotations
ax.annotate('Late breakthrough\nat iteration 42', xy=(42, 1.8278), xytext=(30, 1.95),
            color='#ffdd00', fontsize=8,
            arrowprops=dict(arrowstyle='->', color='#ffdd00', lw=1.2))

ax.annotate('Outer ring radius\n0.7 → 0.45', xy=(11, 1.2398), xytext=(14, 1.4),
            color='#4a9eff', fontsize=8,
            arrowprops=dict(arrowstyle='->', color='#4a9eff', lw=1.2))

# Formatting
ax.set_xlabel('Iteration', color='#cccccc', fontsize=11)
ax.set_ylabel('Sum of Radii (combined_score)', color='#cccccc', fontsize=11)
ax.set_title('EvoX Circle Packing — 50 Iterations (gemma3:12b local)\nStarting: 0.9598  ->  Best: 1.8278  (+90.4%)',
             color='white', fontsize=13, pad=15)

ax.tick_params(colors='#888888')
ax.spines['bottom'].set_color('#333333')
ax.spines['left'].set_color('#333333')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(-1, 51)
ax.set_ylim(0.4, 2.9)
ax.grid(True, alpha=0.12, color='#ffffff')
ax.legend(loc='lower right', facecolor='#1a1d2e', edgecolor='#333333', labelcolor='white', fontsize=9)

plt.tight_layout()
plt.savefig('circle_packing_gemma3.png', dpi=150, bbox_inches='tight', facecolor='#0f1117')
print("Saved to circle_packing_gemma3.png")