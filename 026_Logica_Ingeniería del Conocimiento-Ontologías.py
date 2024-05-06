# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:12:03 2024}


@author: jared
"""

# Definimos nuestra ontología utilizando diccionarios
ontologia = {
    "Persona": {
        "propiedades": {
            "Nombre": None,
            "Edad": None,
            "ViveEn": None
        }
    }
}

# Creamos instancias individuales de personas y les asignamos valores para las propiedades
juan = {
    "Nombre": "Juan",
    "Edad": 30,
    "ViveEn": "Madrid"
}

maria = {
    "Nombre": "Maria",
    "Edad": 25,
    "ViveEn": "Barcelona"
}

# Mostramos la ontología y las instancias de personas
print("Ontología:")
for clase, info in ontologia.items():
    print(f"- {clase}:")
    for propiedad in info["propiedades"]:
        print(f"  - {propiedad}")
print("\nInstancias de personas:")
print("- Juan:", juan)
print("- Maria:", maria)

"""
### Objetivo:
El objetivo de este ejemplo es mostrar cómo se puede implementar una ontología simple utilizando diccionarios en Python. En la ontología, definimos una clase 'Persona' con propiedades como 'Nombre', 'Edad' y 'ViveEn'. Luego, creamos instancias individuales de personas (Juan y Maria) y les asignamos valores para estas propiedades. Finalmente, mostramos la ontología y las instancias de personas.
"""
