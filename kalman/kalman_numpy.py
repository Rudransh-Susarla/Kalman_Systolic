import numpy as np


class KalmanFilterNumPy:
    """
    Standard Kalman Filter implementation using NumPy.
    This serves as the reference baseline for correctness
    and performance comparison against the systolic version.
    """

    def __init__(self, dt=0.01):

        # State vector: [x, y, vx, vy]^T
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

        # Measurement matrix (we observe x and y only)
        self.H = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ])

        # Process noise covariance
        self.Q = np.eye(4) * 0.01

        # Measurement noise covariance
        self.R = np.eye(2) * 0.1

        # Identity matrix (used in covariance update)
        self.I = np.eye(4)


    def step(self, z):
        """
        Performs one full Kalman filter iteration:
        Prediction + Update
        """

        A, H, Q, R = self.A, self.H, self.Q, self.R

        # -----------------------------
        # Prediction
        # -----------------------------

        # State prediction
        self.X = A @ self.X

        # Covariance prediction
        self.P = A @ self.P @ A.T + Q

        # -----------------------------
        # Update
        # -----------------------------

        # Innovation covariance
        S = H @ self.P @ H.T + R

        # Kalman gain
        K = self.P @ H.T @ np.linalg.inv(S)

        # Innovation (measurement residual)
        y = z - H @ self.X

        # State update
        self.X = self.X + K @ y

        # Covariance update
        self.P = (self.I - K @ H) @ self.P

        return self.X[0, 0], self.X[1, 0]
