# -*- coding: utf-8 -*-
"""
Created on Sat May  4 10:55:28 2024

@author: jared
"""

# Definimos una función para evaluar la lógica modal
def evaluar_logica_modal(formula, mundo):
    if formula[0] == '◇':  # Operador "posiblemente"
        return evaluar_logica_modal(formula[1], mundo)
    elif formula[0] == '□':  # Operador "necesariamente"
        return all(evaluar_logica_modal(subformula, mundo) for subformula in formula[1])
    else:  # Operador atómico
        return formula in mundo

# Definimos una fórmula en lógica modal
formula = ('□', [('p',), ('q',)])

# Definimos un modelo de mundo posible (interpretación)
interpretacion = {'p': True, 'q': True}

# Evaluamos la fórmula en el modelo de mundo posible
resultado = evaluar_logica_modal(formula, interpretacion)

# Mostramos el resultado
print("El resultado de la evaluación es:", resultado)
