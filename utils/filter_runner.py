import time
import numpy as np

def run_filter(filter_obj, x_meas, y_meas, filter_type="alternative"):
    """
    Runs a filter over the full measurement sequence.

    Parameters
    ----------
    filter_obj  : object with a .step() method
    x_meas      : noisy X measurement array
    y_meas      : noisy Y measurement array
    filter_type : str — "pure", "systolic", or "alternative"

    Returns
    -------
    est_x, est_y : np.ndarray of position estimates
    elapsed      : wall-clock runtime in seconds
    """
    est_x, est_y = [], []
    t0 = time.perf_counter()

    steps = len(x_meas)

    for k in range(steps):
        if filter_type == "pure":
            z = [[float(x_meas[k])], [float(y_meas[k])]]
            ex, ey = filter_obj.step(z)
        elif filter_type == "systolic":
            z = np.array([[x_meas[k]], [y_meas[k]]])
            ex, ey = filter_obj.step(z)
        else:
            # alternative expecting floating values directly
            ex, ey = filter_obj.step(float(x_meas[k]), float(y_meas[k]))

        est_x.append(ex)
        est_y.append(ey)

    elapsed = time.perf_counter() - t0
    return np.array(est_x), np.array(est_y), elapsed
