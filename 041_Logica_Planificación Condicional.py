# -*- coding: utf-8 -*-
"""


@author: jared
"""

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

    def ejecutar(self, estado):
        # Verificar si se cumplen todas las precondiciones
        for precondicion in self.precondiciones:
            if precondicion not in estado:
                return False

        # Aplicar los efectos de la acción al estado
        for efecto in self.efectos:
            if efecto[0] == '-':
                estado.discard(efecto[1:])
            else:
                estado.add(efecto)

        return True

# Definimos las acciones disponibles
acciones = [
    Accion("Recoger", {"RobotEnCasilla", "ObjetoEnCasilla"}, {"-ObjetoEnCasilla", "RobotConObjeto"}),
    Accion("Mover", {"RobotEnCasilla", "-RobotConObjeto"}, {"-RobotEnCasilla", "RobotEnOtraCasilla"}),
    Accion("Soltar", {"RobotConObjeto"}, {"ObjetoEnCasilla", "-RobotConObjeto"})
]

# Definimos el estado inicial y el estado meta
estado_inicial = {"RobotEnCasilla", "ObjetoEnCasilla"}
estado_meta = {"RobotConObjeto"}

# Planificación condicional
plan = []
estado_actual = estado_inicial.copy()
for accion in acciones:
    if accion.ejecutar(estado_actual):
        plan.append(accion.nombre)
        if estado_meta.issubset(estado_actual):
            break  # Se ha alcanzado el estado meta, terminar la planificación
    else:
        plan = None  # No se puede alcanzar el estado meta con las acciones disponibles
        break

# Imprimir el plan resultante
if plan:
    print("Plan encontrado:", plan)
else:
    print("No se pudo encontrar un plan.")
""" ##OBJETIVO
El objetivo de este código es ilustrar un ejemplo básico de planificación condicional en Python.    
e definen acciones con precondiciones y efectos, y se intenta alcanzar un estado meta a partir de un estado inicial aplicando estas acciones.
La planificación condicional implica ejecutar acciones solo si se cumplen sus precondiciones.
El objetivo es encontrar un plan de acciones que lleve al estado meta desde el estado inicial

"""