from abc import ABC, abstractmethod
#constructor
class Membresia(ABC):
    def _init_(self, correo_suscriptor: str, numero_tarjeta: str):
        #atributos de instancia
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta
    #getter 
    @property 
    def correo_suscriptor(self):   
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta
    
    #metodo abstracto
    @abstractmethod
    def cambiar_membresia(self, tipo: int):
        pass

    @abstractmethod
    def cancelar_membresia(self, tipo: int):
        pass 

    @abstractmethod   
    def crear_nueva_membresia(self, tipo: int):
        pass  
   
  
        
class Gratis(Membresia):
    def _init_(self, correo_suscriptor:str, numero_tarjeta:str):
            super().__init__(correo_suscriptor, numero_tarjeta)
            self._costo = 0
            self._max_dispositivos = 1
            
            # Lógica para cambiar la membresía
    def cambiar_membresia(self, tipo: int):       
        if tipo in range(1, 5):
            return self._crear_nueva_membresia(tipo)
        else:
            return self   
    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
#1
class Basica(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._costo = 3000
        self._max_dispositivos = 2
        
    # Lógica para cambiar la membresía
    def cambiar_membresia(self, tipo: int):
        if tipo in range(2, 4):
            return self._crear_nueva_membresia(tipo)
        else:
            return self
        
    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)        
        
#2
class Familiar(Basica):
    
    
    
    
    
    def cambiar_membresia(self, tipo: int):
        if tipo in [1, 3, 4]:
            # Lógica para cambiar la membresía
            pass
        else:
            return self

    def modificar_control_parental(self):
        # Lógica para modificar el control parental
        pass
#3
class SinConexion(Basica):
    
    
    
    
    
    def cambiar_membresia(self, tipo: int):
        if tipo in [1, 2, 4]:
            # Lógica para cambiar la membresía
            pass
        else:
            return self

    def aumentar_contenido_sin_conexion(self):
        # Lógica para aumentar el contenido sin conexión
        pass
#4
class Pro(Familiar, SinConexion):
    
    
    
    
    
    def cambiar_membresia(self, tipo: int):
        if 1 <= tipo <= 3:
            # Lógica para cambiar la membresía
            pass
        else:
            return self

    def modificar_control_parental(self):
        # Lógica para modificar el control parental
        pass

    def aumentar_contenido_sin_conexion(self):
        # Lógica para aumentar el contenido sin conexión
        pass

# Ejemplo de uso
g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_membresia(1)
print(type(b))
f = b.cambiar_membresia(2)
print(type(f))
sc = f.cambiar_membresia(3)
print(type(sc))
pro = sc.cambiar_membresia(4)
print(type(pro))
