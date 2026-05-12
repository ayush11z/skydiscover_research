import matplotlib.pyplot as plt

# GPT-4o run data parsed from log
iterations = [0, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 22, 24, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 40, 41, 42, 43, 45, 46, 47, 48]
scores =     [0.9598, 0.7446, 1.6845, 1.7380, 1.7071, 1.5300, 1.7460, 1.3818, 1.7380, 1.4724, 1.9611, 1.6352, 1.5275, 1.1811, 1.2612, 1.7919, 1.6526, 1.8666, 1.9040, 1.7460, 1.8601, 1.7838, 1.4833, 1.0898, 1.8844, 1.2612, 0.9909, 1.3818, 1.5112, 1.1513, 1.3976, 1.5393, 1.4545, 1.5508, 1.9116, 1.5287, 1.2771]
new_bests =  [False, False, True, True, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

# Strategy switch points
strategy_switches = [13, 22, 29, 35, 41, 47]

# Running best
running_best = []
current_best = 0
for s in scores:
    current_best = max(current_best, s)
    running_best.append(current_best)

fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor('#0f1117')
ax.set_facecolor('#0f1117')

# Individual scores
ax.scatter(iterations, scores, color='#4a9eff', alpha=0.5, s=35, zorder=3, label='Iteration score')

# Running best line
ax.step(iterations, running_best, where='post', color='#00ff88', linewidth=2.5, zorder=4, label='Best score so far')

# New best stars
best_iters = [iterations[i] for i, b in enumerate(new_bests) if b]
best_scores_vals = [scores[i] for i, b in enumerate(new_bests) if b]
ax.scatter(best_iters, best_scores_vals, color='#ffdd00', s=150, zorder=5, marker='*', label='New best found')

# Strategy switch lines
for i, sw in enumerate(strategy_switches):
    label = 'EvoX strategy switch' if i == 0 else None
    ax.axvline(x=sw, color='#ff6b6b', linestyle='--', alpha=0.5, linewidth=1, label=label)

# AlphaEvolve SOTA reference
ax.axhline(y=2.635, color='#ff9944', linestyle=':', linewidth=1.5, alpha=0.8)
ax.text(1, 2.67, 'AlphaEvolve SOTA (2.635)', color='#ff9944', fontsize=8)

# Annotations
ax.annotate('Hexagonal packing\ndiscovered (+75%)', xy=(5, 1.6845), xytext=(8, 1.45),
            color='#ffdd00', fontsize=8,
            arrowprops=dict(arrowstyle='->', color='#ffdd00', lw=1.2))

ax.annotate('Best: 1.9611', xy=(15, 1.9611), xytext=(20, 2.05),
            color='#ffdd00', fontsize=8,
            arrowprops=dict(arrowstyle='->', color='#ffdd00', lw=1.2))

# Formatting
ax.set_xlabel('Iteration', color='#cccccc', fontsize=11)
ax.set_ylabel('Sum of Radii (combined_score)', color='#cccccc', fontsize=11)
ax.set_title('EvoX Circle Packing — 50 Iterations (gpt-4o only)\nStarting: 0.9598  ->  Best: 1.9611  (+104.3%)',
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
plt.savefig('circle_packing_gpt4o.png', dpi=150, bbox_inches='tight', facecolor='#0f1117')
print("Saved to circle_packing_gpt4o.png")
