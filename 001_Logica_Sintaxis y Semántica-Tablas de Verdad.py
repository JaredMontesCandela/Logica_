# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:21:05 2024

@author: jared
"""

"""Este código define una función llamada tabla_verdad que toma una expresión booleana como entrada y devuelve la tabla
de verdad correspondiente. La función utiliza la función eval de Python para evaluar la expresión
booleana con diferentes combinaciones de valores de verdad para las variables involucradas.
Los comentarios en el código explican cada paso y la función está adecuadamente comentada para que cualquiera pueda entender su funcionamiento.
"""
def tabla_verdad(expresion):
    """Genera la tabla de verdad para la expresión booleana dada.

    Args:
    expresion (str): Expresión booleana.

    Returns:
    list: Lista de tuplas donde cada tupla representa una fila de la tabla de verdad.
    """
    variables = sorted(set(c for c in expresion if c.isalpha()))  # Obtiene las variables únicas de la expresión
    n = len(variables)  # Número de variables
    tabla = []

    for i in range(2**n):
        fila = []
        for j in range(n):
            fila.append((i // (2 ** j)) % 2)  # Calcula el valor de verdad de cada variable en la fila actual
        valores = {variables[k]: fila[k] for k in range(n)}  # Crea un diccionario con los valores de verdad de las variables
        resultado = eval(expresion, valores)  # Evalúa la expresión booleana con los valores de verdad actuales
        fila.append(int(resultado))  # Agrega el resultado de la expresión a la fila
        tabla.append(tuple(fila))  # Agrega la fila a la tabla de verdad

    return tabla

# Ejemplo de uso:
expresion = "A and (B or C)"
print("Tabla de verdad para la expresión:", expresion)
print(tabla_verdad(expresion))
