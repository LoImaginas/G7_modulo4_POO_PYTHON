from datetime import datetime   # Importa la clase datetime del módulo datetime
from error import LargoExcedidoError, SubTipoInvalidoError  # Importa las clases de excepción desde el archivo error.py

def manejar_excepciones():    # Función para manejar las excepciones
    try:
        nombre_campaña = "Campaña de marketing " * 30  # Simula un nombre de campaña demasiado largo
        if len(nombre_campaña) > 250:  
            raise LargoExcedidoError("El nombre de la campaña es demasiado largo")  # Lanza una excepción si el nombre de la campaña es demasiado largo

    except LargoExcedidoError as e:   # Captura la excepción de nombre de campaña demasiado largo
        # Obtiene la fecha y la hora actual     
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')     
        # Abre el archivo de registro de errores añadiendo al final del archivo
        with open("dia13_prueba/errores.log", "a+") as file:
            # Escribe el mensaje de la excepción junto con la fecha y la hora
            file.write(f"[{now}] LargoExcedidoError: {e.mensaje}\n")

    try:
        sub_tipo_invalido = "invalido"  # Simula un subtipo de anuncio inválido
        if sub_tipo_invalido not in ("instream", "outstream"): # Verifica si el subtipo de anuncio es válido
            raise SubTipoInvalidoError("Subtipo de anuncio inválido", sub_tipo_invalido)  # Lanza una excepción si el subtipo de anuncio es inválido

    except SubTipoInvalidoError as e:  # Captura la excepción de subtipo de anuncio inválido
        # Obtiene la fecha y la hora actual   
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Abre el archivo de registro de errores en modo de añadir al final del archivo
        with open("dia13_prueba/errores.log", "a+") as file:
            # Escribe el mensaje de la excepción junto con la fecha y la hora
            file.write(f"[{now}] SubTipoInvalidoError: {e.mensaje}, Subtipo: {e.subtipo}\n")

if __name__ == "__main__":  # Verifica si este es el archivo principal que se está ejecutando
    manejar_excepciones()  # Llama a la función para manejar las excepciones