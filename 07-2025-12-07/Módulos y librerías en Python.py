# ============================================================
# CLASE 7 · MÓDULOS Y LIBRERÍAS EN PYTHON
# Uso de random, statistics y sys.argv
#
# En esta clase aprendemos:
# - Qué es un módulo en Python
# - Cómo importar módulos completos o funciones específicas
# - Generar valores aleatorios con random
# - Calcular promedios con statistics
# - Usar sys para interactuar con la computadora
# - Recibir argumentos desde la línea de comandos (sys.argv)
#
# ============================================================

import random
moneda = random.choice(['cara', 'cruz'])
print("El resultado de la moneda es:", moneda)

## Este de abojo es lo mismo de arriba, pero importando solo lo que se necesita###
from random import choice
moneda = choice(['cara', 'cruz'])
print("El resultado de la moneda es:", moneda)

## Este de abojo genera un número aleatorio entre 1 y 10 ## usando la librería random ##
import random 
numero = random.randint(1, 10)
print("El número aleatorio entre 1 y 10 es:", numero)

##Este es para revolver biblioteca Random, utilizando la función shuffle ##
import random
cartas = ['Jota', 'reina', 'Diamantes', 'Corazones', 'Picas', 'Tréboles']
random.shuffle(cartas)
print("El orden de las cartas después de barajarlas es:")
print(cartas)

##Estadistica es igual a promedio##
import statistics
print(statistics.mean([90,80]))  # Salida: 3

##sys es un modulo que sirve para hablar con tu computadora desde python##
import sys
print(sys.version)

### Usando sys para recibir argumentos desde la línea de comandos ##
## signigifica que puedes pasar información a tu programa sin necesidar de escribir cada linea ##
## Sustituyendo input() ## o el nombre del usuario ## o cualquier otro dato ##
#para que un script pueda trabajar solo
#Para automatizar tareas 
#para usar el programa con diferentes datos sin cambiar el código fuente##
#para no utilizar tu mouse o teclado##
import sys
try:
    print("Hola, mi nombre es", sys.argv[1])
except IndexError:
    print("Falta el argumento")


#import sys #en esta linea estoy importando la librería sys ##
if len(sys.argv) < 2: #va a esta buscando si pusiste menos de 2 argumentos ##
    print("Muy pocos argumentos") 
elif len(sys.argv) > 2: #va a buscar si le pususte menos de 2 argumentos ##
    
    print("Demasiados argumentos")
else: #es el opuesto, te obliga a poner dos argumentos ##
    print("Hola, mi nombre es", sys.argv[3])