# -*- coding: utf-8 -*-
"""
@author: jared
"""

import re

class Parser:
    def __init__(self, cadena):
        self.cadena = cadena
        self.posicion = 0

    def analizar(self):
        """
        Realiza el análisis sintáctico de la expresión.

        Returns:
        - bool: True si la expresión es válida, False en caso contrario.
        """
        try:
            self.expr()
            return True
        except SyntaxError:
            return False

    def expr(self):
        """
        Verifica la estructura de la expresión.
        """
        self.term()
        while self.posicion < len(self.cadena) and self.cadena[self.posicion] in ['+', '-']:
            self.posicion += 1
            self.term()

    def term(self):
        """
        Verifica la estructura del término.
        """
        self.factor()
        while self.posicion < len(self.cadena) and self.cadena[self.posicion] in ['*', '/']:
            self.posicion += 1
            self.factor()

    def factor(self):
        """
        Verifica la estructura del factor.
        """
        if re.match(r'\d+', self.cadena[self.posicion:]):
            self.posicion += len(re.match(r'\d+', self.cadena[self.posicion:]).group())
        elif self.cadena[self.posicion] == '(':
            self.posicion += 1
            self.expr()
            if self.cadena[self.posicion] != ')':
                raise SyntaxError("Error de sintaxis: se esperaba ')'")
            self.posicion += 1
        else:
            raise SyntaxError("Error de sintaxis: token no reconocido")

# Ejemplo de uso
expresion = "2 * (3 + 4)"
parser = Parser(expresion)
es_valida = parser.analizar()
if es_valida:
    print("La expresión es sintácticamente válida.")
else:
    print("La expresión tiene errores de sintaxis.")


"""
El objetivo de este código es realizar un análisis sintáctico de una expresión aritmética para verificar su estructura.
"""
