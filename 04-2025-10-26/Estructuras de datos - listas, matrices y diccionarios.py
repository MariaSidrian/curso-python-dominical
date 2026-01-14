#=======================================================
#  Clase 04 – Listas, matrices y diccionarios en Python
# Curso Python Dominical
# Tema: Colecciones, métodos y recorridos con for
#=======================================================


"""# **LISTA**
En programación, una lista es una estructura de datos que se utiliza para almacenar una colección ordenada de elementos.
Sección nueva
Estos elementos pueden ser de cualquier tipo (números, texto, objetos, etc.), y puedes acceder, modificar, agregar o eliminar elementos fácilmente.

Características principales de una lista:

Ordenada:
Los elementos tienen una posición o índice (por ejemplo, el primer elemento está en la posición 0).

Mutable (en la mayoría de los lenguajes):
Puedes cambiar los valores, añadir nuevos elementos o eliminar otros.

Permite duplicados:
Una lista puede contener elementos repetidos.

Heterogénea (en algunos lenguajes como Python):
Puede contener distintos tipos de datos dentro de la misma lista.

Ejemplo en Python

Crear una lista

numeros = [10, 20, 30, 40]

Acceder a un elemento

print(numeros[1])   # Muestra: 20

Agregar un elemento

numeros.append(50)

Eliminar un elemento

numeros.remove(30)

Recorrer la lista

for n in numeros:

    print(n)


Salida:

10

20

40

50
"""

#Ejemplo de lista en Phyton
#Tema: Mario Kart

#Definimos lista de corredores iniciaes
corredores = ["Mario", "Luigi", "Yoshi", "Bowser"]

#Mostramos toda la lista
print("Lista de corredores:", corredores)

#Ejemplo de lista, solo Mario y Bowser

#Definimos lista de corredores iniciaes
corredores = ["Mario", "Luigi", "Yoshi", "Bowser"]

#Mostramos toda la lista
print(corredores[0], corredores[3])

#Ejemplo de lista, solo Mario y Bowser (con dos print)

#Definimos lista de corredores iniciaes
corredores = ["Mario", "Luigi", "Yoshi", "Bowser"]

#Mostramos la lista
print(corredores[0])
print(corredores[3])

#Ejemplo de lista (Dominando el -1, -2, o 1, 2)

#Definimos lista de corredores iniciaes
corredores = ["Mario", "Luigi", "Yoshi", "Bowser"]

#Mostramos la lista
print(corredores[-1])
print(corredores[-3])

#Ejemplo de lista (Dominando el -1, -2, o 1, 2)

#Definimos lista de corredores iniciaes
corredores = ["Mario", "Luigi", "Yoshi", "Bowser"]

#Mostramos la lista
print(corredores[1])
print(corredores[2])

#Ejemplo de lista, mismo ejemplo pero ahora con Len

# Definimos lista de corredores iniciales
corredores = ["Mario", "Luigi", "Yoshi", "Bowser"]

# Mostramos el último elemento (equivalente a -1)
print(corredores[len(corredores) - 1])  # Bowser

# Mostramos el elemento que está tres posiciones antes del final (equivalente a -3)
print(corredores[len(corredores) - 4])  # Mario

"""# **APPEND**

En Python, el método append() se usa para agregar un elemento al final de una lista.

Sintaxis

lista.append(elemento)


lista: es la lista a la que quieres agregar algo.

elemento: es el valor (número, cadena, lista, objeto, etc.) que se agregará al final.

Ejemplo básico

frutas = ["manzana", "plátano", "uva"]

frutas.append("naranja")

print(frutas)


Salida:

["manzana", "plátano", "uva", "naranja"]

Ejemplo con números

numeros = [1, 2, 3]

numeros.append(4)

print(numeros)


Salida:

[1, 2, 3, 4]

Importante

append() solo agrega un elemento a la vez.
Si agregas una lista, se inserta como un solo elemento, no se combinan:

a = [1, 2, 3]

a.append([4, 5])

print(a)


Salida:

[1, 2, 3, [4, 5]]


Si quieres agregar varios elementos individualmente, usa extend():

a = [1, 2, 3]

a.extend([4, 5])

print(a)


Salida:

[1, 2, 3, 4, 5]
"""

resultado = (corredores)
print(resultado)
resultado.append("Toad")
print(resultado)

# Definimos una lista
resultado = ["Mario", "Luigi"]

# Agregamos nuevos elementos
resultado.append("Princess")
resultado.append("Toad")
resultado.append("Koopa")
resultado.append("Yoshi")

# Agregamos una lista dentro de otra lista
resultado.append(["Bowser", "Waluigi"])

print(resultado) #PERO SALEN CORCHETES EN LA RESPUESTA

# Definimos una lista
resultado = ["Mario", "Luigi"]

