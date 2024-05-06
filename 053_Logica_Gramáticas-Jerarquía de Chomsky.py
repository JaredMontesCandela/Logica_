# -*- coding: utf-8 -*-
"""
@author: jared
"""

# Definición de la gramática
gramatica = {
    'S': ['NP VP'],
    'NP': ['Det N', 'Det N PP'],
    'VP': ['V NP', 'V NP PP'],
    'PP': ['P NP'],
    'Det': ['el', 'la', 'un', 'una'],
    'N': ['perro', 'gato', 'hombre', 'mujer'],
    'V': ['persigue', 'come', 'duerme', 'corre'],
    'P': ['en', 'sobre', 'bajo', 'junto a']
}

# Impresión de la gramática
print("Gramática:")
for categoria, producciones in gramatica.items():
    print(categoria, '->', ' | '.join(producciones))

"""
Este ejemplo define una gramática que describe la estructura de las frases en español
La gramática está compuesta por producciones que definen cómo se pueden generar
las diferentes partes de la oración, como sustantivos (N), verbos (V), determinantes (Det), etc.
"""