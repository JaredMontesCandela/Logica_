# -*- coding: utf-8 -*-
"""
Created on Sat May  4 10:46:11 2024

@author: jared
"""

class AgenteLogico:
    def __init__(self, mundo):
        self.mundo = mundo

    def planificar(self):
        # Reglas lógicas para planificar el movimiento del bloque A sobre el bloque B
        # 1. Si A está sobre B, no hacemos nada.
        # 2. Si A está sobre otro bloque y el bloque B está libre, movemos A sobre B.
        # 3. Si A está en el suelo y B está libre, movemos A sobre B.
        if ('A' in self.mundo and 'B' in self.mundo) and (self.mundo['A'] == 'B'):
            print("A ya está sobre B, no es necesario hacer nada.")
        elif ('A' in self.mundo and 'B' in self.mundo) and (self.mundo['A'] != 'B' and self.mundo['B'] is None):
            print("Mover A sobre B")
            self.mundo['B'] = 'A'
            self.mundo['A'] = None
        elif 'A' in self.mundo and 'B' not in self.mundo:
            print("Mover A sobre el suelo")
            self.mundo['B'] = 'A'
            self.mundo['A'] = None
        else:
            print("No es posible realizar la acción")

# Mundo de bloques
mundo_de_bloques = {'A': 'B', 'B': None, 'C': None}

# Creamos un agente lógico
agente = AgenteLogico(mundo_de_bloques)

# Planificamos la acción
agente.planificar()
