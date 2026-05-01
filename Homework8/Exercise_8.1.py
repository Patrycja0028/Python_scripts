# Create the following NumPy arrays:
# (a) float from 0.0 to 1.0 step 0.1, shape=(11,),
# (b) int zeros (1 byte) with shape=(5,6),
# (c) complex with shape=(9,), powers of x = complex(0, 1): 1, x, x**2, ..., x**8. 

import numpy as np

a = np.linspace(0.0, 1.0, 11)
print("(a):\n", a)

b = np.zeros((5, 6), dtype=np.int8)
print("(b) dtype:", b.dtype, "\n", b)

x = complex(0, 1)
powers = np.arange(9)
c = x ** powers
print("(c):\n", c)
