from abc import ABC, abstractmethod # Importa la clase ABC y el decorador abstractmethod desde el módulo abc
from error import SubTipoInvalidoError  # Importa la clase de excepción SubTipoInvalidoError desde el archivo error.py

# Define la clase base Anuncio que hereda de ABC (clase abstracta)
class Anuncio(ABC):  
    # Constructor de la clase Anuncio
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
          # Inicializa los atributos privados de la clase
        self.__ancho = ancho if ancho > 0 else 1  # Si el ancho es mayor a cero, se asigna; de lo contrario, se asigna 1
        self.__alto = alto if alto > 0 else 1  # Si el alto es mayor a cero, se asigna; de lo contrario, se asigna 1
        self.__url_archivo = url_archivo # URL del archivo del anuncio
        self.__url_clic = url_clic  # URL de clic del anuncio
        self.__sub_tipo = sub_tipo # Subtipo del anuncio

      #getter y setter
    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, value):
        # Verifica que el valor sea mayor a cero, si no, asigna 1
        pass

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        # Valida que el subtipo esté dentro de los permitidos
        pass
        
    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, value):
        # Verifica que el valor sea mayor a cero, si no, asigna 5
        pass
    
    #Método abstracto para comprimir el anuncio (debe ser implementado en las subclases)   
    @abstractmethod
    def comprimir_anuncio(self):
        pass
    # Método abstracto para redimensionar el anuncio (debe ser implementado en las subclases)
    @abstractmethod
    def redimensionar_anuncio(self):
        pass
    # Método estático para mostrar los formatos disponibles (no utiliza atributos de instancia)
    @staticmethod
    def mostrar_formatos():
        print("FORMATO:")
        print("==========")
        
# Define la subclase Video que hereda de Anuncio
class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    # Constructor de la clase Video
    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo) # Llama al constructor de la clase Anuncio con valores predeterminados para ancho y alto
        self.duracion = duracion if duracion > 0 else 5 # Asigna la duración del video (si es mayor a cero); de lo contrario, asigna 5

    def comprimir_anuncio(self):
        print("COMPRESION DE VIDEO NO IMPLEMENTADA AUN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AUN")
# Define la subclase Display que hereda de Anuncio
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESION DE ANUNCIOS DISPLAY NO IMPLEMENTADA AUN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AUN")
# Define la subclase Social que hereda de Anuncio
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESION DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AUN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AUN")


    


class Video(Anuncio):
    def __init__(self, duracion: int):
        super().__init__(1, 1, 'video')
        self.duracion = duracion

class Display(Anuncio):
    pass  # Implementa métodos específicos según lo solicitado
