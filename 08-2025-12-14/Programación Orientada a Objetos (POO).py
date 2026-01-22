# ============================================================
# CLASE 8 · PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# Clases, Herencia y Clases Padre/Hija
#
# En esta clase aprendemos:
# - Qué es una clase en Python
# - Cómo definir una clase padre
# - Cómo crear clases hijas usando herencia
# - Uso del método __init__ (constructor)
# - Métodos genéricos y métodos heredados
# - Identificar relaciones entre clases (__bases__ y __subclasses__)
# - Aplicar herencia con ejemplos reales (Animal, Perro, etc.)
#
# ============================================================

# ------------------------------------------------------------
# 1. CLASE PADRE
# ------------------------------------------------------------
class Animal:
    """
    Clase padre Animal.
    Representa un animal genérico.
    """

    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def sonido(self):
        """
        Método genérico.
        Cada animal hará un sonido distinto.
        """
        pass

    def moverse(self):
        """
        Método genérico.
        Cada animal se mueve de forma distinta.
        """
        pass

    def describeme(self):
        """
        Método común para todos los animales.
        """
        print(f"Soy un {type(self).__name__}, especie: {self.especie}, edad: {self.edad}")


# ------------------------------------------------------------
# 2. CLASES HIJAS (HERENCIA)
# ------------------------------------------------------------

class Perro(Animal):
    def sonido(self):
        return "Guau 🐶"

    def moverse(self):
        return "Corre en cuatro patas"


class Gato(Animal):
    def sonido(self):
        return "Miau 🐱"

    def moverse(self):
        return "Camina y salta silenciosamente"


class Vaca(Animal):
    def sonido(self):
        return "Muuu 🐮"

    def moverse(self):
        return "Camina lentamente"


class Abeja(Animal):
    def sonido(self):
        return "Bzzz 🐝"

    def moverse(self):
        return "Vuela"


# ------------------------------------------------------------
# 3. USO DE LAS CLASES
# ------------------------------------------------------------

perro = Perro("Mamífero", "8 años")
gato = Gato("Mamífero", "3 años")
vaca = Vaca("Mamífero", "5 años")
abeja = Abeja("Insecto", "1 año")

animales = [perro, gato, vaca, abeja]

for animal in animales:
    animal.describeme()
    print("Sonido:", animal.sonido())
    print("Movimiento:", animal.moverse())
    print("-" * 40)


# ------------------------------------------------------------
# 4. VERIFICACIÓN DE HERENCIA
# ------------------------------------------------------------

# Saber de qué clase hereda Perro
print("Perro hereda de:", Perro.__bases__)

# Saber qué clases heredan de Animal
print("Clases hijas de Animal:", Animal.__subclasses__())