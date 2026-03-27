import pandas as pd
import numpy as np


def load_drone_data(csv_path, noise_std=0.3, seed=42):
    """
    Loads drone trajectory data and generates noisy measurements.

    Parameters
    ----------
    csv_path : str
        Path to the drone trajectory CSV file.

    noise_std : float
        Standard deviation of measurement noise.

    seed : int
        Random seed for reproducibility.

    Returns
    -------
    x_true : np.ndarray
        Ground truth X positions

    y_true : np.ndarray
        Ground truth Y positions

    x_meas : np.ndarray
        Noisy measured X positions

    y_meas : np.ndarray
        Noisy measured Y positions
    """

    # Load CSV
    df = pd.read_csv(csv_path)

    # Remove accidental spaces in column names
    df.columns = df.columns.str.strip()

    # Expected columns from dataset
    required_cols = ["p_RS_R_x [m]", "p_RS_R_y [m]"]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column in dataset: {col}")

    # Extract ground truth
    x_true = df["p_RS_R_x [m]"].to_numpy()
    y_true = df["p_RS_R_y [m]"].to_numpy()

    # Random generator
    rng = np.random.default_rng(seed)

    # Add measurement noise
    x_meas = x_true + rng.normal(0, noise_std, len(x_true))
    y_meas = y_true + rng.normal(0, noise_std, len(y_true))

    return x_true, y_true, x_meas, y_meas
