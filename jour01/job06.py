class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom


animal = Animal()


print(f"Âge initial de l'animal : {animal.age}")


animal.vieillir()

print(f"Âge après vieillissement : {animal.age}")


animal.nommer("Rex")


print(f"Nom de l'animal : {animal.prenom}")
