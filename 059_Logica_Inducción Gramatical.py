# -*- coding: utf-8 -*-
"""
@author: jared
"""

# Ejemplo de Inducción Gramatical en Python

# Ejemplos de expresiones matemáticas simples
ejemplos = [
    "2 + 3",
    "5 - 1",
    "4 * 6",
    "10 / 2",
]

# Función para inducir una gramática a partir de ejemplos de expresiones matemáticas
def inducir_gramatica(ejemplos):
    # Crear una lista de reglas de producción basadas en los ejemplos
    reglas = []
    for ejemplo in ejemplos:
        partes = ejemplo.split()
        if len(partes) == 3:
            reglas.append(f"expresion -> {partes[0]} OPERADOR {partes[2]}")
        elif len(partes) == 1:
            reglas.append(f"expresion -> {partes[0]}")
    return reglas

# Función para generar expresiones a partir de la gramática inducida
def generar_expresiones(gramatica, n=5):
    # Imprimir las reglas de la gramática
    print("Gramática inducida:")
    for regla in gramatica:
        print(regla)
    print("\nExpresiones generadas:")
    # Generar expresiones a partir de la gramática inducida
    for i in range(n):
        expresion = "2 + 2"  # Expresión inicial
        for regla in gramatica:
            partes = regla.split(" -> ")[1].split()
            for parte in partes:
                if parte in ["OPERADOR", "+", "-", "*", "/"]:
                    expresion += f" {parte} 2"
                else:
                    expresion += f" {parte}"
        print(expresion)

# Inducir la gramática a partir de los ejemplos
gramatica = inducir_gramatica(ejemplos)

# Generar expresiones a partir de la gramática inducida
generar_expresiones(gramatica)
