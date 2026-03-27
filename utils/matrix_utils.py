import numpy as np


def pad_to_4x4(M):
    """
    Pads a matrix to 4×4 with zeros.

    This is required because the systolic array accelerator
    operates on fixed 4×4 matrices.

    Parameters
    ----------
    M : numpy.ndarray
        Input matrix of shape (r, c)

    Returns
    -------
    padded : numpy.ndarray
        4×4 padded matrix
    """

    M = np.asarray(M, dtype=np.float32)

    rows, cols = M.shape

    padded = np.zeros((4, 4), dtype=np.float32)

    padded[:rows, :cols] = M

    return padded


def unpad(M, rows, cols):
    """
    Removes padding from a 4×4 matrix.

    Parameters
    ----------
    M : numpy.ndarray
        4×4 matrix from systolic accelerator

    rows : int
        original number of rows

    cols : int
        original number of columns

    Returns
    -------
    numpy.ndarray
        matrix of shape (rows, cols)
    """

    M = np.asarray(M, dtype=np.float32)

    return M[:rows, :cols]
