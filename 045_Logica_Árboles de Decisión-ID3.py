# -*- coding: utf-8 -*-
"""

@author: jared
"""

import numpy as np

class NodoDecision:
    def __init__(self, caracteristica=None, valor=None, predicciones=None, subarboles=None):
        self.caracteristica = caracteristica  # Índice de la característica para dividir el conjunto de datos
        self.valor = valor  # Valor de la característica para dividir el conjunto de datos
        self.predicciones = predicciones  # Diccionario de clases y su frecuencia en el subconjunto de datos
        self.subarboles = subarboles  # Subárboles para cada valor de la característica

def calcular_entropia(y):
    clases, conteos = np.unique(y, return_counts=True)
    probabilidades = conteos / len(y)
    entropia = -np.sum(probabilidades * np.log2(probabilidades))
    return entropia

def calcular_ganancia_entropia(X, y, caracteristica):
    valores = np.unique(X[:, caracteristica])
    ganancia_entropia = calcular_entropia(y)
    for valor in valores:
        mascara = X[:, caracteristica] == valor
        y_subconjunto = y[mascara]
        ganancia_entropia -= len(y_subconjunto) / len(y) * calcular_entropia(y_subconjunto)
    return ganancia_entropia

def construir_arbol_id3(X, y, caracteristicas):
    # Si todos los ejemplos pertenecen a la misma clase, devolver un nodo hoja con esa clase
    if len(np.unique(y)) == 1:
        return NodoDecision(predicciones={y[0]: len(y)})

    # Si no quedan características para dividir o el conjunto de datos es vacío, devolver un nodo hoja con la clase más común
    if len(caracteristicas) == 0 or len(X) == 0:
        clase_mas_comun = np.argmax(np.bincount(y))
        return NodoDecision(predicciones={clase_mas_comun: len(y)})

    # Calcular la ganancia de información para cada característica
    ganancias = [calcular_ganancia_entropia(X, y, caracteristica) for caracteristica in caracteristicas]
    mejor_caracteristica = caracteristicas[np.argmax(ganancias)]

    # Construir un diccionario de subárboles para cada valor de la mejor característica
    subarboles = {}
    valores = np.unique(X[:, mejor_caracteristica])
    for valor in valores:
        mascara = X[:, mejor_caracteristica] == valor
        X_subconjunto = X[mascara]
        y_subconjunto = y[mascara]
        subarboles[valor] = construir_arbol_id3(X_subconjunto, y_subconjunto, [c for c in caracteristicas if c != mejor_caracteristica])

    return NodoDecision(caracteristica=mejor_caracteristica, subarboles=subarboles)

def predecir(arbol, muestra):
    if arbol.predicciones is not None:
        return list(arbol.predicciones.keys())[0]
    valor = muestra[arbol.caracteristica]
    subarbol = arbol.subarboles[valor]
    return predecir(subarbol, muestra)

# Ejemplo de uso
X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y = np.array([1, 1, 0, 0])
caracteristicas = list(range(X.shape[1]))  # Índices de las características

arbol = construir_arbol_id3(X, y, caracteristicas)

muestra = [1, 1]
prediccion = predecir(arbol, muestra)
print("La predicción para la muestra {} es: {}".format(muestra, prediccion))

""" ##OBJETIVO
El objetivo de este código es proporcionar un ejemplo de implementación del algoritmo de árboles de decisión ID3 en PythonEn una implementación real, la lógica de vigilancia y replanificación sería más sofisticada y adaptada a las necesidades específicas del proyecto.
El código construye un árbol de decisión basado en un conjunto de datos de entrenamiento 
y luego utiliza el árbol entrenado para hacer predicciones sobre nuevas muestras.
El objetivo de este código es demostrar cómo funciona el algoritmo ID3 para la construcción de árboles de decisión en Python.
"""