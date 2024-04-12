class Personaje:
    # Definimos el método constructor
    def __init__(self, nombre):
        # Inicializa los atributos del personaje
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
    
   #metodo getter
    @property
    def get_nombre(self):
        return self.get_nombre
    @property
    def get_nivel(self):
        return self.get_nivel
    @property
    def get_experiencia(self):
        return self.get_experiencia
    
    #metodo setter
    @nombre.setter
    def nombre(self,nombre:str):
        self.nombre = nombre 
    @nivel.setter
    def nivel(self,nivel:int):
        self.nivel = nivel
    @experiencia.setter
    def experiencia(self,experiencia:int):
        self.experiencia = experiencia
    

    """@property
    def estado(self):
        return f"nombre:{self.nombre} nivel:{self.nivel} experiencia:{self.experiencia}""""
    
    def __str__ (self):
        return f"nombre:{self.nombre} nivel:{self.nivel} experiencia:{self.experiencia}"






   
    
    