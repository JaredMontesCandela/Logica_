# -*- coding: utf-8 -*-
"""
Created on Sat May  4 09:58:51 2024

@author: jared
"""

class SistemaRecomendacionPeliculas:
    """Sistema de recomendación de películas basado en reglas de conocimiento."""

    def __init__(self, conocimiento):
        self.conocimiento = conocimiento

    def recomendar_pelicula(self, usuario):
        """Recomienda una película al usuario basándose en su perfil."""
        peliculas_recomendadas = []
        for regla in self.conocimiento:
            if regla.evaluar(usuario):
                peliculas_recomendadas.append(regla.pelicula)
        return peliculas_recomendadas

class ReglaRecomendacion:
    """Regla de recomendación que relaciona el perfil del usuario con una película."""

    def __init__(self, perfil, pelicula):
        self.perfil = perfil
        self.pelicula = pelicula

    def evaluar(self, usuario):
        """Evalúa si el perfil del usuario coincide con la regla."""
        return all(usuario.get(atributo) == valor for atributo, valor in self.perfil.items())

# Ejemplo de uso
conocimiento = [
    ReglaRecomendacion({"genero": "acción", "edad": "adulto"}, "Terminator"),
    ReglaRecomendacion({"genero": "comedia", "edad": "joven"}, "Superbad"),
    ReglaRecomendacion({"genero": "romance", "edad": "adulto"}, "The Notebook"),
]
#Datos del usuario
sistema_recomendacion = SistemaRecomendacionPeliculas(conocimiento)
usuario = {"genero": "comedia", "edad": "joven"}

peliculas_recomendadas = sistema_recomendacion.recomendar_pelicula(usuario)
print("Peliculas recomendadas para el usuario:", peliculas_recomendadas)

# Objetivo:
"""
El objetivo de este código es implementar un sistema de recomendación de películas basado en reglas de conocimiento.
El sistema utiliza reglas de recomendación que relacionan el perfil del usuario (como género y edad) con películas específicas.
El objetivo es proporcionar recomendaciones de películas personalizadas para los usuarios basándose en su perfil y preferencias.
Este ejemplo muestra cómo aplicar ingeniería del conocimiento para diseñar un sistema de recomendación que utiliza reglas de conocimiento para recomendar películas a los usuarios.
"""
