from abc import ABC, abstractmethod
from customtkinter import CTk, CTkLabel, CTkFrame

class UsuarioBase(ABC):
    def __init__(self, root):
        self.root = root

    @abstractmethod
    def crear_bienvenida_frame(self, nombre_usuario, callback):
        pass