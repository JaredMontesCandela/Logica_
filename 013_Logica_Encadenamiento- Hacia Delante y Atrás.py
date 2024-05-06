# -*- coding: utf-8 -*-
"""


@author: jared
"""
class SistemaRecomendacionRestaurantes:
    """Sistema de recomendación de restaurantes con encadenamiento hacia adelante y hacia atrás."""

    def __init__(self, base_conocimiento, reglas):
        self.base_conocimiento = base_conocimiento
        self.reglas = reglas

    def encadenamiento_hacia_adelante(self):
        """Realiza el encadenamiento hacia adelante en el sistema de recomendación."""
        hechos_nuevos = True
        while hechos_nuevos:
            hechos_nuevos = False
            for regla in self.reglas:
                if regla.aplicar(self.base_conocimiento):
                    hechos_nuevos = True

    def encadenamiento_hacia_atras(self, objetivo):
        """Realiza el encadenamiento hacia atrás en el sistema de recomendación."""
        return self.verificar_objetivo(objetivo, {})

    def verificar_objetivo(self, objetivo, sustitucion):
        """Verifica si se puede probar el objetivo con la sustitución dada."""
        for regla in self.reglas:
            if regla.conclusion == objetivo:
                if regla.evaluar_antecedentes(self, sustitucion):
                    return sustitucion
        return False

class ReglaRecomendacion:
    """Regla de recomendación basada en preferencias del cliente."""

    def __init__(self, antecedentes, conclusion):
        self.antecedentes = antecedentes
        self.conclusion = conclusion

    def evaluar_antecedentes(self, sistema, sustitucion):
        """Evalúa si se cumplen los antecedentes de la regla."""
        for antecedente in self.antecedentes:
            if antecedente not in sistema:
                return False
        return True

    def aplicar(self, base_conocimiento):
        """Aplica la regla si los antecedentes se cumplen."""
        if self.evaluar_antecedentes(base_conocimiento, {}):
            base_conocimiento.append(self.conclusion)
            return True
        return False


# Ejemplo de uso
base_conocimiento = ["tipo(italiano, pasta)", "tipo(chino, arroz)", "tipo(mexicano, tacos)"]
reglas = [
    ReglaRecomendacion(["tipo(X, pasta)"], "recomendacion(X, 'Spaghetti House')"),
    ReglaRecomendacion(["tipo(X, arroz)"], "recomendacion(X, 'Chopsticks')"),
    ReglaRecomendacion(["tipo(X, tacos)"], "recomendacion(X, 'Taco Stand')")
]

sistema = SistemaRecomendacionRestaurantes(base_conocimiento, reglas)

print("Encadenamiento hacia adelante:")
sistema.encadenamiento_hacia_adelante()
print("Base de conocimiento actualizada:", sistema.base_conocimiento)

print("\nEncadenamiento hacia atrás:")
objetivo = "recomendacion(chino, Restaurante)"
sustitucion = sistema.encadenamiento_hacia_atras(objetivo)
print("Objetivo:", objetivo)
print("Sustitución encontrada:", sustitucion)

# Objetivo:
"""
El objetivo de este código es implementar un sistema de recomendación de restaurantes con encadenamiento hacia adelante y hacia atrás.
El encadenamiento hacia adelante utiliza las reglas de recomendación para inferir recomendaciones de restaurantes en función de los tipos de cocina.
El encadenamiento hacia atrás permite a los usuarios solicitar recomendaciones específicas y encontrar restaurantes recomendados para un tipo de cocina dado.
Este ejemplo muestra cómo usar un sistema de recomendación con ambos tipos de encadenamiento para proporcionar recomendaciones personalizadas de restaurantes.
"""
