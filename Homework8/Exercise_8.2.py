# (a) Create an arbitrary one dimensional array called v1.
v1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print("8.2 (a) v1:", v1)

# (b) Create a new array (or a view) v2 which consists of items with odd indices of v1.
v2 = v1[1::2]
print("8.2 (b) v2 (odd indices):", v2)

# (c) Create a new array (or a view) v3 in backwards ordering from v1. 
v3 = v1[::-1]
print("8.2 (c) v3 (reversed):", v3)
