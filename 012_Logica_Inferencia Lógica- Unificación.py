# -*- coding: utf-8 -*-
"""
Created on Sat May  4 10:01:30 2024

@author: jared
"""

class Unificador:
    """Clase para realizar unificación en inferencia lógica."""

    @staticmethod
    def unificar(termino1, termino2, sustitucion=None):
        """Realiza la unificación de dos términos."""
        if sustitucion is None:
            sustitucion = {}

        if sustitucion is False:
            return False

        if termino1 == termino2:
            return sustitucion

        if isinstance(termino1, str) and termino1[0].islower():
            return Unificador.unificar_variable(termino1, termino2, sustitucion)
        elif isinstance(termino2, str) and termino2[0].islower():
            return Unificador.unificar_variable(termino2, termino1, sustitucion)
        elif isinstance(termino1, list) and isinstance(termino2, list):
            return Unificador.unificar(termino1[1:], termino2[1:], Unificador.unificar(termino1[0], termino2[0], sustitucion))
        else:
            return False

    @staticmethod
    def unificar_variable(variable, termino, sustitucion):
        """Realiza la unificación cuando uno de los términos es una variable."""
        if variable in sustitucion:
            return Unificador.unificar(sustitucion[variable], termino, sustitucion)
        elif termino in sustitucion:
            return Unificador.unificar(variable, sustitucion[termino], sustitucion)
        else:
            sustitucion[variable] = termino
            return sustitucion

# Ejemplo de uso
termino1 = ["f", "X", "a"]
termino2 = ["f", "b", "Y"]
sustitucion = Unificador.unificar(termino1, termino2)
print("Sustitución unificada:", sustitucion)

# Objetivo:
"""
El objetivo de este código es implementar un algoritmo de unificación en inferencia lógica.
La unificación es un proceso utilizado en inferencia lógica para encontrar una sustitución común que haga que dos términos sean idénticos.
Este ejemplo muestra cómo utilizar la clase Unificador para unificar dos términos dados y encontrar una sustitución que los haga iguales.
"""
