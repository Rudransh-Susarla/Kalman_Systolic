"""
components.py
=============
Contains highly reusable plotting components for graph construction.
"""
import matplotlib.pyplot as plt
import numpy as np

def add_trajectory_subplot(ax, x_true, y_true, x_meas, y_meas, est_x, est_y, label, color, rmse_val, lw=1.5):
    """Adds a trajectory plot with ground truth and measurements to an axis."""
    ax.scatter(x_meas, y_meas, s=1, color="lightgray", alpha=0.5, label="Noisy GPS", zorder=1)
    ax.plot(x_true, y_true, color="black", linewidth=2, label="Ground Truth", zorder=10)
    ax.plot(est_x, est_y, color=color, linewidth=lw, label=f"{label} (RMSE={rmse_val:.4f} m)", zorder=5)

    ax.set_title(f"XY Trajectory - {label}", fontsize=12)
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(True, alpha=0.4)

def add_error_plot(ax, x_true, est_x, title, ylabel, color="blue"):
    """Adds an absolute error plot over time to an axis."""
    n = min(len(x_true), len(est_x))
    t_axis = np.arange(n)
    err = np.abs(x_true[:n] - est_x[:n])
    
    ax.plot(t_axis, err, color=color, linewidth=1.5, alpha=0.9)
    ax.set_title(title, fontsize=12)
    ax.set_xlabel("Timestep")
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.4)

def add_systolic_diagram(ax):
    """Draws a 4x4 weight-stationary systolic array diagram on the given axis."""
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_aspect('equal')
    ax.axis("off")

    ax.set_title("4×4 Systolic Array (Weight-Stationary)", fontsize=10)

    size = 4

    for i in range(size):
        for j in range(size):
            rect = plt.Rectangle((j, 3 - i), 0.9, 0.9, linewidth=1.5, edgecolor='navy', facecolor='#cfe2ff')
            ax.add_patch(rect)
            ax.text(
                j + 0.45, 3 - i + 0.45, f"PE\n{i}{j}",
                ha='center', va='center', fontsize=8, fontweight='bold', color='navy'
            )

            if j < 3:
                ax.annotate(
                    "", xy=(j + 1, 3 - i + 0.45), xytext=(j + 0.9, 3 - i + 0.45),
                    arrowprops=dict(arrowstyle="->", color='steelblue', lw=1.2)
                )

            if i < 3:
                ax.annotate(
                    "", xy=(j + 0.45, 3 - i - 0.1), xytext=(j + 0.45, 3 - i),
                    arrowprops=dict(arrowstyle="->", color='steelblue', lw=1.2)
                )

    for j in range(4):
        ax.text(j + 0.45, 4.15, f"B[:,{j}]↓", ha='center', fontsize=8, color='darkred')

    for i in range(4):
        ax.text(-0.45, 3 - i + 0.45, f"A[{i},:]→", ha='right', fontsize=8, color='darkred')
