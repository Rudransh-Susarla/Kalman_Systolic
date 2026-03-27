"""
kalman_python.py
================
Classic Kalman Filter implemented entirely in pure Python.

NO NumPy. NO external libraries.
All matrix operations use lists of lists and the
python_matrix module written from scratch.

State vector: X = [x, y, vx, vy]^T
Measurement:  z = [x_meas, y_meas]^T
"""

from utils.python_matrix import (
    mat_zeros, mat_eye, mat_scale,
    mat_add, mat_sub,
    mat_mul, mat_transpose, mat_inv
)


class KalmanFilterPython:
    """
    Standard Kalman Filter using pure Python matrix operations.

    Serves as the classical baseline — compared against the
    systolic array accelerated version. No NumPy used anywhere.
    """

    def __init__(self, dt=0.01):

        # -----------------------------------------------
        # State vector: [x, y, vx, vy]^T   (4×1)
        # -----------------------------------------------
        self.X = [[0.0], [0.0], [0.0], [0.0]]

        # -----------------------------------------------
        # State covariance matrix P         (4×4)
        # -----------------------------------------------
        self.P = mat_eye(4)

        # -----------------------------------------------
        # State transition matrix A         (4×4)
        # Models constant-velocity motion:
        #   x  ← x  + vx * dt
        #   y  ← y  + vy * dt
        #   vx ← vx
        #   vy ← vy
        # -----------------------------------------------
        self.A = [
            [1.0, 0.0,  dt, 0.0],
            [0.0, 1.0, 0.0,  dt],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ]

        # -----------------------------------------------
        # Measurement matrix H              (2×4)
        # We observe only x and y positions:
        #   z = H × X  →  extracts [x, y] from state
        # -----------------------------------------------
        self.H = [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0]
        ]

        # -----------------------------------------------
        # Process noise covariance Q        (4×4)
        # Low value → trust the model more
        # -----------------------------------------------
        self.Q = mat_scale(mat_eye(4), 0.01)

        # -----------------------------------------------
        # Measurement noise covariance R    (2×2)
        # Represents sensor (GPS) noise level
        # -----------------------------------------------
        self.R = mat_scale(mat_eye(2), 0.1)

        # -----------------------------------------------
        # Identity matrix                   (4×4)
        # -----------------------------------------------
        self.I = mat_eye(4)


    # ---------------------------------------------------
    # PREDICTION STEP
    # ---------------------------------------------------

    def predict(self):
        """
        Project state and covariance forward one timestep.

        X = A × X
        P = A × P × Aᵀ + Q
        """
        A = self.A

        # Predict state
        self.X = mat_mul(A, self.X)

        # Predict covariance
        AP   = mat_mul(A, self.P)
        APAT = mat_mul(AP, mat_transpose(A))
        self.P = mat_add(APAT, self.Q)


    # ---------------------------------------------------
    # UPDATE STEP
    # ---------------------------------------------------

    def update(self, z):
        """
        Correct the prediction using a new measurement z.

        z: measurement as a (2×1) list of lists [[x], [y]]

        S = H × P × Hᵀ + R          (innovation covariance)
        K = P × Hᵀ × S⁻¹            (Kalman gain)
        y = z - H × X               (innovation / residual)
        X = X + K × y               (state update)
        P = (I - K × H) × P         (covariance update)
        """
        H = self.H
        P = self.P

        # Innovation covariance (2×2)
        HP  = mat_mul(H, P)
        HPH = mat_mul(HP, mat_transpose(H))
        S   = mat_add(HPH, self.R)

        # Kalman gain (4×2)
        PHT = mat_mul(P, mat_transpose(H))
        K   = mat_mul(PHT, mat_inv(S))

        # Innovation — difference between measurement and prediction
        HX = mat_mul(H, self.X)
        y  = mat_sub(z, HX)

        # Corrected state
        Ky = mat_mul(K, y)
        self.X = mat_add(self.X, Ky)

        # Corrected covariance
        KH = mat_mul(K, H)
        self.P = mat_mul(mat_sub(self.I, KH), P)


    # ---------------------------------------------------
    # FULL STEP
    # ---------------------------------------------------

    def step(self, z):
        """
        Run one full Kalman iteration: Predict → Update.

        Parameters
        ----------
        z : list of lists [[x_meas], [y_meas]]
            New measurement at this timestep.

        Returns
        -------
        (x_est, y_est) : tuple of floats
            Filtered position estimate.
        """
        self.predict()
        self.update(z)

        return self.X[0][0], self.X[1][0]
