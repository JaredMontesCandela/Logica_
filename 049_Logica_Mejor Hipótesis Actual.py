# -*- coding: utf-8 -*-
"""
@author: jared
"""

import numpy as np

class Hipotesis:
    def __init__(self, umbral, polaridad, caracteristica):
        self.umbral = umbral
        self.polaridad = polaridad
        self.caracteristica = caracteristica

def predecir_hipotesis(hipotesis, muestra):
    valor_caracteristica = muestra[hipotesis.caracteristica]
    if hipotesis.polaridad == 1:
        return 1 if valor_caracteristica >= hipotesis.umbral else -1
    else:
        return 1 if valor_caracteristica < hipotesis.umbral else -1

def calcular_error(hipotesis, X, y):
    errores = np.ones(len(y))
    for i, muestra in enumerate(X):
        errores[i] = 0 if predecir_hipotesis(hipotesis, muestra) == y[i] else 1
    return np.mean(errores)

def encontrar_mejor_hipotesis(X, y):
    mejor_error = float('inf')
    mejor_hipotesis = None
    n, m = X.shape

    for caracteristica in range(m):
        valores_unicos = np.unique(X[:, caracteristica])
        for umbral in valores_unicos:
            for polaridad in [1, -1]:
                hipotesis = Hipotesis(umbral, polaridad, caracteristica)
                error_actual = calcular_error(hipotesis, X, y)
                if error_actual < mejor_error:
                    mejor_error = error_actual
                    mejor_hipotesis = hipotesis

    return mejor_hipotesis

# Ejemplo de uso
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([1, -1, -1, 1])

mejor_hipotesis = encontrar_mejor_hipotesis(X, y)
print("La mejor hipótesis encontrada es:")
print("Umbral:", mejor_hipotesis.umbral)
print("Polaridad:", "Positiva" if mejor_hipotesis.polaridad == 1 else "Negativa")
print("Característica:", mejor_hipotesis.caracteristica)

"""
El código implementa una búsqueda exhaustiva sobre todas las
características y umbrales posibles para encontrar la mejor hipótesis.
El objetivo es ilustrar cómo funciona el algoritmo de Mejor Hipótesis Actual (BHC) y cómo se puede implementar en Python
"""
