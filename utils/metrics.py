import numpy as np


def rmse(pred_x, pred_y, true_x, true_y):
    """
    Computes Root Mean Square Error (RMSE) between
    predicted and true drone trajectories.

    Parameters
    ----------
    pred_x : array-like
        Predicted X positions

    pred_y : array-like
        Predicted Y positions

    true_x : array-like
        Ground truth X positions

    true_y : array-like
        Ground truth Y positions

    Returns
    -------
    float
        RMSE value
    """

    pred_x = np.asarray(pred_x)
    pred_y = np.asarray(pred_y)
    true_x = np.asarray(true_x)
    true_y = np.asarray(true_y)

    n = len(pred_x)

    if n == 0:
        raise ValueError("Prediction arrays are empty.")

    if len(pred_y) != n:
        raise ValueError("pred_x and pred_y must have the same length.")

    # Compute Euclidean error per timestep
    error = np.sqrt(
        (pred_x - true_x[:n])**2 +
        (pred_y - true_y[:n])**2
    )

    # Return mean RMSE
    return np.mean(error)
