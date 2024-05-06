# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:21:50 2024

@author: jared
"""

# Definimos una clase para representar una tarea en la planificación de orden parcial
class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.precedencias = set()  # Conjunto de tareas que deben completarse antes de esta tarea

    def agregar_precedencia(self, tarea):
        self.precedencias.add(tarea)

# Función para realizar la planificación de orden parcial
def planificacion_orden_parcial(tareas):
    # Creamos un diccionario para almacenar el tiempo de finalización de cada tarea
    tiempo_finalizacion = {}

    # Inicializamos el tiempo de finalización de cada tarea como 0
    for tarea in tareas:
        tiempo_finalizacion[tarea] = 0

    # Iteramos sobre todas las tareas
    for tarea in tareas:
        # Si la tarea no tiene precedencias, su tiempo de finalización es 0
        if not tarea.precedencias:
            tiempo_finalizacion[tarea] = 0
        else:
            # Si tiene precedencias, calculamos su tiempo de finalización como el máximo de los tiempos de finalización de sus precedencias más 1
            tiempo_finalizacion[tarea] = max(tiempo_finalizacion[precedencia] for precedencia in tarea.precedencias) + 1

    return tiempo_finalizacion

# Creamos algunas tareas
tarea_A = Tarea("A")
tarea_B = Tarea("B")
tarea_C = Tarea("C")
tarea_D = Tarea("D")
tarea_E = Tarea("E")

# Definimos las precedencias entre las tareas
tarea_B.agregar_precedencia(tarea_A)
tarea_C.agregar_precedencia(tarea_A)
tarea_D.agregar_precedencia(tarea_B)
tarea_D.agregar_precedencia(tarea_C)
tarea_E.agregar_precedencia(tarea_D)

# Creamos una lista con todas las tareas
tareas = [tarea_A, tarea_B, tarea_C, tarea_D, tarea_E]

# Realizamos la planificación de orden parcial
tiempo_finalizacion = planificacion_orden_parcial(tareas)

# Mostramos el tiempo de finalización de cada tarea
for tarea, tiempo in tiempo_finalizacion.items():
    print("Tarea:", tarea.nombre, "- Tiempo de finalización:", tiempo)