# Agregamos nuevos elementos uno por uno
resultado.append("Princess")
resultado.append("Toad")
resultado.append("Koopa")
resultado.append("Yoshi")

# Agregamos varios elementos SIN corchetes internos
resultado.extend(["Bowser", "Waluigi"])

print(resultado)

# Explicación rápida:
#.append() ➜ agrega un solo elemento al final (incluso si es una lista).
#.extend() ➜ desempaqueta los elementos de otra lista y los agrega uno por uno.

"""#** REMOVE**
En Python, el método .remove() se usa para eliminar un elemento específico de una lista.

 Sintaxis

lista.remove(elemento)


lista: la lista donde vas a eliminar algo.

elemento: el valor que quieres quitar (no su posición, sino su contenido).

 Ejemplo básico

frutas = ["manzana", "plátano", "uva", "naranja"]

frutas.remove("uva")

print(frutas)


Salida:

["manzana", "plátano", "naranja"]


 Si el elemento no existe, Python da error:

frutas = ["manzana", "plátano"]

frutas.remove("pera")  #  Error


Error:

ValueError: list.remove(x): x not in list



Para evitar eso, puedes comprobar antes:

if "pera" in frutas:
    frutas.remove("pera")

 Solo elimina la primera aparición del valor:

numeros = [1, 2, 3, 2, 4]

numeros.remove(2)

print(numeros)


Salida:

[1, 3, 2, 4]


(El primer 2 desapareció, el segundo no.)
"""

#Eliminar a Koopa
resultado = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]
resultado.remove("Koopa Troopa")

print(resultado)

"""## **INSERT**
En Python, el método .insert() se usa para insertar un elemento en una posición específica dentro de una lista.

 Sintaxis

lista.insert(posición, elemento)


posición: el índice (número) donde se insertará el elemento.

elemento: el valor que quieres agregar.

 Si la posición ya está ocupada, el nuevo valor se mueve a la derecha.

 Ejemplo básico

frutas = ["manzana", "plátano", "naranja"]

frutas.insert(1, "uva")  # Inserta en la posición 1

print(frutas)


Salida:

["manzana", "uva", "plátano", "naranja"]

 Si insertas al inicio

frutas.insert(0, "kiwi")

print(frutas)


Salida:

["kiwi", "manzana", "uva", "plátano", "naranja"]

 Si insertas más allá del final

Si el índice es mayor que la longitud de la lista, el elemento se agrega al final:

frutas.insert(100, "sandía")

print(frutas)


Salida:

["kiwi", "manzana", "uva", "plátano", "naranja", "sandía"]
"""

# Lista original
resultado = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]

# Eliminar a Koopa Troopa
resultado.remove("Koopa Troopa")

# Insertar "Roman" y "Gerardo" en la posición donde estaba Koopa Troopa (índice 4)
resultado.insert(4, "Roman")
resultado.insert(5, "Gerardo")

print(resultado)

"""Agregando a María con INSERT

"""

# Lista original
resultado = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]
resultado.remove("Koopa Troopa")
resultado.insert(4, "Roman")
resultado.insert(5, "Gerardo")
resultado.append("Massy")    #Agregando a Massy y Maria
resultado.append("Maria")
resultado.remove("Maria")
resultado.insert(0, "Maria")    #Poniendo a Maria en el inicio
print(resultado)

"""En Python, el método .reverse() se usa para invertir el orden de los elementos de una lista en el mismo lugar (es decir, modifica la lista original).

 Sintaxis
lista.reverse()


No necesita argumentos.

 Ejemplo básico

numeros = [1, 2, 3, 4, 5]


numeros.reverse()

print(numeros)


Salida:

[5, 4, 3, 2, 1]

 Importante

No devuelve una nueva lista, solo cambia el orden en la existente.
Es decir:

print(numeros.reverse())  #  Devuelve None


Si quieres crear una lista nueva invertida sin modificar la original:

numeros = [1, 2, 3, 4, 5]

nueva = list(reversed(numeros))

print(nueva)


Salida:

[5, 4, 3, 2, 1]

 Otra forma (slicing)

También puedes usar rebanado:

numeros = [1, 2, 3, 4, 5]

invertida = numeros[::-1]

print(invertida)


Salida:

[5, 4, 3, 2, 1]

Agregando a María con REVERSE
"""

# Lista original
resultado = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]
resultado.remove("Koopa Troopa")
resultado.insert(4, "Roman")
resultado.insert(5, "Gerardo")
resultado.append("Massy")    #Agregando a Massy y Maria
resultado.append("Maria")
resultado.reverse()       #Poniedo a Maria al inicio con REVERSE
print(resultado)

