#Let p=(x,y) be a point in a plane. Define the following functions using lambda:
#(a) a test if p is in unit (filled) circle,
#(b) a test if the coordinates of p are positive,
#(c) a sorting key (y decreasing, x increasing),
#(d) a sorting key (the sum |x|+|y|).

#Using tests: list(filter((lambda p: ...), point_list))
#Using sorting keys: point_list.sort(key=lambda p: ...)

# a)
is_in_circle = lambda p: p[0]**2 + p[1]**2 <= 1
is_in_circle(p)  #False
is_in_circle((1,1))  #False
is_in_circle((0,1))  #True
is_in_circle((0,0))  #True

# b)
is_positive = lambda p: p[0] > 0 and p[1] > 0
is_positive((0,0))  # False
is_positive((1,1))  #True
is_positive((1,-1))  #False

# c)
key1 = lambda p: (-p[1], p[0])

# d)
key2 = lambda p: abs(p[0]) + abs(p[1])

### usage
points = [(0,0), (1,1), (0.5,0.5), (-1,2)]

#inside
list(filter(is_in_circle, points)) # [(0, 0), (0.5, 0.5)]
#positive
list(filter(is_positive, points)) # [(1, 1), (0.5, 0.5)]

# sort by key1
points.sort(key=key1)
print(points)  #[(-1, 2), (1, 1), (0.5, 0.5), (0, 0)]

#sort by key2
points.sort(key=key2)
print(points)  #[(0, 0), (0.5, 0.5), (1, 1), (-1, 2)]
