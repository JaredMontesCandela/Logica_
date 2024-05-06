# -*- coding: utf-8 -*-
"""


@author: jared
"""

class Explicacion:
    def __init__(self, caracteristica, valor, relevancia):
        """
        Clase que representa una explicación para un valor de característica específico.
        
        Args:
        - caracteristica (int): El índice de la característica.
        - valor (any): El valor de la característica.
        - relevancia (float): La relevancia del valor de la característica en relación con la clase positiva.
        """
        self.caracteristica = caracteristica
        self.valor = valor
        self.relevancia = relevancia

def calcular_relevancia(X, y, caracteristica, valor):
    """
    Calcula la relevancia de un valor de característica en relación con la clase positiva.

    Args:
    - X (numpy.ndarray): Matriz de características.
    - y (numpy.ndarray): Vector de etiquetas de clase.
    - caracteristica (int): Índice de la característica.
    - valor (any): Valor de la característica.

    Returns:
    - float: Relevancia del valor de la característica.
    """
    relevancia_total = 0
    total_ejemplos = len(y)
    ejemplos_coincidentes = sum(1 for i in range(total_ejemplos) if X[i][caracteristica] == valor and y[i] == 1)

    if ejemplos_coincidentes > 0:
        relevancia_total = ejemplos_coincidentes / total_ejemplos

    return relevancia_total

def encontrar_explicaciones(X, y):
    """
    Encuentra explicaciones relevantes para cada valor único de cada característica.

    Args:
    - X (numpy.ndarray): Matriz de características.
    - y (numpy.ndarray): Vector de etiquetas de clase.

    Returns:
    - list: Lista de objetos de explicación relevantes.
    """
    explicaciones = []

    for caracteristica in range(len(X[0])):
        valores_unicos = set(X[:, caracteristica])
        for valor in valores_unicos:
            relevancia = calcular_relevancia(X, y, caracteristica, valor)
            explicacion = Explicacion(caracteristica, valor, relevancia)
            explicaciones.append(explicacion)

    return explicaciones

# Ejemplo de uso
import numpy as np

X = np.array([[1, 'sol'], [0, 'nublado'], [1, 'lluvia'], [0, 'sol']])
y = np.array([1, 0, 1, 0])

explicaciones = encontrar_explicaciones(X, y)
for explicacion in explicaciones:
    print("Característica:", explicacion.caracteristica)
    print("Valor:", explicacion.valor)
    print("Relevancia:", explicacion.relevancia)
    print()

"""
El objetivo de este código es encontrar explicaciones relevantes para cada valor único de cada característica en un conjunto de datos dado
Las explicaciones indican la relevancia de cada valor de característica en relación con la clase positiva.
Este código proporciona una implementación básica
para calcular la relevancia de cada valor de característica y generar una lista de explicaciones relevantes.
"""