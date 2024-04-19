"""
Lolett Llanquinao 
Leonardo Llaupe
Juan Torres
Claudio Mendez
"""


from error import DimensionErrorException
class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        try:
            if ancho >= 1 and ancho <= Foto.MAX:
                self.__ancho = ancho
        except Exception as error:
            raise DimensionErrorException(f'error: El ancho no puede ser mayor a {Foto.MAX}')  

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        try:
            self.__alto = alto
        except:
            pass
foto_1 = Foto(2000,2000, "https://...") 
print(foto_1.ancho)
foto_1.ancho = 2600 #setter del ancho    