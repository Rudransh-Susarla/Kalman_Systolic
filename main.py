import numpy as np
import time

# Kalman Filters
from kalman.kalman_python import KalmanFilterPython
from kalman.kalman_systolic import KalmanFilterSystolic

# Utilities
from utils.dataset_loader import load_drone_data
from utils.metrics import rmse
from utils.diagram import print_systolic_diagram
from utils.visualization import plot_results

# Systolic array (for validation)
from systolic.systolic_array_c import SystolicArray4x4


# =====================================
# RUN BOTH FILTERS & BENCHMARK
# =====================================

def run_filters(x_true, y_true, x_meas, y_meas, dt=0.01):

    steps = len(x_true)

    kf_pure = KalmanFilterPython(dt=dt)
    kf_sa = KalmanFilterSystolic(dt=dt)

    est_x_pure, est_y_pure = [], []
    est_x_sa, est_y_sa = [], []

    # ---------- Pure Python Kalman Filter ----------
    t0 = time.perf_counter()

    for k in range(steps):

        # Measurement as pure Python list-of-lists
        z = [[float(x_meas[k])], [float(y_meas[k])]]

        ex, ey = kf_pure.step(z)

        est_x_pure.append(ex)
        est_y_pure.append(ey)

    t_pure = time.perf_counter() - t0


    # ---------- Systolic Kalman Filter ----------
    t0 = time.perf_counter()

    for k in range(steps):

        z = np.array([[x_meas[k]], [y_meas[k]]])

        ex, ey = kf_sa.step(z)

        est_x_sa.append(ex)
        est_y_sa.append(ey)

    t_sa = time.perf_counter() - t0


    return (
        np.array(est_x_pure), np.array(est_y_pure),
        np.array(est_x_sa), np.array(est_y_sa),
        t_pure, t_sa
    )


# =====================================
# MAIN
# =====================================

if __name__ == "__main__":

    # ------------------------------------------------
    # 1. Validate Systolic Array Implementation
    # ------------------------------------------------

    print("\n[TEST] Validating 4×4 Systolic Array...")

    sa_test = SystolicArray4x4()

    A_test = np.random.rand(4, 4)
    B_test = np.random.rand(4, 4)

    C_sa = sa_test.multiply(A_test, B_test)
    C_np = A_test @ B_test

    # Convert NumPy result to float32 for fair comparison
    max_err = np.max(np.abs(C_sa - C_np.astype(np.float32)))

    print(f"Max element-wise error vs NumPy: {max_err:.2e}")

    # float32 tolerance
    assert max_err < 1e-4, "Systolic array result mismatch!"

    print("✓ Systolic array validated successfully\n")


    # ------------------------------------------------
    # 2. Print Systolic Architecture Diagram
    # ------------------------------------------------

    print_systolic_diagram()


    # ------------------------------------------------
    # 3. Load Drone Dataset
    # ------------------------------------------------

    CSV_PATH = "dataset/MH_03_medium/mav0/state_groundtruth_estimate0/data.csv"

    print("[INFO] Loading dataset...")

    x_true, y_true, x_meas, y_meas = load_drone_data(
        CSV_PATH,
        noise_std=0.3
    )

    print(f"[INFO] Dataset loaded: {len(x_true)} steps")


    # ------------------------------------------------
    # 4. Run Kalman Filters
    # ------------------------------------------------

    print("[INFO] Running filters...")

    (
        est_x_pure, est_y_pure,
        est_x_sa, est_y_sa,
        t_pure, t_sa
    ) = run_filters(x_true, y_true, x_meas, y_meas)


    # ------------------------------------------------
    # 5. Compute Metrics
    # ------------------------------------------------

    n = len(est_x_pure)

    rmse_pure = rmse(est_x_pure, est_y_pure, x_true, y_true)
    rmse_sa = rmse(est_x_sa, est_y_sa, x_true, y_true)


    # ------------------------------------------------
    # 6. Print Results
    # ------------------------------------------------

    print("\n" + "=" * 50)
    print("RESULTS SUMMARY")
    print("=" * 50)

    print(f"Steps processed        : {n}")
    print(f"Pure Python KF RMSE    : {rmse_pure:.4f} m")
    print(f"Systolic KF RMSE       : {rmse_sa:.4f} m")
    print(f"Pure Python runtime    : {t_pure:.3f} s")
    print(f"Systolic runtime       : {t_sa:.3f} s")

    if t_pure > 0:
        print(f"Overhead (SA vs Pure)  : {t_sa/t_pure:.2f}×")

    print("=" * 50)

    print("\nNOTE:")
    print("The systolic overhead here is due to Python simulation.")
    print("In real FPGA/ASIC hardware, systolic arrays run PEs")
    print("in parallel and are significantly faster.\n")


    # ------------------------------------------------
    # 7. Plot Results
    # ------------------------------------------------

    plot_results(
        x_true, y_true,
        x_meas, y_meas,
        est_x_pure, est_y_pure,
        est_x_sa, est_y_sa,
        rmse_pure, rmse_sa,
        t_pure, t_sa
    )