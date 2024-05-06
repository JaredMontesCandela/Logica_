# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:12:42 2024

@author: jared
"""
# Definimos nuestra taxonomía utilizando diccionarios
taxonomia = {
    "Animal": {
        "subcategorias": {
            "Mamifero": {
                "objetos": ["Perro", "Gato", "Elefante"]
            },
            "Ave": {
                "objetos": ["Aguila", "Pato", "Gorrión"]
            }
        }
    },
    "Planta": {
        "subcategorias": {
            "Flor": {
                "objetos": ["Rosa", "Girasol", "Lirio"]
            },
            "Arbusto": {
                "objetos": ["Cactus", "Hiedra", "Bambú"]
            }
        }
    }
}

# Mostramos la taxonomía y los objetos en cada categoría
print("Taxonomía:")
for categoria, info in taxonomia.items():
    print(f"- {categoria}:")
    for subcategoria, objetos in info["subcategorias"].items():
        print(f"  - {subcategoria}:")
        print("    - Objetos:", objetos["objetos"])

"""
### Objetivo:
El objetivo de este ejemplo es mostrar cómo se puede implementar una taxonomía de categorías y objetos utilizando diccionarios en Python. En la taxonomía, tenemos categorías como 'Animal' y 'Planta', cada una con subcategorías y objetos asociados. La taxonomía nos permite organizar y clasificar diferentes tipos de objetos en un sistema jerárquico.
"""

