import random


class Beatflow:
    def __init__(self):
        self.lista_reproduccion = []

    def reproducir_cancion(self, cancion):
        print("Reproduciendo:", cancion)

    def agregar_cancion_cola(self, cancion):
        self.cola_canciones.append(cancion)
        print("Agregando", cancion, "a la cola de reproducción")
    
class Cancion:
    def __init__(self, nombre, artista,):
        self.nombre = nombre
        self.artista = artista

    def __str__(self):
        return f"{self.nombre} - {self.artista}"    

class Buscador:
    def __init__(self, catalogo_canciones):
        self.catalogo_canciones = catalogo_canciones

    def buscar_por_nombre(self, nombre_cancion):
        resultados = [cancion for cancion in self.catalogo_canciones if nombre_cancion.lower() in cancion.lower()]
        return resultados

    def buscar_por_artista(self, nombre_artista):
        resultados = [cancion for cancion in self.catalogo_canciones if nombre_artista.lower() in cancion['artista'].lower()]
        return resultados
    
class Biblioteca:
    def __init__(self):
        self.listas_reproduccion = {}

    def ver_lista_reproduccion(self, nombre_lista):
        if nombre_lista in self.listas_reproduccion:
            lista = self.listas_reproduccion[nombre_lista]
            print(f"\nLista de reproducción '{nombre_lista}':")
            lista.mostrar_lista()
        else:
            print(f"No se encontró la lista de reproducción '{nombre_lista}'.")

    def visualizar_cancion_lista(self, nombre_lista, indice_cancion):
        if nombre_lista in self.listas_reproduccion:
            lista = self.listas_reproduccion[nombre_lista]
            lista.visualizar_cancion(indice_cancion)
        else:
            print(f"No se encontró la lista de reproducción '{nombre_lista}'.")

class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
