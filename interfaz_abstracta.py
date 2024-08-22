from abc import ABC, abstractmethod

class InterfazAbstracta(ABC):
    
    @abstractmethod
    def crear_bienvenida_frame(self, nombre_usuario, callback):
        """Método abstracto para crear un frame de bienvenida"""
        pass

    @abstractmethod
    def metodo_adicional(self):
        """Otro método abstracto que se requiere"""
        pass
