from usuario import Usuario
from datetime import datetime
import json

#Fecha y hora actual
lista_usuarios = []
log_error = open('dia12_desafio/error.log', 'a+')
now = datetime.now()
# Leer línea a línea el archivo usuarios.txt, y crear
# una instancia de Usuario a partir de los datos de cada línea leída
with open("dia12_desafio/usuarios.txt")as usuarios:
    #print(usuarios.readline())
     #print(uaurios.readline())
    linea = usuarios.readline()
    #print(linea)
    #print(linea)              #{"nombre": "Page", 
    #print(json.loads(linea))  #{'nombre': 'Page', 
    while linea:
        try:
            usuario = json.loads(linea)
            lista_usuarios.append(Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
        except json.decoder.JSONDecodeError as e:
            log_error.write(f"[{now.strftime('%d-%m-%Y %H:%M:%S')}] ERROR: {e}\n")
        finally:
            linea = usuarios.readline()
           
for usuario in lista_usuarios:
    print(f'{usuario.nombre}  {usuario.apellidos}  {usuario.email}  {usuario.genero}')
    
    
 ####################  VERSION DEL PROFE ##############   
 
 # from usuario import Usuario
 # from datetime import datetime  
 # import json
 #
 #lista_usuarios = []
 #
 #with open("dia12_desafio/usuarios.txt") as usuarios:
 ####print(usuarios.readline())
 ####print(usuarios.readline())
 #   linea = usuarios.readline()
 #   while linea:
 #          try:
 ####print(linea)
 ####print(linea)
 ####print(json.loads(linea))
 #              dicc_usuario = json.loads(linea)
 #              usuario = Usuario(dicc_usuario["nombre"], dicc_usuario["apellido"], dicc_usuario["email"], dicc_usuario["genero"])
 #              lista_usuarios.append(usuario)
 #
 #              linea = usuarios.readline()
 #          except Exception as e:
 #              with open("dia12_desafio/logs/error.log", "a+") as log:
 #otra opcion    with open("dia12_desafio/logs/{fecha_hora.strftime("%Y/%m/%d_%H
 #                  fecha_hora = datatime.now()
 #                  print(fecha_hora.strftime("%Y/%m/%d, %H:%M:%S"))
 #                  log.write(f"[{fecha_hora.strftime('%Y/%m/%d, %H:%M:%S')}]{e}\n")
 #                  print(e)
 #                  log.close()#### cerrar log dentro del with        
 #          finally:
 #              linea=usuarios.readline()
 #print(lista_usuarios)