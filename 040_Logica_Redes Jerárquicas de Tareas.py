# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:35:21 2024

@author: jared
"""

class Tarea:
    def __init__(self, nombre, sub_tareas=None):
        self.nombre = nombre
        self.sub_tareas = sub_tareas if sub_tareas else []

    def agregar_subtarea(self, sub_tarea):
        self.sub_tareas.append(sub_tarea)

def imprimir_tareas(tarea, nivel=0):
    print("  " * nivel + tarea.nombre)
    for sub_tarea in tarea.sub_tareas:
        imprimir_tareas(sub_tarea, nivel + 1)

# Crear las tareas
tarea_principal = Tarea("Tarea Principal")
tarea_secundaria1 = Tarea("Tarea Secundaria 1")
tarea_secundaria2 = Tarea("Tarea Secundaria 2")
tarea_terciaria = Tarea("Tarea Terciaria")

# Construir la jerarquía de tareas
tarea_principal.agregar_subtarea(tarea_secundaria1)
tarea_principal.agregar_subtarea(tarea_secundaria2)
tarea_secundaria1.agregar_subtarea(tarea_terciaria)

# Imprimir la estructura de tareas
print("Estructura de Tareas:")
imprimir_tareas(tarea_principal)

"""
Objetivo:
El objetivo de este código es proporcionar una representación básica de una red jerárquica de tareas en Python. Se define una clase Tarea que puede contener sub-tareas. Luego, se crea un conjunto de tareas y se organiza jerárquicamente. Finalmente, se imprime la estructura de tareas para visualizar la jerarquía.
"""
