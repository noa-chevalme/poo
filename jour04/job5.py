import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    def aire(self):
        return self.__largeur * self.__hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius
    
    def aire(self):
        return math.pi * (self.__radius ** 2)

# Instanciation et test des méthodes aire
rectangle = Rectangle(10, 5)
cercle = Cercle(7)

print("Aire du rectangle:", rectangle.aire())
print("Aire du cercle:", cercle.aire())
