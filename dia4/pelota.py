class Pelota():
    #atributos de Clase
    marca = "adidas"
    
    #Metodo Constructor
    def __init__(self,color: str, tamanio = 20, material= "plástico"):

        print("Metodo constructor al crear el objeto")
        self.tamanio = tamanio
        self.material = material
        self.rebotes = 0
        self.__color = color #ocultando el atributo
        self.marca = "Adidas"
        self.__password= "qwerty"

    #metodo oculto
    def __getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color = color

    def setPassword(self,password):
        self.__password = password

    #getter
    @property
    def color(self):
        return self.__color
    #setter
    @color.setter
    def color(self,color: str):
        self.__color = color if color != "" else "Verde"

    @color.deleter
    def color(self):
        del self.__color

pelota_futbol = Pelota("Amarillo",16,"plástico")
#print(pelota_futbol.__color)
#print("getcolor()",pelota_futbol.getColor())
print("metodo getter",pelota_futbol.color)#SIN PARENTESIS

print(pelota_futbol.tamanio,pelota_futbol.material)
()
#pelota2 = Pelota() #TypeError: Pelota.__init__() missing 3 required positional arguments: 'color', 'tamanio', and 'material'

pelota3 = Pelota(0,material="plastico")
print(pelota3.tamanio,pelota3.material)
pelota3.rebotes= 10
#pelota4 = Pelota()#TypeError: Pelota.__init__() missing 1 required positional argument: 'color'

print(Pelota.marca, pelota_futbol.marca)