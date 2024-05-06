# -*- coding: utf-8 -*-
"""
@author: jared
"""

class Hipotesis:
    def __init__(self, longitud):
        self.caracteristicas = ['?' for _ in range(longitud)]
        self.positiva = False

def espacio_versiones(X, y):
    n, m = X.shape
    longitud = m
    hipotesis = Hipotesis(longitud)

    for i in range(n):
        if y[i] == 1:
            for j in range(m):
                if hipotesis.caracteristicas[j] == '?' or hipotesis.caracteristicas[j] == X[i][j]:
                    hipotesis.caracteristicas[j] = X[i][j]
            hipotesis.positiva = True

    return hipotesis

# Ejemplo de uso
X = [['sol', 'calor', 'alta', 'debil'],
     ['sol', 'calor', 'alta', 'fuerte'],
     ['nublado', 'calor', 'alta', 'debil'],
     ['lluvia', 'templado', 'alta', 'debil'],
     ['lluvia', 'frio', 'normal', 'debil'],
     ['lluvia', 'frio', 'normal', 'fuerte'],
     ['nublado', 'frio', 'normal', 'fuerte'],
     ['sol', 'templado', 'alta', 'debil'],
     ['sol', 'frio', 'normal', 'debil'],
     ['lluvia', 'templado', 'normal', 'debil'],
     ['sol', 'templado', 'normal', 'fuerte'],
     ['nublado', 'templado', 'alta', 'fuerte'],
     ['nublado', 'calor', 'normal', 'debil'],
     ['lluvia', 'templado', 'alta', 'fuerte']]
y = [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1]

hipotesis_final = espacio_versiones(X, y)
print("Hipótesis final:")
print("Características:", hipotesis_final.caracteristicas)
print("Clasificación:", "Positiva" if hipotesis_final.positiva else "Negativa")

"""
 El algoritmo de Espacio de Versiones y AQ busca una hipótesis que cubra todos
los ejemplos positivos y no cubra ningún ejemplo negativo en el conjunto de datos
En este ejemplo, se muestra cómo el algoritmo actualiza gradualmente la hipótesis
para reflejar los ejemplos positivos vistos. La hipótesis final representa un conjunto
de reglas que describen el concepto subyacente en los datos.

"""
