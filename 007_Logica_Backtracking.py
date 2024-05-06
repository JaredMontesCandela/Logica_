# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:19:41 2024

@author: jared
"""

class NReinas:
    """Clase para resolver el problema de las N reinas utilizando backtracking."""

    def __init__(self, N):
        self.N = N
        self.solucion = [-1] * N

    def es_seguro(self, fila, columna):
        """Verifica si es seguro colocar una reina en la posición dada."""
        for i in range(fila):
            # Verifica si hay una reina en la misma columna o en diagonales
            if self.solucion[i] == columna or \
               self.solucion[i] - i == columna - fila or \
               self.solucion[i] + i == columna + fila:
                return False
        return True

    def resolver(self, fila=0):
        """Resuelve el problema de las N reinas utilizando backtracking."""
        if fila == self.N:
            return True  # Todas las reinas están colocadas

        for columna in range(self.N):
            if self.es_seguro(fila, columna):
                self.solucion[fila] = columna
                if self.resolver(fila + 1):
                    return True
                # Si la solución no es válida, retrocede y prueba con la siguiente columna
                self.solucion[fila] = -1
        return False

    def mostrar_solucion(self):
        """Muestra la solución."""
        for fila in range(self.N):
            fila_solucion = ""
            for columna in range(self.N):
                if self.solucion[fila] == columna:
                    fila_solucion += "Q "
                else:
                    fila_solucion += ". "
            print(fila_solucion)
        print("\n")

# Ejemplo de uso
N = 4  # Tamaño del tablero (N x N)
n_reinas = NReinas(N)
if n_reinas.resolver():
    print("Solución encontrada:")
    n_reinas.mostrar_solucion()
else:
    print("No se encontró ninguna solución.")

# Objetivo:
"""
El objetivo de este código es resolver el problema de las N reinas utilizando el algoritmo de backtracking en Python. El problema consiste en colocar N reinas en un tablero de ajedrez de tamaño N × N de tal manera que ninguna reina amenace a otra. 

La clase NReinas implementa el algoritmo de backtracking para encontrar todas las posibles soluciones al problema. Se verifica si es seguro colocar una reina en una posición determinada y, si es así, se avanza recursivamente hasta encontrar una solución. Si se encuentra una solución, se muestra en el tablero; de lo contrario, se informa que no se encontró ninguna solución.

Este ejemplo ilustra cómo se puede aplicar el algoritmo de backtracking para resolver un problema clásico de combinaciones y cómo se puede implementar de manera eficiente en Python.
"""
