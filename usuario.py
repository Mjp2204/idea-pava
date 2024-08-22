from interfaz_abstracta import InterfazAbstracta
import customtkinter as ctk

class UsuarioBase(InterfazAbstracta):
    
    def __init__(self, root):
        self.root = root

    def metodo_adicional(self):
        """Implementación parcial o vacía del método adicional"""
        pass
