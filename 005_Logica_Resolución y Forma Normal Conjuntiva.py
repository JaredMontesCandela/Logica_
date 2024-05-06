# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:45:08 2024

@author: jared
"""

from sympy import symbols, Or, And, Not, to_cnf
from sympy.logic.boolalg import to_dnf

class LogicaProposicional:
    """Clase para operaciones de lógica proposicional."""

    @staticmethod
    def resolucion(expresion1, expresion2):
        """Realiza la resolución de dos expresiones lógicas.

        Args:
        expresion1: Primera expresión lógica.
        expresion2: Segunda expresión lógica.

        Returns:
        bool: True si la resolución es satisfactoria, False en caso contrario.
        """
        clausula1 = expresion1.args
        clausula2 = expresion2.args

        for c1 in clausula1:
            for c2 in clausula2:
                if c1 == Not(c2) or Not(c1) == c2:
                    return True
        return False

    @staticmethod
    def forma_normal_conjuntiva(expresion):
        """Convierte una expresión lógica a su forma normal conjuntiva (FNC).

        Args:
        expresion (str): Expresión lógica.

        Returns:
        str: Forma normal conjuntiva (FNC) de la expresión.
        """
        simbolos = symbols(expresion)
        expresion_logica = eval(expresion)

        # Convertir a forma normal disyuntiva (FND)
        fnd = to_dnf(expresion_logica, True)

        # Convertir a forma normal conjuntiva (FNC)
        fnc = to_cnf(fnd, True)

        return str(fnc)

# Definir las variables de proposición
P, Q = symbols('P Q')

# Expresiones lógicas
expresion1 = Or(P, Q)
expresion2 = Not(P)

# Verificar resolución
se_resuelve = LogicaProposicional.resolucion(expresion1, expresion2)

# Convertir expresión a forma normal conjuntiva (FNC)
fnc_expresion1 = LogicaProposicional.forma_normal_conjuntiva(str(expresion1))
fnc_expresion2 = LogicaProposicional.forma_normal_conjuntiva(str(expresion2))

# Objetivo:
"""
El objetivo de este código es demostrar cómo aplicar la resolución y convertir una expresión lógica a su forma normal conjuntiva (FNC) en Python.
La resolución es un método de inferencia utilizado en la lógica proposicional para demostrar la validez de una fórmula. La FNC es una forma estándar 
de representar una expresión lógica que es útil en diversos algoritmos y técnicas de razonamiento.
"""

# Resultados
print("Se resuelve por resolución:", se_resuelve)
print("FNC de la expresión 1:", fnc_expresion1)
print("FNC de la expresión 2:", fnc_expresion2)
