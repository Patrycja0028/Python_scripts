# (a) Create a two dimensional array called m1, shape=(4,5).
m1 = np.arange(20).reshape(4, 5)
print("(a) m1:\n", m1)

# (b) Create a new array (or a view) m2 from m1, in which the elements of each row are in reverse order.
m2 = m1[:, ::-1]
print("(b) m2 (rows reversed):\n", m2)

# (c) Create a new array (or a view) m3 from m1, in which the elements of each column are in reverse order.
m3 = m1[::-1, :]
print("(c) m3 (cols reversed):\n", m3)

# (d) Remove the first row, the last row, the first column, and the last column of m1, and create a new array (or a view) m4. 
m4 = m1[1:-1, 1:-1]
print("(d) m4 (cropped):\n", m4)
