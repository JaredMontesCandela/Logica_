# -*- coding: utf-8 -*-
"""
@author: jared
"""

class AnalizadorSemantico:
    def __init__(self, expresion):
        self.expresion = expresion

    def analizar(self):
        """
        Realiza el análisis semántico de la expresión.

        Returns:
        - bool: True si la expresión es semánticamente válida, False en caso contrario.
        """
        try:
            resultado = eval(self.expresion)
            return True
        except Exception as e:
            print("Error semántico:", e)
            return False

# Ejemplo de uso
expresion = "2 * (3 + 4)"  # Expresión aritmética válida
analizador = AnalizadorSemantico(expresion)
es_valida = analizador.analizar()
if es_valida:
    print("La expresión es semánticamente válida.")
else:
    print("La expresión tiene errores semánticos.")


"""
Si la expresión se evalúa correctamente sin errores, se considera que es semánticamente 
válida. Si ocurre algún error durante la evaluación, se informa y se considera que la expresión tiene errores semánticos.
"""