# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:32:01 2024

@author: jared
"""




class MotorDiagnostico:
    """Motor de diagnóstico para identificar la causa raíz de un problema."""

    def __init__(self, reglas):
        self.reglas = reglas

    def diagnosticar(self, sintoma):
        """Realiza el diagnóstico basado en los síntomas."""
        causas = []
        for regla in self.reglas:
            if regla.evaluar(sintoma):
                causas.append(regla.causa)
        return causas

class ReglaDiagnostico:
    """Regla de diagnóstico que relaciona síntomas con causas."""

    def __init__(self, sintomas, causa):
        self.sintomas = sintomas
        self.causa = causa

    def evaluar(self, sintoma):
        """Evalúa si los síntomas coinciden con la regla."""
        return all(sintoma.get(sintoma_nombre) == valor for sintoma_nombre, valor in self.sintomas.items())

# Ejemplo de uso
reglas = [
    ReglaDiagnostico({"fiebre": True, "tos": True}, "Gripe"),
    ReglaDiagnostico({"dolor_cabeza": True, "fatiga": True}, "Migraña"),
    ReglaDiagnostico({"dolor_cabeza": True, "nauseas": True}, "Migraña"),
    ReglaDiagnostico({"fiebre": False, "dolor_garganta": True}, "Resfriado"),
]

motor_diagnostico = MotorDiagnostico(reglas)
sintoma = {"fiebre": True, "tos": True}
causas = motor_diagnostico.diagnosticar(sintoma)
print("Causas probables del síntoma:", causas)

# Objetivo:
"""
El objetivo de este código es implementar un motor de diagnóstico que identifique la causa raíz de un problema basado en reglas de diagnóstico y síntomas proporcionados.
Las reglas de diagnóstico establecen las relaciones entre los síntomas y las posibles causas. El motor de diagnóstico evalúa los síntomas y determina las causas probables del problema basándose en estas reglas.
Este ejemplo muestra cómo utilizar reglas de diagnóstico y un motor de diagnóstico para realizar un diagnóstico de enfermedades basado en síntomas proporcionados.
"""
