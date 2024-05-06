# -*- coding: utf-8 -*-
"""

@author: jared
"""

class Regla:
    def __init__(self, antecedente, consecuente, confianza):
        """
        Clase que representa una regla aprendida por el algoritmo FOIL.

        Args:
        - antecedente (list): Lista de condiciones del antecedente.
        - consecuente (str): Consecuente de la regla.
        - confianza (float): Confianza de la regla.
        """
        self.antecedente = antecedente
        self.consecuente = consecuente
        self.confianza = confianza

def calcular_confianza(positivos_cubiertos, total_cubiertos, total_positivos):
    """
    Calcula la confianza de una regla.

    Args:
    - positivos_cubiertos (int): Número de ejemplos positivos cubiertos por la regla.
    - total_cubiertos (int): Número total de ejemplos cubiertos por la regla.
    - total_positivos (int): Número total de ejemplos positivos en el conjunto de datos.

    Returns:
    - float: Confianza de la regla.
    """
    return positivos_cubiertos / total_cubiertos if total_cubiertos > 0 else 0

def aprender_reglas_foil(ejemplos_positivos, ejemplos_negativos, variables):
    """
    Aprende reglas utilizando el algoritmo FOIL.

    Args:
    - ejemplos_positivos (list): Lista de ejemplos positivos.
    - ejemplos_negativos (list): Lista de ejemplos negativos.
    - variables (list): Lista de variables.

    Returns:
    - list: Lista de reglas aprendidas.
    """
    reglas = []

    for variable in variables:
        antecedente = [variable]
        positivos_cubiertos = sum(1 for ejemplo in ejemplos_positivos if variable in ejemplo)
        negativos_cubiertos = sum(1 for ejemplo in ejemplos_negativos if variable in ejemplo)
        total_cubiertos = positivos_cubiertos + negativos_cubiertos

        for ejemplo in ejemplos_positivos:
            if all(var in ejemplo for var in antecedente):
                total_cubiertos += 1

        confianza = calcular_confianza(positivos_cubiertos, total_cubiertos, len(ejemplos_positivos))
        reglas.append(Regla(antecedente, "positivo", confianza))

    return reglas

# Ejemplo de uso
ejemplos_positivos = [["sol", "calor", "alta", "debil"],
                      ["sol", "calor", "alta", "fuerte"],
                      ["nublado", "calor", "alta", "debil"],
                      ["lluvia", "templado", "alta", "debil"]]
ejemplos_negativos = [["lluvia", "frio", "normal", "debil"],
                      ["lluvia", "frio", "normal", "fuerte"],
                      ["nublado", "frio", "normal", "fuerte"]]
variables = ["sol", "calor", "alta", "debil", "nublado", "lluvia", "frio", "normal", "fuerte", "templado"]

reglas_aprendidas = aprender_reglas_foil(ejemplos_positivos, ejemplos_negativos, variables)
for regla in reglas_aprendidas:
    print("Antecedente:", regla.antecedente)
    print("Consecuente:", regla.consecuente)
    print("Confianza:", regla.confianza)
    print()
"""

El objetivo de este código es aprender reglas de clasificación utilizando el algoritmo FOIL. 
El algoritmo busca patrones en los ejemplos positivos y negativos para generar reglas de clasificación.
Estas reglas se utilizan para predecir la clase de nuevos ejemplos. El código proporciona una implementación
básica del algoritmo FOIL y muestra cómo se pueden aprender reglas a partir de ejemplos de entrenamiento.
"""
