class Madre():
    def __init__(self, color: str,**parametros):
        super().__init__(**parametros)
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

class Padre():
    def __init__(self, tamanio: int, **parametros):
        super().__init__(**parametros)
        self.__tamanio = tamanio

    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio: int):
        self.__tamanio = tamanio

class Hija(Madre,Padre):
    """ sobreescritura de los constructores"""
    #def __init__(self, color: str, tamanio: int ):
    #    Madre.__init__(self,color)
    #    Padre.__init__(self,tamanio)
    def __init__(self,deuda=0,**parametros):
        super().__init__(**parametros) #agregamos esto al constructor de madre y padre

#atributo de instancia propio de hija 
        self.deuda = deuda

#objeto
#princesa = Hija("Azul",80)
princesa = Hija(color ="azul",tamanio = 80, deuda= 350)

print(princesa.tamanio, princesa.color)