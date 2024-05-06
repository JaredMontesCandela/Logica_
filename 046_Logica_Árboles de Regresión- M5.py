# -*- coding: utf-8 -*-
"""

@author: jared
"""

import numpy as np

class NodoRegresion:
    def __init__(self, caracteristica=None, valor=None, prediccion=None, subarboles=None):
        self.caracteristica = caracteristica  # Índice de la característica para dividir el conjunto de datos
        self.valor = valor  # Valor de la característica para dividir el conjunto de datos
        self.prediccion = prediccion  # Valor de la predicción en este nodo (media de las etiquetas)
        self.subarboles = subarboles  # Subárboles para cada valor de la característica

def calcular_error_cuadratico_medio(y):
    media = np.mean(y)
    error_cuadratico_medio = np.mean((y - media) ** 2)
    return error_cuadratico_medio

def calcular_error_absoluto_medio(y):
    media = np.mean(y)
    error_absoluto_medio = np.mean(np.abs(y - media))
    return error_absoluto_medio

def calcular_ganancia_reduccion_varianza(X, y, caracteristica, valor):
    mascara = X[:, caracteristica] == valor
    y_subconjunto = y[mascara]
    y_promedio = np.mean(y_subconjunto)
    varianza_total = np.var(y)
    varianza_subconjunto = np.var(y_subconjunto)
    ganancia = varianza_total - (len(y_subconjunto) / len(y)) * varianza_subconjunto
    return ganancia

def construir_arbol_m5(X, y, caracteristicas, min_muestras_por_hoja):
    # Si solo hay un número mínimo de muestras en una hoja, devolver un nodo hoja con la predicción promedio
    if len(y) <= min_muestras_por_hoja:
        return NodoRegresion(prediccion=np.mean(y))

    # Si todos los ejemplos tienen la misma etiqueta, devolver un nodo hoja con esa etiqueta
    if len(np.unique(y)) == 1:
        return NodoRegresion(prediccion=y[0])

    # Si no quedan características para dividir o el conjunto de datos es vacío, devolver un nodo hoja con la predicción promedio
    if len(caracteristicas) == 0 or len(X) == 0:
        return NodoRegresion(prediccion=np.mean(y))

    # Calcular la ganancia de reducción de la varianza para cada característica y valor
    ganancias = []
    for caracteristica in caracteristicas:
        valores = np.unique(X[:, caracteristica])
        for valor in valores:
            ganancia = calcular_ganancia_reduccion_varianza(X, y, caracteristica, valor)
            ganancias.append(ganancia)

    mejor_ganancia = max(ganancias)
    mejor_caracteristica, mejor_valor = None, None
    for caracteristica in caracteristicas:
        valores = np.unique(X[:, caracteristica])
        for valor in valores:
            ganancia = calcular_ganancia_reduccion_varianza(X, y, caracteristica, valor)
            if ganancia == mejor_ganancia:
                mejor_caracteristica, mejor_valor = caracteristica, valor

    # Construir un diccionario de subárboles para cada valor de la mejor característica
    subarboles = {}
    mascara = X[:, mejor_caracteristica] == mejor_valor
    X_subconjunto = X[mascara]
    y_subconjunto = y[mascara]
    subarboles[mejor_valor] = construir_arbol_m5(X_subconjunto, y_subconjunto, [c for c in caracteristicas if c != mejor_caracteristica], min_muestras_por_hoja)

    return NodoRegresion(caracteristica=mejor_caracteristica, valor=mejor_valor, subarboles=subarboles)

def predecir(arbol, muestra):
    if arbol.prediccion is not None:
        return arbol.prediccion
    valor = muestra[arbol.caracteristica]
    subarbol = arbol.subarboles.get(valor)  # Utilizamos .get() para manejar el caso de que el valor no esté presente
    if subarbol is None:
        # Si no hay un subárbol correspondiente al valor de la muestra, devolvemos la predicción promedio de todos los ejemplos
        return np.mean([subarbol.prediccion for subarbol in arbol.subarboles.values()])
    return predecir(subarbol, muestra)

# Ejemplo de uso
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([2, 3, 4, 5])
caracteristicas = list(range(X.shape[1]))  # Índices de las características

arbol = construir_arbol_m5(X, y, caracteristicas, min_muestras_por_hoja=1)

muestra = [3, 3]
prediccion = predecir(arbol, muestra)
print("La predicción para la muestra {} es: {}".format(muestra, prediccion))


""" ##OBJETIVO
El código construye un árbol de regresión basado en un conjunto de datos de entrenamientoEl código construye un árbol de decisión basado en un conjunto de datos de entrenamiento 
y luego utiliza el árbol entrenado para hacer predicciones sobre nuevas muestras.El objetivo de este código es demostrar cómo funciona el algoritmo ID3 para la construcción de árboles de decisión en Python.
El objetivo de este código es demostrar cómo funciona el algoritmo M5 para la construcción de árboles de regresión en Python.
"""
