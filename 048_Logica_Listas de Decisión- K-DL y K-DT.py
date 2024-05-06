# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:13:57 2024

@author: jared
"""

import numpy as np

class NodoKD:
    def __init__(self, valor, izquierda=None, derecha=None, eje=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha
        self.eje = eje

def construir_kd_arbol(datos, profundidad=0):
    n = datos.shape[1]
    eje = profundidad % n
    mediana = np.median(datos[:, eje])
    datos_izquierda = datos[datos[:, eje] < mediana]
    datos_derecha = datos[datos[:, eje] >= mediana]

    if len(datos_izquierda) == 0 or len(datos_derecha) == 0:
        return NodoKD(valor=mediana, eje=eje)

    return NodoKD(valor=mediana, eje=eje,
                  izquierda=construir_kd_arbol(datos_izquierda, profundidad + 1),
                  derecha=construir_kd_arbol(datos_derecha, profundidad + 1))

def imprimir_kd_arbol(arbol, indent=""):
    if arbol is not None:
        print(indent + "Eje {}: {}".format(arbol.eje, arbol.valor))
        imprimir_kd_arbol(arbol.izquierda, indent + "  ")
        imprimir_kd_arbol(arbol.derecha, indent + "  ")

# Ejemplo de uso
datos = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])
arbol = construir_kd_arbol(datos)
imprimir_kd_arbol(arbol)
