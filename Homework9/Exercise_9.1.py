import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)

plt.figure(figsize=(8, 5))

plt.plot(x, y1, color='red', linestyle='-', label='sin(x)')
plt.plot(x, y2, color='green', linestyle='--', label='cos(x)')
plt.plot(x, y3, color='blue', linestyle=':', label='exp(-x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykresy funkcji')
plt.legend()

plt.grid(True)

plt.show()
