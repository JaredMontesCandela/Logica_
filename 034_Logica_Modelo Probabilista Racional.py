# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:56:47 2024

@author: jared
"""

# Importamos la biblioteca numpy para cálculos numéricos
import numpy as np

# Definimos una función para el Modelo Probabilista Racional
def modelo_probabilista_racional(probabilidades, utilidades):
    # Calculamos la utilidad esperada para cada opción
    utilidad_esperada = np.dot(probabilidades, utilidades)
    
    # Seleccionamos la opción con la mayor utilidad esperada
    mejor_opcion = np.argmax(utilidad_esperada)
    
    return mejor_opcion

# Ejemplo de uso del Modelo Probabilista Racional
probabilidades = [0.2, 0.4, 0.3, 0.1]  # Probabilidades de cada opción
utilidades = [10, 5, 8, 3]  # Utilidades asociadas a cada opción

# Calculamos la mejor opción según el Modelo Probabilista Racional
mejor_opcion = modelo_probabilista_racional(probabilidades, utilidades)

# Mostramos la mejor opción
print("La mejor opción es la opción", mejor_opcion + 1)
