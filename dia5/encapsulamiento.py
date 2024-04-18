#Delimita un conjunto de datos, y los métodos que afectan esos datos, dentro de una misma
#unidad, restringiendo así el acceso y uso de los datos y métodos “encapsulados”. 
#Un ejemplo clásico corresponde a una Clase, ya que dentro de su estructura encierra todos los
#métodos y atributos que permiten definir un objeto de dicha clase.
#Normalmente, en programación orientada a objetos, al encapsular el comportamiento y el
#estado de un objeto dentro de la clase que lo define, estos no son posibles de acceder ni
#modificar desde otras clases, sino que necesariamente debe hacerse por medio del objeto.

class Auto:
    __color = "Blanco"
     #METODO PUBLICO
    def __cambiar_color(self, color):
        print("Nuevo color",color)
        self.__color = color
        
    def imprimir_estado(self,nuevo_color):
        print(self.__color) #llamado al atributo
        self.__cambiar_color(nuevo_color)
        print(self.__color) #llamado al getter
        
#getter --> obtener un valor 
    @property
    def color(self):
        return self.__color        
     
nissan = Auto()     
#print(nissan.__color)# AttributeError: 'Auto' object has no attribute '__color'
#print(Auto.__color()) #AttributeError: type object 'Auto' has no attribute '__color'

#nissan.cambiar_color("negro")    
nissan.imprimir_estado("Negro")
print("")
print(nissan.color)  #llamado al metodo getter
print(nissan._Auto__color)