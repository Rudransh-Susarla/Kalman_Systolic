#ifndef SYSTOLIC_ARRAY_H
#define SYSTOLIC_ARRAY_H

#define N 4

/*
    4×4 Systolic Array Matrix Multiply

    Computes:
        C = A × B

    Inputs:
        A[N][N]  → first matrix
        B[N][N]  → second matrix

    Output:
        C[N][N]  → result matrix
*/

void systolic_multiply(float A[N][N], float B[N][N], float C[N][N]);

#endif
