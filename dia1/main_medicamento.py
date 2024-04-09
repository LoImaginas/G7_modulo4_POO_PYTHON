from medicamento import Medicamento
#istancia de la clase o creacion de un objeto 
paracetamol = Medicamento()
aspirina = Medicamento()

print(paracetamol.descuento) #0.05
print(aspirina.descuento) #0.05

paracetamol.descuento = 0.06
print(paracetamol.descuento) #0.06
print(aspirina.descuento) #0.05

    
precio = int(input("ingrese el precio a validar >"))
#llamado a un metodo estatico
es_valido = Medicamento.validar_mayor_a_cero(precio)
if es_valido:
    print("el precio ingresado es valido")#2000 #el precio ingresado es valido
else:
    print("el precio ingresado no es valido")   
print("")    
if paracetamol.IVA == aspirina.IVA and paracetamol.descuento == aspirina.descuento:    
        print("Todas las instancias(objetos) tienen las mismas valores de IVA y descuento")
        print("el valor del iVA es", Medicamento.IVA) #el valor del iVA es 0.18
        print("El valor de descunto es", Medicamento.descuento)  #El valor de descunto es 0.05