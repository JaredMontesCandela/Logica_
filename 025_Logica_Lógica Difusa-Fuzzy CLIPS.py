# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:26:22 2024

@author: jared
"""
import numpy as np

# Definición de las funciones de pertenencia
def pertenencia_fria(x):
    if x <= 25:
        return 1
    elif 25 < x <= 50:
        return (50 - x) / 25
    else:
        return 0

def pertenencia_templada(x):
    if 25 < x <= 50:
        return (x - 25) / 25
    elif 50 < x <= 75:
        return (75 - x) / 25
    else:
        return 0

def pertenencia_calurosa(x):
    if x <= 50:
        return 0
    elif 50 < x <= 75:
        return (x - 50) / 25
    else:
        return 1

def pertenencia_baja(x):
    if x <= 50:
        return 1
    elif 50 < x <= 75:
        return (75 - x) / 25
    else:
        return 0

def pertenencia_media(x):
    if 50 < x <= 75:
        return (x - 50) / 25
    elif 75 < x <= 100:
        return (100 - x) / 25
    else:
        return 0

def pertenencia_alta(x):
    if x <= 75:
        return 0
    elif 75 < x <= 100:
        return (x - 75) / 25
    else:
        return 1

# Definición de las reglas difusas
def inferencia_difusa(temperatura):
    if pertenencia_fria(temperatura) > 0:
        return pertenencia_baja
    elif pertenencia_templada(temperatura) > 0:
        return pertenencia_media
    elif pertenencia_calurosa(temperatura) > 0:
        return pertenencia_alta

# Ejemplo de inferencia difusa
temperatura_ambiente = 30
funcion_pertenencia_velocidad = inferencia_difusa(temperatura_ambiente)
velocidad = np.mean([funcion_pertenencia_velocidad(temperatura_ambiente - 5), 
                     funcion_pertenencia_velocidad(temperatura_ambiente),
                     funcion_pertenencia_velocidad(temperatura_ambiente + 5)])

# Mostramos la velocidad de salida
print("Velocidad del ventilador:", velocidad)

"""
### Objetivo:
El objetivo de este ejemplo es implementar lógica difusa sin utilizar bibliotecas externas, definir manualmente las funciones de pertenencia para la temperatura y la velocidad del ventilador, y utilizar reglas difusas simples para determinar la velocidad del ventilador en función de la temperatura ambiente. Esta implementación es más básica que la anterior y sirve como una introducción a la lógica difusa en Python sin dependencias externas.
"""
