import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts !")

    def est_vivant(self):
        return self.vie > 0

    def afficher_vie(self):
        print(f"{self.nom} : {self.vie} points de vie")

class Jeu:
    def __init__(self):
        self.niveau = None
    
    def choisirNiveau(self):
        niveau = input("Choisissez un niveau de difficulté (facile, normal, difficile) : ").lower()
        if niveau == "facile":
            self.niveau = 100
        elif niveau == "normal":
            self.niveau = 75
        else:
            self.niveau = 50

    def lancerJeu(self):
        self.choisirNiveau()
        joueur = Personnage("Joueur", self.niveau)
        ennemi = Personnage("Ennemi", self.niveau)
        
        while joueur.est_vivant() and ennemi.est_vivant():
            joueur.attaquer(ennemi)
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)
            joueur.afficher_vie()
            ennemi.afficher_vie()
            input("Appuyez sur Entrée pour continuer...")
        
        if joueur.est_vivant():
            print("Félicitations ! Vous avez gagné !")
        else:
            print("Game Over. L'ennemi vous a vaincu.")

# Lancer le jeu
jeu = Jeu()
jeu.lancerJeu()