""" En conclusión:

Los métodos de listas en Python permiten modificar, agregar y organizar los elementos de manera sencilla y directa.

append() agrega un elemento al final de la lista.

remove() elimina la primera coincidencia de un valor específico.

insert() permite colocar un elemento en una posición exacta, desplazando los demás.

reverse() invierte el orden completo de los elementos.

Estos métodos son esenciales para manipular listas de forma eficiente, ya que permiten añadir, quitar, ordenar o reorganizar datos sin necesidad de crear listas nuevas.
"""

corredores = ['Maria', 'Massy', 'Donkey Kong Jr.', 'Bowser', 'Toad', 'Gerardo', 'Roman', 'Yoshi', 'Princess', 'Luigi', 'Mario']

# Recorremos la lista con un bucle FOR (CLASE DEL 19/10/2025)
for corredor in corredores:
    print(corredor)

"""## **MATRICEZ**
En Python, una matriz se puede representar usando listas dentro de listas.
Cada lista interna representa una fila de la matriz.

 Ejemplo de matriz

matriz = [

    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


Visualmente:

1  2  3

4  5  6

7  8  9

 Acceder a elementos

Puedes acceder usando índices:

print(matriz[0][0])  # 1 (fila 0, columna 0)

print(matriz[1][2])  # 6 (fila 1, columna 2)

 Recorrer toda la matriz

for fila in matriz:

    for elemento in fila:
        print(elemento, end=" ")
    print()


Salida:

1 2 3

4 5 6

7 8 9

 Modificar un valor

matriz[1][1] = 50

print(matriz)


Salida:

[[1, 2, 3], [4, 50, 6], [7, 8, 9]]

 Agregar una nueva fila

matriz.append([10, 11, 12])

print(matriz)

 En conclusión:

Una matriz en Python se crea usando listas dentro de listas, lo que permite almacenar datos en filas y columnas.
Se pueden acceder, modificar o recorrer fácilmente con índices y bucles, lo que la hace muy útil para operaciones numéricas, tablas o estructuras bidimensionales.
"""

# Matriz.py
# Una matriz es una lista que contiene otras listas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mostrar la matriz completa
print("Matriz completa:")
for fila in matriz:
    print(fila)

# Acceder a un valor específico (fila 2, columna 3)
print("\nElemento en fila 2, columna 3:")
print(matriz[1][2])  # Recuerda: Python empieza en índice 0

"""## **DICCIONARIO**
En Python, un diccionario es una estructura de datos que almacena información en pares clave-valor.


Cada clave es única.


Cada valor puede ser cualquier tipo de dato: número, cadena, lista, otra estructura, etc.

Los diccionarios no tienen un orden fijo (antes de Python 3.7), aunque ahora conservan el orden de inserción.

 Sintaxis
diccionario = {

    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}

 Ejemplo básico

persona = {

    "nombre": "María",
    "edad": 19,
    "ciudad": "CDMX"
}

print(persona)


Salida:

{'nombre': 'María', 'edad': 19, 'ciudad': 'CDMX'}

 Acceder a valores

print(persona["nombre"])  # María

print(persona["edad"])    # 19

 Modificar o agregar valores

 Modificar

persona["edad"] = 20

 Agregar

persona["profesion"] = "Estudiante"

print(persona)


Salida:

{'nombre': 'María', 'edad': 20, 'ciudad': 'CDMX', 'profesion': 'Estudiante'}

 Eliminar elementos

del persona["ciudad"]

print(persona)


Salida:

{'nombre': 'María', 'edad': 20, 'profesion': 'Estudiante'}

 Recorrer un diccionario

for clave, valor in persona.items():

    print(clave, ":", valor)


Salida:

nombre : María

edad : 20

profesion : Estudiante


 En resumen:
Un diccionario es como una agenda o tabla donde puedes buscar información por una clave, en lugar de por un índice como en las listas.


---

###  Diccionario ejemplo

```python
persona = {
    "nombre": "María",
    "edad": 19,
    "ciudad": "CDMX",
    "profesion": "Estudiante"
}
```

Visualmente se puede ver como:

| Clave     | Valor      |
| --------- | ---------- |
| nombre    | María      |
| edad      | 19         |
| ciudad    | CDMX       |
| profesion | Estudiante |

---

###  Acceso a valores

```python
print(persona["nombre"])   # María
print(persona["edad"])     # 19
```

###  Agregar o modificar

```python
persona["edad"] = 20        # modificar
persona["hobby"] = "leer"   # agregar
```

###  Recorrer todo el diccionario

```python
for clave, valor in persona.items():
    print(clave, ":", valor)
```

**Salida:**

```
nombre : María
edad : 20
ciudad : CDMX
profesion : Estudiante
hobby : leer
```



"""

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",

    }
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

escuela = {
    "Hermione": "Excel",
    "Harry": "Power bi",
    "Ron": "Python",
    "Draco": "IA"
}
print(escuela["Hermione"])