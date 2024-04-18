from medicamento import Medicamento

#instancia de la clase o creacion de un objeto
paracetamol  = Medicamento()
aspirina = Medicamento()

print(paracetamol.descuento)
print(aspirina.descuento)

#Modificacion del estado de un objeto
paracetamol.descuento = 0.06

print(paracetamol.descuento)
print(aspirina.descuento)

Medicamento.descuento = 0.04
ibuprofeno = Medicamento()
print(ibuprofeno.descuento)

precio = int(input("Ingrese el precio a validar > "))
#llamado a un metodo estatico
es_valido = Medicamento.validar_mayor_a_cero(precio)

if es_valido:
    print("El precio ingresado es valido")
else:
    print("El precio ingresado NO es valido")

print(paracetamol.descuento, aspirina.descuento)

if paracetamol.IVA == aspirina.IVA and paracetamol.descuento == aspirina.descuento:
    print("Todas las instancias(objetos), tienen los mismmos valores de IVA y descuento")
    print("El valor del IVA es", Medicamento.IVA)
    print("El valor de descuento es", Medicamento.descuento)

Medicamento.IVA = 0.19
#ibuprofeno.modificar_atributo()
print(ibuprofeno.IVA)
print(aspirina.IVA)

print(paracetamol.descuento, aspirina.descuento,ibuprofeno.descuento)