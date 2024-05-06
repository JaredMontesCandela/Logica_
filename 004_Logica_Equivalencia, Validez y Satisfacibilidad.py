# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:43:02 2024

@author: jared
"""
class LogicaProposicional:
    """Clase para operaciones de lógica proposicional."""

    @staticmethod
    def equivalencia(expresion1, expresion2):
        """Verifica si dos expresiones lógicas son equivalentes.

        Args:
        expresion1 (str): Primera expresión lógica.
        expresion2 (str): Segunda expresión lógica.

        Returns:
        bool: True si las expresiones son equivalentes, False en caso contrario.
        """
        return expresion1 == expresion2

    @staticmethod
    def validez(expresion):
        """Verifica si una expresión lógica es válida.

        Args:
        expresion (str): Expresión lógica.

        Returns:
        bool: True si la expresión es válida para cualquier interpretación, False en caso contrario.
        """
        # La expresión es válida si siempre evalúa a True
        return all(eval(expresion) for i in range(2))

    @staticmethod
    def satisfacibilidad(expresion):
        """Verifica si una expresión lógica es satisfacible.

        Args:
        expresion (str): Expresión lógica.

        Returns:
        bool: True si la expresión es satisfacible para al menos una interpretación, False en caso contrario.
        """
        # La expresión es satisfacible si al menos una interpretación la evalúa a True
        return any(eval(expresion) for i in range(2))

# Definir las variables de proposición
P = True
Q = False

# Expresiones lógicas
expresion1 = "P and Q"
expresion2 = "Q and P"

# Verificar equivalencia
es_equivalente = LogicaProposicional.equivalencia(expresion1, expresion2)

# Verificar validez de la expresión 1
es_valida = LogicaProposicional.validez(expresion1)

# Verificar satisfacibilidad de la expresión 1
es_satisfacible = LogicaProposicional.satisfacibilidad(expresion1)

# Objetivo:
"""
El objetivo de este código es demostrar cómo verificar la equivalencia, validez y satisfacibilidad de expresiones lógicas en Python.
Esto puede ser útil en la verificación de modelos, razonamiento automatizado y otras aplicaciones donde se trabaja con lógica proposicional.
"""

# Resultados
print("Las expresiones son equivalentes:", es_equivalente)
print("La expresión 1 es válida:", es_valida)
print("La expresión 1 es satisfacible:", es_satisfacible)
