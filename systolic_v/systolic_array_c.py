import ctypes
import numpy as np
import os


class SystolicArray4x4:
    """
    Python wrapper for the 4x4 C systolic array accelerator.
    Uses ctypes to call the compiled systolic.dll library.
    """

    def __init__(self):

        # Get path of this file
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Path to compiled DLL
        dll_path = os.path.join(current_dir, "systolic.dll")

        # Load the C library
        self.lib = ctypes.CDLL(dll_path)

        # Define 4x4 float matrix type
        self.Matrix4x4 = (ctypes.c_float * 4) * 4

        # Define argument types of C function
        self.lib.systolic_multiply.argtypes = [
            self.Matrix4x4,
            self.Matrix4x4,
            self.Matrix4x4
        ]


    def multiply(self, A, B):
        """
        Perform 4x4 matrix multiplication using the C systolic array.
        """

        # Ensure numpy float32 arrays
        A = np.asarray(A, dtype=np.float32)
        B = np.asarray(B, dtype=np.float32)

        # Convert numpy arrays to C arrays
        A_c = self.Matrix4x4(*[tuple(row) for row in A])
        B_c = self.Matrix4x4(*[tuple(row) for row in B])

        C_c = self.Matrix4x4()

        # Call C function
        self.lib.systolic_multiply(A_c, B_c, C_c)

        # Convert result back to numpy
        C = np.array([[C_c[i][j] for j in range(4)] for i in range(4)],
                     dtype=np.float32)

        return C
