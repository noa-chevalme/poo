class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        # Attributs privés
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50  # Initialisation du réservoir à 50 par défaut

    # Accesseurs et mutateurs pour la marque
    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    # Accesseurs et mutateurs pour le modèle
    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    # Accesseurs et mutateurs pour l'année
    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    # Accesseurs et mutateurs pour le kilométrage
    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    # Accesseurs et mutateurs pour l'état en marche
    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print(f"La voiture {self.__marque} {self.__modele} a démarré.")
        else:
            print("Le réservoir est trop vide pour démarrer. Veuillez faire le plein.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print(f"La voiture {self.__marque} {self.__modele} est arrêtée.")

    # Méthode pour afficher les informations de la voiture
    def afficher_info(self):
        print(f"Marque: {self.__marque}")
        print(f"Modèle: {self.__modele}")
        print(f"Année: {self.__annee}")
        print(f"Kilométrage: {self.__kilometrage} km")
        print(f"En marche: {'Oui' if self.__en_marche else 'Non'}")
        print(f"Réservoir: {self.__reservoir} litres")

# Exemple d'utilisation
ma_voiture = Voiture(" Porsche", "Taycan Sport Turismo", 2020, 15000)

# Affichage des informations de la voiture
ma_voiture.afficher_info()

# Tentative de démarrer la voiture
ma_voiture.demarrer()

# Remplissage du réservoir
ma_voiture._Voiture__reservoir = 3  # On simule un plein suffisant

# Tentative de démarrer à nouveau après avoir fait le plein
ma_voiture.demarrer()

# Arrêter la voiture
ma_voiture.arreter()

# Affichage des informations après l'arrêt
ma_voiture.afficher_info()
