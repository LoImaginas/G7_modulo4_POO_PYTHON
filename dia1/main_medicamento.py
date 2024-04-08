from medicamento import Medicamento
#istancia de la clase o creacion de un objeto 
paracetamol = Medicamento()
aspirina = Medicamento()

print(paracetamol.descuento) #0.05
print(aspirina.descuento) #0.05

paracetamol.descuento = 0.06
print(paracetamol.descuento) #0.06
print(aspirina.descuento) #0.05
