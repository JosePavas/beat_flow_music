import random


import sys

class Cancion:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista

    def __str__(self):
        return f"{self.nombre} - {self.artista}"    

class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        print(f"Canción '{cancion}' agregada a la lista '{self.nombre}'.")
    
    # def agregar_cancion(self, cancion, nombre_lista):
    #     if nombre_lista in self.listas_reproduccion:
    #         lista = self.listas_reproduccion[nombre_lista]
    #         lista.agregar_cancion(cancion)
    #         print(f"Canción '{cancion}' agregada a la lista '{self.nombre}'.")
    #     else:
    #         print("No existe una lista de reproducción con ese nombre.")
        
    def eliminar_cancion(self, indice):
        if 0 <= indice < len(self.canciones):
            cancion_eliminada = self.canciones.pop(indice)
            print(f"Canción '{cancion_eliminada}' eliminada de la lista '{self.nombre}'.")
        else:
            print("Índice de canción fuera de rango.")

    def mostrar_lista(self):
        if self.canciones:
            print(f"\nLista de reproducción '{self.nombre}':")
            for i, cancion in enumerate(self.canciones):
                print(f"{i+1}. {cancion}")
        else:
            print(f"\nLa lista de reproducción '{self.nombre}' está vacía.")

class BeatFlow:
    def __init__(self):
        self.listas_reproduccion = {}

    def crear_lista_reproduccion(self, nombre_lista):
        if nombre_lista not in self.listas_reproduccion:
            self.listas_reproduccion[nombre_lista] = ListaReproduccion(nombre_lista)
            print(f"Lista de reproducción '{nombre_lista}' creada exitosamente.")
        else:
            print("Ya existe una lista de reproducción con ese nombre.")

    def ver_listas_reproduccion(self):
        print("\nListas de reproducción disponibles:")
        for nombre_lista in self.listas_reproduccion:
            print(nombre_lista)

    # def agregar_cancion(self, cancion, nombre_lista):
    #     if nombre_lista in self.listas_reproduccion:
    #         lista = self.listas_reproduccion[nombre_lista]
    #         lista.agregar_cancion(cancion)
    #         print(f"Canción '{cancion}' agregada a la lista '{self.nombre}'.")
    #     else:
    #         print("No existe una lista de reproducción con ese nombre.")
    
    def agregar_cancion(self, nombre_lista, cancion):
        if nombre_lista in self.listas_reproduccion:
            self.listas_reproduccion[nombre_lista].agregar_cancion(cancion)
        else:
            print("No existe una lista de reproducción con ese nombre.")

    def eliminar_cancion(self, nombre_lista, indice):
        if nombre_lista in self.listas_reproduccion:
            self.listas_reproduccion[nombre_lista].eliminar_cancion(indice)
        else:
            print("No existe una lista de reproducción con ese nombre.")

    def ver_canciones_lista(self, nombre_lista):
        if nombre_lista in self.listas_reproduccion:
            self.listas_reproduccion[nombre_lista].mostrar_lista()
        else:
            print("No existe una lista de reproducción con ese nombre.")


