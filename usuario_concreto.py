from usuario import UsuarioBase
import customtkinter as ctk

class UsuarioConcreto(UsuarioBase):
    
    def __init__(self, root):
        super().__init__(root)

    def crear_bienvenida_frame(self, nombre_usuario, callback):
        frame = ctk.CTkFrame(self.root, bg_color=self.root.cget('bg'))
        frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure([0, 1], weight=1)

        welcome_message = f"Bienvenido, {nombre_usuario}!"
        subtitle_message = "Iniciaremos en unos instantes..."

        ctk.CTkLabel(frame, text=welcome_message, font=('Arial', 16), fg_color=self.root.cget('bg'), bg_color=self.root.cget('bg')).grid(column=0, row=0, padx=20, pady=(20, 10))
        ctk.CTkLabel(frame, text=subtitle_message, font=('Arial', 12), fg_color=self.root.cget('bg'), bg_color=self.root.cget('bg')).grid(column=0, row=1, padx=20, pady=(10, 20))

        self.root.after(5000, lambda: callback())  

        return frame
