# -*- coding: utf-8 -*-
"""

@author: jared
"""

# Definimos las funciones de pertenencia manualmente
def funcion_pertenencia_baja(x):
    if x <= 50:
        return 1
    elif 50 < x <= 75:
        return (75 - x) / 25
    else:
        return 0

def funcion_pertenencia_media(x):
    if 25 < x <= 50:
        return (x - 25) / 25
    elif 50 < x <= 75:
        return 1
    elif 75 < x <= 100:
        return (100 - x) / 25
    else:
        return 0

def funcion_pertenencia_alta(x):
    if x <= 75:
        return 0
    elif 75 < x <= 100:
        return (x - 75) / 25
    else:
        return 1

# Definimos una función de activación para cada regla
def funcion_activacion_baja(velocidad):
    return funcion_pertenencia_baja(velocidad)

def funcion_activacion_media(velocidad):
    return funcion_pertenencia_media(velocidad)

def funcion_activacion_alta(velocidad):
    return funcion_pertenencia_alta(velocidad)

# Definimos una función de agregación para combinar las funciones de pertenencia
def funcion_agregacion(baja, media, alta):
    return max(baja, media, alta)

# Definimos una función de desfuzificación para obtener un valor de salida
def desfuzificar(baja, media, alta):
    return (baja * 25 + media * 50 + alta * 75) / (baja + media + alta)

# Definimos la velocidad de entrada
velocidad_entrada = 70

# Calculamos las funciones de activación para cada regla
activacion_baja = funcion_activacion_baja(velocidad_entrada)
activacion_media = funcion_activacion_media(velocidad_entrada)
activacion_alta = funcion_activacion_alta(velocidad_entrada)

# Calculamos la función de agregación
agregacion = funcion_agregacion(activacion_baja, activacion_media, activacion_alta)

# Desfuzificamos para obtener la potencia de salida
potencia_salida = desfuzificar(activacion_baja, activacion_media, activacion_alta)

# Mostramos la potencia de salida
print("Potencia de salida:", potencia_salida)
