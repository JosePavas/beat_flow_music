import beatflow

class UIConsola:

    def __init__(self):
        self.beatflow: beatflow = beatflow()
        self.opciones = {
            "1": self.abrir_beatflow,
            "2": self.salir
        }
def mostrar_menu(listas_reproduccion):
    print("\n*** Menú de BeatFlow ***")
    print("1. Crear lista de reproducción")
    print("2. Ver listas de reproducción")
    print("3. Seleccionar lista de reproducción")
    print("4. Agregar canción a la lista de reproducción seleccionada")
    print("5. Eliminar canción de la lista de reproducción seleccionada")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")
    return opcion

def funcionalidad_menu():
    listas_reproduccion = []

    while True:
        opcion = mostrar_menu(listas_reproduccion)

        if opcion == "1":
            beatflow.crear_lista_reproduccion(listas_reproduccion)
        elif opcion == "2":
            beatflow.ver_listas_reproduccion(listas_reproduccion)
        elif opcion == "3":
            lista_seleccionada = beatflow.seleccionar_lista(listas_reproduccion)
            if lista_seleccionada:
                lista_seleccionada.ver_lista()
        elif opcion == "4":
            lista_seleccionada = beatflow.seleccionar_lista(listas_reproduccion)
            if lista_seleccionada:
                beatflow.agregar_cancion(lista_seleccionada)
        elif opcion == "5":
            lista_seleccionada = beatflow.seleccionar_lista(listas_reproduccion)
            if lista_seleccionada:
                beatflow.eliminar_cancion(lista_seleccionada)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
