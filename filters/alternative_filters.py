"""
alternative_filters.py
======================
Five alternative filtering techniques for drone trajectory tracking.
Each filter is designed to be a drop-in alternative to the Kalman Filter,
accepting the same noisy (x, y) measurements and returning position estimates.

All implementations use only NumPy — no specialised frameworks.

Filters included:
    1. MovingAverageFilter    — sliding window mean
    2. LeastSquaresFilter     — rolling polynomial regression (degree 2)
    3. ComplementaryFilter    — heuristic sensor-fusion blend
    4. MedianFilter           — sliding window median
"""

import numpy as np
from collections import deque


# ─────────────────────────────────────────────
# 1. MOVING AVERAGE FILTER
# ─────────────────────────────────────────────

class MovingAverageFilter:
    """
    Smooths position estimates by averaging the last `window` measurements.

    Limitations vs Kalman Filter
    ----------------------------
    - Fixed lag of window/2 timesteps — lags behind fast manoeuvres.
    - All samples in the window carry equal weight regardless of age.
    - No motion model → cannot predict ahead.
    - No uncertainty quantification.
    """

    def __init__(self, window: int = 10):
        self.window = window
        self._buf_x = deque(maxlen=window)
        self._buf_y = deque(maxlen=window)

    def step(self, x_meas: float, y_meas: float):
        self._buf_x.append(x_meas)
        self._buf_y.append(y_meas)
        return float(np.mean(self._buf_x)), float(np.mean(self._buf_y))

# ─────────────────────────────────────────────
# 2. LEAST SQUARES POLYNOMIAL FILTER
# ─────────────────────────────────────────────

class LeastSquaresFilter:
    """
    Fits a degree-`deg` polynomial to the last `window` measurements using
    NumPy least squares, then evaluates it at the latest timestep.

    Limitations vs Kalman Filter
    ----------------------------
    - Batch method: reprocesses the entire window every step — O(window)
      per update vs O(1) for Kalman.
    - Polynomial extrapolation diverges quickly for non-polynomial motion
      (e.g., banking turns, sudden stops).
    - No probabilistic noise model; all measurements treated equally.
    - Requires at least `deg + 1` samples before producing a fitted output;
      falls back to the raw measurement until then.
    """

    def __init__(self, window: int = 20, deg: int = 2):
        self.window = window
        self.deg = deg
        self._buf_x = deque(maxlen=window)
        self._buf_y = deque(maxlen=window)
        self._t_buf = deque(maxlen=window)
        self._t = 0

    def step(self, x_meas: float, y_meas: float):
        self._buf_x.append(x_meas)
        self._buf_y.append(y_meas)
        self._t_buf.append(self._t)
        self._t += 1

        n = len(self._buf_x)

        # Need at least deg+1 points to fit the polynomial
        if n < self.deg + 1:
            return x_meas, y_meas

        t_arr = np.array(self._t_buf)
        t_norm = t_arr - t_arr[-1]          # centre around current time

        coeffs_x = np.polyfit(t_norm, np.array(self._buf_x), self.deg)
        coeffs_y = np.polyfit(t_norm, np.array(self._buf_y), self.deg)

        # Evaluate polynomial at current time (t_norm = 0)
        x_est = float(np.polyval(coeffs_x, 0.0))
        y_est = float(np.polyval(coeffs_y, 0.0))

        return x_est, y_est


# ─────────────────────────────────────────────
# 3. COMPLEMENTARY FILTER
# ─────────────────────────────────────────────

class ComplementaryFilter:
    """
    Blends a dead-reckoning (model-based) prediction with the raw GPS
    measurement using a fixed ratio α:

        x̂_t = α · (x̂_{t−1} + v̂ · dt)  +  (1 − α) · z_t

    Velocity v̂ is estimated as the finite difference of recent measurements.

    Parameters
    ----------
    alpha : float in [0, 1]
        Weight given to the model prediction.
        High α → trust the model (smooth but may drift).
        Low α → trust GPS (accurate but noisy).
    dt : float
        Timestep in seconds.

    Limitations vs Kalman Filter
    ----------------------------
    - α is hand-tuned and static; no covariance tracking.
    - Velocity is a crude finite difference — no noise filtering.
    - Only blends two information sources; cannot generalise to N sensors.
    - No formal uncertainty estimate or optimality guarantee.
    """

    def __init__(self, alpha: float = 0.7, dt: float = 0.01):
        if not (0 <= alpha <= 1):
            raise ValueError("alpha must be in [0, 1]")
        self.alpha = alpha
        self.dt = dt
        self._x_hat = None
        self._y_hat = None
        self._vx = 0.0
        self._vy = 0.0

    def step(self, x_meas: float, y_meas: float):
        if self._x_hat is None:
            self._x_hat = x_meas
            self._y_hat = y_meas
            return self._x_hat, self._y_hat

        # Dead-reckoning prediction
        x_pred = self._x_hat + self._vx * self.dt
        y_pred = self._y_hat + self._vy * self.dt

        # Fuse prediction with measurement
        x_fused = self.alpha * x_pred + (1 - self.alpha) * x_meas
        y_fused = self.alpha * y_pred + (1 - self.alpha) * y_meas

        # Update crude velocity estimate from fused positions
        self._vx = (x_fused - self._x_hat) / self.dt
        self._vy = (y_fused - self._y_hat) / self.dt

        self._x_hat = x_fused
        self._y_hat = y_fused

        return self._x_hat, self._y_hat


# ─────────────────────────────────────────────
# 4. MEDIAN FILTER
# ─────────────────────────────────────────────

class MedianFilter:
    """
    Replaces each measurement with the median of the last `window` samples.

    Excellent for eliminating impulsive (spike) outliers but poor at
    handling the Gaussian noise that dominates real drone sensors.

    Limitations vs Kalman Filter
    ----------------------------
    - Non-linear and non-predictive; purely a smoothing operation.
    - Introduces a lag of window//2 timesteps.
    - Ineffective against Gaussian noise (the dominant sensor noise type).
    - No motion model, no uncertainty estimate, no multi-sensor fusion.
    """

    def __init__(self, window: int = 11):
        self.window = window
        self._buf_x = deque(maxlen=window)
        self._buf_y = deque(maxlen=window)

    def step(self, x_meas: float, y_meas: float):
        self._buf_x.append(x_meas)
        self._buf_y.append(y_meas)
        return float(np.median(self._buf_x)), float(np.median(self._buf_y))
