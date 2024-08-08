
class Viajero:
    def __init__(self):
        self.nombre = ""
        self.destino = ""
        self.actividades = []

    def guardar_info(self):
        self.nombre = input("Ingrese nombre: ")
        self.destino = input("Ingrese destino: ")
        self.fecha_viaje = input("Ingrese la fecha de su viaje (en formato YYYY-MM-DD): ")

    def agregar_actividad(self):
        actividad = input("Ingrese sus actividades a realizar: ")
        self.actividades.append(actividad)
        print("¡Actividad agregada con éxito!")

    def recordar_actividades(self):
        if len(self.actividades) == 0:
            print("No hay actividades agregadas")
        else:
            print("Sus actividades son: ")
            for idx, actividad in enumerate (self.actividades, start=1):
                  print(f"{idx}. {actividad}")
    
    def mostrar_datos_viajero(self):
        print("\nDatos del Viajero:")
        print(f"Nombre: {self.nombre}")
        print(f"Destino: {self.destino}")
        print(f"Fecha del Viaje: {self.fecha_viaje}")


