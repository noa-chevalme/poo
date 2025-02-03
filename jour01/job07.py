class Personnage:
    def __init__(self, x, y, taille_plateau):
        self.x = x
        self.y = y
        self.taille_plateau = taille_plateau 

    def gauche(self):
        if self.y > 0:
            self.y -= 1
        print(f"Position actuelle : {self.position()}")

    def droite(self):
        if self.y < self.taille_plateau - 1:
            self.y += 1
        print(f"Position actuelle : {self.position()}")

    def haut(self):
        if self.x > 0:
            self.x -= 1
        print(f"Position actuelle : {self.position()}")

    def bas(self):
        if self.x < self.taille_plateau - 1:
            self.x += 1
        print(f"Position actuelle : {self.position()}")

    def position(self):
        return (self.x, self.y)


personnage = Personnage(2, 2, 5)


print(f"Position initiale : {personnage.position()}")


personnage.gauche()  
personnage.droite()  
personnage.haut()    
personnage.bas()     
