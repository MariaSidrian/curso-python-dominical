# ============================================================
# CLASE 9 · ECUACIONES CUADRÁTICAS EN PYTHON
# Uso de la Fórmula General y Programación Orientada a Objetos
#
# En esta clase aprendemos:
# - Resolver ecuaciones de segundo grado (ax² + bx + c = 0)
# - Calcular el discriminante
# - Validar raíces reales
# - Aplicar Programación Orientada a Objetos (POO)
# - Uso del módulo math
#
# ============================================================


#RESUELVE LA ECUACION 2x² + 9X +10 = 0
#UTILIZANDO LA FORMULA GENERAL
import math

a=2
b=9
c=10

d=(b**2)-(4*(a)*(c))

x1=(-b+math.sqrt(d))/(2*a)

x2=(-b-math.sqrt(d))/(2*a)

print(f"El valor de x1 es: {x1}")
print(f"El valor de x2 es: {x2}")

#OTRA FORMA DE HACERLO
if d>=0:
    x1=(-b+math.sqrt(d))/(2*a)

    x2=(-b-math.sqrt(d))/(2*a)

    print(f"El valor de x1 es: {x1}")
    print(f"El valor de x2 es: {x2}")
else:
    print("No existen raices de números negativos.")

#MISMA OPERACION INTRODUCIENDO LOS VALORES a, b y c
#Definicion de funciones
#Escribe un programa en Phyton que le pida al usuario un número entero, válida que la entrada sea correcta y repita la pregunta hasta que se ingrese un valor válido.Cuando el usuario escriba un número entero, el programa deberá mostrar el resultado en pantalla en el formato: "x is {valor}"

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d=(b**2)-(4*(a)*(c))
if d>=0:

    x1=(-b+math.sqrt(d))/(2*a)

    x2=(-b-math.sqrt(d))/(2*a)

    print(f"El valor de x1 es: {x1}")
    print(f"El valor de x2 es: {x2}")
else:
    print("No existen raices de números negativos.")

#TAREA: CONVERTIR ESTE CÓDIGO A POO (PROGRAMACIÓN ORIENTADA A OBJETOS)
"""class 
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d=(b**2)-(4*(a)*(c))
if d>=0:

    x1=(-b+math.sqrt(d))/(2*a)

    x2=(-b-math.sqrt(d))/(2*a)

    print(f"El valor de x1 es: {x1}")
    print(f"El valor de x2 es: {x2}")
else:
    print("No existen raices de números negativos.") """""


import math

# Definimos la clase
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def resolver(self):
        d = (self.b ** 2) - (4 * self.a * self.c)

        if d >= 0:
            x1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(d)) / (2 * self.a)

            print(f"El valor de x1 es: {x1}")
            print(f"El valor de x2 es: {x2}")
        else:
            print("No existen raíces de números negativos.")


# -------- PROGRAMA PRINCIPAL --------

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

ecuacion = EcuacionCuadratica(a, b, c)
ecuacion.resolver()

