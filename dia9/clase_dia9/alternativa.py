class Alternativa():
    def __init__(self,contenido="",ayuda= ""):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self):
        print(f"contenido {self.contenido}")
        
        if self.ayuda != "":
            print(f"ayuda: {self.ayuda}")

#prueba
if __name__ == "__main__":
    alternativa= Alternativa()
    alternativa.contenido = "Esto es un contenido"

    alternativa.mostrar_alternativa()