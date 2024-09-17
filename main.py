from user_concre import ConcretoUsuario
from programador import Programador
import os

# Ruta del archivo de datos de usuario
USER_DATA_FILE = 'users.txt'

class Main:
    def __init__(self):
        self.usuario = None
        self.programador = None

    def run(self):
        # Solicitar y verificar credenciales del usuario
        nombre, contraseña = self.solicitar_datos_registro()
        
        if self.verificar_credenciales(nombre, contraseña):
            print("Inicio de sesión exitoso")
            self.iniciar_sesion_usuario(nombre, contraseña)
        else:
            print("Credenciales incorrectas o usuario no encontrado.")
            self.registrar_usuario(nombre, contraseña)
            if self.verificar_credenciales(nombre, contraseña):
                print("Registro exitoso y sesión iniciada.")
                self.iniciar_sesion_usuario(nombre, contraseña)
            else:
                print("Error: No se pudo registrar el usuario")

    def solicitar_datos_registro(self):
        # Validar que el usuario y contraseña no sean vacíos
        while True:
            nombre = input("Ingrese su nombre de usuario: ").strip()
            contraseña = input("Ingrese su contraseña: ").strip()
            if nombre and contraseña:
                return nombre, contraseña
            else:
                print("Error: El nombre de usuario y la contraseña no pueden estar vacíos.")

    def verificar_credenciales(self, nombre_usuario, contraseña_usuario):
        try:
            if not os.path.exists(USER_DATA_FILE):
                return False
            
            with open(USER_DATA_FILE, 'r') as file:
                for line in file:
                    # Saltar líneas vacías o incorrectamente formateadas
                    if ',' not in line or line.strip() == '':
                        continue
                    
                    usuario, contraseña = line.strip().split(',', 1)  # Limitar el split a 2 partes
                    if usuario == nombre_usuario and contraseña == contraseña_usuario:
                        return True
            return False
        except FileNotFoundError:
            print(f"Error: El archivo {USER_DATA_FILE} no existe.")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    def registrar_usuario(self, nombre_usuario, contraseña_usuario):
        try:
            with open(USER_DATA_FILE, 'a') as file:
                file.write(f'{nombre_usuario},{contraseña_usuario}\n')
        except Exception as e:
            print(f"Error al registrar usuario: {e}")

    def iniciar_sesion_usuario(self, nombre, contraseña):
        self.usuario = ConcretoUsuario(nombre, contraseña, False)
        self.programador = Programador()
        self.usuario.iniciar_sesion()

if __name__ == "__main__":
    main = Main()
    main.run()
