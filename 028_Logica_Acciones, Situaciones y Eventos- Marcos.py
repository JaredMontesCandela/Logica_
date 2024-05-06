# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:40:00 2024

@author: jared
"""

# Definimos una clase para representar acciones
class Accion:
    def __init__(self, nombre, precondiciones=None, efectos=None):
        self.nombre = nombre
        self.precondiciones = precondiciones if precondiciones is not None else []
        self.efectos = efectos if efectos is not None else []

# Definimos una clase para representar situaciones
class Situacion:
    def __init__(self, nombre, acciones=None):
        self.nombre = nombre
        self.acciones = acciones if acciones is not None else []

# Definimos una clase para representar eventos
class Evento:
    def __init__(self, nombre, situaciones=None):
        self.nombre = nombre
        self.situaciones = situaciones if situaciones is not None else []

# Creamos algunas acciones
ir_trabajo = Accion("Ir al trabajo", precondiciones=["Despertarse", "Vestirse"])
trabajar = Accion("Trabajar")
almorzar = Accion("Almorzar")

# Creamos una situación que involucra estas acciones
situacion_trabajo = Situacion("Día de trabajo", acciones=[ir_trabajo, trabajar, almorzar])

# Creamos un evento que involucra la situación de ir al trabajo
evento_lunes = Evento("Lunes", situaciones=[situacion_trabajo])

# Mostramos la información del evento
print("Evento:", evento_lunes.nombre)
for situacion in evento_lunes.situaciones:
    print("\nSituación:", situacion.nombre)
    print("Acciones:")
    for accion in situacion.acciones:
        print("-", accion.nombre)
        print("  Precondiciones:", accion.precondiciones)
        print("  Efectos:", accion.efectos)

"""
### Objetivo:
El objetivo de este ejemplo es mostrar cómo se pueden representar acciones, situaciones y eventos utilizando clases en Python, creando una estructura básica de marcos. Las acciones representan las acciones que pueden ocurrir en una situación dada, las situaciones representan el contexto en el que ocurren estas acciones, y los eventos representan la secuencia de situaciones que suceden en un periodo de tiempo determinado. Este enfoque proporciona una forma estructurada de modelar y entender el comportamiento en diferentes situaciones y eventos.
"""
