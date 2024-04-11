class Auto():
    def __init__(self,color: str = "blanco"):
        self.__color=color
    
    def __str__(self):
        return f"Metodo sobre cargado, color: {self.__color}"

nissan = Auto()
print(nissan)#<__main__.Auto object at 0x10ccf9dc0>

toyota = Auto("Negro")
print(toyota)