#Clase 03 – Estructuras de repetición: while y for
#Curso Python Dominical
#Tema: Repetición de instrucciones y control de ciclos


#**Forma de hacer que un programa diga "miau" varias veces sin while.**


print("miau")
print("miau")
print("miau")
print("miau")
print("miau")
print("miau")
print("miau")
print("miau")
print("miau")

"""# **While**
¿Qué es while?

while es una estructura de repetición que ejecuta un bloque de código mientras se cumpla una condición.

A diferencia de for, no está necesariamente ligada a un número de repeticiones, sino a una condición lógica que puede ser verdadera o falsa.

Sintaxis general
En Python:

while condición:

    # código que se repite

En JavaScript, C, Java:

while (condición) {

    // código que se repite
}

Ejemplo en Python:

i = 0

while i < 5:

    print("Hola", i)

    i += 1


Salida:

Hola 0

Hola 1

Hola 2

Hola 3

Hola 4


Esto hace lo mismo que el for anterior, pero con un enfoque diferente:

Empiezas con i = 0

El bucle se repite mientras i sea menor que 5

Dentro del bucle, i se incrementa para evitar un bucle infinito

¡Cuidado! Bucle infinito

Si olvidas actualizar la condición dentro del bucle, puedes crear un bucle infinito.

while True:

    print("Esto nunca se detiene...")

 **Diferencias clave entre for y while**

Característica	for	while

Uso típico	Número fijo de repeticiones	Repetir hasta que algo cambie
Control	Tiene inicio, fin y paso claros	Solo depende de una condición
Riesgo de bucle infinito	Menor	Mayor si olvidas cambiar la condición

¿Cuándo usar cuál?

Usa for si sabes cuántas veces quieres repetir algo.

Usa while si no sabes cuántas veces, pero sabes la condición para parar.

**Forma de hacer que un programa diga "miau" varias veces con while.**
Preguntarse los 5 PORQUE de programacion. Ejemplo: Que es la i en el diagrama de flujo con while (i=1)? i= es la condicion del while.


#Ejemplo 1
i = 5

while i != 0:
  print(f"miau")
  i = i - 1

#Cuando un ciclo no para, que estas batallando y se mantiene en ciclo, teclear CTRL + C

#Ejemplo 2 Con una condicion diferente y iniciando desde el 0
i = 0

while i < 8:
  print(f"miau {i}")
  i += 1

"""### **For**
#En programación, for es una estructura de control que se utiliza para ejecutar un bloque de código de manera repetitiva (es decir, en un bucle o loop), generalmente un número determinado de veces.

#¿Qué hace exactamente?

#El bucle for itera sobre una secuencia (como una lista, un rango de números, una cadena de texto, etc.) o repite un bloque de instrucciones mientras se cumpla una condición específica.

#Ejemplo en Python:

for i in range(5):

    print("Hola", i)


#¿Qué hace este código?

#range(5) genera los números del 0 al 4.

#i toma uno de esos valores en cada iteración.

#Se imprime "Hola" seguido del valor de i.

"""Salida:

Hola 0

Hola 1

Hola 2

Hola 3

Hola 4

#¿Para qué se usa?

Recorrer listas, arrays o colecciones.

Ejecutar una tarea varias veces.

Procesar elementos uno a uno.




"""

#Ejemplo 1
for _ in [5, 1, 2]:    #El 5, 1, 2 solo son como cajas de valores, le estamos dando la instruccion de que imprima "miau" en cada uno de los valores.
  print("miau")

#Ejemplo 2
for x in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
  print(f"miau {x}") #Al poner la x, declaras que imprima miau + el valor de X que es lo que esta dentro del []

for i in range(3):
  print(f"miau ") #Al poner la i, declaras que imprima miau sin el valor de i porque no lo decralaraste en print(f"miau {i}")

"""Ejemplo de salto de linea (lo de fime con el \n)"""

print("miau\nmiau\nmiau")

print("miau\n\nmiau\n\nmiau")#Poner \n\n, es doble salto

print("miau\n\n" * 3)  #Con salto

print("miau" * 3 )  #Sin salto

print("miau\n\n" * 3, end="") #El end="", es limpieza de trabajo, elimina linea sin utilizar

#Repetir hasta que el usuario ingrese un numero positivo
while True:
  n = int(input("Cual es n?")) #Pedir un numero al usuario
  if n > 0:                    #Si el numero es mayor que 0
    break                      #Salir del bucle
#Imprimir "miau" n veces
for _ in range(n):
      print("miau")