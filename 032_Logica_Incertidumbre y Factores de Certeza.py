# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:46:11 2024

@author: jared
"""

# Definimos una función para calcular el factor de certeza
def factor_certeza(valor, factor):
    return valor * factor

# Ejemplo de uso de factores de certeza
resultado_verdadero = 1
factor_alto = 0.9
factor_medio = 0.6
factor_bajo = 0.3

# Calculamos el resultado con diferentes factores de certeza
resultado_alto = factor_certeza(resultado_verdadero, factor_alto)
resultado_medio = factor_certeza(resultado_verdadero, factor_medio)
resultado_bajo = factor_certeza(resultado_verdadero, factor_bajo)

# Mostramos los resultados
print("Resultado con factor de certeza alto:", resultado_alto)
print("Resultado con factor de certeza medio:", resultado_medio)
print("Resultado con factor de certeza bajo:", resultado_bajo)
