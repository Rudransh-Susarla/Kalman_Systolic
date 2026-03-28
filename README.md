# Drone Path Tracking — Unified Filter Benchmark

A Python project that tracks drone trajectories using a **Kalman Filter** accelerated by a **hardware-inspired 4×4 Systolic Array**, benchmarked against a standard NumPy implementation and a suite of **Alternative Filtering Techniques**.

---

## 📌 Overview

| Feature | Details |
|--------|---------|
| Dataset | EuRoC MAV — `MH_03_medium` |
| Primary Filter | 2D Kalman Filter (x, y, vx, vy) |
| Accelerator | 4×4 Systolic Array (C + OpenMP, compiled to DLL) |
| Baselines | Standard NumPy matrix operations |
| Alternative Filters | Moving Average, EMA, Least Squares, Complementary, Median |
| Metric | RMSE (metres), Runtime Speedup |

---

## 🗂️ Project Structure

```
Project_3/
├── main.py                    # Unified entry point & runner
├── kalman/
│   ├── kalman_numpy.py        # NumPy Kalman Filter (reference)
│   └── kalman_systolic.py     # Systolic accelerated Kalman Filter
├── filters/
│   └── alternative_filters.py # Moving Avg, EMA, Least Squares, etc.
├── systolic/
│   ├── systolic_array.c       # C implementation of 4×4 systolic array
│   ├── systolic_array.h       # Header file
│   └── systolic_array_c.py    # Python ctypes wrapper
├── utils/
│   ├── dataset_loader.py      # Load EuRoC CSV + add noise
│   ├── matrix_utils.py        # Pad/unpad matrices
│   ├── metrics.py             # RMSE calculation
│   ├── diagram.py             # ASCII architecture diagram
│   ├── filter_runner.py       # Helper to execute tracking tasks
│   └── plotting/              # Modular visualization tools
│       ├── config.py
│       ├── components.py
│       └── composites.py
└── dataset/
    └── MH_03_medium/          # Drone flight CSV data
```

---

## 🚀 How to Run

### Prerequisites

```bash
pip install numpy pandas matplotlib
```

> The systolic array is pre-compiled as `systolic.dll` (Windows).  
> To recompile on Windows (requires GCC + OpenMP):
> ```bash
> gcc -O2 -fopenmp -shared -o systolic/systolic.dll systolic/systolic_array.c
> ```

### Run

The project provides a unified execution interface with several command-line arguments to customize your run:

```bash
# Run all (Kalman validation, Pure vs. Systolic, and all Alternative filters)
python main.py

# Skip the initial systolic array math validation
python main.py --skip-validation

# Run only Kalman filters (skip alternative filters)
python main.py --skip-alternatives

# Skip all graphical visualizations (fastest)
python main.py --skip-plots
```

---

## 📊 Output

- **Console Summary**: Tabular comparison of RMSE, runtime, and calculated speedup between Pure NumPy and Systolic Kalman approaches alongside other active filters.
- **Visual Plots**: Multiple isolated windows displaying the trajectory paths, performance of individual filters (e.g., Drone path tracking overview, Kalman filter comparisons, and Individual Alternative Filter profiles).

---

## 💡 Systolic Array Architecture

```
      B0      B1      B2      B3
       ↓       ↓       ↓       ↓
A0 →  PE00 →  PE01 →  PE02 →  PE03
       ↓       ↓       ↓       ↓
A1 →  PE10 →  PE11 →  PE12 →  PE13
       ↓       ↓       ↓       ↓
A2 →  PE20 →  PE21 →  PE22 →  PE23
       ↓       ↓       ↓       ↓
A3 →  PE30 →  PE31 →  PE32 →  PE33
```

Each PE performs: `accumulator += a_in × b_in`  
Total cycles for 4×4 multiply: **10 clock cycles** (same principle as Google TPUs)

---

## 📄 License

MIT
