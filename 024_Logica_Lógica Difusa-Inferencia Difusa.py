# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:23:23 2024

@author: jared
"""

# Funciones de pertenencia para la temperatura ambiente
def pertenencia_fria(x):
    if x <= 20:
        return 1
    elif 20 < x <= 25:
        return (25 - x) / 5
    else:
        return 0

def pertenencia_calida(x):
    if 20 < x <= 25:
        return (x - 20) / 5
    elif 25 < x <= 30:
        return (30 - x) / 5
    else:
        return 0

def pertenencia_calurosa(x):
    if x <= 25:
        return 0
    elif 25 < x <= 30:
        return (x - 25) / 5
    else:
        return 1

# Funciones de pertenencia para la velocidad del ventilador
def pertenencia_lenta(x):
    if x <= 2:
        return 1
    elif 2 < x <= 4:
        return (4 - x) / 2
    else:
        return 0

def pertenencia_media(x):
    if 2 < x <= 4:
        return (x - 2) / 2
    elif 4 < x <= 6:
        return (6 - x) / 2
    else:
        return 0

def pertenencia_rapida(x):
    if x <= 4:
        return 0
    elif 4 < x <= 6:
        return (x - 4) / 2
    else:
        return 1

# Funciones de pertenencia para la temperatura de salida
def pertenencia_fria_salida(x):
    if x <= 15:
        return 1
    elif 15 < x <= 20:
        return (20 - x) / 5
    else:
        return 0

def pertenencia_calida_salida(x):
    if 15 < x <= 20:
        return (x - 15) / 5
    elif 20 < x <= 25:
        return (25 - x) / 5
    else:
        return 0

def pertenencia_calurosa_salida(x):
    if x <= 20:
        return 0
    elif 20 < x <= 25:
        return (x - 20) / 5
    else:
        return 1

# Definimos las reglas difusas
def inferencia_difusa(temperatura_ambiente, velocidad_ventilador):
    # Calculamos el grado de pertenencia a cada conjunto difuso para la temperatura ambiente
    grado_fria = pertenencia_fria(temperatura_ambiente)
    grado_calida = pertenencia_calida(temperatura_ambiente)
    grado_calurosa = pertenencia_calurosa(temperatura_ambiente)

    # Calculamos el grado de pertenencia a cada conjunto difuso para la velocidad del ventilador
    grado_lenta = pertenencia_lenta(velocidad_ventilador)
    grado_media = pertenencia_media(velocidad_ventilador)
    grado_rapida = pertenencia_rapida(velocidad_ventilador)

    # Aplicamos las reglas difusas para determinar la temperatura de salida
    temperatura_fria = min(grado_fria, grado_lenta)
    temperatura_calida = min(grado_calida, grado_media)
    temperatura_calurosa = min(grado_calurosa, grado_rapida)

    # Defuzzificar para obtener la temperatura de salida final
    temperatura_salida = (temperatura_fria * 15 + temperatura_calida * 20 + temperatura_calurosa * 25) / (
            temperatura_fria + temperatura_calida + temperatura_calurosa)

    return temperatura_salida

# Ejemplo de inferencia difusa
temperatura_ambiente = 22
velocidad_ventilador = 3
temperatura_salida = inferencia_difusa(temperatura_ambiente, velocidad_ventilador)

# Mostramos la temperatura de salida
print("Temperatura de salida del aire acondicionado:", temperatura_salida)
