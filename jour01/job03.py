class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Résultat de l'addition :", resultat)

operation = Operation(nombre1=2, nombre2=3)

print("Nombre1 :", operation.nombre1)
print("Nombre2 :", operation.nombre2)

operation.addition()
