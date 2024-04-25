class Error(Exception):
    # Define la clase base de excepción Error que hereda de Exception
    pass

class LargoExcedidoError(Error):
    # Define una subclase LargoExcedidoError que hereda de Error
    def __init__(self, mensaje):
        # Define el método __init__ para inicializar la excepción
        self.mensaje = mensaje   # Almacena el mensaje de la excepción

class SubTipoInvalidoError(Error):
    # Define una subclase SubTipoInvalidoError que hereda de Error
    def __init__(self, mensaje, subtipo):
        # Define el método __init__ para inicializar la excepción
        self.mensaje = mensaje  # Almacena el mensaje de la excepción
        self.subtipo = subtipo  # Almacena el subtipo asociado a la excepción