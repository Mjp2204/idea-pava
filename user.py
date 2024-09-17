from usuario import ConcretoUsuario
import os

class IniciarSesion(ConcretoUsuario):
    def __init__(self, nombre, contraseña, recordarme):
        super().__init__(nombre, contraseña, recordarme)

    def solicitar_datos(self):
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contraseña_usuario = input("Ingrese su contraseña: ")
        return nombre_usuario, contraseña_usuario

    def verificar_credenciales(self, nombre_usuario, contraseña_usuario, filename):
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write("")  

        with open(filename, "r") as f:
            users = [line.strip().split(":") for line in f]
            for user, pwd in users:
                if user == nombre_usuario and pwd == contraseña_usuario:
                    return True
        return False

    def iniciar_sesion(self, filename):
        nombre_usuario, contraseña_usuario = self.solicitar_datos()
        if self.verificar_credenciales(nombre_usuario, contraseña_usuario, filename):
            print("Inicio de sesión exitoso")
            self.check_and_add_user(nombre_usuario, contraseña_usuario, filename)
        else:
            print("Error: nombre de usuario o contraseña inválidos")

    def check_and_add_user(self, username, password, filename):
        with open(filename, "r") as f:
            users = [line.strip().split(":") for line in f]
            if [user for user, pwd in users if user == username]:
                print("El usuario ya existe.")
                return
        with open(filename, "a") as f:
            f.write(f"{username}:{password}\n")
        print("Usuario agregado exitosamente.")

iniciar_sesion = IniciarSesion("admin", "password", True)
iniciar_sesion.iniciar_sesion("users.txt")