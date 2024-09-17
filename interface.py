from abc import ABC, abstractmethod  
class Interface(ABC):     
    @abstractmethod     
    def iniciar_sesion(self):         
        pass        

    @abstractmethod
    def mostrar_bienvenida(self, nombre_usuario):         
        pass          
    
    @abstractmethod     
    def mostrar_botones(self, frame, root):         
        pass