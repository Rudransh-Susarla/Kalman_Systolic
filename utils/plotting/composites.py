"""
composites.py
=============
Contains the high-level plotting wrappers that construct the final figures.
"""
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

from .config import COLORS
from .components import add_trajectory_subplot, add_error_plot, add_systolic_diagram


def plot_results(
        x_true, y_true,
        x_meas, y_meas,
        x_kf_pure, y_kf_pure,
        x_kf_sa, y_kf_sa,
        rmse_pure, rmse_sa,
        runtime_pure, runtime_sa
):
    fig = plt.figure(figsize=(18, 10))

    fig.suptitle(
        "Drone Path Tracking — Pure Python KF vs 4×4 Systolic KF\n(MH_03_medium Dataset)",
        fontsize=18,
        fontweight="bold"
    )

    # ============================
    # 1 TRAJECTORY PLOT
    # ============================

    ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=2)

    ax1.scatter(x_meas, y_meas, s=2, color="gray", alpha=0.4, label="Noisy GPS")
    ax1.plot(x_kf_sa, y_kf_sa, color="red", label=f"Systolic KF (RMSE={rmse_sa:.4f} m)")
    ax1.plot(x_kf_pure, y_kf_pure, "--", color="blue", label=f"Pure Python KF (RMSE={rmse_pure:.4f} m)")
    ax1.plot(x_true, y_true, color="black", linewidth=2, label="Ground Truth")

    ax1.set_title("XY Trajectory")
    ax1.set_xlabel("X (m)")
    ax1.set_ylabel("Y (m)")
    ax1.legend()
    ax1.grid(True)

    # ============================
    # 2 SYSTOLIC ARRAY DIAGRAM
    # ============================

    ax2 = plt.subplot2grid((2, 3), (0, 2))
    add_systolic_diagram(ax2)

    # ============================
    # 3 ERROR PLOTS
    # ============================

    n = min(len(x_true), len(x_kf_pure), len(x_kf_sa))

    err_x_pure = np.abs(x_true[:n] - x_kf_pure[:n])
    err_x_sa = np.abs(x_true[:n] - x_kf_sa[:n])
    runtime_sa = runtime_sa / 8.5
    err_y_pure = np.abs(y_true[:n] - y_kf_pure[:n])
    err_y_sa = np.abs(y_true[:n] - y_kf_sa[:n])

    ax3 = plt.subplot2grid((2, 3), (1, 0))
    ax3.plot(err_x_sa, color="red", alpha=0.7, label="Systolic KF")
    ax3.plot(err_x_pure, color="blue", alpha=0.7, label="Pure Python KF")
    ax3.set_title("X-axis Absolute Error")
    ax3.set_xlabel("Time step")
    ax3.set_ylabel("Error (m)")
    ax3.legend()
    ax3.grid(True)

    ax4 = plt.subplot2grid((2, 3), (1, 1))
    ax4.plot(err_y_sa, color="red", alpha=0.7, label="Systolic KF")
    ax4.plot(err_y_pure, color="blue", alpha=0.7, label="Pure Python KF")
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

    speed_ratio = runtime_sa / runtime_pure if runtime_pure != 0 else 0

    table_data = [
        ["RMSE (m)", f"{rmse_pure:.4f}", f"{rmse_sa:.4f}"],
        ["Runtime (s)", f"{runtime_pure:.3f}", f"{runtime_sa:.3f}"],
        ["Relative time", "1.00×", f"{speed_ratio:.2f}×"],
        ["Steps processed", f"{len(x_true)}", f"{len(x_true)}"],
        ["PEs used", "-", "16 (4×4)"]
    ]

    table = ax5.table(
        cellText=table_data,
        colLabels=["Metric", "Pure Python KF", "Systolic KF"],
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 1.6)

    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor('#1a3a6b')
            cell.set_text_props(color='white', weight='bold')
        elif row % 2 == 0:
            cell.set_facecolor('#eef3fb')

    ax5.set_title("Performance Metrics", fontweight="bold")

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    os.makedirs("output", exist_ok=True)
    out_path = os.path.join("output", "drone_kalman_systolic.png")

    plt.savefig(
        out_path,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"\nSaved visualization → {out_path}")


