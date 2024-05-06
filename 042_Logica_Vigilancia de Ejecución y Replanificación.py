# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:47:27 2024

@author: jared
"""

class Tarea:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

class Planificador:
    def __init__(self, tareas):
        self.tareas = tareas

    def ejecutar_tarea(self, tarea):
        print("Ejecutando tarea:", tarea.nombre)
        # Simular la ejecución de la tarea
        for i in range(tarea.duracion):
            print("  Progreso:", i + 1, "/", tarea.duracion)
        print("Tarea completada:", tarea.nombre)

    def vigilar_ejecucion(self, tarea_actual):
        # Simular la vigilancia de ejecución
        problema = None  # Supongamos que no hay problemas por ahora
        if problema:
            print("Se detectó un problema durante la ejecución:", problema)
            print("Replanificando...")
            self.replanificar(tarea_actual)

    def replanificar(self, tarea_actual):
        # Simular la replanificación
        print("Replanificando tarea:", tarea_actual.nombre)
        # Aquí podrías implementar lógica para generar un nuevo plan basado en el problema detectado

# Definimos las tareas del proyecto
tarea1 = Tarea("Diseñar", 5)
tarea2 = Tarea("Desarrollar", 7)
tarea3 = Tarea("Probar", 4)

# Creamos una lista de tareas planificadas
tareas_planificadas = [tarea1, tarea2, tarea3]

# Creamos un planificador y ejecutamos las tareas planificadas
planificador = Planificador(tareas_planificadas)
for tarea in tareas_planificadas:
    planificador.ejecutar_tarea(tarea)
    planificador.vigilar_ejecucion(tarea)

""" ##OBJETIVO
Este es un ejemplo básico para ilustrar el concepto de vigilancia de ejecución y replanificación
En una implementación real, la lógica de vigilancia y replanificación sería más sofisticada y adaptada a las necesidades específicas del proyecto.
"""