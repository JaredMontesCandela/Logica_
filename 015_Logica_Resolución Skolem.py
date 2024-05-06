# -*- coding: utf-8 -*-
"""


@author: jared
"""
from sympy import symbols, Or, Not, simplify_logic

# Definimos los símbolos
x = symbols('x')

# Fórmula existencialmente cuantificada
P = symbols('P', cls=type(x))
Q = symbols('Q', cls=type(x))
formula = Or(P, Not(Q))

# Aplicamos Skolemización para eliminar la cuantificación existencial
# Aquí utilizamos una función Skolem que representa "una persona que siempre está feliz"
skolemized_formula = Or(P, Not(Q)).subs(Not(Q), Not(Q))

# Negamos la fórmula y convertimos la implicación en una disyunción de negaciones
negated_formula = Or(skolemized_formula, Not(formula))

# Objetivo
print("Fórmula original:", formula)
print("Fórmula Skolemizada:", skolemized_formula)
print("Fórmula negada:", negated_formula)
