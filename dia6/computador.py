class Computador():
    def __init__(self):
        self.ram = ""
        self.disco_duro =""
        self.teclado = ""
        self.mouse = ""
        
class Ram():
    def __init__(self,velocidad,bite):
        self.velocidad = velocidad
        self.bite = bite
        
class DiscoDuro():
    def __init__(self,capacidad):
        self.capacidad=capacidad
        self.tipo="ssd"
        
        
class Teclado():
    def __init__(self):
        self.idioma = "esp"
        self.cant_teclas = 100 
        
        
#cuando se agrega como atributo es agregacion 
#class Teclado():
#def __init__(self,idioma: str, cant_teclas: int):
#     self.idioma = idioma
#     self.cant_teclas = cant_teclas         
        
class Mouse():
    def __init__(self):
        self.tipo = ""
        self.conectividad = ""    
        
#cuando se agrega como atributo es agregacion           
#class Mouse():
#def __init__(self,tipo: str, conectividad: srt):
#     self.tipo = tipo
#     self.conectividad = conectividad         
             
    
class Computador:
    def __init__(self,teclado:Teclado, mouse:Mouse) :
        #componentes y perifericos
        #Composición es el proceso de hacer una instancia dentro de otra clase
        #el computador esta compuesto de 
        self.ram = Ram(1500,32)  #composicion
        #atributo de instancia de tipo objeto dentro del computador
        self.disco_duro = DiscoDuro(1024) #compisicion    
        
        self.teclado= teclado #agregacion
        self.mouse= mouse  #agregacion
        
#AGREGACION:
#Instancia de clase que se toma como atributo      
teclado = Teclado("latino",120)
mouse = Mouse("gamer", "bluetooth") 

computador_gamer = Computador(teclado,mouse)              
              
 
print(computador_gamer.ram.velocidad) #1500
print(computador_gamer.teclado.cant_teclas) #120       
        