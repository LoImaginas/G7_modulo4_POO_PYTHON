from pizza import Pizza

print("Atributos de clase:")
print("Pizza.es_valida:", Pizza.es_valida)

elemento = "salsa de tomate"
valores_posibles = ["salsa de tomate", "salsa bbq"]
print("¿El elemento '{}' está presente en la lista {}?".format(elemento, valores_posibles))
print(Pizza.validar_elemento(elemento, valores_posibles))

mi_pizza = Pizza()
mi_pizza.hacer_pedido()

if mi_pizza.es_valida:
    print("Ingredientes vegetales:", mi_pizza.ingrediente_vegetal_1, mi_pizza.ingrediente_vegetal_2)
    print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
    print("Tipo de masa:", mi_pizza.tipo_masa)
    print("¿Es una pizza válida?", mi_pizza.es_valida)
else:
    print("¡El pedido realizado no es válido!")