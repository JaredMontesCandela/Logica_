# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:38:26 2024

@author: jared
"""

class MotorInferencia:
    """Motor de inferencia para realizar inferencias lógicas proposicionales."""

    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def inferir(self, regla):
        """Realiza una inferencia lógica basada en una regla dada.

        Args:
        regla (tuple): Regla lógica en forma de tupla (antecedente, consecuente).

        Returns:
        bool: Resultado de la inferencia.
        """
        antecedente, consecuente = regla
        if self.base_conocimiento.obtener_verdad(antecedente):
            return self.base_conocimiento.obtener_verdad(consecuente)
        else:
            return False

class BaseConocimiento:
    """Base de conocimiento para almacenar información y determinar la verdad de proposiciones."""

    def __init__(self):
        self.conocimiento = {}

    def agregar_conocimiento(self, proposicion, verdad):
        """Agrega información a la base de conocimiento.

        Args:
        proposicion (str): Proposición lógica.
        verdad (bool): Valor de verdad de la proposición.
        """
        self.conocimiento[proposicion] = verdad

    def obtener_verdad(self, proposicion):
        """Recupera el valor de verdad de una proposición.

        Args:
        proposicion (str): Proposición cuyo valor de verdad se desea conocer.

        Returns:
        bool: Valor de verdad de la proposición.
        """
        return self.conocimiento.get(proposicion, False)

# Crear una instancia de la base de conocimiento
base = BaseConocimiento()

# Agregar información a la base de conocimiento
base.agregar_conocimiento("P", True)
base.agregar_conocimiento("Q", False)
base.agregar_conocimiento("R", True)

# Crear una instancia del motor de inferencia
motor = MotorInferencia(base)

# Realizar inferencias lógicas
regla = ("P and Q", "R")
resultado = motor.inferir(regla)

# Objetivo de la Inferencia Lógica Proposicional
"""
El objetivo de esta implementación es realizar inferencias lógicas proposicionales basadas en reglas dadas y en la información almacenada en una base de conocimiento. 
La base de conocimiento contiene proposiciones y sus valores de verdad asociados, mientras que el motor de inferencia utiliza estas proposiciones y reglas para deducir 
nuevos hechos. Esto puede ser útil en sistemas expertos, razonamiento automatizado y otras aplicaciones donde se necesita tomar decisiones basadas en lógica proposicional.
"""

# Imprimir resultado de la inferencia
print("La inferencia es:", resultado)
