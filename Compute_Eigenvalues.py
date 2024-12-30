"""
Tento kód definuje funkci compute_and_plot_eigenvalues, která přijímá 
čtvercovou matici jako vstup, spočítá její vlastní čísla a vlastní vektory 
pomocí funkce np.linalg.eig z knihovny numpy, a vykreslí vlastní čísla pomocí Matplotlibu. 
Na konci kódu je příklad použití této funkce pro náhodně generovanou čtvercovou matici řádu N.
"""

import numpy as np
import matplotlib.pyplot as plt

def compute_and_plot_eigenvalues(matrix):
    # Výpočet vlastních čísel a vlastních vektorů
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    # Vykreslení vlastních čísel
    plt.figure()
    plt.scatter(eigenvalues.real, eigenvalues.imag, color='red', marker='o')
    plt.xlabel('Reálná část')
    plt.ylabel('Imaginární část')
    plt.title('Vlastní čísla matice')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()
    
    return eigenvalues, eigenvectors

# Příklad použití
N = 10
real_part = np.random.rand(N, N)
imaginary_part = np.random.rand(N, N)
matrix = real_part + 1j * imaginary_part  # Generování náhodné komplexní čtvercové matice řádu N

eigenvalues, eigenvectors = compute_and_plot_eigenvalues(matrix)

# Výpis výsledků
print("Vlastní čísla:")
print(eigenvalues)
print("Vlastní vektory:")
print(eigenvectors)