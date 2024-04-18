from ingredientes import ingredientes_carne, ingredientes_vegetales, tipos_masa

class Pizza:
    es_valida = False

class Pizza:
    es_valida = False

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def hacer_pedido(self):
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico(pepperoni, salami, jamón, pollo): ").lower()
        self.ingrediente_vegetal_1 = input("Ingrese el primer ingrediente vegetal(champinones, cebolla, pimientos, tomate):").lower()
        self.ingrediente_vegetal_2 = input("Ingrese el segundo ingrediente vegetal(champinones, cebolla, pimientos, tomate):").lower()
        self.tipo_masa = input("Ingrese el tipo de masa(tradicional, integral, fina): ").lower()

        self.es_valida = all([
            self.validar_elemento(self.ingrediente_proteico, ingredientes_carne),
            self.validar_elemento(self.ingrediente_vegetal_1, ingredientes_vegetales),
            self.validar_elemento(self.ingrediente_vegetal_2, ingredientes_vegetales),
            self.validar_elemento(self.tipo_masa, tipos_masa)
        ])

if __name__ == "__main__":
    print("Atributos de clase:")


    elemento = "salsa de tomate"
    valores_posibles = ["salsa de tomate", "salsa bbq"]
    print("¿El elemento '{}' está presente en la lista {}?".format(elemento, valores_posibles))
    print(Pizza.validar_elemento(elemento, valores_posibles))

    mi_pizza = Pizza()
    mi_pizza.hacer_pedido()

    print("Ingredientes vegetales:", mi_pizza.ingrediente_vegetal_1, mi_pizza.ingrediente_vegetal_2)
    print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
    print("Tipo de masa:", mi_pizza.tipo_masa)
    print("¿Es una pizza válida?", mi_pizza.es_valida)