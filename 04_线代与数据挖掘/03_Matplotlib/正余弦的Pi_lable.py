"""
手动设置刻度位置与标签
适用场景：固定范围（如 [-2π, 2π]或 [0, 2π]）的三角函数图的快速出图。
思路：用 plt.xticks/ticks同时指定刻度位置与对应的 LaTeX标签（如 -2π、-π、0、π、2π）。
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y1, y2 = np.sin(x), np.cos(x)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y1, label=r'$\sin x$')
ax.plot(x, y2, label=r'$\cos x$')

# 设置 π 刻度与标签
ticks = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]
labels = [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$']
ax.set_xticks(ticks)
ax.set_xticklabels(labels)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()