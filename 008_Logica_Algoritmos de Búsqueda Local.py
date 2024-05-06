# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:22:04 2024

@author: jared
"""

import random

class HillClimbing:
    """Implementación del algoritmo de Hill Climbing para búsqueda local."""

    def __init__(self, funcion, paso=0.01, limite_iteraciones=1000):
        """
        Inicializa el algoritmo de Hill Climbing.

        Args:
        funcion (function): La función unidimensional a maximizar.
        paso (float): El tamaño del paso para explorar vecinos.
        limite_iteraciones (int): El límite máximo de iteraciones.
        """
        self.funcion = funcion
        self.paso = paso
        self.limite_iteraciones = limite_iteraciones

    def buscar_maximo_local(self, x_inicial):
        """
        Busca el máximo local de la función.

        Args:
        x_inicial (float): El punto inicial de búsqueda.

        Returns:
        tuple: La coordenada x del máximo local y el valor correspondiente de la función.
        """
        x_actual = x_inicial
        valor_actual = self.funcion(x_actual)

        for _ in range(self.limite_iteraciones):
            x_vecino = x_actual + random.uniform(-self.paso, self.paso)
            valor_vecino = self.funcion(x_vecino)

            if valor_vecino > valor_actual:
                x_actual = x_vecino
                valor_actual = valor_vecino

        return x_actual, valor_actual

# Función de ejemplo: f(x) = -x^2 + 2x + 1
def funcion_ejemplo(x):
    """
    Función de ejemplo para la optimización.

    Args:
    x (float): El valor de la variable independiente.

    Returns:
    float: El valor de la función en el punto x.
    """
    return -x**2 + 2*x + 1

# Ejemplo de uso
hill_climbing = HillClimbing(funcion_ejemplo)
x_maximo, valor_maximo = hill_climbing.buscar_maximo_local(random.uniform(-10, 10))
print("Máximo local encontrado:")
print("x =", x_maximo)
print("Valor =", valor_maximo)
