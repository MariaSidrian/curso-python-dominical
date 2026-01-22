###############################################################
#Clase 10 - Listas dinámicas y comprensión de listas

#En esta clase aprendemos dos formas de crear listas en Python:

#1 La forma tradicional usando ciclos for.
#2 La forma moderna y optimizada usando comprensión de listas (list comprehension).

#La comprensión de listas permite escribir código más corto, limpio y legible,
#ideal para crear listas a partir de otras listas o entradas del usuario.
##################################################################


#Crearemos una lista en la que nosotros tenemos que agregar de cuantos digitos sera.
numeros=[1,2,3,4,5]
lista=[]
tamaño=int(input("Ingresa el tamaño de la lista"))
for i in range(tamaño):
    lista.append((input()))
print(lista)

#Inicio d enseñanza de compresores
#BASICAMENTE LISTAS DENTRO DE LISTAS
"Qué es un compresor? - Cada una de estas construcciones consta de una expresión que determina como modificar "
"el elemento de la lista original, seguida de una o varias clausulas for y opcinalmente una o varias clausulas." 
######EJEMPLO########
l1=[1,2,3,4,5]
print(f"Lista original: {l1}")

l2=[i**2 for i in l1]
print(f"Lista comprimida 2: {l2}")

l3=[n for n in l1 if n%2==0]
print(f"Lista comprimida 2: {l3}")

#AHORA, utilizaremos el primero problemas para hacerlo como el segundo
#t=[int(input()) for _ in range(5)]
#print(t)

print("SIN COMPRESORES")
lista=[]
tamaño=int(input("Ingresa el tamaño de la lista: "))
for i in range(tamaño):
    lista.append((input()))
print(lista)

print("CON COMPRESORES")
tam=int(input("Ingresa el tamaño de la lista: "))
t=[int(input()) for _ in range(tam)]
print(t)

#REPASAR TEORIA EN CONJUNTOS, PAGINA 77
#EMPEZAR EL CURSO DE PHYTON 1 DE NETAACADEMYCISCO