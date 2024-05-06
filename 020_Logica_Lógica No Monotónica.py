# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:05:40 2024

@author: jared
"""

class MundoBloques:
    def __init__(self):
        self.bloques = set()

    def apilar(self, bloque_superior, bloque_inferior):
        if bloque_superior != bloque_inferior and bloque_superior not in self.bloques and bloque_inferior in self.bloques:
            self.bloques.add(bloque_superior)

    def desapilar(self, bloque_superior, bloque_inferior):
        if bloque_superior in self.bloques and bloque_inferior in self.bloques:
            self.bloques.remove(bloque_superior)

    def verificar_estado(self, bloque):
        return bloque in self.bloques

# Creamos un mundo de bloques
mundo = MundoBloques()

# Realizamos algunas acciones en el mundo de bloques
mundo.apilar('B', 'A')
mundo.apilar('C', 'B')
mundo.desapilar('C', 'B')

# Verificamos el estado de ciertos bloques
print("¿El bloque A está en algún lugar?", mundo.verificar_estado('A'))  # True
print("¿El bloque B está en algún lugar?", mundo.verificar_estado('B'))  # False
print("¿El bloque C está en algún lugar?", mundo.verificar_estado('C'))  # False
