class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    # Getters
    def get_nom(self):
        return self.__nom

    def get_nb_habitants(self):
        return self.__nb_habitants

    # Setter pour modifier le nombre d'habitants
    def set_nb_habitants(self, nb_habitants):
        if isinstance(nb_habitants, int) and nb_habitants >= 0:
            self.__nb_habitants = nb_habitants
        else:
            print("Erreur : Le nombre d'habitants doit être un entier positif.")

    # Méthode pour ajouter un habitant
    def ajouter_habitant(self):
        self.__nb_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()  # Ajoute l'habitant à la ville dès la création de la personne

    # Getters
    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville

    # Méthode pour ajouter une personne à la population de la ville
    def ajouterPopulation(self):
        self.__ville.ajouter_habitant()

    # Affichage des infos de la personne
    def afficher(self):
        print(f"{self.__nom}, {self.__age} ans, habite à {self.__ville.get_nom()}.")


# Création des villes
paris = Ville("Paris", 1_000_000)
marseille = Ville("Marseille", 861_635)

# Affichage du nombre d'habitants des villes
print(f"Nombre d'habitants à Paris : {paris.get_nb_habitants()}")
print(f"Nombre d'habitants à Marseille : {marseille.get_nb_habitants()}")

# Création des personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage des habitants des villes après l'ajout des personnes
print(f"Nombre d'habitants à Paris après ajout : {paris.get_nb_habitants()}")
print(f"Nombre d'habitants à Marseille après ajout : {marseille.get_nb_habitants()}")

# Affichage des informations des personnes
john.afficher()
myrtille.afficher()
chloe.afficher()
