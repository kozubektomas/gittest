"""
Tento kód řeší Poissonovu úlohu (-\Delta u(x, y) = f(x, y)) na obdélníku ((0, Lx) \times (0, Ly)) 
s Dirichletovými okrajovými podmínkami pomocí metody konečných diferencí. 
Výsledné řešení je vykresleno pomocí konturového grafu v Matplotlibu.
"""

import numpy as np
import matplotlib.pyplot as plt

def poisson_2d(Lx, Ly, Nx, Ny, f, u_left, u_right, u_bottom, u_top):
    # Diskretizace intervalu (0, Lx) a (0, Ly)
    x = np.linspace(0, Lx, Nx+1)
    y = np.linspace(0, Ly, Ny+1)
    hx = Lx / Nx
    hy = Ly / Ny

    # Matice a vektor pravé strany
    A = np.zeros(((Nx-1)*(Ny-1), (Nx-1)*(Ny-1)))
    b = np.zeros((Nx-1)*(Ny-1))

    # Naplnění matice A a vektoru b
    for j in range(1, Ny):
        for i in range(1, Nx):
            k = (j-1)*(Nx-1) + (i-1)
            A[k, k] = -2/hx**2 - 2/hy**2
            if i > 1:
                A[k, k-1] = 1/hx**2
            if i < Nx-1:
                A[k, k+1] = 1/hx**2
            if j > 1:
                A[k, k-(Nx-1)] = 1/hy**2
            if j < Ny-1:
                A[k, k+(Nx-1)] = 1/hy**2
            b[k] = f(x[i], y[j])

    # Dirichletovy okrajové podmínky
    for i in range(1, Nx):
        b[i-1] -= u_bottom(x[i]) / hy**2
        b[(Ny-2)*(Nx-1) + (i-1)] -= u_top(x[i]) / hy**2
    for j in range(1, Ny):
        b[(j-1)*(Nx-1)] -= u_left(y[j]) / hx**2
        b[(j-1)*(Nx-1) + (Nx-2)] -= u_right(y[j]) / hx**2

    # Řešení soustavy rovnic
    u_inner = np.linalg.solve(A, b)

    # Rekonstrukce řešení včetně okrajových podmínek
    u = np.zeros((Ny+1, Nx+1))
    u[0, :] = u_bottom(x)
    u[-1, :] = u_top(x)
    u[:, 0] = u_left(y)
    u[:, -1] = u_right(y)
    for j in range(1, Ny):
        for i in range(1, Nx):
            u[j, i] = u_inner[(j-1)*(Nx-1) + (i-1)]

    # Vykreslení nenulových prvků matice A
    plt.figure()
    plt.spy(A, markersize=1)
    plt.title('Nenulové prvky matice A')
    plt.show()

    return x, y, u

# Definice parametrů
Lx = 1
Ly = 1
Nx = 20
Ny = 20
f = lambda x, y: -2 * (np.pi**2) * np.sin(np.pi * x) * np.sin(np.pi * y)
u_left = lambda y: 0
u_right = lambda y: 0
u_bottom = lambda x: 0
u_top = lambda x: np.sin(np.pi*x/Lx)

# Řešení Poissonovy úlohy
x, y, u = poisson_2d(Lx, Ly, Nx, Ny, f, u_left, u_right, u_bottom, u_top)

# Vykreslení výsledného řešení
X, Y = np.meshgrid(x, y)
plt.contourf(X, Y, u, 20, cmap='viridis')
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Řešení Poissonovy úlohy ve 2D')
plt.show()

# Vykreslení výsledného řešení - 3D povrchový graf
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, u, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u(x, y)')
ax.set_title('Řešení Poissonovy úlohy ve 2D - 3D povrchový graf')
plt.show()

