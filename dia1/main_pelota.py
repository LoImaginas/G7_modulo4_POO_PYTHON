#importar pelota
#opcion1 
import pelota
#opcion2
from pelota import Pelota

#INSTANCIAR O CREAR OBJETO
#opcion1
pelota_de_andy = pelota.Pelota()
#opcion2
pelota_de_andy = Pelota()

print(pelota_de_andy) #<pelota.Pelota object at 0x104f7e7b0>
print(type(pelota_de_andy)) #<class 'pelota.Pelota'>
print(pelota_de_andy.forma) #redondeada

pelota_de_andy.material = "Plastico"
print(pelota_de_andy.material) #Plastico

pelota_tenis = Pelota()
print(pelota_tenis.material)
pelota_tenis.material ="Caucho"

#metodos estaticos
#no se necesita crear un objeto para invocar al metodo
print(Pelota.crear_rebote) #[<function Pelota.crear_rebote at 0x10b795f80> 0, 1, 0]
print(Pelota.crear_rebote()) #[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

Pelota.imprimir_posiciones() #[3, 0, 2, 1, 0]
print(Pelota.posiciones) #[3, 0, 2, 1, 0]
print("")

pelota_futbol = Pelota() 
print(pelota_futbol.posiciones) #[3, 0, 2, 1, 0]

#metodo no estatico 
pelota_futbol.rebotar()
print(pelota_futbol.posiciones) #[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

pelota_basket = Pelota()
print(pelota_basket.posiciones)#3, 0, 2, 1, 0]

#metodo no estatico, permiten crear atributos 
#de tipo "atributo de instancia"
pelota_basket.nuevo_atributo()
print(pelota_basket.color) #blanco
#print (pelota_futbol.color)#AttributeError: 'Pelota' object has no attribute 'color'

#la instancia de una clase, es la creacion de un objeto a traves de una clase
#que es un atributo de instancia: es una caracteristica o atributo que se le atribuye a traves de un metodo no estatico
#existen dos tipos de metodos, estaticos y no estaticos
#la diferencia es que los estaticos no afecta los atributos de la clase y los no estaticos si afecra los atributos de una clase