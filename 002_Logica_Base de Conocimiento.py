# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:31:20 2024

@author: jared
"""

class BaseConocimiento:
    """Base de conocimiento para almacenar y recuperar información."""

    def __init__(self):
        self.conocimiento = {}

    def agregar_conocimiento(self, tema, informacion):
        """Agrega información a la base de conocimiento bajo un tema dado.

        Args:
        tema (str): Tema al que pertenece la información.
        informacion (str): Información a ser almacenada.
        """
        if tema in self.conocimiento:
            self.conocimiento[tema].append(informacion)
        else:
            self.conocimiento[tema] = [informacion]

    def obtener_informacion(self, tema):
        """Recupera la información almacenada bajo un tema dado.

        Args:
        tema (str): Tema del que se desea recuperar la información.

        Returns:
        list: Lista de información relacionada con el tema.
        """
        if tema in self.conocimiento:
            return self.conocimiento[tema]
        else:
            return []

# Crear una instancia de la base de conocimiento
base = BaseConocimiento()

# Agregar información sobre Python
base.agregar_conocimiento("Python", "Python es un lenguaje de programación de alto nivel.")
base.agregar_conocimiento("Python", "Python es conocido por su sintaxis simple y legible.")

# Agregar información sobre IA
base.agregar_conocimiento("IA", "La inteligencia artificial es el campo de estudio de algoritmos y modelos computacionales que buscan emular la inteligencia humana.")
base.agregar_conocimiento("IA", "La IA abarca áreas como el aprendizaje automático, el procesamiento de lenguaje natural y la visión por computadora.")


# Ejemplo de uso: Mostrar información sobre Python y IA
print("Información sobre Python:")
print(base.obtener_informacion("Python"))

print("\nInformación sobre IA:")
print(base.obtener_informacion("IA"))

# Objetivo de la Base de Conocimiento
"""
El objetivo de esta base de conocimiento es almacenar información sobre diferentes temas, como Python y la Inteligencia Artificial (IA), 
y proporcionar un mecanismo para recuperar esta información cuando sea necesario. Esto puede ser útil para consultas rápidas o para mantener 
un repositorio organizado de conocimiento sobre ciertos temas.
"""