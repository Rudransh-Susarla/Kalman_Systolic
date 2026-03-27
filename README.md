# Drone Path Tracking — Kalman Filter + 4×4 Systolic Array

A Python project that tracks drone trajectories using a **Kalman Filter** accelerated by a **hardware-inspired 4×4 Systolic Array**, benchmarked against a standard NumPy implementation.

---

## 📌 Overview

| Feature | Details |
|--------|---------|
| Dataset | EuRoC MAV — `MH_03_medium` |
| Filter | 2D Kalman Filter (x, y, vx, vy) |
| Accelerator | 4×4 Systolic Array (C + OpenMP, compiled to DLL) |
| Baseline | Standard NumPy matrix operations |
| Metric | RMSE (metres) |

---

## 🗂️ Project Structure

```
Project_3/
├── main.py                    # Entry point
├── kalman/
│   ├── kalman_numpy.py        # NumPy Kalman Filter (reference)
│   └── kalman_systolic.py     # Systolic accelerated Kalman Filter
├── systolic/
│   ├── systolic_array.c       # C implementation of 4×4 systolic array
│   ├── systolic_array.h       # Header file
│   └── systolic_array_c.py    # Python ctypes wrapper
├── utils/
│   ├── dataset_loader.py      # Load EuRoC CSV + add noise
│   ├── matrix_utils.py        # Pad/unpad matrices
│   ├── metrics.py             # RMSE calculation
│   ├── diagram.py             # ASCII architecture diagram
│   └── visualization.py      # Matplotlib plots
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

```bash
python main.py
```

---

## 📊 Output

- Console summary: RMSE, runtime, speedup ratio
- Saved plot: `drone_kalman_systolic.png`

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
