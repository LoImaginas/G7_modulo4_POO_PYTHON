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

pelota 
