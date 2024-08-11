from customtkinter import CTk, CTkLabel, CTkButton, CTkFrame, CTkEntry, CTkCheckBox
import os
import sys
from PIL import Image, ImageTk
from usuario_concreto import UsuarioBase  # Importa la clase UsuarioBase
from botones_base import BotonesBase  # Importa la clase BotonesBase

# Rutas y colores
ruta_logo = 'imagenes/logo.png'
c_negro = '#010101'
c_blanco = '#FFFFFF'
user_data_file = 'info.txt'

# Clase concreta Interfaz que hereda de UsuarioBase
class Interfaz(UsuarioBase):
    def __init__(self, root):
        super().__init__(root)
        self.logo_image = None
        self.nombre = None
        self.contraseña = None
        self.recordarme = None
        self.frame_inicio = None
        self.crear_interfaz()

    def crear_interfaz(self):
        try:
            image = Image.open(ruta_logo)
            self.logo_image = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            sys.exit(1)

        self.root.iconphoto(False, self.logo_image)

        self.frame_inicio = CTkFrame(self.root, width=480, height=500, bg_color=c_negro)
        self.frame_inicio.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)
        self.frame_inicio.columnconfigure(0, weight=1)
        self.frame_inicio.rowconfigure([0, 1, 2, 3, 4], weight=1)

        CTkLabel(self.frame_inicio, image=self.logo_image, text='').grid(column=0, row=0, padx=20, pady=20, sticky='n')

        self.nombre = CTkEntry(self.frame_inicio, font=('Arial', 12), placeholder_text='Nombre', border_color=c_blanco, fg_color=c_negro, width=220, height=40)
        self.nombre.grid(column=0, row=1, padx=10, pady=5, sticky='nsew')

        self.contraseña = CTkEntry(self.frame_inicio, font=('Arial', 12), placeholder_text='Contraseña', border_color=c_blanco, fg_color=c_negro, width=220, height=40, show='*')
        self.contraseña.grid(column=0, row=2, padx=10, pady=5, sticky='nsew')

        self.recordarme = CTkCheckBox(self.frame_inicio, text='Recordarme', hover_color=c_blanco, border_color=c_blanco, fg_color=c_blanco)
        self.recordarme.grid(column=0, row=3, padx=10, pady=5, sticky='nsew')

        bt_iniciar = CTkButton(self.frame_inicio, font=('Arial', 12), border_color=c_blanco, fg_color=c_negro, hover_color=c_blanco, corner_radius=12, border_width=2, text='INICIAR SESION', height=40, command=self.iniciar_sesion)
        bt_iniciar.grid(column=0, row=4, padx=10, pady=10, sticky='nsew')

    def iniciar_sesion(self):
        nombre_usuario = self.nombre.get()
        contraseña_usuario = self.contraseña.get()
        recordar = 1 if self.recordarme.get() else 0

        if recordar == 1:
            self.guardar_info(nombre_usuario, contraseña_usuario, recordar)
            print(f"Datos guardados: {nombre_usuario}, {contraseña_usuario}")
        else:
            if os.path.exists(user_data_file):
                os.remove(user_data_file)
                print("Datos de inicio de sesión eliminados.")

        print("Inicio de sesión exitoso")
        self.mostrar_bienvenida(nombre_usuario)

    def mostrar_bienvenida(self, nombre_usuario):
        if self.frame_inicio:
            self.frame_inicio.destroy()
            self.frame_inicio = None

        self.frame_bienvenida = self.crear_bienvenida_frame(nombre_usuario, self.abrir_botonera)

    def abrir_botonera(self):
        if hasattr(self, 'frame_bienvenida') and self.frame_bienvenida:
            self.frame_bienvenida.destroy()
            self.frame_bienvenida = None

        # Cierra la ventana actual y abre una nueva ventana para los botones
        self.root.destroy()

        nueva_ventana = CTk()
        nueva_ventana.title("Gestor de Tareas")
        nueva_ventana.geometry('480x500')
        nueva_ventana.config(bg=c_negro)

        app_botonera = BotonesBase(nueva_ventana)
        nueva_ventana.mainloop()

    def guardar_info(self, nombre, contraseña, recordar):
        with open(user_data_file, 'w') as file:
            file.write(f'{nombre}\n{contraseña}\n{recordar}')

    def cargar_datos(self):
        if os.path.exists(user_data_file):
            with open(user_data_file, 'r') as file:
                datos_guardados = file.readlines()
                if len(datos_guardados) >= 3:
                    nombre_guardado = datos_guardados[0].strip()
                    contraseña_guardada = datos_guardados[1].strip()
                    recordarme_guardado = int(datos_guardados[2].strip())

                    self.nombre.insert(0, nombre_guardado)
                    self.contraseña.insert(0, contraseña_guardada)

                    if recordarme_guardado == 1:
                        self.recordarme.select()
                    else:
                        self.recordarme.deselect()

    def crear_bienvenida_frame(self, nombre_usuario, callback):
        frame = CTkFrame(self.root, bg_color=self.root.cget('bg'))
        frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure([0, 1], weight=1)

        welcome_message = f"Bienvenido, {nombre_usuario}!"
        subtitle_message = "Iniciaremos en unos instantes..."

        CTkLabel(frame, text=welcome_message, font=('Arial', 16), fg_color=self.root.cget('bg'), bg_color=self.root.cget('bg')).grid(column=0, row=0, padx=20, pady=(20, 10))
        CTkLabel(frame, text=subtitle_message, font=('Arial', 12), fg_color=self.root.cget('bg'), bg_color=self.root.cget('bg')).grid(column=0, row=1, padx=20, pady=(10, 20))

        self.root.after(5000, lambda: callback())  

        return frame

if __name__ == "__main__":
    root = CTk()
    root.title("Programador de Tareas")
    root.geometry('480x500')
    root.config(bg=c_negro)

    app = Interfaz(root)
    app.cargar_datos()

    root.mainloop()
