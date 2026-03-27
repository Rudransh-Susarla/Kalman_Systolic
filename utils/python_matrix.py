"""
python_matrix.py
================
Pure Python matrix operations using lists of lists.
No NumPy, no external libraries — classic linear algebra from scratch.

Every matrix is represented as a list of rows:
    M = [[row0_col0, row0_col1, ...],
         [row1_col0, row1_col1, ...], ...]
"""


# -------------------------------------------------------
# Constructors
# -------------------------------------------------------

def mat_zeros(rows, cols):
    """Return a (rows × cols) zero matrix."""
    return [[0.0] * cols for _ in range(rows)]


def mat_eye(n):
    """Return an (n × n) identity matrix."""
    M = mat_zeros(n, n)
    for i in range(n):
        M[i][i] = 1.0
    return M


# -------------------------------------------------------
# Element-wise operations
# -------------------------------------------------------

def mat_add(A, B):
    """Element-wise addition: C = A + B"""
    rows, cols = len(A), len(A[0])
    return [[A[i][j] + B[i][j] for j in range(cols)]
            for i in range(rows)]


def mat_sub(A, B):
    """Element-wise subtraction: C = A - B"""
    rows, cols = len(A), len(A[0])
    return [[A[i][j] - B[i][j] for j in range(cols)]
            for i in range(rows)]


def mat_scale(A, s):
    """Scalar multiplication: C = s * A"""
    return [[A[i][j] * s for j in range(len(A[0]))]
            for i in range(len(A))]


# -------------------------------------------------------
# Matrix multiplication (classic O(n³) algorithm)
# -------------------------------------------------------

def mat_mul(A, B):
    """
    Classic triple-loop matrix multiplication: C = A × B

    A : (rA × cA)
    B : (cA × cB)
    C : (rA × cB)
    """
    rA = len(A)
    cA = len(A[0])
    cB = len(B[0])

    C = mat_zeros(rA, cB)

    for i in range(rA):
        for k in range(cA):
            a_ik = A[i][k]
            if a_ik == 0.0:          # Skip zero multiplications
                continue
            for j in range(cB):
                C[i][j] += a_ik * B[k][j]

    return C


# -------------------------------------------------------
# Transpose
# -------------------------------------------------------

def mat_transpose(A):
    """Return transposed matrix: C = Aᵀ"""
    rows = len(A)
    cols = len(A[0])
    return [[A[i][j] for i in range(rows)]
            for j in range(cols)]


# -------------------------------------------------------
# Matrix inverse (Gauss-Jordan elimination)
# -------------------------------------------------------

def mat_inv(A):
    """
    Compute the inverse of a square matrix using
    Gauss-Jordan elimination with partial pivoting.

    Returns A⁻¹ as a list of lists.
    Raises ValueError if the matrix is singular.
    """
    n = len(A)

    # Build augmented matrix [A | I]
    aug = []
    for i, row in enumerate(A):
        identity_row = [1.0 if i == j else 0.0 for j in range(n)]
        aug.append(row[:] + identity_row)

    for col in range(n):

        # --- Partial pivoting: find row with largest absolute value ---
        max_val = abs(aug[col][col])
        max_row = col
        for row in range(col + 1, n):
            if abs(aug[row][col]) > max_val:
                max_val = abs(aug[row][col])
                max_row = row

        if max_val < 1e-12:
            raise ValueError("Matrix is singular — cannot invert.")

        # Swap pivot row into place
        aug[col], aug[max_row] = aug[max_row], aug[col]

        # Scale pivot row so the diagonal becomes 1
        pivot = aug[col][col]
        aug[col] = [x / pivot for x in aug[col]]

        # Eliminate all other rows in this column
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = [aug[row][j] - factor * aug[col][j]
                            for j in range(2 * n)]

    # Extract the right half — that's A⁻¹
    return [row[n:] for row in aug]


# -------------------------------------------------------
# Utility: convert nested list → printable string
# -------------------------------------------------------

def mat_str(A, precision=4):
    """Pretty-print a matrix for debugging."""
    fmt = f"{{:.{precision}f}}"
    rows = ["  [" + ", ".join(fmt.format(v) for v in row) + "]"
            for row in A]
    return "[\n" + "\n".join(rows) + "\n]"
