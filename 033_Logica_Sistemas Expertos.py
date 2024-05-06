# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:48:42 2024

@author: jared
"""

# Definimos una función para el sistema experto
def sistema_experto(sintomas):
    if "fiebre" in sintomas and "tos" in sintomas:
        return "Posible infección respiratoria"
    elif "dolor de cabeza" in sintomas and "náuseas" in sintomas:
        return "Posible migraña"
    elif "erupción cutánea" in sintomas:
        return "Posible reacción alérgica"
    else:
        return "No se puede determinar la enfermedad"

# Ejemplo de uso del sistema experto
sintomas_paciente_1 = ["fiebre", "tos"]
sintomas_paciente_2 = ["dolor de cabeza", "náuseas"]
sintomas_paciente_3 = ["erupción cutánea", "picazón"]

# Evaluamos los síntomas de cada paciente con el sistema experto
diagnostico_paciente_1 = sistema_experto(sintomas_paciente_1)
diagnostico_paciente_2 = sistema_experto(sintomas_paciente_2)
diagnostico_paciente_3 = sistema_experto(sintomas_paciente_3)

# Mostramos los diagnósticos
print("Diagnóstico del paciente 1:", diagnostico_paciente_1)
print("Diagnóstico del paciente 2:", diagnostico_paciente_2)
print("Diagnóstico del paciente 3:", diagnostico_paciente_3)
