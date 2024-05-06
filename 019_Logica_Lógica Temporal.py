# -*- coding: utf-8 -*-
"""


@author: jared
"""

# Definimos una función para evaluar la lógica temporal
def evaluar_logica_temporal(formula, mundo_actual):
    if formula[0] == '□':  # Operador "en el presente"
        return formula[1] in mundo_actual
    elif formula[0] == '◊':  # Operador "en el pasado"
        return any(subformula in mundo for mundo in mundo_actual for subformula in formula[1])
    elif formula[0] == '◇':  # Operador "en el futuro"
        return any(evaluar_logica_temporal(subformula, mundo) for mundo in mundo_actual for subformula in formula[1])
    else:  # Operador atómico
        return formula in mundo_actual

# Definimos una fórmula en lógica temporal
formula = ('◇', ('evento_c',))

# Definimos un modelo de mundo posible (interpretación)
interpretacion = [
    ('evento_a', 'evento_b'),
    ('evento_b', 'evento_c'),
    ('evento_d',)
]

# Evaluamos la fórmula en el modelo de mundo posible (en el futuro)
resultado = evaluar_logica_temporal(formula, interpretacion)

# Mostramos el resultado
print("El resultado de la evaluación es:", resultado)

