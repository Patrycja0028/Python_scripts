# Create a function that calculates, for the point (x,y), the sum of distances from two points in the plane: (-1,0) and (1,0). Show the function values using imshow(). 

#import numpy as np
#import matplotlib.pyplot as plt

def distance_sum(x, y):
    d1 = np.sqrt((x + 1)**2 + y**2)
    d2 = np.sqrt((x - 1)**2 + y**2)
    return d1 + d2

x = np.linspace(-3, 3, 500)
y = np.linspace(-3, 3, 500)

X, Y = np.meshgrid(x, y)

Z = distance_sum(X, Y)

plt.figure(figsize=(8, 6))

img = plt.imshow(
    Z,
    extent=[-3, 3, -3, 3],
    origin='lower',
    cmap='viridis'
)

plt.colorbar(img, label='Suma odległości')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Suma odległości od punktów (-1,0) i (1,0)')

plt.show()
