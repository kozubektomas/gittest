import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig, axis = plt.subplots()
axis.plot(x, y, 'r-', label='sin(x)')
axis.set_xlabel('x')
axis.set_ylabel('y')
axis.set_title('Testovací graf')
axis.grid(True)
axis.legend()

plt.show()
