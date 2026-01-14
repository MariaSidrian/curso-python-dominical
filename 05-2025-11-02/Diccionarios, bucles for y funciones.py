# ============================================================
# Clase 05 – Diccionarios, bucles for y funciones
# Curso Python Dominical
# Tema: Recorridos, estructuras clave-valor y definición de funciones
# ============================================================


#Ejemplo de diccionario
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

#Ejemplo de diccionario pero con FOR y separado con coma
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",

    }
#print(students["Hermione"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])
for student in students:
    print(student, students[student], sep=", ")
escuela = {
    "Hermione": "Excel",
    "Harry": "Power bi",
    "Ron": "Python",
    "Draco": "IA"
}
print(escuela["Hermione"])

#Ejemplo de diccionario pero con FOR sin coma
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",

    }
#print(students["Hermione"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])
for student in students:
    print(student, students[student], )
escuela = {
    "Hermione": "Excel",
    "Harry": "Power bi",
    "Ron": "Python",
    "Draco": "IA"
}
print(escuela["Hermione"])

# 3 signos de gato con FOR
for _ in range(3):
    print("#")

# 20 signos de gato con FOR
for _ in range(20):
    print("#")

# 3 signos de gato con FOR
for _ in range(3):
    print("#")

for _ in range (3):
    print("##")

def main():
    print_column(3)
def print_column(height):
    print("#\n" * height, end="")
main()

def main():
    print_column(2)
def print_column(height):
    print("#####\n" * height, end="")

main()

def saludar():
  return "Hola Mundo"
resultado = saludar()
print(resultado)