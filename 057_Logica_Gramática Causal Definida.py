# -*- coding: utf-8 -*-
"""
@author: jared
"""

import re

# Definición de la gramática causal
GRAMATICA_CAUSAL = {
    "S": ["CAUSA CONSECUENCIA"],
    "CAUSA": ["SUJETO VERBO_ACCION OBJETO"],
    "CONSECUENCIA": ["VERBO_RESULTADO OBJETO_RESULTADO"],
    "SUJETO": ["El conductor", "La lluvia", "El viento"],
    "VERBO_ACCION": ["provocó", "ocasionó", "generó"],
    "OBJETO": ["el accidente", "el choque", "el incidente"],
    "VERBO_RESULTADO": ["resultó en", "ocasionó", "produjo"],
    "OBJETO_RESULTADO": ["daños", "heridos", "retrasos"]
}

# Función para analizar una oración y determinar si es gramaticalmente válida según la gramática causal definida
def analizar_oracion(oracion):
    oracion = oracion.lower()  # Convertir la oración a minúsculas para hacerla coincidir con la gramática
    for regla in GRAMATICA_CAUSAL["S"]:
        if coincidir(oracion, regla):
            return True
    return False

# Función para verificar si una oración coincide con una regla gramatical
def coincidir(oracion, regla):
    tokens_oracion = oracion.split()
    tokens_regla = regla.split()
    if len(tokens_oracion) != len(tokens_regla):
        return False
    for token_oracion, token_regla in zip(tokens_oracion, tokens_regla):
        if token_regla in GRAMATICA_CAUSAL:
            if token_oracion not in GRAMATICA_CAUSAL[token_regla]:
                return False
        elif token_oracion != token_regla:
            return False
    return True

# Ejemplo de uso
oraciones = [
    "El conductor provocó el accidente resultando en daños.",
    "La lluvia generó el incidente ocasionando heridos.",
    "El viento ocasionó el choque produciendo retrasos."
]

for oracion in oraciones:
    if analizar_oracion(oracion):
        print(f'La oración "{oracion}" es gramaticalmente válida.')
    else:
        print(f'La oración "{oracion}" tiene errores gramaticales.')


"""
En este ejemplo, la gramática causal se define como un diccionario de Python donde las claves son los símbolos no terminales y los valores son listas de reglas de producción"""

