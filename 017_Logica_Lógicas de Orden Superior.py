# -*- coding: utf-8 -*-
"""


@author: jared
"""
from sympy import symbols, Eq, solve

# Definimos los símbolos
x = symbols('x')

# Definimos una función de orden superior
f_x = 2*x  # Por ejemplo, f(x) = 2x
funcion_superior = f_x + 1

# Definimos una ecuación que involucra la función de orden superior
ecuacion = Eq(funcion_superior, 5)

# Resolvemos la ecuación para encontrar el valor de x que satisface la función
solucion = solve(ecuacion, x)

# Mostramos la solución
print("La solución para x que satisface la función es:", solucion)


