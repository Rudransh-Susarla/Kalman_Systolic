import numpy as np

# C-based systolic accelerator
from systolic.systolic_array_c import SystolicArray4x4

from utils.matrix_utils import pad_to_4x4, unpad


class KalmanFilterSystolic:
    """
    Kalman Filter using a 4×4 systolic array accelerator
    for all matrix multiplications.
    """

    def __init__(self, dt=0.01):

        # Systolic array accelerator
        self.sa = SystolicArray4x4()

        # State vector [x, y, vx, vy]^T
        self.X = np.zeros((4, 1))

        # Covariance matrix
        self.P = np.eye(4)

        # State transition matrix
        self.A = np.array([
            [1, 0, dt, 0],
            [0, 1, 0, dt],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        # Measurement matrix
        self.H = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ])

        # Process noise
        self.Q = np.eye(4) * 0.01

        # Measurement noise
        self.R = np.eye(2) * 0.1

        # Identity matrix
        self.I = np.eye(4)


    # -------------------------------------------------
    # Matrix multiply using systolic accelerator
    # -------------------------------------------------

    def _matmul(self, A, B):

        ra, ca = A.shape
        rb, cb = B.shape

        A_pad = pad_to_4x4(A)
        B_pad = pad_to_4x4(B)

        C_pad = self.sa.multiply(A_pad, B_pad)

        return unpad(C_pad, ra, cb)


    # -------------------------------------------------
    # Prediction step
    # -------------------------------------------------

    def predict(self):

        # X = A X
        self.X = self._matmul(self.A, self.X)

        # P = A P A^T + Q
        AP = self._matmul(self.A, self.P)

        APAT = self._matmul(AP, self.A.T)

        self.P = APAT + self.Q


    # -------------------------------------------------
    # Update step
    # -------------------------------------------------

    def update(self, z):

        H = self.H
        P = self.P

        # S = H P H^T + R
        HP = self._matmul(H, P)
        HPH = self._matmul(HP, H.T)

        S = HPH + self.R

        # Kalman Gain
        PHT = self._matmul(P, H.T)

        S_inv = np.linalg.inv(S)

        K = self._matmul(PHT, S_inv)

        # Innovation
        HX = self._matmul(H, self.X)

        y = z - HX

        # State update
        Ky = self._matmul(K, y)

        self.X = self.X + Ky

        # Covariance update
        KH = self._matmul(K, H)

        self.P = self._matmul(self.I - KH, P)


    # -------------------------------------------------
    # Full Kalman step
    # -------------------------------------------------

    def step(self, z):

        self.predict()

        self.update(z)

        return self.X[0, 0], self.X[1, 0]
