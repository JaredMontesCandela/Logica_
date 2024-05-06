# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:21:13 2024

@author: jared
"""

# Definimos la función de pertenencia para el conjunto difuso "baja"
def pertenencia_baja(x):
    if x <= 150:
        return 1
    elif 150 < x <= 160:
        return (160 - x) / 10
    else:
        return 0

# Definimos la función de pertenencia para el conjunto difuso "media"
def pertenencia_media(x):
    if 150 < x <= 160:
        return (x - 150) / 10
    elif 160 < x <= 170:
        return 1
    elif 170 < x <= 180:
        return (180 - x) / 10
    else:
        return 0

# Definimos la función de pertenencia para el conjunto difuso "alta"
def pertenencia_alta(x):
    if x <= 170:
        return 0
    elif 170 < x <= 180:
        return (x - 170) / 10
    else:
        return 1

# Definimos la altura de una persona
altura = 165

# Calculamos el grado de pertenencia a cada conjunto difuso
grado_baja = pertenencia_baja(altura)
grado_media = pertenencia_media(altura)
grado_alta = pertenencia_alta(altura)

# Mostramos el grado de pertenencia a cada conjunto difuso
print("Grado de pertenencia a 'baja':", grado_baja)
print("Grado de pertenencia a 'media':", grado_media)
print("Grado de pertenencia a 'alta':", grado_alta)
