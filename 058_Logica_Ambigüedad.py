# -*- coding: utf-8 -*-
"""
@author: jared
"""

# Ejemplo de ambigüedad en la evaluación de expresiones lógicas en Python
def funcion_ambigua(x, y):
    return x > 5 or y < 10 and x != y

# Evaluación de la función con distintos valores de entrada
print(funcion_ambigua(6, 8))   # ¿Es True o False?
print(funcion_ambigua(8, 6))   # ¿Es True o False?


def funcion_clara(x):
    return (x > 5 or x < 10) and x != 8
print(" ")
print(funcion_clara(6))   # True
print(funcion_clara(8))   # False

