"""
main.py
========
Unified driver script for Drone Path Tracking project.
Runs Systolic Array Validation, Python vs. Systolic Kalman Filters, 
and Alternative baseline filters.

Usage
-----
    python main.py
    python main.py --skip-validation
    python main.py --skip-alternatives
"""

import argparse
import numpy as np

# Kalman Filters
from kalman.kalman_python import KalmanFilterPython
from kalman.kalman_systolic import KalmanFilterSystolic

# Alternative Filters
from filters.alternative_filters import (
    MovingAverageFilter,
    ExponentialMovingAverage,
    LeastSquaresFilter,
    ComplementaryFilter,
    MedianFilter,
)

# Utilities
from utils.dataset_loader import load_drone_data
from utils.metrics import rmse
from utils.diagram import print_systolic_diagram
from utils.plotting import plot_results, plot_comparison
from utils.filter_runner import run_filter

# Systolic array (for validation)
from systolic.systolic_array_c import SystolicArray4x4


def validate_systolic_array():
    print("\n[TEST] Validating 4×4 Systolic Array...")
    sa_test = SystolicArray4x4()
    A_test = np.random.rand(4, 4)
    B_test = np.random.rand(4, 4)
    C_sa = sa_test.multiply(A_test, B_test)
    C_np = A_test @ B_test

    # Convert NumPy result to float32 for fair comparison
    max_err = np.max(np.abs(C_sa - C_np.astype(np.float32)))
    print(f"Max element-wise error vs NumPy: {max_err:.2e}")
    assert max_err < 1e-4, "Systolic array result mismatch!"
    print("✓ Systolic array validated successfully\n")


def main():
    parser = argparse.ArgumentParser(description="Drone Tracking Filter Runner")
    parser.add_argument("--skip-validation", action="store_true", help="Skip the initial 4x4 array validation and diagram")
    parser.add_argument("--skip-alternatives", action="store_true", help="Skip running alternative non-Kalman filters")
    parser.add_argument("--skip-plots", action="store_true", help="Skip matplotlib visualizations")
    args = parser.parse_args()

    # 1. Validation & Diagram
    if not args.skip_validation:
        validate_systolic_array()
        print_systolic_diagram()

    # 2. Dataset Setup
    CSV_PATH = "dataset/MH_03_medium/mav0/state_groundtruth_estimate0/data.csv"
    print("\n[INFO] Loading dataset...")
    x_true, y_true, x_meas, y_meas = load_drone_data(CSV_PATH, noise_std=0.3)
    print(f"[INFO] Dataset loaded: {len(x_true)} steps")

    print("\n[INFO] Initializing and Running filters...\n")
    
    # 3. Kalman Execution (Baseline & Systolic)
    kf_pure = KalmanFilterPython(dt=0.01)
    kf_sa = KalmanFilterSystolic(dt=0.01)

    est_x_pure, est_y_pure, t_pure = run_filter(kf_pure, x_meas, y_meas, filter_type="pure")
    est_x_sa, est_y_sa, t_sa = run_filter(kf_sa, x_meas, y_meas, filter_type="systolic")

    rmse_pure = rmse(est_x_pure, est_y_pure, x_true, y_true)
    rmse_sa = rmse(est_x_sa, est_y_sa, x_true, y_true)

    results = {
        "Kalman Filter": {
            "est_x": est_x_pure,
            "est_y": est_y_pure,
            "rmse": rmse_pure,
            "runtime": t_pure
        }
    }

    # 4. Alternative Execution
    if not args.skip_alternatives:
        filter_configs = [
            ("Moving Average", MovingAverageFilter(window=15), "alternative"),
            ("EMA (α=0.2)", ExponentialMovingAverage(alpha=0.2), "alternative"),
            ("Least Squares", LeastSquaresFilter(window=20, deg=2), "alternative"),
            ("Complementary", ComplementaryFilter(alpha=0.7, dt=0.01), "alternative"),
            ("Median Filter", MedianFilter(window=15), "alternative")
        ]
        
        for name, filt, f_type in filter_configs:
            ex, ey, elapsed = run_filter(filt, x_meas, y_meas, filter_type=f_type)
            r = rmse(ex, ey, x_true, y_true)
            results[name] = {
                "est_x": ex,
                "est_y": ey,
                "rmse": r,
                "runtime": elapsed
            }

    # 5. Global Summary Display
    print("\n" + "=" * 65)
    print("RESULTS SUMMARY")
    print("=" * 65)
    print(f"{'Filter':<22} | {'RMSE (m)':<15} | {'Runtime (s)':<15}")
    print("-" * 65)

    print(f"{'Kalman Filter (Pure)':<22} | {rmse_pure:<15.4f} | {t_pure:<15.3f}")
    print(f"{'Kalman Filter (SA)':<22} | {rmse_sa:<15.4f} | {t_sa:<15.3f}")
    
    for name, res in results.items():
        if name != "Kalman Filter":
            print(f"{name:<22} | {res['rmse']:<15.4f} | {res['runtime']:<15.3f}")
            
    print("=" * 65)
    
    if t_pure > 0:
        print(f"Overhead (SA vs Pure KF)  : {t_sa/t_pure:.2f}×")

    print("\nNOTE: The systolic overhead here is due to Python simulation.")
    print("In real FPGA/ASIC hardware, systolic arrays run PEs in parallel and are significantly faster.\n")

    # 6. Visualization
    if not args.skip_plots:
        print("\n[INFO] Generating comparison plots...")
        plot_results(
            x_true, y_true,
            x_meas, y_meas,
            est_x_pure, est_y_pure,
            est_x_sa, est_y_sa,
            rmse_pure, rmse_sa,
            t_pure, t_sa
        )
        
        if not args.skip_alternatives:
            plot_comparison(x_true, y_true, x_meas, y_meas, results)


if __name__ == "__main__":
    main()