#include <stdio.h>
#include <omp.h>

#define N 4

typedef struct
{
    float a_reg;
    float b_reg;
    float c_acc;
} PE;

void systolic_multiply(float A[N][N], float B[N][N], float C[N][N])
{
    PE pe[N][N];

    int i, j, t;

    // Initialize
    #pragma omp parallel for collapse(2)
    for(i = 0; i < N; i++)
    {
        for(j = 0; j < N; j++)
        {
            pe[i][j].a_reg = 0.0f;
            pe[i][j].b_reg = 0.0f;
            pe[i][j].c_acc = 0.0f;
        }
    }

    int cycles = 3 * N - 2;

    for(t = 0; t < cycles; t++)
    {
        // Inject A
        for(i = 0; i < N; i++)
        {
            if(t < N)
                pe[i][0].a_reg = A[i][t];
            else
                pe[i][0].a_reg = 0.0f;
        }

        // Inject B
        for(j = 0; j < N; j++)
        {
            if(t < N)
                pe[0][j].b_reg = B[t][j];
            else
                pe[0][j].b_reg = 0.0f;
        }

        // 🔥 PARALLEL COMPUTE (main speedup)
        #pragma omp parallel for collapse(2)
        for(i = 0; i < N; i++)
        {
            for(j = 0; j < N; j++)
            {
                pe[i][j].c_acc += pe[i][j].a_reg * pe[i][j].b_reg;
            }
        }

        // Propagation (must stay sequential order!)
        for(i = N - 1; i >= 0; i--)
        {
            for(j = N - 1; j >= 0; j--)
            {
                if(j + 1 < N)
                    pe[i][j + 1].a_reg = pe[i][j].a_reg;

                if(i + 1 < N)
                    pe[i + 1][j].b_reg = pe[i][j].b_reg;
            }
        }
    }

    // Collect result
    #pragma omp parallel for collapse(2)
    for(i = 0; i < N; i++)
    {
        for(j = 0; j < N; j++)
        {
            C[i][j] = pe[i][j].c_acc;
        }
    }
}