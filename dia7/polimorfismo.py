class Padre():
    #atributo de clase
    color = "verde"
    #constructor
    def __init__(self, tamanio: int):
        #atributos de instancia
        self.__tamanio = tamanio #atributo oculto/privado

    #metodos estaticos

    #metodos de instancia
    def cambia_color(self, color: str):
        if color != "":
            self.color = color    
    
    #sobrecarga
    def __str__(self):
        return f"El color es {self.color}, y de tamanio {self.__tamanio}"

    #getter - setters
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio: int):
        if tamanio > 0:
            self.__tamanio = tamanio
        else:
            self.__tamanio = 0

#HERENCIA -> hereda TODO, y cada uno de los hijos puede tener sus propios metodos y atributos
class Hija(Padre):
    peso = 100
    #polimorfismo: cambio en el comportamiento del metodo
    def cambia_color(self, color: str):
        #if color != "":
        self.color = color

class Hijo(Padre):
    deuda = 120
    #sobreescrir el constructor
    def __init__(self, tamanio: int, saldo = 0):
        super().__init__(tamanio)#llamado al constructor del Padre
        self.__saldo =  saldo

    @property
    def saldo(self):
        return self.__saldo

class Nieto(Hija):
    pañal = "XL"

#instancia de la clase hija (creando un objeto)
hijita = Hija(100)
hijita.cambia_color("")

print(f"el color de la clase hija es {hijita.color}")

regalon = Nieto(50)
#Llamado al metodo del padre a traves de la hija
super(type(hijita),hijita).cambia_color("gris")
print(f"el color de la clase hija es {hijita.color}")

#instancia de la clase HIJO
hijito = Hijo(10,1200)
print(hijito.tamanio,hijito.saldo,hijito.deuda)

#ISINSTANCE isinstance(objeto, clase_a_comparar)
print(f"hijita es intancia de Hija: {isinstance(hijita,Hija)}") #true
print(f"hijita es intancia de Hioj: {isinstance(hijita,Hijo)}") # false
print(f"hijita es intancia de Padre: {isinstance(hijita,Padre)}") #true
print(f"hijita es intancia de Nieto: {isinstance(hijita,Nieto)}") #false

#objeto regalon
print(f"regalon es intancia de Nieto: {isinstance(hijita,Nieto)}") #false
print(f"regalon es intancia de Hija: {isinstance(hijita,Hija)}") # true
print(f"regalon es intancia de Hijo: {isinstance(hijita,Hijo)}") #false
print(f"regalon es intancia de Padre: {isinstance(hijita,Padre)}") #true



