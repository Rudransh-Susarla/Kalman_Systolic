import numpy as np
import subprocess
import os


def pad_matrix(M):
    """Pad any matrix up to 4x4 with zeros."""
    P = np.zeros((4, 4), dtype=float)
    r, c = M.shape
    P[:r, :c] = M
    return P


def systolic_multiply(A, B):
    """
    Multiply two matrices (up to 4x4) using the Verilator systolic array.

    Inputs are written as full float64 values — no fixed-point encoding.
    Results are read back as float64 with full precision (%.17g in Verilog).
    The output is sliced back to the original result shape before returning.
    """
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    ra, ca = A.shape
    rb, cb = B.shape

    # This file lives at project/systolic/systolic_array_python.py
    # obj_dir is at         project/systolic/obj_dir/
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    obj_dir     = os.path.join(script_dir, "obj_dir")
    input_path  = os.path.join(obj_dir, "input.txt")
    output_path = os.path.join(obj_dir, "output.txt")

    # Write padded matrices as plain float64 — 17 significant digits
    A_pad = pad_matrix(A)
    B_pad = pad_matrix(B)

    with open(input_path, "w") as f:
        for row in A_pad:
            f.write(" ".join(f"{v:.17g}" for v in row) + "\n")
        for row in B_pad:
            f.write(" ".join(f"{v:.17g}" for v in row) + "\n")

    # Run Verilator binary from obj_dir so $fopen("input.txt") resolves
    result = subprocess.run(
        ["./Vsystolic_array"],
        cwd=obj_dir,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Verilator simulation failed:\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )

    # Read full-precision float64 results
    C = []
    with open(output_path) as f:
        for line in f:
            line = line.strip()
            if line:
                C.append(list(map(float, line.split())))

    C = np.array(C)  # shape (4, 4)

    # Slice back to the correct output shape
    return C[:ra, :cb]
