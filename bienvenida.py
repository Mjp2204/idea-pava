from usuario import ConcretoUsuario

class BienvenidaUsuario(ConcretoUsuario):
    def __init__(self, nombre, contraseña, recordarme):
        super().__init__(nombre, contraseña, recordarme)
    
    def bienvenida_usuario(self):
        return f"Bienvenido al programa, {self.nombre}!"

    def mostrar_bienvenida(self):
        return f"Bienvenido al programa, {self.nombre}!\nEste programa te permite iniciar sesión y guardar tus credenciales.\nPara empezar, ingresa tus credenciales."
    
    def solicitar_credenciales(self):
        nombre = input("Ingrese su nombre de usuario: ").strip()
        contraseña = input("Ingrese su contraseña: ").strip()
        self.nombre = nombre
        self.contraseña = contraseña
        return nombre, contraseña