import numpy as np
import pandas as pd
# Initialize matrix A and B
A = np.array([[1,2,4],[5,3,2]])
B = np.array([[1,3,4],[1,1,1]])
print(A)
print(B)
# Initialize constant s
s = 2

# See how element-wise addition works
add_AB = A + B
print(add_AB)

# See how scalar multiplication works
mult_As = A * s
print(mult_As)

# What happens if we have a Matrix + scalar?
add_As = A + s
print(add_As)

#