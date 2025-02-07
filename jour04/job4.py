class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    def aire(self):
        return self.__largeur * self.__hauteur

# Instanciation et test de la méthode aire
rectangle = Rectangle(10, 5)
print("Aire du rectangle:", rectangle.aire())
