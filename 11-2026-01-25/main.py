from Calculadora import Calculadora

class Main:
    def __init__(self):
        self.calculadora=Calculadora() #Aqui le esta diciendo el self.c que tiene que ser
                                       #igual a a calculadora del otro archivo
    def funcionamiento_calculadora(self):
        a=float(input("Ingresa el primer numero: "))
        b=float(input("Ingresa el segundo numero: "))

        print("El resultado de la suma es:",self.calculadora.suma(a,b))
        print("El resultado de la resta es:",self.calculadora.resta(a,b))
        print("El resultado de la multiplicacion es:",self.calculadora.multiplicacion(a,b))

        try:
            print("El resultado de la division es:",self.calculadora.division(a,b))
        except ZeroDivisionError as e:
            print(f"Error: {e}")
if __name__=="__main__":
    Calculadora=Main()
    Calculadora.funcionamiento_calculadora()

#TAREA: Agregar la opcion de elegir que operacion quiero hacer + la opcion de salir,
#Aparte de que de mensaje como "El resultado es:", "Saliste con exito",
#OPCIONAL:#
#Ya por último que al terminar la operación regreses de nuevo al menu de eleccion de operaciones.
