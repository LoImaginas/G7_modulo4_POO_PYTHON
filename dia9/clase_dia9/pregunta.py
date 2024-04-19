from alternativa import Alternativa

class Pregunta():
    def __init__(self,enunciado = "",ayuda = "",requerida = False,alternativas = []):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        #lista de alternativas
        self.__lista_alternativas = [
                                        Alternativa(dicc["contenido"],dicc["ayuda"]) for dicc in alternativas
                                    ]

    def mostrar_pregunta(self):
        print(self.enunciado)

        if self.ayuda != "":
            print(f"ayuda: {self.ayuda}")

        for obj_alt in self.__lista_alternativas:
            obj_alt.mostrar_alternativa()


#prueba
if __name__ == "__main__":
    
    lista_alternativas = []
    
    alternativas = [
        {"contenido":"contenido 1", "ayuda":""},
        {"contenido":"contenido 2", "ayuda":"ayudita para el contenido 2"},
        {"contenido":"contenido 3", "ayuda":""}
        ]
    
    for dicc in alternativas:
        lista_alternativas.append(Alternativa(dicc["contenido"],dicc["ayuda"]))


    pregunta = Pregunta("enunciado", "ayuda", True,alternativas )
    #pregunta.__lista_alternativas[0].ayuda
    pregunta.mostrar_pregunta()