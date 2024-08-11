from customtkinter import CTk, CTkLabel, CTkFrame

class UsuarioBase:
    def __init__(self, root):
        self.root = root

    def crear_bienvenida_frame(self, nombre_usuario, callback):
        frame = CTkFrame(self.root, bg_color=self.root.cget('bg'))
        frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure([0, 1], weight=1)

        welcome_message = f"Bienvenido, {nombre_usuario}!"
        subtitle_message = "Iniciaremos en unos instantes..."

        CTkLabel(frame, text=welcome_message, font=('Arial', 16), fg_color=self.root.cget('bg'), bg_color=self.root.cget('bg')).grid(column=0, row=0, padx=20, pady=(20, 10))
        CTkLabel(frame, text=subtitle_message, font=('Arial', 12), fg_color=self.root.cget('bg'), bg_color=self.root.cget('bg')).grid(column=0, row=1, padx=20, pady=(10, 20))

        self.root.after(5000, lambda: callback())  # Llama a la función de callback después de 5 segundos

        return frame
