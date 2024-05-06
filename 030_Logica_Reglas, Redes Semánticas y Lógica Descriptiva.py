# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:43:17 2024

@author: jared
"""

# Definimos una clase para representar reglas
class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

# Definimos una clase para representar nodos en la red semántica
class Nodo:
    def __init__(self, nombre, propiedades=None, relaciones=None):
        self.nombre = nombre
        self.propiedades = propiedades if propiedades is not None else {}
        self.relaciones = relaciones if relaciones is not None else {}

# Creamos algunos nodos para representar conceptos en la red semántica
nodo_persona = Nodo("Persona", propiedades={"Género": "Masculino"})
nodo_animal = Nodo("Animal", propiedades={"Género": "Femenino"})
nodo_mascota = Nodo("Mascota", relaciones={"Es un tipo de": "Animal"})

# Creamos algunas reglas que relacionan conceptos en la red semántica
regla_1 = Regla("Persona", "Mascota")
regla_2 = Regla("Animal", "Mascota")

# Mostramos la información de los nodos y las reglas
print("Nodos en la red semántica:")
for nodo in [nodo_persona, nodo_animal, nodo_mascota]:
    print(f"- {nodo.nombre}:")
    print("  Propiedades:", nodo.propiedades)
    print("  Relaciones:", nodo.relaciones)

print("\nReglas:")
print(f"- Si es {regla_1.antecedente}, entonces es {regla_1.consecuente}")
print(f"- Si es {regla_2.antecedente}, entonces es {regla_2.consecuente}")

"""
### Objetivo:
El objetivo de este ejemplo es mostrar cómo se pueden representar reglas y redes semánticas utilizando lógica descriptiva en Python. En la red semántica, creamos nodos para representar conceptos y establecemos propiedades y relaciones entre ellos. Luego, definimos reglas que relacionan estos conceptos en la red semántica. Este enfoque proporciona una forma estructurada de modelar relaciones entre conceptos y realizar inferencias basadas en estas reglas en Python.
"""
