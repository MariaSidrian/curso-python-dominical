#Clase 1 - Fundamentos de Python
# Tema: print(), tipos de datos, variables y conversiones

print("Hola", "Mundo", 2025)

"""**Tipos de datos y variables**


*   int - 10
*   float - 3.14
*   str - "hola"
*   bool - true/false
*   variables - contenedores de datos

sep (decide con que se pega cada palabra).
"""

print("A", "B", "C", sep="-")

"""Lo que va dentro de las comillas del end es con lo que se va a separar los dos print.

"""

print("1234", end="       ")
print("5678")

#Ejemplo mostrando sep y end
print("Phyton", "es", "genial", sep="***", end=" --> ")
print("Aprendamos mas")

"""Si pongo el 2 con comillas (num = "2") sigue siendo 2 pero como texto, (estas llenando el contenedor)."""

#funcion print, Que es una variable?
num = 2
print(num)

"""Suma de 2 Enteros (Con comillas lo pone como texto y sin comillas la operacion)"""

Resultado_de_la_suma = 2 + 2
print(Resultado_de_la_suma)

"""Suma de 2 Variables Enteras (agregando sep y end)"""

#Ejemplo 1
Num_1 = 5
Num_2 = 5
Resultado_de_la_suma = Num_1 + Num_2
print("Resultado de la suma es: ",Resultado_de_la_suma, sep="--------",end="***")

#Ejemplo 2
Num_1 = 5
Num_2 = 5
Resultado_de_la_suma = Num_1 + Num_2
print("Num_1 + Num_2: ",Num_1 + Num_2, sep="--------",end="***")

"""Numero flotante

"""

#Ejemplo con flot
pi = 3.14
radio = 2
area_circulo = pi * (radio * radio) # O puedes poner (radio ** 2)
print(area_circulo)

"""Booleano"""

#Ejemplo 1
es_soleado = True
esta_lloviendo = False
print(es_soleado)    #Print imprime el resultado de la variable que estas declarando.
print(esta_lloviendo)

#Ejemplo 2
num1 = 2
num2 = 2
print(num1 >= num2)

"""
saludo

"""

saludo = "!Hola, mundo!"
letra = 'a'
print(saludo)
print(letra)
texto_comillas_simples = 'Esto puede ser un saludo : "!Hola, mundo!"'
texto_comillas_dobles = "Esto puede ser un saludo : '!Hola, mundo'"
print(texto_comillas_simples)
print(texto_comillas_dobles)

"""Convertir un tipo de dato a otro, ejemplo: millas a km, celsius a farenheit, etc, y como demostramos que tipo de dato es.

"""

numero_texto = 38.5
numero_entero = float(numero_texto)
print(numero_entero)
print(type(numero_entero))