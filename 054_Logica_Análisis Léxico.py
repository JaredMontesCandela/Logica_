# -*- coding: utf-8 -*-
"""
@author: jared
"""

import re

def analizador_lexico(cadena):
    """
    Analizador léxico que divide una cadena en tokens.

    Args:
    - cadena (str): La cadena de entrada a analizar.

    Returns:
    - list: Lista de tokens encontrados en la cadena.
    """
    # Definición de patrones para identificar tokens
    patron_identificador = r'[a-zA-Z][a-zA-Z0-9_]*'
    patron_numero = r'\d+'
    patron_operador = r'[\+\-\*/]'
    patron_parentesis = r'[\(\)]'
    patron_espacio = r'\s+'

    # Combinación de todos los patrones
    patron_general = '|'.join([patron_identificador, patron_numero, patron_operador, patron_parentesis, patron_espacio])

    # Lista para almacenar los tokens encontrados
    tokens = []

    # Búsqueda de tokens en la cadena
    for coincidencia in re.finditer(patron_general, cadena):
        token = coincidencia.group().strip()
        if not re.match(patron_espacio, token):
            tokens.append(token)

    return tokens

# Ejemplo de uso
cadena = "x = 10 + y * (5 - 3)"
tokens = analizador_lexico(cadena)
print("Tokens encontrados:", tokens)


"""
En este ejemplo, los tokens pueden ser identificadores (variables), números, operadores aritméticos o paréntesis
El analizador utiliza expresiones regulares para identificar y extraer los tokens de la cadena de entrada. 
La función analizador_lexico devuelve una lista de tokens encontrados en la cadena.
Este ejemplo proporciona una implementación básica de un analizador léxico en Python.
"""