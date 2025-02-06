class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre  # Attribut privé
        self.__auteur = auteur  # Attribut privé
        self.__pages = pages  # Attribut privé

    # Accesseur pour le titre
    def getTitre(self):
        return self.__titre

    # Mutateur pour le titre
    def setTitre(self, nouveau_titre):
        self.__titre = nouveau_titre

    # Accesseur pour l'auteur
    def getAuteur(self):
        return self.__auteur

    # Mutateur pour l'auteur
    def setAuteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    # Accesseur pour le nombre de pages
    def getPages(self):
        return self.__pages

    # Mutateur pour le nombre de pages
    def setPages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self.__pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    # Méthode pour afficher les informations du livre
    def afficher(self):
        return f"Titre : {self.__titre}\nAuteur : {self.__auteur}\nNombre de pages : {self.__pages}"

# Instanciation d'un livre avec des valeurs initiales
livre = Livre("Le Petit ", "Saint-Exupéry", 96)

# Affichage des informations du livre
print(livre.afficher())

# Modification du nombre de pages (valide)
livre.setPages(120)
print("\nAprès modification du nombre de pages :")
print(livre.afficher())

# Tentative de modification du nombre de pages (valide)
livre.setPages(-50)  # Cela générera un message d'erreur
