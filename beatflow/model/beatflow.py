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
    def reproducir_cola(self):
        if self.cola_reproduccion:
            self.cancion_actual = self.cola_reproduccion.pop(0)
            print(f"Reproduciendo: {self.cancion_actual}")
        else:
            print("La cola de reproducción está vacía.")

    def siguiente_cancion(self):
        if self.cola_reproduccion:
            self.cancion_actual = self.cola_reproduccion[0]
            print(f"Siguiente canción: {self.cancion_actual}")
        else:
            print("La cola de reproducción está vacía.")

    def anterior_cancion(self):
        if len(self.cola_reproduccion) >= 2:
            self.cola_reproduccion.insert(1, self.cancion_actual)
            self.cancion_actual = self.cola_reproduccion.pop(0)
            print(f"Reproduciendo anterior: {self.cancion_actual}")
        else:
            print("No hay canción anterior en la cola de reproducción.")

    def buscar_cancion(self, nombre_cancion):
        for lista in self.listas_reproduccion.values():
            for cancion in lista.canciones:
                if nombre_cancion.lower() in cancion.nombre.lower():
                    print(f"Se encontró la canción '{cancion}' en la lista '{lista.nombre}'.")
                    return
        print(f"No se encontró la canción '{nombre_cancion}' en ninguna lista de reproducción.")

    def subir_volumen(self, cantidad):
        self.volumen = min(100, self.volumen + cantidad)
        print(f"Volumen subido a {self.volumen}.")

    def bajar_volumen(self, cantidad):
        self.volumen = max(0, self.volumen - cantidad)
        print(f"Volumen bajado a {self.volumen}.")

    def reproducir_random(self):
        todas_las_canciones = [cancion for lista in self.listas_reproduccion.values() for cancion in lista.canciones]
        random.shuffle(todas_las_canciones)
        self.cola_reproduccion = todas_las_canciones
        print("Reproduciendo en orden aleatorio:")
        for cancion in self.cola_reproduccion:
            print(cancion)

