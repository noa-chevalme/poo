class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Valeur de x : {self.x}")

    def afficherY(self):
        print(f"Valeur de y : {self.y}")

    def changerX(self, new_x):
        self.x = new_x
        print(f"Nouvelle valeur de x : {self.x}")

    def changerY(self, new_y):
        self.y = new_y
        print(f"Nouvelle valeur de y : {self.y}")


point1 = Point(3, 5)


point1.afficherLesPoints()

point1.afficherX()
point1.afficherY()


point1.changerX(10)
point1.changerY(15)


point1.afficherLesPoints()
