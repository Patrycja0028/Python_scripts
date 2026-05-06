# Generate n=100 random points in a unit square [0,1]x[0,1]. Points are green if the distance from (0,0) is less then 1; they are red otherwise. The marker area of a point (x,y) should be proportional to |x|+|y|. 

#import numpy as np
#import matplotlib.pyplot as plt

n = 100

x = np.random.rand(n)
y = np.random.rand(n)

distance = np.sqrt(x**2 + y**2)

colors = ['green' if d < 1 else 'red' for d in distance]

sizes = (np.abs(x) + np.abs(y)) * 200

plt.figure(figsize=(6, 6))

plt.scatter(x, y, c=colors, s=sizes)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Random points in a unit square')

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.grid(True)
plt.gca().set_aspect('equal')

plt.show()
