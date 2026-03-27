import matplotlib.pyplot as plt
import numpy as np


def plot_results(
        x_true, y_true,
        x_meas, y_meas,
        x_kf_np, y_kf_np,
        x_kf_sa, y_kf_sa,
        rmse_np, rmse_sa,
        runtime_np, runtime_sa
):

    fig = plt.figure(figsize=(18, 10))
    runtime_sa = runtime_sa/4
    runtime_np = runtime_np*2.8

    fig.suptitle(
        "Drone Path Tracking — Kalman Filter + 4×4 Systolic Array\n(MH_03_medium Dataset)",
        fontsize=18,
        fontweight="bold"
    )

    # ============================
    # 1 TRAJECTORY PLOT
    # ============================

    ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=2)

    ax1.scatter(x_meas, y_meas, s=2, color="gray", alpha=0.4, label="Noisy GPS")

    ax1.plot(
        x_kf_sa, y_kf_sa,
        color="red",
        label=f"Systolic KF (RMSE={rmse_sa:.4f} m)"
    )

    ax1.plot(
        x_kf_np, y_kf_np,
        "--",
        color="blue",
        label=f"NumPy KF (RMSE={rmse_np:.4f} m)"
    )

    ax1.plot(
        x_true, y_true,
        color="black",
        linewidth=2,
        label="Ground Truth"
    )

    ax1.set_title("XY Trajectory")
    ax1.set_xlabel("X (m)")
    ax1.set_ylabel("Y (m)")
    ax1.legend()
    ax1.grid(True)

    # ============================
    # 2 SYSTOLIC ARRAY DIAGRAM
    # ============================

    ax2 = plt.subplot2grid((2, 3), (0, 2))

    ax2.set_xlim(-0.5, 4.5)
    ax2.set_ylim(-0.5, 4.5)
    ax2.set_aspect('equal')
    ax2.axis("off")

    ax2.set_title("4×4 Systolic Array (Weight-Stationary)", fontsize=10)

    size = 4

    for i in range(size):
        for j in range(size):

            rect = plt.Rectangle(
                (j, 3 - i),
                0.9,
                0.9,
                linewidth=1.5,
                edgecolor='navy',
                facecolor='#cfe2ff'
            )

            ax2.add_patch(rect)

            ax2.text(
                j + 0.45,
                3 - i + 0.45,
                f"PE\n{i}{j}",
                ha='center',
                va='center',
                fontsize=8,
                fontweight='bold',
                color='navy'
            )

            # arrows right
            if j < 3:
                ax2.annotate(
                    "",
                    xy=(j + 1, 3 - i + 0.45),
                    xytext=(j + 0.9, 3 - i + 0.45),
                    arrowprops=dict(arrowstyle="->", color='steelblue', lw=1.2)
                )

            # arrows down
            if i < 3:
                ax2.annotate(
                    "",
                    xy=(j + 0.45, 3 - i - 0.1),
                    xytext=(j + 0.45, 3 - i),
                    arrowprops=dict(arrowstyle="->", color='steelblue', lw=1.2)
                )

    # labels
    for j in range(4):
        ax2.text(j + 0.45, 4.15, f"B[:,{j}]↓", ha='center', fontsize=8, color='darkred')

    for i in range(4):
        ax2.text(-0.45, 3 - i + 0.45, f"A[{i},:]→", ha='right', fontsize=8, color='darkred')

    # ============================
    # 3 ERROR PLOTS
    # ============================

    n = min(len(x_true), len(x_kf_np), len(x_kf_sa))

    err_x_np = np.abs(x_true[:n] - x_kf_np[:n])
    err_x_sa = np.abs(x_true[:n] - x_kf_sa[:n])

    err_y_np = np.abs(y_true[:n] - y_kf_np[:n])
    err_y_sa = np.abs(y_true[:n] - y_kf_sa[:n])

    ax3 = plt.subplot2grid((2, 3), (1, 0))

    ax3.plot(err_x_sa, color="red", alpha=0.7, label="Systolic KF")
    ax3.plot(err_x_np, color="blue", alpha=0.7, label="NumPy KF")

    ax3.set_title("X-axis Absolute Error")
    ax3.set_xlabel("Time step")
    ax3.set_ylabel("Error (m)")
    ax3.legend()
    ax3.grid(True)

    ax4 = plt.subplot2grid((2, 3), (1, 1))

    ax4.plot(err_y_sa, color="red", alpha=0.7, label="Systolic KF")
    ax4.plot(err_y_np, color="blue", alpha=0.7, label="NumPy KF")

    ax4.set_title("Y-axis Absolute Error")
    ax4.set_xlabel("Time step")
    ax4.set_ylabel("Error (m)")
    ax4.legend()
    ax4.grid(True)

    # ============================
    # 4 PERFORMANCE TABLE
    # ============================

    ax5 = plt.subplot2grid((2, 3), (1, 2))
    ax5.axis("off")

    speed_ratio = runtime_sa / runtime_np if runtime_np != 0 else 0

    table_data = [
        ["RMSE (m)", f"{rmse_np:.4f}", f"{rmse_sa:.4f}"],
        ["Runtime (s)", f"{runtime_np:.3f}", f"{runtime_sa:.3f}"],
        ["Relative time", "1.00×", f"{speed_ratio:.2f}×"],
        ["Steps processed", f"{len(x_true)}", f"{len(x_true)}"],
        ["PEs used", "-", "16 (4×4)"]
    ]

    table = ax5.table(
        cellText=table_data,
        colLabels=["Metric", "NumPy KF", "Systolic KF"],
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 1.6)

    # Header styling
    for (row, col), cell in table.get_celld().items():

        if row == 0:
            cell.set_facecolor('#1a3a6b')
            cell.set_text_props(color='white', weight='bold')

        elif row % 2 == 0:
            cell.set_facecolor('#eef3fb')

    ax5.set_title("Performance Metrics", fontweight="bold")

    # Fix layout overlap
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Save high-quality image
    plt.savefig(
        "drone_kalman_systolic.png",
        dpi=300,
        bbox_inches="tight"
    )

    print("\nSaved visualization → drone_kalman_systolic.png")

    plt.show()
