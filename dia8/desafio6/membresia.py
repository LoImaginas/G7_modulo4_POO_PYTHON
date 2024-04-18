"""
Nombres: 
-Lolett Llanquinao 
-Jocelyn Cantero
-Juan Torres
-Leonardo Llaupe
-Claudio Mendez
Fecha:17-04-2024

implementación de clases para un sistema de membresía. 
Incluye una clase abstracta Membresia y sus clases derivadas Gratis, Basica, 
Familiar, SinConexion y Pro. 
Clases:
    - Membresia: Clase abstracta que define la estructura básica de una membresía.
    - Gratis: Clase que representa una membresía gratuita con opciones limitadas.
    - Basica: Clase que representa una membresía básica con más funciones que Gratis.
    - Familiar: Clase que representa una membresía para múltiples usuarios.
    - SinConexion: Clase que representa una membresía con acceso sin conexión.
    - Pro: Clase que representa una membresía premium con todas las funciones.

Cada clase implementa métodos para cambiar la membresía actual a una diferente.

"""


from abc import ABC, abstractmethod
#constructor
class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
       # Constructor de la clase Membresia
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta
    #Getter para el atributo correo_suscriptor
    @property 
    def correo_suscriptor(self):   
        return self.__correo_suscriptor
    # Getter para el atributo numero_tarjeta
    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta
    
    #metodo abstracto para cambiar la membresia
    @abstractmethod
    def cambiar_membresia(self, tipo: int):
        pass
    #metodo abstracto para crear nueva membresia
    @abstractmethod   
    def crear_nueva_membresia(self, tipo: int):
        pass  
   
  #metodo para cancelar membresia
    def cancelar_membresia(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)
#clase gratis        
class Gratis(Membresia):
    def __init__(self, correo_suscriptor:str, numero_tarjeta:str):
        # Constructor de la clase Gratis
            super().__init__(correo_suscriptor, numero_tarjeta)
            self._costo = 0
            self._max_dispositivos = 1
            
            # Lógica para cambiar la membresía de la clase gratis
    def cambiar_membresia(self, tipo: int):       
        if tipo in range(1, 5):
            return self._crear_nueva_membresia(tipo)
        else:
            return self   
        # Método para crear una nueva membresía
    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
      # Método necesario para implementar en la clase abstracta Membresia
    def crear_nueva_membresia(self, tipo: int):
        return self._crear_nueva_membresia(tipo)   
        
#1 Clase Basica
class Basica(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        #Constructor de la clase Basica
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._costo = 3000
        self._max_dispositivos = 2
        
    # Lógica para cambiar la membresía de la clase basica
    def cambiar_membresia(self, tipo: int):
        if tipo in range(2, 4):
            return self._crear_nueva_membresia(tipo)
        else:
            return self
    # Método para crear una nueva membresía  
    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)        

    # Implementación del método abstracto
    def crear_nueva_membresia(self, tipo: int):
        return self._crear_nueva_membresia(tipo)  
        
#2 Clase Familiar
class Familiar(Basica):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
         #Constructor de la clase Familiar
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._costo = 5000
        self._max_dispositivos = 5
        self._dias_regalo = 7
        
        # Lógica para cambiar la membresía de la clase familiar
    def cambiar_membresia(self, tipo: int):
        if tipo in [1, 3, 4]:   
            return self._crear_nueva_membresia(tipo) 
        else:
            return self
    # Método para crear una nueva membresía
    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

        # Lógica para modificar el control parental
    def modificar_control_parental(self):
        pass
    
#3 Clase SinConexion
class SinConexion(Basica):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
         #Constructor de la clase SinConexion
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._costo = 3500
        self._max_dispositivos = 2
        self._dias_regalo = 7
    
     # Lógica para cambiar la membresía
    def cambiar_membresia(self, tipo: int):
        if tipo in [1, 2, 4]:
            return self._crear_nueva_membresia(tipo)
        else:
            return self    
        # Método para crear una nueva membresía
    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

       # Lógica para aumentar el contenido sin conexión
    def aumentar_contenido_sin_conexion(self):
        pass
#4 Clase Pro
class Pro(Familiar, SinConexion):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
         #Constructor de la clase Pro
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._costo = 7000
        self._max_dispositivos = 6
        self._dias_regalo = 15
    
    # Lógica para cambiar la membresía
    def cambiar_membresia(self, tipo: int):
        if tipo in range(1, 3):
            return self._crear_nueva_membresia(tipo)   
        else:
            return self
    # Método para crear una nueva membresía 
    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)    

    # Lógica para modificar el control parental
    def modificar_control_parental(self):
        pass
    # Lógica para aumentar el contenido sin conexión
    def aumentar_contenido_sin_conexion(self):
        pass

# Ejemplo de uso
g = Gratis("correo@prueba.cl", "123456789")
print(type(g))
b = g.cambiar_membresia(1)
print(type(b))
f = b.cambiar_membresia(2)
print(type(f))
sc = f.cambiar_membresia(3)
print(type(sc))
pro = sc.cambiar_membresia(4)
print(type(pro))
