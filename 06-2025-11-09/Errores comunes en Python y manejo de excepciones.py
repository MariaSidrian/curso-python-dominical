# ============================================
# Clase 5 – Errores y manejo de excepciones en Python
# ============================================


# **SyntaxError**

"""Un SyntaxError (error de sintaxis) aparece cuando el intérprete de Python (o cualquier lenguaje de programación) no puede entender el código porque no sigue las reglas de la sintaxis del lenguaje.

En palabras simples:


El código está “mal escrito” según las reglas de Python, así que el programa ni siquiera puede empezar a ejecutarse.
"""

#jemplo 1: Paréntesis o comillas faltantes


print("Hola mundo")


"""Error: 

SyntaxError: EOL while scanning string literal


 Explicación:

Falta cerrar las comillas. Python llega al final de la línea esperando el cierre "."""

 #Corrección:

print("Hola mundo")

"""# **ValueError**
 Definición sencilla:


Un ValueError ocurre cuando el tipo de dato es correcto, pero su valor no tiene sentido para la operación que se intenta hacer.

Es decir: Python entiende qué tipo de dato le diste, pero no puede usar ese valor en ese contexto."""

#Ejemplo 1: Convertir texto no numérico a número
numero = int("10")


"""Error:

ValueError: invalid literal for int() with base 10: 'hola'


 Explicación:

int() espera algo que parezca un número, pero "hola" no puede convertirse a entero."""

#Corrección:

numero = int("10")  #  Esto sí es válido

"""# **NameError**
 Definición sencilla:

Un NameError ocurre cuando Python intenta usar una variable, función o nombre que no ha sido definido o no existe en ese momento del programa.

En palabras simples: estás usando un nombre que Python no conoce."""

#Ejemplo 1: Variable no definida

print("nombre")


"""Error:

NameError: name 'nombre' is not defined


 Explicación:

Estás pidiendo imprimir la variable nombre, pero nunca la creaste antes."""

#Corrección:

nombre = "María"

print(nombre)


#Declarar valor

x = int(input("Cual es el valor de x?"))
print(f"x es igual a {x}")  #La f sirve para declarar cual es el valor de x

#EXCEPCION

try:
  x = int(input("Cuál es el valor de x?"))
  print(f"x es igual a {x}")  #La f sirve para declarar cual es el valor de x
except ValueError:
  print("x no es un número válido")

#Ciclo SIN ROMPER

try:
  x = int(input("Cuál es el valor de x?"))
  print(f"x es igual a {x}")  #La f sirve para declarar cual es el valor de x
  print(f"x es igual a {y}")
except NameError:
  print("y no esta definido")
except ValueError:
  print("x no es un número válido")    #Si pones una respuesta que necesite un valor de valor, se imprime hata abajo los dos print, pero si es solo hasta el error de nombre, solo se imprime el primer print

#Ciclo CON BREAK

while True:
  try:
      x = int(input("Cuál es el valor de x?"))
      break

  except ValueError:
    print("x no es un número válido")

#Definicion de funciones
#Escribe un programa en Phyton que le pida al usuario un número entero, válida que la entrada sea correcta y repita la pregunta hasta que se ingrese un valor válido.Cuando el usuario escriba un número entero, el programa deberá mostrar el resultado en pantalla en el formato: "x is {valor}"

def main():
  x = get_int()
  print(f"x is {x}")

def get_int():
  while True:
    try:
      x = int(input("Cuál es el valor de x?"))
    except ValueError:
      print("x no es un número válido")
    else:
      break
  return x

main() 