import time
from documentos import *
from viajero import Viajero

class Menu:
    def __init__(self):
        self.viajero = Viajero()
        self.documento = Documentos()

    
    def mostrar_menu(self):
        print("\n--- Menú del Viajero ---")
        print("1. Establecer datos del viajero")
        print("2. Mostrar datos del viajero")
        print("3. Agregar actividades")
        print("4. Recordar actividades")
        print("5. Documentación necesaria para el viaje")
        print("6. Marcar documento como empacado")
        print("7. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion == '1':
            self.viajero.establecer_datos()
        elif opcion == '2':
            self.viajero.mostrar_datos_viajero()
        elif opcion == '3':
            self.viajero.agregar_actividad()
        elif opcion == '4':
            self.viajero.recordar_actividades()
        elif opcion == '5':
            self.viajero.mejor_hora_para_dormir()
        elif opcion == '6':
            self.documentos.mostrar_documentos()
        elif opcion == '7':
            self.documentos.mostrar_documentos()
            numero = input("Ingrese el número del documento que ha empacado: ")
            self.documentos.tachar_documento(numero)
        elif opcion == '8':
            print("Gracias por usar el programa. ¡Buen viaje!")
            return False
        else:
            print("Opción no válida, por favor intente de nuevo.")
        return True

def main():
    menu = Menu()
    while True:
        menu.mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if not menu.ejecutar_opcion(opcion):
            break
        time.sleep(2)

if __name__ == "__main__":
    main()