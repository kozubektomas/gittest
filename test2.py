import numpy as np
import matplotlib.pyplot as plt

def plot_sin_cx(c):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(c * x)

    fig, axis = plt.subplots()
    axis.plot(x, y, 'r-', label=f'sin({c}*x)')
    axis.set_xlabel('x')
    axis.set_ylabel('y')
    axis.set_title(f'Graf funkce sin({c}*x)')
    axis.grid(True, linestyle='--', color='lightgrey')
    axis.legend()

    # Přesunutí os do bodu (0,0)
    axis.spines['left'].set_position('zero')
    axis.spines['bottom'].set_position('zero')
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')

    plt.show()

# Příklad použití s parametrem c
c = 2  # Zde můžete změnit hodnotu parametru c
plot_sin_cx(c)