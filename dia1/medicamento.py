class Medicamento():
    #atributos
    descuento = 0.05
    IVA = 0.18
    
    @staticmethod
    def validar_mayor_a_cero(numero:int):
        return numero >0
    
    #los metodos estaticos no pueden modificar los atributos de una clase 
    