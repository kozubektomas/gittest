"""
Tento kód definuje funkci plot_and_integrate, která přijímá funkci f, 
počáteční bod a a koncový bod b jako vstupy. Funkce vykreslí f(x) na intervalu (a, b) 
pomocí Matplotlibu a spočítá numericky určitý integrál z f(x) na intervalu (a, b) 
pomocí funkce quad z knihovny scipy.integrate. 
Na konci kódu je příklad použití této funkce pro výraz sin(x) * exp(x) na intervalu (0, π).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def plot_and_integrate(f, a, b):
    # Diskretizace intervalu (a, b)
    x = np.linspace(a, b, 1000)
    y = f(x)

    # Vykreslení funkce
    plt.plot(x, y, label=f'$f(x)$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Funkce $f(x)$ na intervalu ({a}, {b})')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Numerický výpočet určitého integrálu
    integral, error = quad(f, a, b)
    return integral, error

# Definice funkce f(x)
f = lambda x: np.sin(x) * np.exp(x)

# Definice intervalu
a = 0
b = np.pi

# Vykreslení funkce a výpočet integrálu
integral, error = plot_and_integrate(f, a, b)

# Výpis výsledků
print(f"Určitý integrál z f(x) na intervalu ({a}, {b}): {integral}")
print(f"Odhad chyby: {error}")