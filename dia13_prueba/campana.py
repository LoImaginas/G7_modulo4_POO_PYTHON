from datetime import date  # Importa la clase date del módulo datetime

class Campana:
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list) -> None:
        # Constructor de la clase Campana
        self.nombre = nombre  # Asigna el nombre de la campaña
        self.fecha_inicio = fecha_inicio  # Asigna la fecha de inicio de la campaña
        self.fecha_termino = fecha_termino  # Asigna la fecha de término de la campaña
        self.anuncios = [self.instancia_de_anuncios(dicc) for dicc in anuncios]  # Instancia los anuncios asociados a la campaña

    def instancia_de_anuncios(self, anuncio: dict):
        # Método para crear instancias de anuncios a partir de un diccionario
        pass  # Este método se debe implementar para crear instancias de anuncios

    def __str__(self):
        # Método especial para representar la campaña como una cadena de texto
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {', '.join([f'{len(self.anuncios)} {tipo}' for tipo in ('Video', 'Display', 'Social')])}"