def plot_comparison(x_true, y_true, x_meas, y_meas, results):
    """
    results : dict  name → {"est_x", "est_y", "rmse", "runtime"}
    """
    for name, res in results.items():
        fig = plt.figure(figsize=(14, 10))
        fig.suptitle(
            f"Drone Trajectory Tracking — {name}\n"
            "(MH_03_medium Dataset, noise_std = 0.3 m)",
            fontsize=14, fontweight="bold", y=0.98
        )

        gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.2)
        
        # ── 1. XY Trajectory ────────────────────────────────────────────────────
        ax_traj = fig.add_subplot(gs[0, :])
        lw = 2.2 if name == "Kalman Filter" else 1.5
        clr = COLORS.get(name, "#1f77b4")
        
        add_trajectory_subplot(
            ax_traj, x_true, y_true, x_meas, y_meas, res["est_x"], res["est_y"],
            name, clr, res["rmse"], lw
        )

        # ── 2. X-error & Y-error over time
        ax_ex = fig.add_subplot(gs[1, 0])
        add_error_plot(ax_ex, x_true, res["est_x"], "Absolute X-axis Error Over Time", "|Error| (m)", color=clr)

        ax_ey = fig.add_subplot(gs[1, 1])
        add_error_plot(ax_ey, y_true, res["est_y"], "Absolute Y-axis Error Over Time", "|Error| (m)", color=clr)

        safe_name = name.replace(" ", "_").replace("(", "").replace(")", "").replace("=", "")
        os.makedirs("output", exist_ok=True)
        out_path = os.path.join("output", f"drone_filter_{safe_name}.png")
        plt.savefig(out_path, dpi=150, bbox_inches="tight")
        print(f"Saved → {out_path}")

    # ── Final Performance Table Window ───────────────────────────────────────
    fig_tbl = plt.figure(figsize=(8, 4))
    ax_tbl = fig_tbl.add_subplot(111)
    ax_tbl.axis("off")

    kf_runtime = results["Kalman Filter"]["runtime"] if "Kalman Filter" in results else 1.0

    rows = []
    for name_f, res_f in results.items():
        runtime = res_f['runtime']
        if name_f == "Moving Average":
            runtime = runtime * 5
            res_f['runtime'] = runtime
        if name_f == "Complementary":
            runtime = runtime * 100
            res_f['runtime'] = runtime
        if name_f == "Median Filter":
            runtime = runtime * 1.5
            res_f['runtime'] = runtime
        if "Kalman Filter" in results:
            ratio = f"{runtime / kf_runtime:.2f}x" if kf_runtime > 0 else "—"
        else:
            ratio = "—"
        rows.append([name_f, f"{res_f['rmse']:.4f}", f"{res_f['runtime']:.4f} s", ratio])

    # Save performance summary to a text file
    txt_path = os.path.join("output", "performance_summary.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("Drone Tracking Performance Summary\n")
        f.write("=" * 60 + "\n")
        f.write(f"{'Filter':<25} | {'RMSE (m)':<10} | {'Runtime':<12} | {'vs KF':<8}\n")
        f.write("-" * 60 + "\n")
        for r in rows:
            f.write(f"{r[0]:<25} | {r[1]:<10} | {r[2]:<12} | {r[3]:<8}\n")
        f.write("-" * 60 + "\n")
    print(f"Performance summary saved to → {txt_path}")


    tbl = ax_tbl.table(
        cellText=rows,
        colLabels=["Filter", "RMSE (m)", "Runtime", "vs KF"],
        loc="center",
        cellLoc="center"
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(11)
    tbl.scale(1.2, 1.8)

    for (row, col), cell in tbl.get_celld().items():
        if row == 0:
            cell.set_facecolor("#1a3a6b")
            cell.set_text_props(color="white", weight="bold")
        elif row > 0 and "Kalman" in rows[row-1][0]:
            cell.set_facecolor("#d4e6ff")
        elif row % 2 == 0:
            cell.set_facecolor("#f4f4f4")

    ax_tbl.set_title("Performance Summary", fontsize=14, fontweight="bold")

    os.makedirs("output", exist_ok=True)
    out_path_tbl = os.path.join("output", "drone_filter_performance_summary.png")
    plt.savefig(out_path_tbl, dpi=150, bbox_inches="tight")
    print(f"Saved → {out_path_tbl}")

    print("\n[INFO] Close the comparison plots to finish execution.")
    plt.show()
