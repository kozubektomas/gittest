import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig, axis = plt.subplots()
axis.plot(x, y, 'r-', label='sin(x)')
axis.set_xlabel('x')
axis.set_ylabel('y')
axis.set_title('Testovací graf')
axis.grid(True, linestyle='--', color='lightgrey')
axis.legend()

# Přesunutí os do bodu (0,0)
axis.spines['left'].set_position('zero')
axis.spines['bottom'].set_position('zero')
axis.spines['right'].set_color('none')
axis.spines['top'].set_color('none')

plt.show()
