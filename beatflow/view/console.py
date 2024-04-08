from beatflow.model.beatflow import BeatFlow, Cancion, ListaReproduccion
import sys

class App:
    def __init__(self):
        self.beatflow = BeatFlow()
        #self.cancion = Cancion()
        #self.lista_reproduccion = ListaReproduccion()

    @staticmethod
    def mostrar_menu():
        print("\n** Menú de BeatFlow **")
        print("1. Crear nueva lista de reproducción")
        print("2. Ver listas de reproducción")
        print("3. Ver canciones de una lista de reproducción")
        print("4. Agregar canción a lista de reproducción")
        print("5. Eliminar canción de lista de reproducción")
        print("6. Salir")

    def ejecutar(self):
        while True:
            App.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre_lista = input("Ingrese el nombre de la nueva lista de reproducción: ")
                self.beatflow.crear_lista_reproduccion(nombre_lista)
            elif opcion == "2":
                self.beatflow.ver_listas_reproduccion()
            elif opcion == "3":
                nombre_lista = input("Ingrese el nombre de la lista de reproducción: ")
                self.beatflow.ver_canciones_lista(nombre_lista)
            elif opcion == "4":
                nombre_lista = input("Ingrese el nombre de la lista de reproducción: ")
                nombre_cancion = input("Ingrese el nombre de la canción: ")
                artista_cancion = input("Ingrese el nombre del artista: ")
                cancion = Cancion(nombre_cancion, artista_cancion)
                
                # Llamada corregida
                self.beatflow.agregar_cancion(nombre_lista, cancion)
                
            elif opcion == "5":
                nombre_lista = input("Ingrese el nombre de la lista de reproducción: ")
                indice_cancion = int(input("Ingrese el índice de la canción que desea eliminar: "))
                self.beatflow.eliminar_cancion(nombre_lista, indice_cancion)
                
            elif opcion == "6":
                print("\n¡Gracias por utilizar BeatFlow!")
                sys.exit()
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")