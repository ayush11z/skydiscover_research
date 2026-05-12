import matplotlib.pyplot as plt
import numpy as np

models = ['gpt-4o', 'gemma3:12b\n(local)', 'gpt-4o-mini', 'qwen2.5-coder\n14b (local)', 'phi4-mini\n(local)']
scores = [1.9611, 1.8278, 1.7262, 1.3687, 0.9598]
colors = ['#00ff88', '#4a9eff', '#4a9eff', '#ff9944', '#ff6b6b']
alphas = [1.0, 0.85, 0.7, 0.7, 0.7]

fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('#0f1117')
ax.set_facecolor('#0f1117')

bars = ax.bar(models, scores, color=colors, alpha=0.85, width=0.6, zorder=3)

# Starting score reference line
ax.axhline(y=0.9598, color='#888888', linestyle='--', linewidth=1.2, alpha=0.7, label='Starting score (0.9598)')

# AlphaEvolve SOTA
ax.axhline(y=2.635, color='#ff9944', linestyle=':', linewidth=1.5, alpha=0.8, label='AlphaEvolve SOTA (2.635)')
ax.text(4.4, 2.67, '2.635', color='#ff9944', fontsize=9)

# Score labels on bars
for bar, score in zip(bars, scores):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
            f'{score:.4f}', ha='center', va='bottom', color='white', fontsize=11, fontweight='bold')

# Improvement labels
improvements = ['+104.3%', '+90.4%', '+79.9%', '+42.6%', '0%']
imp_colors = ['#00ff88', '#4a9eff', '#4a9eff', '#ff9944', '#ff6b6b']
for bar, imp, col in zip(bars, improvements, imp_colors):
    ax.text(bar.get_x() + bar.get_width()/2, 0.1,
            imp, ha='center', va='bottom', color=col, fontsize=10, fontweight='bold')

# Formatting
ax.set_ylabel('Sum of Radii (combined_score)', color='#cccccc', fontsize=12)
ax.set_title('EvoX Circle Packing — Model Comparison (50 iterations each)\nStarting score: 0.9598  |  AlphaEvolve SOTA: 2.635',
             color='white', fontsize=13, pad=15)
ax.tick_params(colors='#888888', labelsize=11)
ax.set_ylim(0, 2.9)
for label in ax.get_xticklabels():
    label.set_color('#cccccc')
ax.spines['bottom'].set_color('#333333')
ax.spines['left'].set_color('#333333')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, alpha=0.12, color='#ffffff', axis='y')
ax.legend(facecolor='#1a1d2e', edgecolor='#333333', labelcolor='white', fontsize=10)

plt.tight_layout()
plt.savefig('circle_packing_model_comparison.png', dpi=150, bbox_inches='tight', facecolor='#0f1117')
print("Saved to circle_packing_model_comparison.png")
