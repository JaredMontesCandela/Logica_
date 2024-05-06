# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:42:12 2024

@author: jared
"""

# Definimos una clase para representar creencias
class Creencia:
    def __init__(self, sujeto, predicado, objeto):
        self.sujeto = sujeto
        self.predicado = predicado
        self.objeto = objeto

# Creamos algunas creencias
creencia_1 = Creencia("Juan", "cree que", "el sol es amarillo")
creencia_2 = Creencia("Maria", "cree que", "los gatos son adorables")

# Mostramos las creencias
print("Creencias:")
print(f"- {creencia_1.sujeto} {creencia_1.predicado} {creencia_1.objeto}")
print(f"- {creencia_2.sujeto} {creencia_2.predicado} {creencia_2.objeto}")

"""
### Objetivo:
El objetivo de este ejemplo es mostrar cómo se pueden representar creencias como objetos mentales en Python utilizando una clase simple. Las creencias son afirmaciones que un individuo tiene sobre el mundo, y pueden ser sobre una amplia variedad de temas. En este ejemplo, creamos objetos de creencia que representan las creencias de dos personas diferentes. Este enfoque proporciona una forma estructurada de modelar las creencias y permite trabajar con ellas de manera programática.
"""
