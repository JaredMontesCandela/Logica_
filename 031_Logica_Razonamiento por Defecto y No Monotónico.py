# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:44:08 2024

@author: jared
"""

# Definimos una función para el razonamiento por defecto
def razonamiento_defecto(hecho):
    conocimiento = ["A", "B", "C"]  # Conocimiento básico
    
    # Si el hecho está en el conocimiento básico, entonces es verdadero
    if hecho in conocimiento:
        return True
    else:
        return False

# Definimos una función para el razonamiento no monotónico
def razonamiento_no_monotonico(hecho, conocimiento):
    # Si el hecho está en el conocimiento, entonces es verdadero
    if hecho in conocimiento:
        return True
    else:
        return False

# Probamos el razonamiento por defecto
print("Razonamiento por defecto:")
print("¿Se cumple A?", razonamiento_defecto("A"))  # True
print("¿Se cumple D?", razonamiento_defecto("D"))  # False (no está en el conocimiento básico)

# Probamos el razonamiento no monotónico
conocimiento_inicial = ["A", "B", "C"]  # Conocimiento inicial
print("\nRazonamiento no monotónico:")
print("Conocimiento inicial:", conocimiento_inicial)
print("¿Se cumple A?", razonamiento_no_monotonico("A", conocimiento_inicial))  # True
print("¿Se cumple D?", razonamiento_no_monotonico("D", conocimiento_inicial))  # False (no está en el conocimiento inicial)
