"""
Tento kód definuje funkci symbolic_calculations, která přijímá výraz f_expr jako vstup 
a vrací jeho derivaci a integrál. Funkce sp.diff se používá pro výpočet derivace 
a funkce sp.integrate pro výpočet integrálu. 
Na konci kódu je příklad použití této funkce pro výraz sin(x) * exp(x).
"""
import sympy as sp

def symbolic_calculations(f_expr,x):
    # Výpočet derivace
    f_prime = sp.diff(f_expr, x)
    
    # Výpočet integrálu
    f_integral = sp.integrate(f_expr, x)
    
    return f_prime, f_integral

# Definice funkce f(x)
x = sp.symbols('x')
#f_expr = sp.sin(x)*sp.exp(x)
f_expr = sp.log(x)

# Výpočet derivace a integrálu
f_prime, f_integral = symbolic_calculations(f_expr,x)

# Výpis výsledků
print(f"Funkce: {f_expr}")
print(f"Derivace: {f_prime}")
print(f"Integrál: {f_integral}")