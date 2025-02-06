class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Accesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def afficher(self):
        print(f"Rectangle: Longueur = {self.__longueur}, Largeur = {self.__largeur}")

rect = Rectangle(10, 5)
rect.afficher()


rect.set_longueur(20)
rect.set_largeur(10)

rect.afficher()
