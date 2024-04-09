from pelota import Pelota

#creacion de objeto o instancia de la clase #crear una variable
pelota_multicolor = Pelota() 
#pelota_multicolor es una variable, se le asigna una clase Pelota
#deja de ser una variable y se transforma en objeto
#print(pelota_multicolor.color) #color es un atributo que se le asigna a nuestra variable
#AttributeError: type object 'Pelota' has no attribute 'color'

#asignar color
pelota_multicolor.asigna_color("rojo")
print(pelota_multicolor.color)
pelota_multicolor.lee_color()

pelota_multicolor.asigna_color("verde")

pelota_multicolor.lee_color_local_y_atributo("amarillo")

pelota_negra = Pelota()
pelota_negra.lee_color_local_y_atributo("Negro") #AttributeError: 'Pelota' object has no attribute 'color'