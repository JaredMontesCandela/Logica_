# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:17:11 2024

@author: jared
"""

class BaseConocimiento:
    """Base de conocimiento para el ejemplo de encadenamiento."""

    def __init__(self):
        self.hechos = {}
        self.reglas = {}

    def agregar_hecho(self, hecho, valor):
        """Agrega un hecho a la base de conocimiento.

        Args:
        hecho (str): Hecho.
        valor (bool): Valor de verdad del hecho.
        """
        self.hechos[hecho] = valor

    def agregar_regla(self, antecedentes, consecuente):
        """Agrega una regla a la base de conocimiento.

        Args:
        antecedentes (list): Lista de antecedentes.
        consecuente (str): Consecuente de la regla.
        """
        self.reglas[consecuente] = antecedentes

class EncadenamientoHaciaAdelante:
    """Implementación del encadenamiento hacia adelante."""

    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def inferir(self):
        """Realiza la inferencia hacia adelante."""

        nuevo_hecho_agregado = True

        while nuevo_hecho_agregado:
            nuevo_hecho_agregado = False

            for consecuente, antecedentes in self.base_conocimiento.reglas.items():
                if consecuente not in self.base_conocimiento.hechos:
                    if all(antecedente in self.base_conocimiento.hechos and self.base_conocimiento.hechos[antecedente] for antecedente in antecedentes):
                        self.base_conocimiento.agregar_hecho(consecuente, True)
                        nuevo_hecho_agregado = True
                        print(f"Se agregó el hecho '{consecuente}' a la base de conocimiento.")

class EncadenamientoHaciaAtras:
    """Implementación del encadenamiento hacia atrás."""

    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def inferir(self, objetivo):
        """Realiza la inferencia hacia atrás."""

        if objetivo in self.base_conocimiento.hechos:
            return self.base_conocimiento.hechos[objetivo]

        for consecuente, antecedentes in self.base_conocimiento.reglas.items():
            if objetivo == consecuente:
                if all(self.inferir(antecedente) for antecedente in antecedentes):
                    self.base_conocimiento.agregar_hecho(objetivo, True)
                    return True

        return False

# Ejemplo de uso
base = BaseConocimiento()
base.agregar_hecho("Q", True)
base.agregar_regla(["P"], "Q")
base.agregar_regla([], "P")

print("Encadenamiento hacia adelante:")
encadenamiento_adelante = EncadenamientoHaciaAdelante(base)
encadenamiento_adelante.inferir()

print("\nEncadenamiento hacia atrás:")
encadenamiento_atras = EncadenamientoHaciaAtras(base)
print("Se puede probar si 'P' es verdadero:", encadenamiento_atras.inferir("P"))
print("Se puede probar si 'Q' es verdadero:", encadenamiento_atras.inferir("Q"))

# Objetivo:
"""
El objetivo de este código es implementar el encadenamiento hacia adelante y hacia atrás en Python. El encadenamiento hacia adelante se utiliza para inferir nuevos hechos a partir de hechos y reglas previamente establecidos en la base de conocimiento. Por otro lado, el encadenamiento hacia atrás se utiliza para determinar si un objetivo dado puede ser probado a partir de la base de conocimiento, utilizando reglas y hechos disponibles.

Este ejemplo ilustra cómo se pueden implementar estos dos métodos de inferencia y cómo se pueden aplicar en una base de conocimiento simple con hechos y reglas.
"""

