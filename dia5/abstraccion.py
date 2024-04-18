#En programación orientada a objetos, el objetivo de la abstracción es disponibilizar solamente 
# la información esencial que permite definir un objeto.
#En Python, pueden existir tanto clases abstractas como métodos abstractos, la cual posee 
# al menos 1 método abstracto, y este es aquel que solo posee firma (sin implementación).

"""
ABSTRACCION:
una clase en abstracta, si tiene a lo menos un metodo abstracto
Metodo Abstracto: son aquellos que solamente tienen la defincion del metodo

Para poder crer una clase abstracta y un metodo abstracto importamos:
form abc import ABC, abstractmethod
    
"""

from abc import ABC, abstractmethod
class Pelota(ABC):  #CLASE ABSTRACTA
    
#DEFINICION del metodo abstracto
    @abstractmethod 
    def rebotar(self,altur:int):
        pass
    
# Creando una subclase: una clase que nace a partir de otra clase   
class PelotaDeJuguete(Pelota):
    def __init__(self):
        self.color="Blanco"
        
        #Obligacion de implementar el metodo abstracto
    def rebotar(self,altura:int):
        pass
    
    def imprimir(self):
        print("metodo de la subclase")
         
#Creacion de objeto
pelotita=PelotaDeJuguete()
#TypeError: Can't instantiate abstract class PelotaDeJuguete without an implementation for abstract method 'rebotar' 
print(pelotita.rebotar(20))          