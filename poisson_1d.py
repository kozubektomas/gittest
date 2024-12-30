"""
Tento kód řeší Poissonovu úlohu (-u''(x) = f(x)) na intervalu ((a, b)) 
s Dirichletovými okrajovými podmínkami (u(a) = ua) a (u(b) = ub) pomocí metody 
konečných diferencí. Výsledné řešení je vykresleno pomocí Matplotlibu.
"""
import numpy as np
import matplotlib.pyplot as plt

def poisson_1d(a, b, N, f, ua, ub):
    # Diskretizace intervalu (a, b)
    x = np.linspace(a, b, N+1)
    h = (b - a) / N

    # Matice a vektor pravé strany
    A = np.zeros((N-1, N-1))
    b = np.zeros(N-1)

    # Naplnění matice A a vektoru b
    for i in range(N-1):
        if i > 0:
            A[i, i-1] = 1 / h**2
        A[i, i] = -2 / h**2
        if i < N-2:
            A[i, i+1] = 1 / h**2
        b[i] = f(x[i+1])

    # Dirichletovy okrajové podmínky
    b[0] -= ua / h**2
    b[-1] -= ub / h**2

    # Řešení soustavy rovnic
    u = np.zeros(N+1)
    u[1:N] = np.linalg.solve(A, b)
    u[0] = ua
    u[-1] = ub

    return x, u

# Definice parametrů
a = 0
b = 1
N = 10
f = lambda x: -np.pi**2 * np.sin(np.pi * x)
ua = 0
ub = 0

# Řešení Poissonovy úlohy
x, u = poisson_1d(a, b, N, f, ua, ub)

# Vykreslení výsledného řešení
plt.plot(x, u, 'r-', label='Numerické řešení')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Řešení Poissonovy úlohy v 1D')
plt.legend()
plt.grid(True)
plt.show()