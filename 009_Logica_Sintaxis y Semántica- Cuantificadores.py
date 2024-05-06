# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:24:45 2024

@author: jared
"""
from sympy import symbols, And, Or

# Definición de símbolos
x, y = symbols('x y')

# Ejemplo de cuantificador universal
dominio = [1, 2, 3, 4, 5]
condicion_universal = And(*[x > 5 for x in dominio])
print("¿Todos los elementos son mayores que cinco?", condicion_universal)

# Ejemplo de cuantificador existencial
condicion_existencial = Or(*[y % 2 == 0 for y in dominio])
print("¿Existe un número par?", condicion_existencial)

# Objetivo:
"""
El objetivo de este código es ilustrar cómo trabajar con cuantificadores en lógica de predicados utilizando la biblioteca SymPy en Python.
Los cuantificadores son herramientas importantes en lógica que permiten cuantificar sobre conjuntos de objetos y expresar proposiciones de manera más general.
En este ejemplo, utilizamos comprensiones de lista para simular cuantificadores en SymPy. Creamos una condición lógica universal y existencial utilizando And y Or respectivamente, junto con las comprensiones de lista para evaluar la condición para cada elemento en el dominio.
"""
