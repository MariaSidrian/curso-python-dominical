# ============================================
# CLASE 11
# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# TEMA: Calculadora básica con manejo de errores
#
# En esta clase se crea una calculadora usando
# clases y métodos, aplicando manejo de
# excepciones para evitar errores como la
# división entre cero.
# ============================================

class Calculadora:
   
    def suma(self,a,b):
        return a+b
    def resta(self,a,b):
        return a-b
    def multiplicacion(self,a,b):
        return a*b 
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:      #Api de excepcion de Python
            raise ("No se puede dividir entre cero...")    #Es como el mensaje de alerta

    