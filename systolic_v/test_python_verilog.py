import numpy as np
from systolic_array_python import systolic_multiply


A = np.array([
[1,2,3,4],
[5,6,7,8],
[1,1,1,1],
[2,2,2,2]
])

B = np.array([
[1,0,0,1],
[0,1,1,0],
[1,0,1,0],
[0,1,0,1]
])

C = systolic_multiply(A,B)

print("Result from Verilog")
print(C)
