from pregunta import Pregunta

class Encuesta():
    def __init__(self,nombre: str,preguntas: list[dict]):
        self.nombre = nombre
        self.__listados_respuestas = []
        self.__preguntas = [
            Pregunta(
                dicc["enunciado"],
                dicc["ayuda"],
                dicc["requerida"],
                dicc["alternativas"]    
                ) for dicc in preguntas
        ]
    def mostrar_encuesta(self):
        print(self.nombre)

        for preg in self.__preguntas:
            preg.mostrar_pregunta()

    def agregar_listado_respuestas(self,listado_respuestas ):
        self.__listados_respuestas.append(listado_respuestas)

class EncuestaLimitadaEdad(Encuesta):
    pass

class EncuestaLimitadaRegion(Encuesta):
    pass