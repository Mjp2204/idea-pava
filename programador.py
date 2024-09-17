import sys
import datetime
class Programador:
    def __init__(self):
        self.menu_principal()

    def menu_principal(self):
        while True:
            print("\nBienvenido al menú principal de tu gestor de tareas")
            print("\n--- Gestor de Tareas ---")
            print("1. Agregar Tarea")
            print("2. Tachar Tarea como Hecha")
            print("3. Mostrar Tareas")
            print("4. Recordar Tarea Importante")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.agregar_tarea()
            elif opcion == '2':
                self.tachar_tarea()
            elif opcion == '3':
                self.mostrar_tareas()
            elif opcion == '4':
                self.recordar_tarea()
            elif opcion == '5':
                self.salir()
            else:
                print("Opción no válida, por favor intente de nuevo.")

    def agregar_tarea(self):
        tarea = input("Ingrese el nombre de la tarea: ")
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")

        try:
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
        except ValueError:
            print("Error: La fecha debe estar en formato YYYY-MM-DD.")
            return

        self.guardar_tarea(tarea, fecha)
        print("Tarea guardada exitosamente.")

    def guardar_tarea(self, tarea, fecha):
        with open('tareas.txt', 'a') as file:
            file.write(f'{tarea} - {fecha}\n')

    def tachar_tarea(self):
        tareas = self.cargar_tareas()

        if not tareas:
            print("No hay tareas para mostrar.")
            return

        print("\n--- Tareas ---")
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea.strip()}")

        indices = input("Ingrese el número de las tareas a tachar (separadas por comas): ").split(',')

        try:
            indices = [int(i) - 1 for i in indices]
        except ValueError:
            print("Error: Ingrese números válidos.")
            return

        tareas_actualizadas = [tarea for i, tarea in enumerate(tareas) if i not in indices]

        with open('tareas.txt', 'w') as file:
            file.writelines(tareas_actualizadas)

        print("Tareas seleccionadas tachadas exitosamente.")

    def cargar_tareas(self):
        try:
            with open('tareas.txt', 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def mostrar_tareas(self):
        tareas = self.cargar_tareas()

        if not tareas:
            print("No hay tareas para mostrar.")
            return

        tareas_ordenadas = sorted(tareas, key=lambda x: datetime.datetime.strptime(x.split(' - ')[1].strip(), '%Y-%m-%d'))

        print("\n--- Tareas Ordenadas por Fecha ---")
        for tarea in tareas_ordenadas:
            print(tarea.strip())

    def recordar_tarea(self):
        tareas = self.cargar_tareas()

        if not tareas:
            print("No hay tareas para mostrar.")
            return

        print("\n--- Tareas ---")
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea.strip()}")

        try:
            indice = int(input("Seleccione el número de la tarea que desea recordar: ")) - 1
            tarea_recordar = tareas[indice]
            self.guardar_tarea_recordar(tarea_recordar)
            print("Tarea a recordar guardada exitosamente.")
        except (ValueError, IndexError):
            print("Error: Selección no válida.")

    def guardar_tarea_recordar(self, tarea):
        with open('tarea_recordar.txt', 'w') as file:
            file.write(tarea)

    def salir(self):
        print("Gracias por usar el programa.")

        sys.exit()

if __name__ == "__main__":
    Programador()
